from func import Channel, Video, PLVideo

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