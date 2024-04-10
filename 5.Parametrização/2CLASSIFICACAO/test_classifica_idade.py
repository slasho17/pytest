from classifica_idade import classifica_idade
import pytest

@pytest.mark.parametrize("idade, categoria_esperada",[
        (10, "Criança"),
        (15, "Adolescente"),
        (39, "Adulto"),
        (66, "Idoso")
    ])
def test_classifica_idade(idade, categoria_esperada):
    assert classifica_idade(idade) == categoria_esperada