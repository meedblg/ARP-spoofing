# ARP-spoofing
A lightweight ARP spoofing tool built with Python, designed for authorized penetration testing and network security assessments.

## Features

Spoofs ARP tables between a target host and the network gateway

Automatically resolves MAC addresses for given IP addresses

Restores original ARP tables on exit (graceful cleanup)

Supports both IPv4 target and router IP via command-line options

## Requirements 

Scapy – packet manipulation library

Root / administrator privileges (required for raw socket operations)

optparse (stdlib, no extra install needed)

## Installation

git clone https://github.com/meedblg/ARP-spoofer.git

cd ARP-spoofer

## Usage

sudo python3 arp_spoofer.py -t <TARGET_IP> -r <ROUTER_IP>

## Options

-t	--target	Target host IP address

-r	--router	Gateway / router IP address

## Example

sudo python3 ARP-spoofer.py -t 192.168.1.100 -r 192.168.1.1

Press Ctrl+C to stop the attack and restore ARP tables automatically.

