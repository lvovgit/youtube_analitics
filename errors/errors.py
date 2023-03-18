class YoutubeApiError(Exception):
    """Класс-исключение для ошибок, связанных с ютубом"""

    def __init__(self, *args):
        self.message = args[0] if args else "Неизвестная ошибка"

    def __str__(self):
        return self.message