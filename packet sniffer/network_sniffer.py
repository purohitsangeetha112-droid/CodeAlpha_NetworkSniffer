from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

# Global counter to keep track of packet numbers
packet_count = 0

def analyze_packet(packet):
    global packet_count
    packet_count += 1

    # We only analyze IPv4 packets
    if IP in packet:
        # 1. Gather basic information
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol_num = packet[IP].proto
        packet_length = len(packet)
        timestamp = datetime.now().strftime("%H:%M:%S")

        # 2. Determine Protocol Name
        proto_name = "Unknown"
        if protocol_num == 6:
            proto_name = "TCP (Web/Email)"
        elif protocol_num == 17:
            proto_name = "UDP (DNS/Video)"
        elif protocol_num == 1:
            proto_name = "ICMP (Ping)"

        # 3. Get Port numbers if it's TCP or UDP
        src_port = "N/A"
        dst_port = "N/A"
        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport

        # 4. Print the formatted output
        print("\n" + "="*55)
        print(f"📦 PACKET #{packet_count} | ⏰ Time: {timestamp} | 📏 Size: {packet_length} bytes")
        print("-" * 55)
        print(f"🌐 Source IP      : {src_ip}")
        print(f"🎯 Destination IP : {dst_ip}")
        print(f"📡 Protocol       : {proto_name} (Code: {protocol_num})")
        
        if src_port != "N/A":
            print(f"🔌 Source Port    : {src_port}")
            print(f"🔌 Dest Port      : {dst_port}")

        # 5. Analyze the Payload (Data)
        if Raw in packet:
            payload = packet[Raw].load
            try:
                # Try to decode as text
                payload_str = payload.decode('utf-8', errors='ignore')
                # Remove newlines so it prints nicely
                clean_payload = payload_str.replace('\n', ' ').replace('\r', '')
                print(f"📝 Payload (Data) : {clean_payload[:50]}...")
            except Exception:
                print("📝 Payload (Data) : [Binary Data / Encrypted]")
        else:
            print("📝 Payload (Data) : [No Data]")
        print("="*55)

def start_sniffer():
    print("🚀 Starting Advanced Network Sniffer...")
    print("⏳ Waiting for packets... (Open Chrome to generate traffic)\n")
    
    # Capture 5 packets (kept it at 5 so the screenshot doesn't get too long)
    sniff(prn=analyze_packet, count=5)

if __name__ == "__main__":
    start_sniffer()