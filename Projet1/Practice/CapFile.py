"""
针对file.pcap的读取，处理
"""
import pyshark
from datetime import datetime

class CaptureFile:
    def __init__(self, filepath = None, tshark_path = None):
        self.cap = pyshark.FileCapture(filepath, tshark_path=tshark_path)
        
    # analysis of protocols

    def protocol_analysis(self):
        protocols = []
    
        for packet in self.cap:
            if hasattr(packet, 'transport_layer'):
                protocols.append(packet.transport_layer)
        
        return protocols
    
    # IP 地址和端口分析：
    def ip_port_analysis(self):
        ip_addresses = []
        ports = []

        for packet in self.cap:
            if 'IP' not in packet:
                continue

            dic = {'src': packet.ip.src, 'dst': packet.ip.dst}

            ip_addresses.append(dic)

            if hasattr(packet, 'transport_layer'):
                dic_ = {'src': packet[packet.transport_layer].srcport, 'dst': packet[packet.transport_layer].dstport}
                ports.append(dic_)
                ports.append(packet[packet.transport_layer].dstport)
        
        return ip_addresses, ports
    
    # 错误和警告分析：
    def error_warning_analysis(self):
        error = 0

        warning = 0

        for packet in self.cap:
            if hasattr(packet, 'sniff_timestamp') and hasattr(packet, 'frame_info'):
                if 'error' in packet.sniff_timestamp:
                    error += 1
                elif 'warning' in packet.sniff_timestamp:
                    warning += 1
                
        print(f'Number of Errors: {error}')

        print(f'Number of Warning: {warning}')
    
    # 应用层分析
    """

        深入分析应用层协议，如 HTTP。

        查看网页请求、响应、文件下载等。

    """

    def http_analysis(self):
        for packet in self.cap:
            if 'HTTP' in packet:
                if hasattr(packet.http, 'request_method'):
                    print(f"HTTP Request Method: {packet.http.request_method}")
                if hasattr(packet.http, 'request_url'):
                    print(f"HTTP URI: {packet.http.request_url}")
                if hasattr(packet.http, 'response_code'):
                    print(f"HTTP Response Code: {packet.http.response_code}")
                print(f"---")
            


    # 时序分析：
    """
    
        查看通信的时间戳信息，了解通信的时间模式。

        检查延迟、响应时间等。

    """

    def time_analysis(self):
        for packet in self.cap:
            print(f"Timestamp: {datetime.utcfromtimestamp(float(packet.sniff_timestamp))}")
            print(f"---")

    # 流量过滤和细节分析：

    """

        使用 Wireshark 的过滤功能，筛选出特定的流量。

        对特定通信进行深入分析，查看数据包的详细信息。

    """

    def filter_and_detail_analysis(self, filter_expression):

        def filter_packet(packet):
            return filter_expression in packet
        
        self.cap.apply_on_packets(filter_packet)

        details = ''
        for packet in self.cap:
            # print(f"Packet Details:")
            # print(f"---")
            # print(f"Frame Number: {packet.number}")
            # print(f"Frame Length: {packet.length}")
            # print(f"Capture Length: {packet.captured_length}")
            # print(f"Arrival Time: {datetime.utcfromtimestamp(float(packet.sniff_timestamp))}")
            detail = f"""Packet Details:
---
Frame Number: {packet.number}, \
Frame Length: {packet.length}, \
Capture Length: {packet.captured_length}\
Arrival Time: {datetime.utcfromtimestamp(float(packet.sniff_timestamp))}
            """
            
            # 访问 Ethernet II 层信息
            if 'Ethernet' in packet:
                eth_layer = packet.eth
                # print(f"Ethernet Source: {eth_layer.src}")
                # print(f"Ethernet Destination: {eth_layer.dst}")
                # print(f"Ethernet Type: {eth_layer.type}")
                layer_info = f"""Ethernet Source: {eth_layer.src} \
Ethernet Destination: {eth_layer.dst} \
Ethernet Type: {eth_layer.type}
                            """
            
            # 访问 IPv6 层信息
            if 'IPv6' in packet:
                ipv6_layer = packet.ipv6
                # print(f"IPv6 Source: {ipv6_layer.src}")
                # print(f"IPv6 Destination: {ipv6_layer.dst}")
                layer_info = f"""
IPv6 Source: {ipv6_layer.src} \
IPv6 Destination: {ipv6_layer.dst}
                            """

            # 访问 UDP 层信息
            if 'UDP' in packet:
                udp_layer = packet.udp
                # print(f"UDP Source Port: {udp_layer.srcport}")
                # print(f"UDP Destination Port: {udp_layer.dstport}")
                layer_info = f"""
UDP Source Port: {udp_layer.srcport} \
UDP Destination Port: {udp_layer.dstport}
                            """

            # 访问数据层信息
            if 'DATA' in packet:
                data_payload = getattr(packet.data, 'data', '')
                # print(f"Data: {data_payload}")
                layer_info = f"""
Data: {data_payload} \
                            """

            details += detail + '\n' + layer_info + '\n---\n'
        with open('E:\Centrale Nantes\AI\A2\Projet1\Practice\Details.txt', 'w') as file:
            file.write(details)

        

    # 安全分析

    """

        检查是否有异常的或恶意的网络活动。

        查找潜在的攻击、扫描或其他不寻常的行为。

    """
    def security_analysis(self):
        for packet in self.cap:
            # 检查通信中的大量数据包
            if int(packet.length) > 1500:
                print(f"Potential large Data Transfer: {packet.number} - {packet.length} bytes")

            # 检查DNS查询中的可疑域名
            if 'DNS' in packet and 'Queries' in packet.dns:
                for query in packet.dns.queries:
                    # malicious.com 可选更改
                    if 'malicious.com' in query.qry_name:
                        print(f"Suspicious DNS Query: {packet.number} - {query.qry_name}")
            
            # 检查HTTP请求中的异常行为
            if 'HTTP' in packet and 'request_method' in packet.http:
                if packet.http.request_method.lower() == 'get' and 'cmd' in packet.http.request_uri.lower():
                    print(f"Potential Command Injection: {packet.number} - {packet.http.request_uri}")
            


    
    # 设备和用户识别：
    
    """

        根据 IP 地址和 MAC 地址，识别网络中的设备。

        查找与特定用户或设备相关的通信。

    """ 
    def device_user_identification(self):
        for packet in self.cap:
            if 'IP' in packet and 'ETH' in packet:
                print(f"Source IP: {packet.ip.src}")   
                print(f"Source MAC: {packet.eth.src}")
                print(f"---")


    # TCP 三次握手检查
    def tcp_handshake_analysis(self):
        
        for packet in self.cap:
            if 'TCP' in packet:
                # 提取TCP标志位
                flags = int(packet.tcp.flags, 16)

                # 判断是否是SYN
                if flags & 0x02 != 0:
            
                    print(f"SYN packet:"
                          f"Source: {packet.ip.src if hasattr(packet, 'ip') else packet.ipv6.src}," 
                          f"Destination: {packet.ip.dst if hasattr(packet, 'ip') else packet.ipv6.dst},"
                          f"Port: {packet.tcp.srcport}")

                    # 判断是否是第一个SYN
                    if flags & 0x10 == 0:
                        print("First connection with server")
                    
                # 判断是否是ACK
                if flags & 0x10 != 0:
                    print(f"ACK packet"
                          f"Source: {packet.ip.src if hasattr(packet, 'ip') else packet.ipv6.src},"
                          f"Destination: {packet.ip.dst if hasattr(packet, 'ip') else packet.ipv6.dst}," 
                          f"Port: {packet.tcp.srcport}")

                    # 判断是否是第一个ACK
                    if flags & 0x02 == 0:
                        print("Server responds to connection for the first time")
                    


if __name__ == '__main__':

    # constant
    filepath = 'E:\Centrale Nantes\AI\A2\Projet1\Practice\cap_src.pcap'

    tshark_path = 'D:\\Wireshark\\tshark.exe'

    cap = CaptureFile(filepath, tshark_path)

    # # analysis of protocols
    # protocols = cap.protocol_analysis()
    # print(protocols)

    # # IP 地址和端口分析：
    # ip_addresses, ports = cap.ip_port_analysis()
    # print(f"ip_addresses:\n{ip_addresses}")
    # print(f"ports:\n{ports}")

    # # 应用层分析
    # cap.http_analysis()

    # # 时序分析：
    # cap.time_analysis()

    # 流量过滤和细节分析：
    filter_expression = '2a01:cb06:8009:64c6:61aa:69d1:5aee:d7c8'
    cap.filter_and_detail_analysis(filter_expression)

    # # 设备和用户识别：
    # cap.device_user_identification()

    # # TCP 三次握手检查
    # cap.tcp_handshake_analysis()






