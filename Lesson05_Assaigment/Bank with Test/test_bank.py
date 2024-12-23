from bank import value

def test_string():
    strings = {
        "furkan": 100,
        "hello": 0,
        "karabacakli": 100,
        "world": 100,
        "halil": 20,
    }

    for string in strings:
        assert value(string)==strings[string]