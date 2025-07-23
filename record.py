import subprocess
import datetime
import os

channel = os.getenv("KICK_CHANNEL", "xqc")
timestamp = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"{channel}_{timestamp}.mp4"

command = [
    "streamlink",
    f"https://kick.com/{channel}",
    "best",
    "-o", output_file
]

print(f"Grabando canal: {channel} → {output_file}")
subprocess.run(command)
