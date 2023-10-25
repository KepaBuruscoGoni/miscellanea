## -*- coding: utf-8 -*-
"""
@author: kburusco
@date: 25/10/2023
"""

import sys


def main():

    print("\n=> Script to read arguments from command line", flush=True)

    script = sys.argv[0]
    name = sys.argv[1]
    surename = sys.argv[2]
    age = sys.argv[3]
    active = sys.argv[4]

    print(f"\n   The input command line is: {' '.join(sys.argv)}")
    print(f"\n   The script name is {script}")
    print(f"\n   My friend {name} {surename} is {age} and prefers being active in the {active}")
    print("\n=> Normal Termination\n", flush=True)

    sys.exit()


if __name__ == '__main__':
        main()
