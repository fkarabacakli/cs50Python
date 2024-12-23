from numb3rs import validate

def test_numb3rs():
    
    checks = {
        "1:1:1:1:1":False,
        "13:23:56:45:23":False,
        "23:453:25:74":False,
        "87:43.9:JL:45":False,
        "1:1:1:1":True,
        "13:23:56:45":True,
        "23:453:25:34":False,
        "87:43.9:JL":False,
        "268:43:9:89":False,
        "127:0:0:1":True,
        "255:255:255:255":True,
        "512:512:512:512":False,
        "1:2:3:1000":False,
        "cat":False,
        "1:2:3:4":True,
        "11:99:22:88":True,
        "199:911:288:882":False,
        "249:249:249:249":True,
    }
    
    for check in checks:
        assert validate(check)==checks[check]

