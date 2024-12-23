from Jar.jar import Jar
import pytest


def test_init():
    ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    assert jar.size == 0
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(4)
    assert jar.size == 9
    with pytest.raises(ValueError):
        jar.deposit(4)
    


def test_withdraw():
    jar = Jar(10)
    jar.deposit(10)
    jar.withdraw(1)
    assert jar.size == 9
    jar.withdraw(4)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(7)