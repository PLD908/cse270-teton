import pytest
import json
from build_sentences import (
    get_seven_letter_word,
    parse_json_from_file,
    choose_sentence_structure,
    get_pronoun,
    get_article,
    get_word,
    fix_agreement,
    build_sentence,
    structures,
    pronouns,
    articles
)


# ------------------------------
# TEST get_seven_letter_word()
# ------------------------------
def test_get_seven_letter_word_valid(mocker):
    mocker.patch("builtins.input", return_value="example")
    assert get_seven_letter_word() == "EXAMPLE"


def test_get_seven_letter_word_invalid(mocker):
    mocker.patch("builtins.input", return_value="short")
    with pytest.raises(ValueError):
        get_seven_letter_word()


# ------------------------------
# TEST parse_json_from_file()
# ------------------------------
def test_parse_json_from_file(tmp_path):
    test_file = tmp_path / "data.json"
    data = {"key": "value"}

    with open(test_file, "w") as f:
        json.dump(data, f)

    assert parse_json_from_file(test_file) == data


def test_parse_json_from_file_mock(mocker):
    mock_open = mocker.patch("builtins.open", mocker.mock_open(read_data='{"a":1}'))
    result = parse_json_from_file("fake.json")
    assert result == {"a": 1}
    mock_open.assert_called_once_with("fake.json", "r")


# ------------------------------
# TEST choose_sentence_structure()
# ------------------------------
def test_choose_sentence_structure(mocker):
    mocker.patch("random.choice", return_value=structures[0])
    assert choose_sentence_structure() == structures[0]


# ------------------------------
# TEST get_pronoun()
# ------------------------------
def test_get_pronoun(mocker):
    mocker.patch("random.choice", return_value="he")
    assert get_pronoun() == "he"


# ------------------------------
# TEST get_article()
# ------------------------------
def test_get_article(mocker):
    mocker.patch("random.choice", return_value="the")
    assert get_article() == "the"


# ------------------------------
# TEST get_word()
# ------------------------------
def test_get_word():
    words = ["Apple", "Ball", "Cat"]
    assert get_word("A", words) == "Apple"
    assert get_word("B", words) == "Ball"
    assert get_word("C", words) == "Cat"


# ------------------------------
# TEST fix_agreement()
# ------------------------------
def test_fix_agreement_rule1():
    sentence = ["he", "quickly", "run"]
    fix_agreement(sentence)
    assert sentence[2] == "runs"  # verb got an "s"


def test_fix_agreement_rule2():
    sentence = ["a", "big", "apple"]
    fix_agreement(sentence)
    assert sentence[0] == "an"


def test_fix_agreement_rule3():
    sentence = ["the", "green", "frog", "quickly", "jump"]
    fix_agreement(sentence)
    assert sentence[4] == "jumps"


# ------------------------------
# TEST build_sentence()
# ------------------------------
def test_build_sentence(mocker):
    seed = "ABCDEFG"

    structure = ["ART", "ADJ", "NOUN"]

    data = {
        "adjectives": ["A_adj", "B_adj", "C_adj", "D_adj", "E_adj", "F_adj", "G_adj"],
        "nouns": ["A_n", "B_n", "C_n", "D_n", "E_n", "F_n", "G_n"],
        "verbs": [],
        "adverbs": [],
        "prepositions": []
    }

    mocker.patch("build_sentences.get_article", return_value="the")

    result = build_sentence(seed, structure, data)

    assert result == "The A_adj B_n".capitalize()
