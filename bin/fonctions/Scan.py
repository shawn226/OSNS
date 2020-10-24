#!/bin/python3
import ipaddress
from pythonping import ping

verbosity = {"level": 0}

def discover_network(network):

    final_nework = "/".join(network)

    hosts = list(ipaddress.ip_network(final_nework).hosts())

    for host in hosts:
        response = ping(str(host), size=10, count=5)
        print(response)
