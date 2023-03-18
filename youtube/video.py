import json
from youtube.basic import Basic
from errors.errors import YoutubeApiError

class Video(Basic):
    def __init__(self, video_id):
        """Инициализируется по id видео

        :param video_id:=-х9
        После создания экземпляра инициализируются адтрибуты:
        - video_name
        - views_count
        - like_count
        """
        super().__init__()
        try:
            self.__video_id = video_id
            if self.info_video['items']:
                self.__video_name = self.info_video['items'][0]['snippet']['title']
                self.__views_count = self.info_video['items'][0]['statistics']['viewCount']
                self.__like_count = self.info_video['items'][0]['statistics']['likeCount']

            else:
                raise YoutubeApiError

        except YoutubeApiError:
            self.__video_name = None
            self.__views_count = None
            self.__like_count = None

    def __str__(self):
        return f'{self.__video_name}'

    @property
    def info_video(self) -> dict:
        """Возвращает словарь с данными по видео"""
        return self._get_video(self.__video_id)

    @property
    def video_id(self):
        """Возвращает id"""
        return self.__video_id

    @property
    def title(self) -> str:
        """Возвращает название видео"""
        return self.__video_name

    @property
    def view_count(self) -> str:
        """Возвращает количество просмотров"""
        return self.__views_count

    @property
    def like_count(self) -> str:
        """Возвращает количество лайков"""
        return self.__like_count

    def print_info(self) -> json:
        """Вывод информации на экран"""
        print(super().dict_to_json(data=self.info_video))


class PLVideo(Video, Basic):

    def __init__(self, video_id, playlist_id):
        """Дополнительно инициализируется id плейлиста
                После создания экземпляра дополнительно инициализируются атрибуты:
                -название плейлиста(playlist_name)
                -id канала(channel_id)"""
        super().__init__(video_id)
        self.__playlist_id = playlist_id
        self.__channel_id = self.info_video['items'][0]['snippet']['channelId']
        self.__playlist_name = self.playlist['items'][0]['snippet']['title']

    def __str__(self):
        return f'{super().__str__()} ({self.__playlist_name})'

    @property
    def playlist_id(self) -> str:
        """Возвращает id плейлиста"""
        return self.__playlist_id

    @property
    def channel_id(self):
        """Возвращает id канала"""
        return self.__channel_id

    @property
    def playlist_name(self) -> str:
        """Возвращает имя плейлиста"""
        return self.__playlist_name

    @property
    def playlist(self) -> dict:
        """Возвращает словарь с данными по плейлисту"""
        return self._get_playlist(self.__playlist_id)

    @property
    def playlist_channel(self) -> dict:
        """Возвращает плейлист канала"""
        return self._get_playlist_channel(self.channel_id)

    def print_info_playlist(self) -> json:
        """Вывод информации о плейлисте на экран"""
        print(super().dict_to_json(data=self.playlist))

    def check_video_in_playlist(self) -> str:
        """Получение информации о нахождении видео в плейлисте"""
        playlist = self.playlist_channel
        music = []
        for item in playlist['items']:
            music.append(item['snippet']['title'])
        if self.playlist_name in music:
            return f"Видео '{self.title}' есть в плейлисте '{self.playlist_name}'"
        return f"Видео '{self.title}' нет в плейлисте '{self.playlist_name}'"