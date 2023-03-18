import json
from youtube.basic import Basic

class Channel(Basic):
    def __init__(self, channel_id: str):
        """Инициализирует по ID канала.
               При создании экземпляра инициализируются атрибуты:
               __channel_id:
               __channel_title
               __channel_description
               __channel_url
               __subscribers_count
               __video_count
               __view_count

               """
        super().__init__()
        self.__channel_id = channel_id
        self.__channel_title = self.channel['items'][0]['snippet']['title']
        self.__channel_description = self.channel['items'][0]['snippet']['description']
        self.__channel_url = "https://www.youtube.com/" + self.channel_id
        self.__subscribers_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.__video_count = self.channel['items'][0]['statistics']['videoCount']
        self.__view_count = self.channel['items'][0]['statistics']['viewCount']


    def __str__(self):
        return f'Yotube-канал: {self.channel_title}'

    def __add__(self, other):
        """Складывает по колличеству подписчиков"""
        return self.subscribers_count + other.subscribers_count

    def __lt__(self, other):
        """Сравнивает < по колличеству подписчиков"""
        return self.subscribers_count < other.subscribers_count

    def __gt__(self, other):
        """Сравнивает > по колличеству подписчиков"""
        return self.subscribers_count > other.subscribers_count

    def __ge__(self, other):
        return self.subscribers_count >= other.subscribers_count

    def __le__(self, other):
        return self.subscribers_count <= other.subscribers_count

    @property
    def channel_id(self) -> str:
        """Возвращает ID канала"""
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, value: str):
        if value != self.__channel_id:
            print('запрещено')
        else:
            self.__channel_id = value

    @property
    def channel_title(self) -> str:
        """Возвращает title канала"""
        return self.__channel_title

    @property
    def channel_description(self) -> str:
        """Возвращает title канала"""
        return self.__channel_description

    @property
    def channel_url(self) -> str:
        """Возвращает url канала"""
        return self.__channel_url

    @property
    def subscribers_count(self) -> int:
        """Возвращает subscribers_count канала"""
        return self.__subscribers_count

    @property
    def video_count(self) -> str:
        """Возвращает video_count канала"""
        return self.__video_count

    @property
    def view_count(self) -> str:
        """Возвращает view_count канала"""
        return self.__view_count

    @property
    def channel(self) -> dict:
        """Возвращает информацию о канале"""
        return self._get_channel(channel_id=self.channel_id)



    def print_info(self) -> json:
        """Вывод информации о канале на экран"""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self):
        with open("../filename.json", "w", encoding="UTF-8") as file:
            data = {
                "id": self.__channel_id,
                "title": self.__channel_title,
                "description": self.__channel_description,
                "url": self.__channel_url,
                "subscriber_count": self.__subscribers_count,
                "video_count": self.__video_count,
                "views_count": self.__view_count
            }
            print(json.dump(data, file, indent=2, ensure_ascii=False))


# chnl1 = Channel('UC3n7MKHEwA9xXBErhXYZbMQ')
# chnl2 = Channel('UCglNYRt1fJ3RmDrWpVG1Bsg')
# chnl1.print_info()

