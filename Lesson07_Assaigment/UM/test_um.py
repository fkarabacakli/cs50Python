
from um import count

def test_um():
    checks = {
        "Hello, World um":1,
        "um":1,
        "Halil Furkan Karabcakli":0,
        "How is it going":0,
        "um, hello, um, world":2,
        "yummy":0,
    }
    for check in checks:
        assert count(check)==checks[check]