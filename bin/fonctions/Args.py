#!/bin/python3
import argparse
from fonctions.Scan import *


def get_arguments(parser):
    args = parser.parse_args()

    verbosity["level"] = args.verbosity

    if args.discover and args.network is not None:
        discover_network(args.network)
    elif args.network is not None:
        print("Scan an IP")

def set_arguments():
    parser = argparse.ArgumentParser(prog="osns",
                                    description="Otter Shell Network Scan -")
    parser.add_argument("-v", "--verbosity", type=int, choices=[0,1,2],
                        default=0,
                        help="Increase output verbosity")
    parser.add_argument("-D", "--discover", action="store_true",
                        help="Map the network to discover hosts")

    parser.add_argument("-n", "--network", nargs='+', action="extend",
                        help="Specify the address network followed by the mask"\
                        " (write 'localhost' to"\
                        " use your own network)")

    get_arguments(parser)
