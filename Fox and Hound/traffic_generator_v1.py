#pip3 install scapy
## Probably could od without it - butttttt, it's easier with it.
from scapy.all import IP, send
import random
import threading
import time

def random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

def random_packet():
    src_ip = random_ip()
    dst_ip = random_ip()
    packet = IP(src=src_ip, dst=dst_ip)
    return packet

def send_packets(interval=1, count=10):
    for _ in range(count):
        packet = random_packet()
        print(f"Sending packet: {packet.summary()}")
        send(packet, verbose=False)
        time.sleep(interval)

def start_traffic_generator(threads=5, interval=0.5, packet_count=100):
    for _ in range(threads):
        threading.Thread(target=send_packets, args=(interval, packet_count)).start()

if __name__ == "__main__":
    start_traffic_generator(threads=3, interval=1, packet_count=10)

# Not sure if this will work effectively - but worth a try.
