import os
from app.utils import utils


def test_root_dir():
    root = utils.root_dir()
    assert os.path.exists(root)
    assert os.path.exists(os.path.join(root, "app"))


def test_str_contains_punctuation():
    assert utils.str_contains_punctuation("hello, world") is True
    assert utils.str_contains_punctuation("你好！") is True
    assert utils.str_contains_punctuation("hello world") is False
    assert utils.str_contains_punctuation("12345") is False


def test_split_string_by_punctuations():
    text = "First sentence. Second sentence, with comma! Third sentence?\nFourth line after newline."
    lines = utils.split_string_by_punctuations(text)
    assert lines == [
        "First sentence",
        "Second sentence",
        "with comma",
        "Third sentence",
        "Fourth line after newline",
    ]


def test_split_string_by_punctuations_number_handling():
    text = "Charged at 2.5% fee for 1,000 years."
    lines = utils.split_string_by_punctuations(text)
    assert lines == ["Charged at 2.5% fee for 1,000 years"]
