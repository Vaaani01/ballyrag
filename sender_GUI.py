from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Define receiver IP
receiver_ip = "http://100.67.37.173:5000/play"  # Change IP

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the URL and timestamp from the form
        video_url = request.form.get("url")
        timestamp = request.form.get("timestamp")

        # Validate inputs
        if video_url and timestamp:
            data = {"url": video_url, "time": timestamp}
            try:
                # Send POST request to receiver (target device)
                res = requests.post(receiver_ip, json=data)
                # Show response or error message
                if res.status_code == 200:
                    return f"Video playing at {timestamp} seconds on target device."
                else:
                    return "Error: Unable to send the video."
            except requests.exceptions.RequestException as e:
                return f"Error: {e}"

    return render_template("index.html")  # Render form

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)  # You can use a different port for sender
