from tabulate import tabulate
from util.create_utils import create_devices
#import util

### Main program
if __name__ == '__main__':
    devices = create_devices(num_devices=7, num_subnets=3)
    print("\n", tabulate(devices, headers="keys"))
