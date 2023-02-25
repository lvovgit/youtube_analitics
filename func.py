import json
import os

import fixture as fixture
# from googleapiclient import channel
from googleapiclient.discovery import build


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
# api_key: str = os.getenv('API_KEY')

# создать специальный объект для работы с API
# youtube = build('youtube', 'v3', developerKey=api_key)
# Alex Burkan
# channel_id = 'UCah9pzaxpAeDLQ20hcufc2g'

# channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

# print(json.dumps(channel, indent=2, ensure_ascii=False))

class Channel:
    channel_id = ''
    data = {}

    def __init__(self, channel_id):
        # self.channel_id = channel_id
        # self.channel_title = channel_title
        # self.channel_description = channel_description
        # self.channel_link = channel_link
        # self.subscribers_count = subscribers_count
        # self.video_count = video_count
        # self.view_count = view_count

        # channel_title, channel_description, channel_link, subscribers_count, video_count, view_count

        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        self.__channel_id = self.channel['items'][0]['id']
        self.channel_title = self.channel['items'][0]['snippet']['title']
        self.channel_description = self.channel['items'][0]['snippet']['description']
        self.channel_link = "https://www.youtube.com/" + self.channel_id
        self.subscribers_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']
        # self.data = {"id": self.__channel_id, "title": self.channel_title}

    def __str__(self):
        return f'Yotube-канал: {self.channel_title}'

    def __add__(self, other):
        return self.subscribers_count + other.subscribers_count

    def __lt__(self, other):
        return self.subscribers_count < other.subscribers_count

    def __gt__(self, other):
        return self.subscribers_count > other.subscribers_count

    def __ge__(self, other):
        return self.subscribers_count >= other.subscribers_count

    def __le__(self, other):
        return self.subscribers_count <= other.subscribers_count

    @classmethod
    def get_service(cls):
        api_key: str = os.getenv('API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def print_info(self):
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self):
        with open("filename.json", "w", encoding="UTF-8") as file:
            data = {
                "id": self.__channel_id,
                "title": self.channel_title,
                "description": self.channel_description,
                "url": self.channel_link,
                "subscriber_count": self.subscribers_count,
                "video_count": self.video_count,
                "views_count": self.view_count
            }
            print(json.dump(data, file, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, value: str):
        if value != self.__channel_id:
            print('запрещено')
        else:
            self.__channel_id = value


chnl1 = Channel('UC3n7MKHEwA9xXBErhXYZbMQ')
chnl2 = Channel('UCglNYRt1fJ3RmDrWpVG1Bsg')
# chnl1.print_info()
# print(chnl1.channel_title)
# chnl1.channel_id = 'sdfdsf'
# print(Channel.get_service())
# print(chnl1.to_json())
# print(chnl1 + chnl2)
