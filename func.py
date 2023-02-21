import os
import json

from googleapiclient import channel
from googleapiclient.discovery import build


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
#api_key: str = os.getenv('API_KEY')

# создать специальный объект для работы с API
#youtube = build('youtube', 'v3', developerKey=api_key)
#Alex Burkan
#channel_id = 'UCah9pzaxpAeDLQ20hcufc2g'

#channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

#print(json.dumps(channel, indent=2, ensure_ascii=False))

class Channel:
    channel_id = ''

    def __init__(self, channel_id):
        self.channel_id = channel_id

        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()


    def print_info(self):
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


coldsteel = Channel('UC3n7MKHEwA9xXBErhXYZbMQ')
coldsteel.print_info()