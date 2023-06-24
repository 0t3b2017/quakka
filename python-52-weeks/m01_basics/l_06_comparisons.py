from util.create_utils import create_devices
from pprint import pprint
from random import randint, uniform
from datetime import datetime

devices = create_devices(num_subnets=2, num_devices=10)

print("    NAME     VENDOR : OS         IP ADDRESS")
print("    ----     ------   -----      ----------")
for device in devices:
    print(
        f'{device["name"]:>8}   {device["vendor"]:>8} : {device["os"]:<8}   {device["ip"]:<15}'
    )

print("\n", "=" * 70, "\n")

print("    NAME     VENDOR : OS         IP ADDRESS")
print("    ----     ------   -----      ----------")
for device in devices:
    if device["vendor"].lower() != "cisco":
        print(
            f'{device["name"]:>8}   {device["vendor"]:>8} : {device["os"]:<8}   {device["ip"]:<15}'
        )

print("\n", "=" * 70, "\n")
print("----- STARTING COMPARISON OF DEVICE NAMES ------------------------------------------")
found = False
for index, device_a in enumerate(devices):
    for device_b in devices[index+1:]:
        if device_a["name"] == device_b["name"]:
            print(f"Found match! {device_a['name']} for both {device_a['ip']} and  {device_b['ip']}")
            found = True
if not found:
    print("No duplicated name found.")
print("Comparison of devices completed")


print("\n", "=" * 70, "\n")
print("----- CREATE TABLE OF ARBITRARY 'STANDARD' VERSIONS FOR EACH VENDOR:OS")
standard_versions = dict()
for device in devices:
    vendor_os = device["vendor"] + ":" + device["os"]
    if vendor_os not in standard_versions:
        standard_versions[vendor_os] = device["version"]
pprint(standard_versions)

print("\n", "=" * 70, "\n")
print("\n----- CREATE LIST OF NON-COMPLIANT DEVICE OS VERSION FOR EACH VENDOR:OS")
non_compliant_devices = dict()
for vendor_os, _ in standard_versions.items():
    non_compliant_devices[vendor_os] = []


for device in devices:
    vendor_os = device["vendor"] + ":" + device["os"]
    if device["version"] != standard_versions[vendor_os]:
        non_compliant_devices[vendor_os].append(device["ip"] + " version: " + device["version"])

pprint(non_compliant_devices)

print("\n", "=" * 70, "\n")
print("\n---- ASSIGMENT, COPY AND DEEP COPY ---------------------------")

devices2 = devices
print(id(devices))
print(id(devices2))
devices2[0]["name"] = "this is a dumb device name"
if devices2 == devices:
    print("\n      Assigment and modification: devices2 STILL equals devices")
    print("      ===> Moral: Assignment is NOT the same as copy!")
    print(f"    devices:  {devices[0]['name']}")
    print(f"    devices2: {devices2[0]['name']}")
else:
    print("     Hun?")

from copy import copy
from copy import deepcopy

devices2 = copy(devices)
print(id(devices))
print(id(devices2))
devices2[0]["name"] = "this is a dumb device name"
if devices2 == devices:
    print("\n      Shallow copy and modification: devices2 STILL equals devices")
    print("      ===> Moral: 'copy()'  only does a SHALLOW (1st level) copy!")
    print("      ===> Result: Uh-on - I just screwed up the original version!!")
    print(f"    devices:  {devices[0]['name']}")
    print(f"    devices2: {devices2[0]['name']}")
else:
    print("     Hun?")

devices2 = deepcopy(devices)
print(id(devices))
print(id(devices2))
devices2[0]["name"] = "this is ANOTHER dumb device name"
if devices2 == devices:
    print("     Hun?")
else:
    print("\n      Deep copy and modification: devices2 no longer equals devices")
    print("    ==> Moral: 'deepcopy()' gives you a complete copy of the original only does a SHALLOW (1st level) copy!")
    print("    ==> Result: I can do whatever I want with my copy, without touching the original object.!!")
    print(f"    devices:  {devices[0]['name']}")
    print(f"    devices2: {devices2[0]['name']}")


new_set_of_devices = create_devices(num_subnets=2, num_devices=25)
if new_set_of_devices == devices:
    print("     Hun?")
else:
    print("\n    Comparisons of complex, deep data is easy in Python")
    print("    ==> Moral: you can compare any two data structures, no matter how deeply nested")

print("\n", "=" * 70, "\n")
print("\n---- COMPARISONS FOR IMPLEMENTING SLAs ---------------------------")
SLA_AVAILABILITY = 96
SLA_RESPONSE_TIME = 1.0

devices = create_devices(num_subnets=2, num_devices=5)
for device in devices:
    device["availability"] = randint(94, 100)
    device["response_time"] = uniform(0.5, 1.1)

    if device["availability"] < SLA_AVAILABILITY:
        print(f"{datetime.now()}: {device['name']:6} - Availability {device['availability']} < {SLA_AVAILABILITY}")
    if device["response_time"] < SLA_RESPONSE_TIME:
        print(f"{datetime.now()}: {device['name']:6} - Response time {device['response_time']} < {SLA_RESPONSE_TIME}")

print("\n", "=" * 70, "\n")
print("\n\n----- COMPARING CLASSES -----------------------------------------")


class DeviceWithEq:

    def __init__(self, name, ip):
        self.name = name
        self.ip_address = ip

    def __eq__(self, other):
        if not isinstance(other, DeviceWithEq):
            return False
        return self.name == other.name and self.ip_address == other.ip_address


d1 = DeviceWithEq("device 1", "10.20.30.1")
d1_equal = DeviceWithEq("device 1", "10.20.30.1")
d1_different = DeviceWithEq("device 2", "10.20.30.2")

print("\n    Comparison with an __eq__ method to handle evaluation")
if d1 == d1_equal:
    print(f"   ===> using __eq__ : success: {d1} equals {d1_equal}")
else:
    print(f"   !!! using __eq__ : uh-oh, classes not equal and they should be")
if d1 == d1_different:
    print(f"   !!! using __eq__ : uh-on, classes equal and they should not be")
else:
    print(f"   ===> using __eq__ : success: {d1} not equal to {d1_different}")


class DeviceWithNoEq:

    def __init__(self, name, ip):
        self.name = name
        self.ip_address = ip


d1 = DeviceWithNoEq("device 1", "10.20.30.1")
d1_equal = DeviceWithNoEq("device 1", "10.20.30.1")
d1_same = d1

print("\n   Comparison WITHOUT an __eq__ method to handle evaluation!")
if d1 == d1_equal:
    print(f"   !!! with no __eq__ : oops, didn't expect this")
else:
    print(f"   ===> with no __eq__ : success: not equal, as expected")
if d1 == d1_same:
    print(f"   ===> with no __eq__ : success: {d1} points to same object instance {d1_same}")
else:
    print(f"   !!! with no __eq__ : oops, didn't expect this")

























