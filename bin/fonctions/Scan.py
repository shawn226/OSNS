#!/bin/python3
import ipaddress
from colorama import Fore, Style
from pythonping import ping
from datetime import datetime

verbosity = {"level": 0}

def discover_network(network):

    final_nework = "/".join(network)

    hosts = list(ipaddress.ip_network(final_nework).hosts())

    nbr_host_tested = 0
    nbr_host_alive = 0
    for host in hosts:
        response = ping(str(host), size=1, count=1)

        nbr_host_tested += 1

        if verbosity["level"] == 1:
            if response.success():
                nbr_host_alive += 1
                print(Fore.GREEN + "Success ! 1 host discovered - ip address :"\
                 " {}".format(host))
        elif verbosity["level"] == 2:
            nbr_host_alive += 1
            if response.success():
                print(Fore.GREEN + "1 host discovered - ip address : {}".format(
                host))
            else:
                print(Fore.RED + "Warning ! No host at {}".format(host))
            print(Style.RESET_ALL, end="")
            print("{} host(s) tested at {}".format(
            nbr_host_tested, datetime.now().strftime("%H:%M:%S")))
            print("")
        else:
            if response.success():
                nbr_host_alive += 1
                print(host)
