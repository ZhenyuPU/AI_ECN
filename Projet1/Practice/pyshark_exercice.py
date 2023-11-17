import pyshark
from scapy.all import wrpcap
import psutil

def get_windows_interfaces():
    interfaces = psutil.net_if_addrs()
    return [interface for interface in interfaces.keys()]

print(get_windows_interfaces())


path = 'D:\\Wireshark\\tshark.exe'
capture = pyshark.LiveCapture(interface= 'WLAN', tshark_path=path)

# Sniff packets and store them in a list
print(capture)
packets = [packet for packet in capture.sniff_continuously(packet_count=100)]

print(packets)
output_file = 'mycapture.cap'
# Write the list of packets to a pcap file using scapy
# wrpcap(output_file, [bytes(packet) for packet in packets])

with open(output_file, 'w') as file:
    for packet in packets:
        file.write(packet)
"""
    bytes(packet.raw_mode()) is used to retrieve the raw binary representation of the packet, 
    and it is then written to the pcap file. 
    This ensures that the packet data is properly handled for writing to the file.
"""


