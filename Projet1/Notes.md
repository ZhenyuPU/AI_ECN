'''
Son numéro de téléphone : 02 40 37 15 78
Son nom d’utilisateur GitHub: M0ustach3

Il faudra voir avec Didier Lime pour le rendu de mi projet.

Pour vendredi prochain :
Une présentation rapide (~15mn) sur les différentes technologies existantes en réseau 

'''

# Projet 1

Points à aborder :
- TCP: Pour communiquer les informations entre les ordinateurs. Des poignées de mains et confirmations sont effectuées entre les extrémités d'envoie et de la reception pour garantir l'intégrité et la séquence.
- DNS: Une alternative du nom de domaine.
- UDP: Une convention de communiquer l'info rapide sans garantir l'intégrité et la séquence.
- HTTP: Une convention de hypertexte pour communiquer les pages, les videos...
- NAT: partager IP commun.
- les pare-feux: Contrôler le réseau pour se defendre de la violence malveillante.


Le modèle OSI : 
7 couches formant des briques s’ajoutant les unes sur les autres (voir photo).

La plupart du temps les ports ne dépassent pas 1000 donc critère intéressant.
Problème potentiel de données chiffrées.
Le NAT n’est utilisé qu’en IPv4 et centrale n’en utilise pas.
La signature d’un paquet s’appelle l’IOC (à creuser).
Certaines plages d’IP sont réservées en publique et ne sont donc utilisées qu’en local.
Éduroam utilise FreeRadius (à creuser aussi).
Il existe des bases de données d’ensemble de paquets malveillants et non malveillants, à nous de les trouver.
Il existe aussi des bases de malware et d’URL problématiques, potentiellement par le même site/entreprise que la base précédente.
Un problème à régler sera la taille des donnés extraites et comment la réduire.

+ apprendre à utiliser WireShark



MAC地址（Media Access Control address）是网络设备（如计算机、网络适配器、路由器等）在数据链路层（OSI模型的第二层）上的硬件地址。它是一个用于唯一标识网络设备的48位（或更少）地址。

MAC地址通常以十六进制表示，由6个字节组成，每两个字节之间用冒号或破折号分隔，例如：00:1A:2B:3C:4D:5E。这个地址是由设备的制造商分配的，因此它在同一网络中的设备应该具有唯一的MAC地址。

数据帧传输：在数据链路层，数据被封装为帧进行传输。每个帧都包含源MAC地址和目标MAC地址，以确保数据正确地从一个设备传输到另一个设备。在本地网络中，路由器和交换机使用MAC地址来决定将数据帧传送到哪个设备。

6 bytes -> 6*8 = 48 bits -> 12 * 4 bits(per hexadecimal digit) -> 12 digits




## OSI model

为了实现主机之间的相互沟通.

OSI模型（Open Systems Interconnection model）是一种用于理解和描述计算机网络功能的概念性框架。它将计算机网络的通信过程划分为七个不同的抽象层次，每个层次负责特定的功能，从而使得网络协议的设计和实现更为模块化。这七个层次从低到高分别是：

1. **物理层（Physical Layer）：**
   - 定义了网络硬件的物理连接和传输媒体（如电缆、光纤）的规范。
   - 主要关注比特流的传输，包括电压、电流、光脉冲等。

2. **数据链路层（Data Link Layer）：**
   - 负责在直连的两个节点之间提供可靠的数据传输。
   - 包括物理地址的定义（如MAC地址）、流量控制、错误检测和纠正等功能。

3. **网络层（Network Layer）：**
   - 主要关注数据在网络中的路由和转发。
   - 提供数据包的传输、路由和逻辑寻址。

4. **传输层（Transport Layer）：**
   - 提供端到端的通信控制，确保数据的可靠传输。
   - 主要协议有TCP（Transmission Control Protocol）和UDP（User Datagram Protocol）。

5. **会话层（Session Layer）：**
   - 管理会话（session）的建立、维护和结束。
   - 提供数据的同步和恢复功能。

6. **表示层（Presentation Layer）：**
   - 负责数据的格式化、加密和压缩，确保一个系统的应用层能理解另一个系统发送的数据。

7. **应用层（Application Layer）：** 如HTTP协议
   - 提供网络服务直接给用户或应用程序。
   - 包括各种网络应用，如文件传输、电子邮件、远程登录等。

每个层次的功能是相互独立的，上层通过下层提供的服务来完成自己的任务。这种分层的结构使得不同层次的协议和技术可以独立地进行发展和改进，而不会对整个系统产生太大的影响。

