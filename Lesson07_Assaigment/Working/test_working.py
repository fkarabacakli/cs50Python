from working import convert

def test_basic():
    checks = {
        "11 am to 9 pm":"11:00 to 21:00",
        "9 am to 6 pm":"09:00 to 18:00",
        "10 pm to 9 am":"22:00 to 09:00",
    }
    for check in checks:
        assert convert(check)==checks[check]

def test_complicated():
    checks = {
        "11:00 am to 9:00 pm":"11:00 to 21:00",
        "9:30 am to 6:45 pm":"09:30 to 18:45",
        "10:35 pm to 9:50 am":"22:35 to 09:50",
        }
    for check in checks:
        assert convert(check)==checks[check]