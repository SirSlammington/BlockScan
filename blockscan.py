#!/bin/python3
import sys
from scanconfig import ScanConfig; from scan import Scan
from colorama import Fore

# Main block
if __name__ == '__main__':
    conf = ScanConfig()
    scan = Scan()

    # Checks if Nmap is installed on the system prior to operation
    if scan.checkInstall() == False:
        print(Fore.RED + 'nmap is not installed on the system.')
    else:
        pass

    # Opens the file with targets in them and enumerates through them individually
    file = conf.getConf('host-file')
    with open(file, 'r'):
        agg_hosts = file.readlines()
        for host in file:
            scan.host = host; scan.flags = conf.getConf('args'); scan.ports = conf.getConf('ports')
            scan.scanTarget()