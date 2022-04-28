# Class for the scan itself
import subprocess
from shlex import split
import nmap

class Scan:
    def __init__(self, configuration):
        self.conf = configuration

    # Method to detect if nmap exists on the system (GNU/Linux only)
    def checkInstall():
        try:
            subprocess.check_output(split('which nmap'))
            return True
        except subprocess.CalledProcessError as subpError:
            print(f'\033[1;31;40m SUBPROCESS Error Code: {subpError.returncode}')
            return False
    
    # Function to iterate through each host
    ''' Problem for future:
    Redirecting stdout should be reserved for a separate function outside of this one.'''
    def scan(hosts, flags, portNums):
        for host in hosts:
            # Removes newline character from end of each item in the list
            host = host.replace('\n', '')
            
            # Output file
            out_file = open(f'{host}.txt', 'w')

            # Scanner object
            scanner = nmap.PortScanner()
            """f'nmap {" ".join(flags)} {host}'"""
            scan = scanner.scan(host, arguments=flags, ports=portNums)
            cmd = scanner.command_line()
            print(cmd)
            ind_scan = subprocess.Popen(split(cmd), stdout=out_file)
            ind_scan.wait() # Waits for scan to complete before moving on to subsequent host
                
            # Writes stdout to a file
            with out_file:
                out_file.write(str(ind_scan.stdout))