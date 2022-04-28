#!/bin/python3
import sys
from scanconfig import ScanConfig; from scan import Scan
import nmap

# Main block
if __name__ == '__main__':
    # Checks if Nmap is installed on the system prior to operation
    if Scan.checkInstall() == False:
        print('\033[1;31;40m nmap is not installed on the system.')
    else:
        pass

    conf = ScanConfig()

    # Opens the file with targets in them and enumerates through them individually
    file = conf.getConf('host-file')
    with open(file, 'r'):
        agg_hosts = file.readlines()
        scanner = nmap.PortScanner()
        for host in file:
            scanner.scan(host, conf.getConf('ports'), conf.getConf('args'))
            print(scanner.command_line())