from pprint import pprint

# DICTIONARY representing a device
device = {
    "name": "switch01",
    "vendor": "cisco",
    "os": "ios",
    "model": "2960",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
}

## SIMPLE PRINT
print("\n_____ SIMPLE PRINT ____________________")
print("device:", device)
print("device name:", device["name"])

## PRETTY PRINT
print("\n____ PRETTY PRINT ____________________")
pprint(device)

# FOR LOOP, NICELY FORMATTED PRINT
print("\n_____ FOR LOOP, USING F-STRING _____________________________")
for key, value in device.items():
    print(f"{key:>16s} : {value} ")


