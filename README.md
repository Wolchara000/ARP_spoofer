# SIMPLE PYTHON ARP_spoofer

For this to work you need to install scapy module (https://scapy.readthedocs.io/en/latest/)

```
pip install --pre scapy[basic]
```

How to use:
```
change:

# VARS
target_ip = "192.168.1.110"
spoof_ip = "192.168.1.1"

to the values you need
```

Usage example:
```
############### Simple ARP SPOOFER by Wolchara000 ###############
192.168.1.110 and 192.168.1.1 were spoofed. You are MITM now!
[+] Send 8 Packets^C
[+]CTRL+C is detected. Stopping Spoofer.

Spoofed MAC's restored
```
Don't forget to:
```
echo 1> /proc/sys/net/ipv4/ip_forward
```
