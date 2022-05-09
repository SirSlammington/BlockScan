#!/usr/bin/python3
from scanconfig import ScanConfig
from scan import Scan
from colorama import Fore
from threading import Thread

# Main block
if __name__ == '__main__':
    conf = ScanConfig('conf.yaml')
    scan = Scan()

    # Checks if Nmap is installed on the system prior to operation
    if scan.checkInstall() == False:
        print(Fore.RED + 'nmap is not installed on the system.\n')
    else:
        print(Fore.GREEN + scan.checkVersion().decode('utf-8'))

    # Opens the file with targets in them and enumerates through them individually
    with open(conf.getConf('host-file'), 'r') as file:
        agg_hosts = file.readlines()
        while len(agg_hosts) != 0:
            try:
                scan_one = Thread(target=scan.scanTarget(agg_hosts[0], conf.parseListArgs(conf.getConf('args')), conf.getConf('ports')))
                scan_two = Thread(target=scan.scanTarget(agg_hosts[1], conf.parseListArgs(conf.getConf('args')), conf.getConf('ports')))
                scan_three = Thread(target=scan.scanTarget(agg_hosts[2], conf.parseListArgs(conf.getConf('args')), conf.getConf('ports')))

                # Starts each scan execution
                scan_one.start()
                scan_two.start()
                scan_three.start()

                # Waits until the main thread is finished before moving on
                scan_one.join()
                scan_two.join()
                scan_three.join()

                # Remove hosts scanned from list
                for i in range(3):
                    agg_hosts.pop(i)
            except IndexError:
                try:
                    Thread(target=scan.scanTarget(agg_hosts[0], conf.parseListArgs(conf.getConf('args')), conf.getConf('ports'))).start()
                    agg_hosts.pop(0)
                except IndexError:
                    print('No more hosts left to scan.')
                    break
                print('No more hosts left to scan.')
                break

    file.close()
