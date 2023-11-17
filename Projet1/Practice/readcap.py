import pyshark

# constant
path = 'D:\\Wireshark\\tshark.exe'

file_path = 'E:/Centrale Nantes/AI/A2/Projet1/Practice/mycapture.pcap'

def filecapture():

    capture = pyshark.FileCapture(file_path, tshark_path=path)


    # print(capture[5])

    print(capture[0].highest_layer)

    # # 使用了display过滤器来限制只显示DNS数据流量
    # capture = pyshark.FileCapture(file_path, display_filter = 'dns', tshark_path=path)

    # for pkt in capture:
    #     print(pkt.highest_layer)


def onlineCapture():
    
    capture = pyshark.LiveCapture(interface='WLAN', tshark_path=path)
    
    # filecapture没有sniff属性
    capture.sniff(timeout=15)

    for packet in capture.sniff_continuously(packet_count=5):
        print('Just arrived:', packet)

    

def remoteCapture(IP):

    capture = pyshark.RemoteCapture(IP, 'WLAN', tshark_path=path)
    capture.sniff(timeout=10)
    print(capture)


def get_capture_count():
    cap = pyshark.FileCapture(file_path, tshark_path=path, keep_packets=False)

    count = []

    def counter(*args):
        count.append(args[0])
    
        """
        apply_on_packets: 是另一种遍历数据包的方式，它接受一个函数作为参数并将之作用于所有的数据包。
        
        Example:
        >>> def print_highest_layer(pkt)
            ...: print pkt.highest_layer
        >>> cap.apply_on_packets(print_highest_layer)

        """

    cap.apply_on_packets(counter, timeout=100)
    return len(count)


def QueryDNS():
    cap = pyshark.LiveCapture(interface='WLAN', bpf_filter='udp port 53', tshark_path=path)
    """
        bpf_filter='udp port 53' 是一个 Berkeley Packet Filter(BPF)过滤器，用于过滤网络数据包。
        在这个特定的例子中，该过滤器的作用是捕获传输层协议为UDP(User Datagram Protocol)且目标端口为53的数据包。
    """
    cap.sniff(packet_count=10)

    # pkt: packet
    def print_dns_info(pkt):
        if pkt.dns.qry_name:
            print('DNS Request from %s: %s' % (pkt.ip.src, pkt.dns.qry_name))
        elif pkt.dns.resp_name:
            print('DNS Response from %s: %s' % (pkt.ip.src, pkt.dns.resp_name))

    cap.apply_on_packets(print_dns_info, timeout=100)


def dynamic_call():
    cap = pyshark.FileCapture(file_path, tshark_path=path)
    """
        protocol = pkt.transport_layer: 提取数据包的传输层协议类型。这个值表示数据包使用的协议，例如 TCP、UDP 等。

        src_addr = pkt.ip.src: 提取数据包的源 IP 地址。这个值表示数据包的起始点的 IP 地址。

        src_port = pkt[pkt.transport_layer].srcport: 提取数据包的源端口号。这个值表示数据包的起始点使用的端口号，例如发送数据包的应用程序的端口号。

        dst_addr = pkt.ip.dst: 提取数据包的目标 IP 地址。这个值表示数据包的目标点的 IP 地址。

        dst_port = pkt[pkt.transport_layer].dstport: 提取数据包的目标端口号。这个值表示数据包的目标点使用的端口号，例如接收数据包的应用程序的端口号。
    """
    def print_conversation_header(pkt):
        try:
            protocol =  pkt.transport_layer
            src_addr = pkt.ip.src
            src_port = pkt[pkt.transport_layer].srcport
            dst_addr = pkt.ip.dst
            dst_port = pkt[pkt.transport_layer].dstport
            print('%s  %s:%s --> %s:%s' % (protocol, src_addr, src_port, dst_addr, dst_port))
        except AttributeError as e:
            #ignore packets that aren't TCP/UDP or IPv4
            pass

    cap.apply_on_packets(print_conversation_header, timeout=100)

if __name__ == '__main__':
    IP = ''
    # filecapture()
    # QueryDNS()
    # print(get_capture_count())
    dynamic_call()

