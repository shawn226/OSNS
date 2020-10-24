import argparse


def get_arguments(parser):
    args = parser.parse_args()

    if args.network is not None:
        print("Scan of the network {} ./. ".format(args.network))
    else:
        print("Scan an IP")

def set_arguments():
    parser = argparse.ArgumentParser(description="Otter Shell Network Scan -")
    parser.add_argument("-v", "--verbosity", type=int, choices=[0,1,2],
                        help="Increase output verbosity")
    parser.add_argument("-n", "--network", nargs='?',
                        help="Specify the address network")

    get_arguments(parser)
