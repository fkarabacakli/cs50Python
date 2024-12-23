import fuel

def test_convert():
    strings = {
        "7/10":70,
        "1/10":10,
        "1/100":1,
        "79/100":79,
    }
    for string in strings:
        assert fuel.convert(string)==strings[string]



def test_gauge():
    strings = {
        1:"EEE",
        78:"%78",
        68:"%68",
        99:"FFF"
    }
    for string in strings:
        assert fuel.gauge(string)==strings[string]

