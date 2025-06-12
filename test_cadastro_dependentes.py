import unittest
from irpf import IRPF

class CadastroDependentesTest(unittest.TestCase):

    def setUp(self):
        self.irpf = IRPF()

    def test_cadastrar_um_dependente(self):
        self.irpf.cadastrar_dependente("Joao")
        self.assertEqual(IRPF.VALOR_DEDUCAO_POR_DEPENDENTE, self.irpf.get_deducao_dependentes())

    def test_cadastrar_dois_dependentes(self):
        self.irpf.cadastrar_dependente("Joao")
        self.irpf.cadastrar_dependente("Maria")
        self.assertEqual(2 * IRPF.VALOR_DEDUCAO_POR_DEPENDENTE, self.irpf.get_deducao_dependentes())

    def test_cadastrar_tres_dependentes(self):
        self.irpf.cadastrar_dependente("Joao")
        self.irpf.cadastrar_dependente("Maria")
        self.irpf.cadastrar_dependente("Jose")
        self.assertEqual(3 * IRPF.VALOR_DEDUCAO_POR_DEPENDENTE, self.irpf.get_deducao_dependentes())

    def test_cadastrar_cinco_dependentes(self):
        dependentes = ["Joao", "Maria", "Jose", "Maria Jose", "Jose Maria"]
        for nome in dependentes:
            self.irpf.cadastrar_dependente(nome)
        self.assertEqual(5 * IRPF.VALOR_DEDUCAO_POR_DEPENDENTE, self.irpf.get_deducao_dependentes())
