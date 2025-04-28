
from flask import Flask, request
import webbrowser

app = Flask(__name__)

@app.route("/play", methods=["POST"])
def play_video():
    data = request.get_json()
    url = data.get("url")
    timestamp = data.get("time")

    if url and timestamp is not None:
        # Add timestamp to URL
        final_url = f"{url}&t={timestamp}"
        webbrowser.open(final_url)
        return {"status": "success"}, 200  # ✅ Send valid JSON back
    else:
        return {"error": "Invalid input"}, 400  # ❌ Also in JSON

app.run(host='0.0.0.0')
