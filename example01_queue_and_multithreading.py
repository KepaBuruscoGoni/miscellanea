# -*- coding: utf-8 -*-
"""
@date: 05/04/2023
@author: @kburusco
"""

import os
import threading
import pandas as pd
from queue import Queue


def main():
    
    print("\n\n => Example of Multithreading and Queue \n")
    # Create a queue to store data from CSV files
    queue = Queue()

    # List of CSV file paths to read
    csv_files = get_list_of_csv_files()

    # Create and start threads to read CSV files and add data to the queue
    threads = []
    for file_path in csv_files:
        t = threading.Thread(target=read_csv_and_enqueue, args=(file_path, queue))
        t.start()
        threads.append(t)

    # Wait for all threads to complete
    for t in threads:
        t.join()

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



if __name__ == "__main__":
    main()
    
    
    