import datetime
import isodate
from youtube.basic import Basic


class PlayList(Basic):
    def __init__(self, playlist_id):
        super().__init__()
        self.__playlist_id = playlist_id
        #self.playlist = youtube.playlists().list(id=playlist_id, part='snippet').execute()
        #self.playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails', maxResults=50).execute()
        self.__title = self.playlist['items'][0]['snippet']['title']
        self.__url = f'https://www.youtube.com/playlist?list={self.playlist_id}'

    def __str__(self):
        return f"Плейлист - '{self.__title}'"

    @property
    def playlist_id(self) -> str:
        """Возвращает id плейлиста"""
        return self.__playlist_id

    @property
    def playlist_title(self) -> str:
        """Возвращает название плейлиста"""
        return self.__title

    @property
    def playlist_url(self) -> str:
        """Возвращает ссылку на плейлист"""
        return self.__url

    @property
    def playlist(self) -> dict:
        """Возвращает данные плейлиста в виде словаря по id плейлиста"""
        return self._get_playlist(playlist_id=self.__playlist_id)

    @property
    def ids_videos(self) -> list:
        """Возвращает список id всех видео в плейлисте"""
        return self._get_ids_videos_in_playlist(playlist_id=self.__playlist_id)

    @property
    def total_duration(self) -> datetime.timedelta:
        """Возвращает общее время плейлиста"""
        return self.get_total_duration()


    def get_total_duration(self) -> datetime.timedelta:
        """Получает общее время всех видео плейлиста"""
        videos = self._get_info_video_in_playlist(ids_videos=self.ids_videos)
        total_duration = datetime.timedelta()

        for video in videos['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration

        return total_duration


    def show_best_video(self):
        """Получает ссылку на лучшее видео в плейлисте по колличеству просмотров"""
        videos = self._get_info_video_in_playlist(ids_videos=self.ids_videos)

        for video in videos['items']:
            views_count = video['statistics']['viewCount']
            video_id = video['id']
            video_link = f'https://www.youtube.com/watch?v={video_id}'
            videos.append({'views': int(views_count), 'url': video_link})
        videos.sort(key=lambda vid: vid['views'], reverse=True)
        for i in videos[:1]:
            print(i['url'])
        return (i['url'])


pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
print(pl.playlist)