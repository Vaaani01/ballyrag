ballyrag 🎭▶️

ballyrag is a lightweight Python-based tool that allows you to remotely trigger YouTube video playback on another device.
Run a small Python server on your mobile and send a simple POST request from your laptop — and the video plays✨
🚀 How It Works

  Device A (Sender):

        Run sender.py

        Enter the target device IP, YouTube URL, and timestamp.

        Sends a POST request to the receiver.

  Device B (Receiver):

        Run receiver.py

        Waits for incoming POST requests.

        On receiving the URL and time, it opens the YouTube video at the specified timestamp in the browser.

⚙️ Requirements

    Python 3.8+

    Libraries:

        Flask (pip install flask)

        Requests (pip install requests)

    Both devices should be on the same network (e.g., hotspot, Wi-Fi).

🛠️ Setup Instructions

    Install Python and necessary libraries on both devices:

pip install flask requests

    On Device B (mobile / target device):

python3 receiver.py

    On Device A (your laptop):

python3 sender.py

    Enter:

        Target IP address (e.g., http://192.168.0.105:5000/play)

        YouTube Video URL

        Timestamp in seconds

    The video will automatically open on Device B’s browser!

📈 Future Enhancements (Planned 🚧)

  - Deploy server permanently (setup Flask/APACHE server).
  
  - Handle multiple devices at once.
  
  - Robust server design (no crash during high usage).
  
  - Force device registration (Access Point Broadcasting).
  
  - Switch backend server from Flask to Apache/Nginx for stability.
  
  - Auto APK generator to make PhantomPlay usable on any Android device.
  
  - Link generation for easy triggering without IP typing.
  
  - Browser-to-browser direct communication.
  
  - Robustness testing and improvements.

👩‍💻 Author : Vaaani01
