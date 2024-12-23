from twttr import shorten


def test_string():
    strings = {
        "furkan": "frkn",
        "hello": "hll",
        "karabacakli": "krbckl",
        "world": "wrld",
    }

    for string in strings:
        assert shorten(string) == strings[string]
