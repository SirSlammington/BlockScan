from ipaddress import IPv4Network
import yaml

# Class for configuration options found in the conf.yaml file
class ScanConfig:
    def __init__(self, filepath):
        # Path to YAML config file
        self.filepath = filepath

        # Grabs the configurations found in a defined YAML file and stores each key-value pair
        '''This is not a particularly clean implementation, as the file isn\'t ever properly closed.
        This will be fixed later.'''
        self.confs = yaml.safe_load(open(self.filepath, 'r')).get('scan-options')
    
    # Returns a specific item from the YAML
    def getConf(self, option):
        data = self.confs
        return data[option]

    # Puts items in a list into a single string
    def parseListArgs(self, options):
        return ' '.join(options)

    # Method to create file based on CIDR block
    def createCIDR_File(self, cidr_block):
        if cidr_block == '':
            return False
        else:
            with open('hosts.txt', 'w') as file:
                block_range = [str(ip) for ip in IPv4Network(cidr_block)]
                for addr in block_range:
                    file.write(str(addr) + '\n')
