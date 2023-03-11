from func import Channel, Video, PLVideo, PlayList

def test_str():
    chnl1 = Channel('UC3n7MKHEwA9xXBErhXYZbMQ')
    chnl2 = Channel('UCglNYRt1fJ3RmDrWpVG1Bsg')
    assert str(chnl1) == 'Yotube-канал: Cold Steel'
    assert str(chnl2) == 'Yotube-канал: Thujoy'

    #assert print(chnl1 > chnl2) is True
def test_add():
    chnl1 = Channel('UC3n7MKHEwA9xXBErhXYZbMQ')
    chnl2 = Channel('UCglNYRt1fJ3RmDrWpVG1Bsg')
    assert chnl1 + chnl2 == 1556000

def test_lt():
    chnl1 = Channel('UC3n7MKHEwA9xXBErhXYZbMQ')
    chnl2 = Channel('UCglNYRt1fJ3RmDrWpVG1Bsg')
    assert (chnl1 < chnl2) is False

def test_gt():
    chnl1 = Channel('UC3n7MKHEwA9xXBErhXYZbMQ')
    chnl2 = Channel('UCglNYRt1fJ3RmDrWpVG1Bsg')
    assert (chnl1 > chnl2) is True

def test_cls_video_pl():
    video1 = Video('9lO06Zxhu88')
    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    assert str(video1) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert str(video2) == 'Пушкин: наше все? (Литература)'


def test_cls_playlist():
    pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
    assert pl.title == 'Редакция. АнтиТревел'
    assert pl.url == 'https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb'
    duration = pl.total_duration
    assert str(duration) == '3:41:01'
    assert str(type(duration)) == "<class 'datetime.timedelta'>"
    assert str(duration.total_seconds()) == "13261.0"
    assert str(pl.show_best_video()) == 'https://www.youtube.com/watch?v=9Bv2zltQKQA'
