def is_positive(numero):
    return numero > 0

def test_is_positivo():
    assert is_positive(4) == True
    assert is_positive(-54) == False
    assert is_positive(0) == False
    assert is_positive(1000) == True