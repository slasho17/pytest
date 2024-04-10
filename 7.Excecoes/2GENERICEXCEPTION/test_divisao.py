import pytest
from divisao import dividir

def test_dividir_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(1,0)
        
def test_dividir_por_zero2():
    with pytest.raises(ZeroDivisionError) as exec_info:
        dividir(1,0)
    assert "Não divide por zero monaa" in str(exec_info)