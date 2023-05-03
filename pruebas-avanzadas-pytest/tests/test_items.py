import pytest

def test_string_is_digit_1():
    items = ["No", "1", "10", "33", "Yes"]
    for item in items:
        assert item.isdigit()

@pytest.mark.parametrize("item", ["No", "1", "10", "33", "Yes"])
def test_string_is_digit_2(item):
    assert item.isdigit()

@pytest.mark.parametrize_3("item", ["0", "1", "10", "33", "9"])
def test_string_is_digit(item):
    assert item.isdigit()

@pytest.mark.parametrize("item, attribute", [("", "format"), (list(), "append")])
def test_attributes(item, attribute):
    assert hasattr(item, attribute)