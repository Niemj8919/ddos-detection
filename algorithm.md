# Algorithm for DDOS-Detection

## netflow的主要信息

(以提供的.pcap.flow文件为例)

- 时间戳 **StartTime**
- 持续时间 **Dur**,duration
- 协议类型 **Proto**,protocol
- 源IP **SrcAddr**,source address
- 方向 **Dir**,direction
- 目标IP **DstAddr**,destination address
- 源端口 **Sport**,source port
- 目标端口 **Dport**,destination port
- 数据流规模 **TolBytes**,total bytes
- 封包大小 **TolPkts**,total packets

主要关注的信息：
1. 时间间距（单位时间内的请求数量）
2. 源IP（源IP的数量，每个IP的请求数量）
3. 持续时间
4. 规模
5. TCP请求的方向

## 攻击特征

针对某一固定目标IP和端口的攻击特征
（传统的消耗目标资源的攻击方式）

- 大多为单向连接（TCP协议中为?> UDP协议中为->)
- 持续时间很短，趋向于0（单向连接时间为0）
- 时间间距很短，单位时间内大量请求
- 来自不同源IP的大小接近或者相等的请求包
- 来自同一IP的大量请求包
- 数据包的总和很大，消耗带宽

注意区分正常用户的流量

例如，当正常工作的服务器突然宕机时，会出现大量单向请求。

## 算法思路

首先筛选单向的连接（疑似攻击流量）

按目标地址进行排序得到连接数最大的认为是攻击的目标服务器

计算该目标地址接收到的数据包的平均时间间隔（单位为us）并得到攻击频率
