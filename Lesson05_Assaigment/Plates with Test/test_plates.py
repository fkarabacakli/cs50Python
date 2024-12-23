from plates import is_valid

def test_plates():
    plates = {
        "cs50": True,
        "furkan": True,
        "7823": False,
    }

    for plate in plates:
        assert is_valid(plate)==plates[plate]