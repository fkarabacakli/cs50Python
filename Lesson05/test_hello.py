from hello import hello

def test_default():
    assert hello("")      =="hello, World"
    assert hello()        =="hello, World"

def test_argument():
    for name in ["furkan","mehmet","semih","betül","ayperi","zeynep"]:
        assert hello(name)==f"hello, {name.strip().title()}"
