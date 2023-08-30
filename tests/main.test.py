import inc_dec
from lib.utils import trim_str_stream

def test_stream_handler():
    assert inc_dec.trim_str_stream('    horray !  \n ') == "horray!"
    assert inc_dec.trim_str_stream(2) == '2'
