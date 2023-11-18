import pyshark
from datetime import datetime
from CapFile import CaptureFile
from scapy.all import sniff, wrpcap

class CaptureLive:
    def __init__ (self, filepath = None, interface = None, tshark_path = None, timeout = None, packet_count = None):
        # super().__init__(filepath = None, tshark_path = None)
        self.interface = interface
        self.packet_count = packet_count
        self.cap = pyshark.LiveCapture(interface, tshark_path = tshark_path, use_json = True, include_raw = True)
        self.cap.sniff(timeout = timeout, packet_count = packet_count)
    
    def details_print(self, filepath):
        packets = sniff(iface = self.interface, count = self.packet_count )
        # packets = [packet for packet in cap.sniff_continuously(packet_count=packet_count)]

        # Write the list of packets to a pcap file using scapy

        # scapy_packets = [packet.get_raw_packet() for packet in packets]
        # wrpcap('Packets.cap', [bytes(packet) for packet in self.cap.sniff_continuously(packet_count=packet_count)])
        wrpcap(filepath, packets)


if __name__ == '__main__':
    # constant

    tshark_path = 'D:\\Wireshark\\tshark.exe'

    caplive = CaptureLive(interface='WLAN', tshark_path=tshark_path, timeout=100, packet_count=100)

    filepath = 'E:\Centrale Nantes\AI\A2\Projet1\Practice\Packets.cap'

    caplive.details_print(filepath)
    