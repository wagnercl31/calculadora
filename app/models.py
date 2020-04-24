class ParametrosCalculo(object):
    def __init__(self, operacao, p1, p2):
        self.operacao = operacao
        self.parametro1 = p1
        self.parametro2 = p2

from app.utils import Impressora

impressora = Impressora()

class Operacao(object):
    def __init__(self, p1, p2):
        impressora.imprimir('Operação sendo criada...')
        self.p1 = p1
        self.p2 = p2

    def calcular(self):
        raise Exception('Operacao abstrata!')


class Soma(Operacao):
    def calcular(self):
        impressora.imprimir('Soma sendo efetuada...')
        return self.p1 + self.p2


class Subtracao(Operacao):
    def calcular(self):
        impressora.imprimir('Subtração sendo efetuada...')
        return self.p1 - self.p2


class Multiplicacao(Operacao):
    impressora.imprimir('Multiplicação sendo efetuada...')
    def calcular(self):
        return self.p1 * self.p2


class Divisao(Operacao):
    impressora.imprimir('Divisão sendo efetuada...')
    def calcular(self):
        return self.p1 / self.p2


class FabricaOperacoes(object):
    @staticmethod
    def criar(parametros_operacao: ParametrosCalculo):
        impressora.imprimir('Criando operação(factory)...')
        if parametros_operacao.operacao == 'soma':
            return Soma(parametros_operacao.parametro1,
                        parametros_operacao.parametro2)
        if parametros_operacao.operacao == 'subtracao':
            return Subtracao(parametros_operacao.parametro1,
                             parametros_operacao.parametro2)
        if parametros_operacao.operacao == 'multiplicacao':
            return Multiplicacao(parametros_operacao.parametro1,
                                 parametros_operacao.parametro2)
        if parametros_operacao.operacao == 'divisao':
            return Divisao(parametros_operacao.parametro1,
                           parametros_operacao.parametro2)

        raise Exception('Operacao inválida!')


class Calculadora(object):
    def __init__(self):
        self.preparada = False

    def preparar(self, parametros_calculo):
        impressora.imprimir('Preparando calculadora...')
        self.parametros_calculo = parametros_calculo
        self.operacao = FabricaOperacoes.criar(parametros_calculo)
        self.preparada = True

        return self

    def calcular(self):
        impressora.imprimir('Calculadora efetuando cálculo...')
        return self.operacao.calcular()
