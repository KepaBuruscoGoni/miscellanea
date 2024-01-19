# -*- coding: utf-8 -*-
"""
@date: 05/04/2023
@author: @kburusco
"""

import os
import pandas as pd
from multiprocessing import Pool
from multiprocessing import Manager
from multiprocessing import cpu_count



def main():

    print("\n\n => Example of Multiprocessing and Queue \n")
    # Create a Queue to store data from CSV files
    # 1) Create manager
    manager = Manager()
    # 2) Create multiprocessing queue
    queue = manager.Queue()

    # List of CSV file paths to read
    csv_files = get_list_of_csv_files()

    # Create a Pool with N - 1 processes where N is the number of cores in your machine
    num_threads = cpu_count() - 1
    # Zip "csv_file" and "queue" arguments to feed starmap
    zipped_csv_queue = [(file_path, queue) for file_path in csv_files]
    with Pool(processes=num_threads,maxtasksperchild=1) as pool: 
        pool.starmap(read_csv_and_enqueue, zipped_csv_queue)
    
    # Wait for all threads to complete
    pool.close()
    pool.join()

    # Aggregate data from the queue into a Pandas DataFrame
    aggregated_df = aggregate_data_from_queue(queue)

    # Perform further data processing or analysis with the aggregated DataFrame
    # Print the aggregated DataFrame
    print(aggregated_df)
    # Export aggregated dataframe to a new CSV file
    aggregated_df.to_csv('aggregated_dataframe.csv',sep=',',index=False)

    print("\n\n => Done \n")
    



'''
########################
# METHODS AND FUNCTIONS
########################
'''


# Get list of CSV files in current directory
def get_list_of_csv_files():
    input_dir = os.getcwd()
    csv_files = []
    csv_files = [ f for f in sorted(os.listdir(input_dir)) 
                 if os.path.isfile(os.path.join(input_dir, f)) and
                 (f[-3:] in ('csv', 'txt')) ]
    return csv_files


# Define a function to read a CSV file and add data to the queue
def read_csv_and_enqueue(file_path, queue):
    df = pd.read_csv(file_path,delimiter='\t')
    queue.put(df)


# Define a function to aggregate data from the queue into a Pandas DataFrame
def aggregate_data_from_queue(queue):
    dfs = []
    while not queue.empty():
        df = queue.get()
        dfs.append(df)
        queue.task_done()
    aggregated_df = pd.concat(dfs)
    return aggregated_df



if __name__ == '__main__':
    main()
    
