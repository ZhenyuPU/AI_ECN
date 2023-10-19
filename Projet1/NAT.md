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
Ce n'est que lorsqu'un appareil interne demande une ressource réseau externe que le périphérique NAT attribue une adresse IP publique disponible à l'appareil, puis libère l'adresse une fois la connexion fermée, la rendant ainsi disponible pour une utilisation par d'autres appareils.
### NAPT

网络地址端口转换，这个是需要考虑端口的，需要进行源地址和目的地址的相互转换，当源地址发送出来时，NAT主机会改写源地址，使其发出的数据能够到达目的地址；同时当外网主机发送数据时，其地址也会被改写使其成功被内网主机接收。

Traduction du port d'adresse réseau, cela nécessite de prendre en compte le port, et l'adresse source et l'adresse de destination doivent être converties l'une en l'autre. Lorsque l'adresse source est envoyée, l'hôte NAT réécrira l'adresse source afin que les données envoyées puissent atteindre le adresse de destination ; en même temps, lorsque l'hôte externe Lorsque l'hôte du réseau envoie des données, son adresse sera également réécrite afin qu'elle puisse être reçue avec succès par l'hôte intranet.

## 根据映射规则分类：
### 完全圆锥型：
Type de cône complet :

所有从同一个内网的（IP，端口）发送出来的请求都会被映射到同一个外网（IP，端口），且任何一个外网主机都可以通过访问映射后的公网地址，实现访问位于内网的主机设备功能。
Toutes les demandes envoyées depuis le même réseau interne (IP, port) seront mappées vers le même réseau externe (IP, port), et tout hôte de réseau externe pourra accéder à l'adresse de réseau public mappée pour accéder à l'emplacement. Fonctions du périphérique hôte Intranet.


### 受限圆锥型：

所有从同一个内网的发送出来的请求都会被映射到通过一个外网。

唯 iAddr:iPort 曾经发送数据包到外部主机（nAddr:any），外部主机才能经由发送数据包给 eAddr:ePort 到达 iAddr:iPort。

Comme la première, toutes les requêtes envoyées depuis le même réseau interne seront mappées via un réseau externe.

Mais ce n'est que si l'intranet iAddr:iPort a déjà envoyé un paquet de données à un hôte externe (nAddr:any), que l'hôte externe peut atteindre iAddr:iPort en envoyant un paquet de données à eAddr:ePort.

### 受限端口圆锥型：

只有特定的端口才能被client接收，即使ip一样也不行。

Similaire au précédent, mais seuls des ports spécifiques peuvent être reçus par le client, même si l'IP est la même.

### 对称型：

每次向外传递都需要建立新的映射关系。
首先只有当外部主机接收过内部主机的信息时，才能向内部主机发送数据包，并且外部主机无法了解与内部主机的映射关系，因而无法直接向内部主机发送数据包，但是可以通过一些穿越技术做到。


Chaque transfert vers l'extérieur nécessite l'établissement d'une nouvelle relation de mappage.
Tout d'abord, ce n'est que lorsque l'hôte externe a reçu des informations de l'hôte interne qu'il peut envoyer des paquets de données à l'hôte interne. L'hôte externe ne peut pas comprendre la relation de mappage avec l'hôte interne, il ne peut donc pas envoyer directement des paquets de données à l'hôte interne. Cependant, cela peut être fait grâce à certaines technologies de traversée.


### 安全性：

对称型 > 端口受限圆锥型 > 受限圆锥型 > 完全圆锥型

Symétrique > Port conique restreint > Conique restreint > Conique complet

## 优点：

解决了IPV4地址短缺的问题，并且对于家庭和小型办公室而言，申请一个独立的IP代价较高，使用NAT可以降低成本。

Cela résout le problème de la pénurie d'adresses IPV4. 

Et pour les familles et les petits bureaux, demander une adresse IP indépendante coûte plus cher. L'utilisation de NAT peut réduire les coûts.

## 缺点：

首先是私有IP不唯一导致无法连接互联网，这意味着对一些因特网协议产生影响， 一些需要初始化从外部网络建立的TCP协议和无状态协议无法实现。并且除非NAT设立了规则否则无法将数据包送到指定的地址。

La première est que l'adresse IP privée n'est pas unique, ce qui entraîne l'impossibilité de se connecter à Internet, ce qui signifie que certains protocoles Internet comme TCP et protocoles sans état qui doivent être initialisés à partir du réseau externe ne peuvent pas être mis en œuvre. 

Et à moins que NAT ne définisse des règles, le paquet de données ne peut pas être envoyé à l'adresse spécifiée.

