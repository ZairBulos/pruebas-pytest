def test_main():
    assert True

def test_long_strings():
    left = "this is a very long strings to be compared with another long string"
    right = "This is a very long string to be compared with another long string"
    assert left == right

def test_lists():
    left = ["sugar", "wheat", "coffee", "salt", "water", "milk"]
    right = ["sugar", "coffee", "wheat", "salt", "water", "milk"]
    assert left == right

def test_lists_2():
    left = ["sugar", "wheat", "coffee", "salt", "water", "milk"]
    right = ["sugar", "wheat", "salt", "water", "milk"]
    assert left == right

def test_dictionaries():
    left = {"street": "Ferry Ln.", "number": 39, "state": "Nevada", "zipcode": 30877, "county": "Frett"}
    right = {"street": "Ferry Lane", "number": 38, "state": "Nevada", "zipcode": 30877, "county": "Frett"}
    assert left == right