![1699568111496](https://cdn.statically.io/gh/ZhenyuPU/picx-images-hosting@master/20231109/1699568111496.fvp5kjyg360.webp)






## **WireShark**

混杂模式: 网络上所有地址都会被抓取, 网络适配器将接收经过物理网络传输的所有数据帧，而不仅仅是发送给适配器的那些。这包括发送到网络上的所有数据流量，而不仅仅是目标地址是本机的流量。如果不开启,那么网卡只接受正确发到本机的数据. 

方便网安人员检查网络 -> 黑客


**Ethernet**:

以太网（Ethernet）和无线局域网（WLAN）是两种不同类型的网络技术，它们之间存在一些关键的区别。以下是它们之间的主要区别：

1. **物理连接：**
   - **以太网：** 使用**物理电缆(如双绞线、光纤等)** 来连接设备。常见的以太网标准包括Ethernet和Fast Ethernet，它们使用不同的传输速率，例如10 Mbps和100 Mbps。
   - **WLAN：** 使用**无线信号传输数据**，通过Wi-Fi技术连接设备。这种无线连接使设备可以在没有物理电缆的情况下进行通信，提供了更大的灵活性和移动性。

2. **连接方式：**
   - **以太网：** 提供点对点的有线连接，通常通过交换机或集线器进行连接。
   - **WLAN：** 提供通过无线接入点（Access Point）连接的无线连接，支持多个设备同时通过无线信号进行通信。

3. **速度和性能：**
   - **以太网：** 通常提供更高的速度和稳定性，适用于需要较大带宽和低延迟的场景。
   - **WLAN：** 速度可能受到无线信号强度、干扰和其他因素的影响，因此在某些情况下可能会表现出较低的性能。

4. **安全性：**
   - **以太网：** 有线连接相对较为安全，因为攻击者需要物理接触电缆才能进行攻击。
   - **WLAN：** 无线信号可能受到窃听和干扰的威胁，因此需要采取额外的安全措施，如加密和访问控制，以保障网络安全。

5. **适用场景：**
   - **以太网：** 常用于固定位置的设备，例如台式计算机、服务器和网络设备。
   - **WLAN：** 适用于移动设备和需要灵活布局的场景，如笔记本电脑、智能手机和其他无线设备。




### 分析网络实例：

当进行网络分析时，具体的实例会根据你面临的问题或场景而有所不同。在这里，我将提供一个简单的网络分析示例，假设你想排查一个主机无法连接到互联网的问题。

**问题描述：**
一台主机无法通过浏览器连接到互联网。你希望使用Wireshark、PyShark和Scapy来分析网络流量，以查找问题的根本原因。

**步骤：**

1. **使用Wireshark捕获数据包：**
   - 打开Wireshark，并选择主机所在的网络接口。
   - 启动捕获，然后让用户尝试通过浏览器连接到互联网。
   - 停止捕获。

2. **分析Wireshark捕获的数据包：**
   - 打开捕获文件（例如，captured_traffic.pcap）。
   - 使用Wireshark过滤器，仅显示与主机IP地址相关的数据包。

3. **PyShark分析：**
   - 使用PyShark编写一个脚本，分析捕获的数据包，查看是否有与HTTP或DNS相关的问题。

```python
import pyshark

cap = pyshark.FileCapture('captured_traffic.pcap')

for packet in cap:
    if 'IP' in packet and 'HTTP' in packet:
        print(f'Timestamp: {packet.sniff_timestamp} | Source: {packet.ip.src} -> Destination: {packet.ip.dst} | HTTP Request: {packet.http.request_uri}')
```

   - 这个脚本将打印捕获文件中包含HTTP请求的数据包的一些基本信息。

4. **Scapy分析：**
   - 使用Scapy检查DNS流量，确保主机能够解析互联网域名。

```python
from scapy.all import *

packets = rdpcap('captured_traffic.pcap')

for packet in packets:
    if DNS in packet:
        print(f'Timestamp: {packet.time} | Source: {packet[IP].src} -> Destination: {packet[IP].dst} | DNS Request: {packet[DNS].qd.qname}')
```

   - 这个脚本将打印捕获文件中包含DNS请求的数据包的一些基本信息。

通过分析这些信息，你可能会发现主机的HTTP请求是否成功，是否有DNS解析问题，以及在网络中是否存在其他异常情况。这只是一个简单的例子，实际的网络分析可能需要更多的步骤和深入的研究，具体取决于问题的复杂性。




协议分析是通过检查网络数据包来深入了解各种网络协议的交互过程。在这个例子中，我将使用Wireshark工具进行协议分析。请注意，Wireshark提供了丰富的功能，本例中只是一个简单的入门示例。

**步骤：**

1. **捕获数据包：**
   - 打开Wireshark，并选择要捕获数据包的网络接口。
   - 启动捕获，然后进行一些网络活动（例如在浏览器中打开网页、执行ping命令等）。

2. **过滤特定协议：**
   - 在Wireshark捕获窗口的过滤框中输入过滤条件，以仅显示特定协议的数据包。
   - 例如，输入 `tcp`、`udp`、`http`、`dns` 等，以过滤相应的协议。

3. **查看数据包列表：**
   - 查看捕获到的数据包列表，每一行代表一个数据包。
   - 选择一个数据包，Wireshark将在下方的窗口中显示详细的协议信息。

4. **查看协议字段：**
   - 展开每个数据包的协议分层，查看各个协议字段的值。
   - 单击数据包中的每个协议，Wireshark将显示相关的字段和信息。

5. **理解协议交互过程：**
   - 对于HTTP，你可以查看HTTP请求和响应，了解客户端和服务器之间的交互。
   - 对于DNS，你可以查看DNS查询和响应，了解域名解析的过程。
   - 对于TCP和UDP，你可以查看源和目标端口、序列号、确认号等字段，了解数据包的传输过程。

6. **统计和分析：**
   - Wireshark提供了各种统计和分析工具，例如流量图、协议分布图等。
   - 使用这些工具可以更全面地了解捕获的网络流量。

这只是一个简单的协议分析示例。在实际情况中，你可能会处理更复杂的网络流量，需要更深入的分析。 Wireshark的强大功能和直观的界面使得深入协议分析变得相对容易。

