import socket
import time
import requests

def discover_receivers():
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp_sock.settimeout(2)  # wait max 2 seconds for replies

    message = b"DISCOVER_RECEIVERS"
    udp_sock.sendto(message, ('<broadcast>', 9999))

    receivers = set()
    start = time.time()

    while time.time() - start < 2:
        try:
            data, addr = udp_sock.recvfrom(1024)
            if data == b"RECEIVER_HERE":
                receivers.add(f"http://{addr[0]}:5000/play")
        except socket.timeout:
            break

    return list(receivers)

# --- Use discovered IPs ---
receiver_ips = discover_receivers()
print("Receivers found:", receiver_ips)

# --- Video input ---
video_url = input("Enter YouTube video URL: ")
timestamp = input("Enter timestamp (in seconds): ")

data = {
    "url": video_url,
    "time": timestamp
}

# --- Send video to all receivers ---
for ip in receiver_ips:
    try:
        res = requests.post(ip, json=data)
        print(f"Sent to {ip} Response:", res.json())
    except Exception as e:
        print(f"Failed to send to {ip}: {e}")

