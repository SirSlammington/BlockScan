# BlockScan
 Python utility to automate Nmap scanning of a large amount of hosts. While this is a built in functionality in Nmap, the main goal of this utility is to allow users to create files based on each address scanned. Beyond this, you can edit the "hosts.txt" file with addresses you'd like to prioritize scanning.

 ## Installation
 ```bash
 git clone https://github.com/SirSlammington/BlockScan
 ```

 ## Usage
 To begin, edit the **conf.yaml** file to configure the options you'd like for your Nmap scan.
 ```yaml
 scan-options:
  cidr-range: ''
  ports: '22-443, 3389'
  args:
    - -T3
    - -Pn
    - -sV
 ```
 The above are the default options. First, make sure to change the `cidr-range` option, as this will create a file named **hosts.txt** that will contain each host that needs to be scanned. This must be in CIDR notation (e.g. `X.X.X.X/24`). You may change the ports and arguments for each scan as your needs arise.

 Once you have made your configurations using the YAML file, you can launch the scan:
 ```bash
 python3 blockscan.py
 ```
 