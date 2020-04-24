from .models import Soma, Subtracao, Operacao


def test_soma():
  assert Soma(10,10) == 20


def test_subtracao():
  assert Subtracao(10,10) == 0