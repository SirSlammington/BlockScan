#!/bin/python3
from scanconfig import ScanConfig
from scan import Scan
from colorama import Fore

# Main block
if __name__ == '__main__':
    conf = ScanConfig('conf.yaml')
    scan = Scan()

    # Checks if Nmap is installed on the system prior to operation
    if scan.checkInstall() == False:
        print(Fore.RED + 'nmap is not installed on the system.')
    else:
        pass

    # Opens the file with targets in them and enumerates through them individually
    with open(conf.getConf('host-file'), 'r') as file:
        agg_hosts = file.readlines()
        for host in agg_hosts:
            scan.scanTarget(host, conf.parseListArgs(conf.getConf('args')), conf.getConf('ports'))
    file.close()