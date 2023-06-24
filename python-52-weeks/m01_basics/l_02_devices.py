from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = list()    # CREATE EMPTY LIST FOR HOLDING DEVICES

# FOR LOOP TO CREATE LARGE NUMBER OF DEVICES
for index in range(10):
    # CREATE DEVICE DICT
    device = dict()

    # RANDOM DEVICE NAME
    device["name"] = (
        choice(["r2", "r3", "r4", "r7", "r10"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )

    # RANDOM VENDOR FROM CHOICE OF CISCO, JUNIPER, ARISTA, HP
    device["vendor"] = choice(["cisco", "juniper", "arista", "hp"])
    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1(T).04","14.1(A).05", "15.1(T)", "16.2(C)" ])
    if device["vendor"] == "juniper":
        device["os"] = choice(["junos"])
        device["version"] = choice(["13.1(T).04","15.1(A).A", "17.1(T)", "15.2(C)" ])
    if device["vendor"] == "arista":
        device["os"] = choice(["eos"])
        device["version"] = choice(["12.1(T).04","14.1(A).05", "15.1(T)", "16.2(C)" ])
    if device["vendor"] == "hp":
        device["os"] = choice(["comware"])
        device["version"] = choice(["12.1(T).04","14.1(A).05", "15.1(T)", "16.2(C)" ])

    # RANDOM IP
    device["ip"] = "10.0.0." + str(index)

    # NICELY FORMATTED PRINT OF THIS ONE DEVICE
    print()
    for key, value in device.items():
        print(f"{key:>16s} : {value}")

    # ADD DEVICE TO THE LIST OF DEVICES
    devices.append(device)

# USE PPRINT TO PRINT DATA AS-IS
print("\n____ DEVICES AS LIST OF DICTS ____________________")
pprint(devices)

# USE 'TABULATE' TO PRINT TABLE OF DEVICES
print("\n____ SORTED DEVICES IN TABULAR FORMAT ____________________")
sorted_devices = sorted(devices, key=itemgetter("vendor", "os", "version"))
print(tabulate(sorted_devices, headers="keys"))