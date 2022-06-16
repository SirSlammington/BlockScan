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

    def checkVersion(self):
        return subprocess.check_output(split('nmap --version'))
    
    # Function to iterate through each host
    ''' 
    Redirecting stdout should be reserved for a separate function outside of this one.
    '''
    def scanTarget(self, host, flags, portNums=None):
        host = host.replace('\n', '')

        # Scanner object
        scanner = nmap.PortScanner()

        # Performs scan (this updates the scanner object with callable data found in a scan)
        try:
            scanner.scan(host, arguments=flags, ports=portNums)
            cmd = scanner.command_line()
            print(Fore.CYAN + cmd)
        except TypeError:
            scanner.scan(host, arguments=flags)
            cmd = scanner.command_line()
            print(Fore.CYAN + cmd)

        # Writes output to file
        with open(f'{host}.txt', 'w') as out_file:
            out_file.write(f'HOST: {host} ({scanner[host].hostname()})\tSTATE: {scanner[host].state()}\n\n')
            for proto in scanner[host].all_protocols():
                out_file.write(f'PROTO: {proto}\n')
                    
                # Ports in overlying protocol
                fport = scanner[host][proto].keys()
                sorted(fport)
                for port in fport:
                    out_file.write(f'PORT: {port}\tSTATUS: {scanner[host][proto][port]["state"]}\n')
        out_file.close()