from syncplay.players.mplayer import MplayerPlayer
from syncplay.players.mpv import MpvPlayer
from syncplay.players.vlc import VlcPlayer
try:
    from syncplay.players.mpc import MPCHCAPIPlayer
except ImportError:
    from syncplay.players.basePlayer import DummyPlayer
    MPCHCAPIPlayer = DummyPlayer
try:
    from syncplay.players.mpcbe import MpcBePlayer
except ImportError:
    from syncplay.players.basePlayer import DummyPlayer
    MpcBePlayer = DummyPlayer


def getAvailablePlayers():
    return [MPCHCAPIPlayer, MpvPlayer, VlcPlayer, MpcBePlayer, MplayerPlayer]
