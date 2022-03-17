from random import choice
import string

def create_devices(num_devices=1, num_subnets=1):

    # CREATE A LIST OF DEVICES
    created_devices = list()    # CREATE EMPTY LIST FOR HOLDING DEVICES

    if num_devices > 254 or num_subnets > 254:
        print("Error: too many devices and/or subnets requested")
        return created_devices

    for subnet_index in range(1, num_subnets+1):

        # FOR LOOP TO CREATE LARGE NUMBER OF DEVICES
        for device_index in range(1, num_devices+1):
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
            device["ip"] = "10.0." + str(subnet_index) + "." + str(device_index)

            # ADD DEVICE TO THE LIST OF DEVICES
            created_devices.append(device)

    return created_devices