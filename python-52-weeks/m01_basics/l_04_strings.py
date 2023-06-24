from pprint import pprint

device1_str = "  r3-L-n7, cisco, catalyst 2960, ios  "

# SPLIT
print("STRING STRIP, SPLIT, REPLACE")
device1 = device1_str.split(",")
print("device1 using split:")
print("     ", device1)

# STRIP
device1 = device1_str.strip().split(",")
print("device1 using strip and split:")
print("     ", device1)

# REMOVE BLANKS
device1 = device1_str.replace(" ", "").split(",")
print("device1 replaced blanks using split:\n     ", device1)

# REMOVE BLANKS, CHANGE COMMA TO COLON
device1_str_colon = device1_str.replace(" ", "").replace(",", ":")
print("device replaced blans, comma to colon:")
print("     ", device1_str_colon)

# LOOP WITH STRIP AND SPLIT
device1 = list()
for item in device1_str.split(","):
    device1.append(item.strip())
print("device1 using loop and strip for each item:")
print("     ", device1)

# STRIP AND SPLIT, SINGLE LINE USING LIST COMPREHENSION
device1 = [item.strip() for item in device1_str.split(",")]
print("device1 using list comprehension")
print("     ", device1)

# IGNORING CASE
print("\n\nIGNORING CASE")
model = "CSR1000V"
if model == "csr1000v":
    print(f"matched: {model}")
else:
    print(f"didn't' match: {model}")

model = "CSR1000V"
if model.lower() == "CSR1000v".lower():
    print(f"matched: {model}")
else:
    print(f"didn't' match: {model}")

# FINDING SUBSTRING
print("\n\nFINDING SUBSTRING")
version = "Virtual XE Software (X86_64LINUX_IOS-UNIVERSALK9-M), Version 16.11.1a, RELEASE SOFTWARE (fc1)"
expected_version = "Version 16.11.1a"
index = version.find(expected_version)
if index >= 0:
    print(f"found version: {expected_version} at location {index}")
else:
    print(f"not found: {expected_version}")


# SEPARATING STRING COMPONENTS
print("\n\nSEPARATING VERSION STRING COMPONENTS")
version_info = version.split(",")
for version_info_part in version_info:
    print(f"version part: {version_info_part.strip()}")


# SEPARATING STRING COMPONENTS AND ENUMERATE
print("\n\nSEPARATING VERSION STRING COMPONENTS")
version_info = version.split(",")
for part_no, version_info_part in enumerate(version_info):
    print(f"version part {part_no}: {version_info_part.strip()}")

###############################################################################
### PARSING DEVICE OUTPUT EXAMPLES

# SHOW INTERFACE STATS
show_interface_stats = """
GigabitEthernet0/0
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor        980      86165        134       8813
             Route cache          9       2306          0          0
                   Total        989      88471        134       8813
Interface GigabitEthernet0/1 is disabled

GigabitEthernet0/2
          Switching path    Pkts In   Chars In   Pkts Out  Chars Out
               Processor         12       1206         34       2526
             Route cache          0          0          0          0
                   Total         12       1206         34       2526
Interface GigabitEthernet0/3 is disabled
"""

interface_counters = dict()
show_interface_stats_lines = show_interface_stats.splitlines()
for index, stats_line in enumerate(show_interface_stats_lines):
    if stats_line.find('GigabitEthernet', 0) == 0:
        totals_line = show_interface_stats_lines[index + 4]
        interface_counters[stats_line] = totals_line.split()[1:]

print("\n\n----------- Interface Counters ---------------------")
pprint(interface_counters)


# SHOW IP ARP
show_ip_arp = """
Protocol  Address          Age (min)  Hardware Addr   Type   Interface
Internet  10.0.0.2                0   c025.2f97.5505  ARPA   GigabitEthernet0/0
Internet  10.0.0.109              5   d094.66b6.54fa  ARPA   GigabitEthernet0/0
Internet  10.0.0.249              -   0c33.a54b.0000  ARPA   GigabitEthernet0/0
"""

arp_table = dict()
# for line in show_ip_arp.splitlines()[2:]:
#     line_split = line.split()
#     arp_table[line_split[1]] = line_split[3]

for arp_line in show_ip_arp.splitlines():
    if arp_line.lower().find("internet", 0) == 0:
        arp_table[arp_line[10:25].strip()] = arp_line[38:52]

print("\n\n----------- ARP Table ---------------------")
pprint(arp_table)






















