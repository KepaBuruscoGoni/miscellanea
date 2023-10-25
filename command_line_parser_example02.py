## -*- coding: utf-8 -*-
"""
@author: kburusco
@date: 25/10/2023
"""

import sys
import argparse


def main():

    print("\n=> Script to read arguments from command line", flush=True)

    args = argument_parser()

    name = args.name
    surename = args.surename
    age = args.age
    active = args.active

    print(f"\n   My friend {name} {surename} is {age} and prefers being active in the {active}")

    print("\n=> Normal Termination\n", flush=True)

    sys.exit()


'''
###############################################
#                FUNCTION
###############################################
'''


def argument_parser():
    argparser = argparse.ArgumentParser(
        description='Script to read arguments from command line')

    argparser.add_argument(
        '-name',
        '--name',
        help='User name [name=Anna]',
        type=str,
        default='Anna'
    )

    argparser.add_argument(
        '-surename',
        '--surename',
        help='User surename [surename=Williams]',
        type=str,
        default='Williams'
    )

    argparser.add_argument(
        '-age',
        '--age',
        help='User age [age=35]',
        type=int,
        default=35
    )

    argparser.add_argument(
        '-active',
        '--active',
        help='Is more active in the morning or in the evening? [active=evening]',
        type=str,
        choices=['morning', 'evening'],
        default='evening'
    )

    arguments = argparser.parse_args()

    return arguments


if __name__ == '__main__':
    main()
