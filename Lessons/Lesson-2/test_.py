import pytest
import exemptions

def test_valid():
    assert exemptions.division(a=10, b=2) == 5
    assert exemptions.division(a=5, b=2) == 2.5

def test_invalid():
    with pytest.raises(ValueError):
        exemptions.division(a=5, b=0)
    with pytest.raises(TypeError):
        exemptions.division(a="test", b="test")
        