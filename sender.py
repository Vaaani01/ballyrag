import requests
receiver_ip = "http://[IP_address]/play"


# Input manually for now
video_url = input("Enter YouTube video URL: ")
timestamp = input("Enter current time (in seconds): ")

data = {
    "url": video_url,
    "time": timestamp
}

# Input manually for now
res = requests.post(receiver_ip, json=data)
try:
    print("Response:", res.json())
except:
    print("Response content:", res.text)

