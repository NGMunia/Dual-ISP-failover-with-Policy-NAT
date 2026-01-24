

# DUAL-ISP Failover with Policy NAT

- The topology is to demostrate Failover when the border router is connected to two ISPs for redundancy.
- In order to track the status of the main ISP connectivity, IPSLA with object tracking is used.
- Ff tracking goes down, routing switches automatically to backup ISP connection, until the main connection is re-established.
- The router does this with the help of Policy NAT using route maps mapping to tracking, ISP-facing interfaces, and subnets to be NATed.
- Fortigate firewall is used to protect the LAN using Zone-based policy firewall.

![Routing](https://img.shields.io/badge/Routing-BGP%20%7C%20OSPF-orange)
![NAT](https://img.shields.io/badge/NAT-Policy_NAT-green)
![Security](https://img.shields.io/badge/Security-ZBF-blue)

---


![Topology](/Topology.PNG)

## Quick Overview

- **Routing:** OSPF (with static route redistribution)
- **Security:** Zone-Based Firewall, Policy NAT
- **Monitoring:** IPSLA with Object tracking

---

## Configuration on Cisco Router Policy NAT

```bash

no ip http secure-server
ip nat inside source route-map ISP-1 interface Ethernet0/2 overload
ip nat inside source route-map ISP-2 interface Ethernet0/3 overload
ip route 0.0.0.0 0.0.0.0 Ethernet0/2 44.67.28.1 track 1
ip route 0.0.0.0 0.0.0.0 Ethernet0/3 72.73.74.1 10
ip ssh version 2
!
ip access-list standard nat-acl
 permit 10.0.0.1
 permit 192.168.10.0 0.0.0.255
 permit 192.168.11.0 0.0.0.255
!
ip sla 1
 icmp-echo 44.67.28.1 source-interface Ethernet0/2
 frequency 10
ip sla schedule 1 life forever start-time now
ipv6 ioam timestamp
!
route-map ISP-2 permit 10
 match ip address nat-acl
 match interface Ethernet0/3
!
route-map ISP-1 permit 10
 match ip address nat-acl
 match track  1
 match interface Ethernet0/2
 ```

---

## Verification on Fortigate
![Topology](Fortigate.PNG)

----

## Verification on End-User PC
![Topology](PC.PNG)