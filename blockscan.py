#!/usr/bin/python3
from scanconfig import ScanConfig
from scan import Scan
from colorama import Fore
import multiprocessing as multp

# Main block
if __name__ == '__main__':
    multp.set_start_method("spawn")
    conf = ScanConfig('conf.yaml')
    scan = Scan()

    # Checks if Nmap is installed on the system prior to operation
    if scan.checkInstall() == False:
        print(Fore.RED + 'nmap is not installed on the system.\n')
    else:
        print(Fore.GREEN + scan.checkVersion().decode('utf-8'))

    # Function to create a "hosts.txt" file if one does not yet exist
    conf.createCIDR_File(conf.getConf('cidr-range'))

    # Opens the file with targets in them and enumerates through them individually
    with open('hosts.txt', 'r') as file:
        agg_hosts = file.readlines()
        while len(agg_hosts) != 0:
            instr = multp.Process
            try:
                # This loop will create the processes ("threads") and subsequently executes them
                for process_count in range(int(conf.getConf('threads'))):
                    # Empty list of all the processes (scans) to be executed
                    processes = []
                    scan_attempt = instr(target=scan.scanTarget, args=(agg_hosts[process_count], conf.parseListArgs(conf.getConf('args')), conf.getConf('ports')))
                    processes.append(scan_attempt)
                    # Starts the "thread"
                    scan_attempt.start()
                    agg_hosts.pop(process_count)
                
                # Joins the processes
                for process in processes:
                    process.join()

            except IndexError:
                try:
                    multp.Process(target=scan.scanTarget(agg_hosts[0], conf.parseListArgs(conf.getConf('args')), conf.getConf('ports'))).start()
                    agg_hosts.pop(0)
                except IndexError:
                    print('No more hosts left to scan.')
                    break
                print('No more hosts left to scan.')
                break

    file.close()