import pyshark
from datetime import datetime

class CaptureLive:
    def __init__ (self, interface = None, tshark_path = None, timeout = None, packet_count = None):
        self.cap = pyshark.LiveCapture(interface, tshark_path)
        self.cap.sniff(timeout = timeout, packet_count = packet_count)
    

    