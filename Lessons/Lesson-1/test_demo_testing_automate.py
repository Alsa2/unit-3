from quizz33 import translate_dna
import pytest

def test_a_to_t():
    assert translate_dna("A") == "T"