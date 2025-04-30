from flask import Flask, request
import webbrowser
import threading
import socket

app = Flask(__name__)

# --- Flask route to receive video request ---
@app.route("/play", methods=["POST"])
def convert_to_seconds(timestamp_str):
    parts = timestamp_str.strip().split(":")
    parts = list(map(int, parts))

    if len(parts) == 1:
        return parts[0]  # already in seconds
    elif len(parts) == 2:
        minutes, seconds = parts
        return minutes * 60 + seconds
    elif len(parts) == 3:
        hours, minutes, seconds = parts
        return hours * 3600 + minutes * 60 + seconds
    else:
        return 0  # fallback

def play_video():
    data = request.get_json()
    url = data.get("url")
    timestamp = data.get("time")

    if url and timestamp is not None:
        total_seconds = convert_to_seconds(timestamp)
        separator = '&' if '?' in url else '?'
        final_url = f"{url}{separator}t={total_seconds}s"
        print("Opening:", final_url)
        webbrowser.open(final_url)
        return {"status": "success", "url": final_url}, 200
    else:
        return {"error": "Invalid input"}, 400


# --- UDP listener for discovery ---
def listen_for_discovery():
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_sock.bind(('', 9999))  # Listen on all interfaces, port 9999

    while True:
        msg, addr = udp_sock.recvfrom(1024)
        if msg.decode() == "DISCOVER_RECEIVERS":
            udp_sock.sendto(b"RECEIVER_HERE", addr)

# --- Start UDP listener in background ---
threading.Thread(target=listen_for_discovery, daemon=True).start()

# --- Run Flask server ---
app.run(host='0.0.0.0')


# from flask import Flask, request
# import webbrowser

# app = Flask(__name__)

# @app.route("/play", methods=["POST"])
# def play_video():
#     data = request.get_json()
#     url = data.get("url")
#     timestamp = data.get("time")

#     if url and timestamp is not None:
#         # Add timestamp to URL
#         final_url = f"{url}&t={timestamp}"
#         webbrowser.open(final_url)
#         return {"status": "success"}, 200  # ✅ Send valid JSON back
#     else:
#         return {"error": "Invalid input"}, 400  # ❌ Also in JSON

# app.run(host='0.0.0.0')
