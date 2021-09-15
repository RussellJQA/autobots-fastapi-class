from utils.string_utils import string_repeater


def test_string_repeater():
    assert string_repeater("!", 10) == "!!!!!!!!!!"
