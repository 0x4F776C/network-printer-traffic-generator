# import required packages
import random
from scapy.all import *

# CSI-traffic-generator v1

# ASCII art
art = """
.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |   ______     | || |  _________   | || |    ______    | || |              | || | ____   ____  | || |  _________   | || |  _______     | || |              | || |     __       | |
| |  |_   __ \   | || | |  _   _  |  | || |  .' ___  |   | || |              | || ||_  _| |_  _| | || | |_   ___  |  | || | |_   __ \    | || |              | || |    /  |      | |
| |    | |__) |  | || | |_/ | | \_|  | || | / .'   \_|   | || |    ______    | || |  \ \   / /   | || |   | |_  \_|  | || |   | |__) |   | || |              | || |    `| |      | |
| |    |  ___/   | || |     | |      | || | | |    ____  | || |   |______|   | || |   \ \ / /    | || |   |  _|  _   | || |   |  __ /    | || |              | || |     | |      | |
| |   _| |_      | || |    _| |_     | || | \ `.___]  _| | || |              | || |    \ ' /     | || |  _| |___/ |  | || |  _| |  \ \_  | || |      _       | || |    _| |_     | |
| |  |_____|     | || |   |_____|    | || |  `._____.'   | || |              | || |     \_/      | || | |_________|  | || | |____| |___| | || |     (_)      | || |   |_____|    | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'
Created by : Lee Chun Hao
Date : 19 October 2020
"""
print(art)

# User input for count and ip address
source_ip_address = input('First 3 octets of source address mask (e.g 192.168.1.), include the dots...\n>> ')
packet_count = input('Number of iterations\n>> ')
destination_ip_address = input('IP address of printer\n>> ')

# IP masking function
def IPMask(src_ip, dst_ip):
    ip = src_ip
    list_of_ip = []
    i = 2
    while i < 255:
        list_of_ip.append(ip+str(i))
        i += 1
    list_of_ip.remove(dst_ip)
    return list_of_ip[random.randrange(len(list_of_ip))]

# Traffic generator
def sendTraffic(count, dst_ip):
    for i in range(int(count)):
        packet_size = random.randrange(1, 65535)
        send(IP(src=IPMask(source_ip_address, destination_ip_address),dst=dst_ip)/TCP(dport=[201,202,204,206,80,213,515,721,722,723,724,725,726,727,728,729,730,731,1023,1024,1024,137,138,139,530,161,162,2000,2501,2502,2503,3001,6869,9100,9101,9102], flags='S')/Raw(RandString(size=packet_size)), count=1)
    return 0

# Main
if __name__ == "__main__":
    sendTraffic(packet_count, destination_ip_address)
