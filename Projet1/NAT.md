# NAT

## NAT简介

NAT是指从私有IP地址到公有地址的映射，实际上是来解决IPV4网址数量不够的问题。由于网址数量有限，为了让更多的IP地址能够访问公网，我们需要建立一种映射连接私有与公有，这就是NAT的作用。允许多个主机共享一个或几个公共IP地址，从而实现高效的网络连接。

NAT fait référence à la translation d'adresses IP privées en adresses IP publiques, et en fait elle est essentiellement conçue(conçevoir) pour résoudre le problème de pénurie d'adresses IPv4. En raison du nombre limité d'adresses IP disponibles, afin de permettre à un plus grand nombre d'adresses IP d'accéder à l'Internet, il est nécessaire de créer une correspondance entre les adresses privées et les adresses publiques, c'est là que réside l'utilité de la NAT. Elle autorise plusieurs hôtes à partager une ou plusieurs adresses IP publiques, permettant ainsi une connectivité réseau efficace.

## NAT的分类：
### Statistic Nat

不考虑端口，只建立私有地址和公有IP的关系。

Quel que soit le port, on envisage de établir une relation entre IP privée et IP pubilque.

Par exemple, iAddr: 199.2.2.3 et EAddr: 1.2.3.4

### Dynamic NAT
La translation entre les adresses IP privées et les adresses IP publiques est temporaire et attribuée dynamiquement. 
Seulement lorsqu'un appareil interne demande une ressource réseau externe, le routeur NAT attribue IP publique disponible à l'appareil, puis une fois la connexion fermée, le port est ainsi disponible pour l'autre appareil.

### NAPT

网络地址端口转换，这个是需要考虑端口的，需要进行源地址和目的地址的相互转换，当源地址发送出来时，NAT主机会改写源地址，使其发出的数据能够到达目的地址；同时当外网主机发送数据时，其地址也会被改写使其成功被内网主机接收。

Traduction du port d'adresse réseau

Cela nécessite de prendre en compte le port.

Lorsque l'adresse source est envoyée, l'hôte NAT réécrit IP afin que les données envoyées puissent atteindre l'adresse de destination ; en même temps, lorsque l'hôte externe  envoie des données, son adresse sera également réécrite afin d'être reçue avec succès par l'hôte intranet.

## 根据映射规则分类：
### 完全圆锥型：
Type de cône complet :

所有从同一个内网的（IP，端口）发送出来的请求都会被映射到同一个外网（IP，端口），且任何一个外网主机都可以通过访问映射后的公网地址，实现访问位于内网的主机设备功能。
Toutes les demandes envoyées depuis le même réseau interne (IP, port) seront mappées vers le même réseau externe (IP, port), et tout hôte de réseau externe peut accéder à l'adresse de réseau public mappée pour accéder à l'emplacement. 

### 受限圆锥型：

所有从同一个内网的发送出来的请求都会被映射到通过一个外网。

唯 iAddr:iPort 曾经发送数据包到外部主机（nAddr:any），外部主机才能经由发送数据包给 eAddr:ePort 到达 iAddr:iPort。

Comme la première, toutes les requêtes envoyées depuis le même réseau interne seront mappées via un réseau externe.

Mais ce n'est que si l'intranet iAddr:iPort a déjà envoyé un paquet à un hôte externe (hAddr:any), que l'hôte externe peut atteindre iAddr:iPort en envoyant un paquet à eAddr:ePort.

### 受限端口圆锥型：

只有特定的端口才能被client接收，即使ip一样也不行。

Similaire au précédent, mais seuls des ports spécifiques peuvent être reçus par le client, même si l'IP est la même.

### 对称型：

每次向外传递都需要建立新的映射关系。
首先只有当外部主机接收过内部主机的信息时，才能向内部主机发送数据包，并且外部主机无法了解与内部主机的映射关系，因而无法直接向内部主机发送数据包，但是可以通过一些穿越技术做到。

Comme le type conique à port restreint, il necessite de la correspondance de IP, de port et de la destination. Quand la destination est differente, une mappage differente est etablie.

Seulement lorsque IP, le port et la destination sont correspondantes, l'hôte externe peut envoyer des paquets à l'hôte interne. 

Mais l'hôte externe ne peut pas comprendre la relation de mappage avec l'hôte interne, il ne peut donc pas envoyer directement des paquets à l'hôte interne. Cependant, cela peut être fait grâce à certaines technologies de traversée.


### 安全性：

对称型 > 端口受限圆锥型 > 受限圆锥型 > 完全圆锥型
Par conséquent, 
Symétrique > Port conique restreint > Conique restreint > Conique complet

## 优点：

解决了IPV4地址短缺的问题，并且对于家庭和小型办公室而言，申请一个独立的IP代价较高，使用NAT可以降低成本。

Cela résout le problème de la pénurie d'adresses IPV4. 

Et pour les familles et les petits bureaux, demander une adresse IP indépendante coûte plus cher. L'utilisation de NAT peut réduire les coûts.

## 缺点：

首先是私有IP不唯一导致无法连接互联网，这意味着对一些因特网协议产生影响， 一些需要初始化从外部网络建立的TCP协议和无状态协议无法实现。并且除非NAT设立了规则否则无法将数据包送到指定的地址。

Mais car IP privée n'est pas unique, ce qui entraîne l'impossibilité de se connecter à Internet. Cela signifie que certains protocoles Internet ne peuvent pas être mis en œuvre. 

Et Pour que le paquet puisse être envoyé à l'adresse spécifiée, il necessite de definir les regles de la translation de NAT.

