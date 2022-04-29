# Class for the scan itself
import subprocess
from shlex import split
import nmap
from colorama import Fore

class Scan:
    # Method to detect if nmap exists on the system (GNU/Linux only)
    def checkInstall(self):
        try:
            subprocess.check_output(split('which nmap'))
            return True
        except subprocess.CalledProcessError as subpError:
            print(Fore.RED + f' SUBPROCESS Error Code: {subpError.returncode}')
            return False
    
    # Function to iterate through each host
    ''' 
    Redirecting stdout should be reserved for a separate function outside of this one.
    '''
    def scanTarget(self, host, flags, ports):
        host = host.replace('\n', '')

        # Scanner object
        scanner = nmap.PortScanner()
            
        cmd = scanner.command_line()
        print(cmd)

        # Performs scan (this updates the scanner object with callable data found in a scan)
        scanner.scan(host, arguments=flags, ports=ports)
                
        # Writes output to file
        with open(f'{host}.txt', 'w') as out_file:
            out_file.write(f'HOST: {host} ({scanner[host].hostname()}) \n STATE: {scanner[host].state()}\n')

            for proto in scanner[host].all_protocols():
                out_file.write(f'PROTO: {proto}')
                    
                # Ports in overlying protocol
                fport = scanner[host][proto].keys()
                fport.sort()
                for port in fport:
                    out_file.write(f'PORT: {port}\tSTATUS: {scanner[host][proto][port]["state"]}')
        out_file.close()