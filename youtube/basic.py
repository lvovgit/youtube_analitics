import json
import os
from googleapiclient.discovery import build

class Basic:
    """Класс для работы с ютубом"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)
    def __new__(cls, *args, **kwargs):
        """Магический метод, запрещает создание нескольких экзепляров класса (можно только один)"""
        if cls is Basic:
            raise ValueError(f'Нельзя создавать экземпляр класса {__class__.__name__}.')
        return super().__new__(cls)

    def __init__(self):
        pass
    @staticmethod
    def dict_to_json(data: dict) -> json:
        """Возвращает словарь в формате json"""
        return json.dumps(data, indent=2, ensure_ascii=False)

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с API ютуба"""
        return cls.youtube

    @classmethod
    def _get_channel(cls, channel_id: str) -> dict:
        """Получает информацию о канале"""
        channel = cls.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return channel

    @classmethod
    def _get_video(cls, video_id) -> dict:
        """Получает данные о видео"""
        video = cls.youtube.videos().list(id=video_id, part='snippet,statistics').execute()
        return video

    @classmethod
    def _get_playlist(cls, playlist_id) -> dict:
        """Получает данные о плейлисте"""
        playlist = cls.youtube.playlists().list(id=playlist_id, part='contentDetails, snippet').execute()
        return playlist

    @classmethod
    def _get_playlist_channel(cls, channel_id: str) -> dict:
        """Получает плейлист канала"""
        playlist = cls.youtube.playlists().list(channelId=channel_id,
                                                part='contentDetails, snippet',
                                                maxResults=50).execute()
        return playlist

    @classmethod
    def _get_ids_videos_in_playlist(cls, playlist_id: str) -> list:
        """Получает все id видео из плейлиста"""
        playlist_videos = cls.youtube.playlistItems().list(playlistId=playlist_id,
                                                           part='contentDetails',
                                                           maxResults=50).execute()

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        return video_ids

    @classmethod
    def _get_info_video_in_playlist(cls, ids_videos: list) -> dict:
        """Получает информацию о видео в плейлисте"""
        video_response = cls.youtube.videos().list(part='contentDetails,statistics',
                                                   id=','.join(ids_videos)).execute()
        return video_response






# print(chnl1.channel_title)
# chnl1.channel_id = 'sdfdsf'
# print(Channel.get_service())
# print(chnl1.to_json())
# print(chnl1 + chnl2)
# try:
#     video1 = Video('9lO06Zxhu8')
#     #print(video1.video_name)
# except Exception:
#     x = 'broken'
#     print(x)
#     if x == 'broken':
#         video1.video_name = None
#     print(video1.video_name)



# video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
#print(video1)
# print(video2)

#pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
# print(pl.title)
# print(pl.url)
#
# duration = pl.total_duration
# print(duration)
# print(type(duration))
# print(duration.total_seconds())
#
#pl.show_best_video()