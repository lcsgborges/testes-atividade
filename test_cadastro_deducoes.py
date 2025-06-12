import unittest
from irpf import IRPF

class CadastrarDeducoesTest(unittest.TestCase):

    def setUp(self):
        self.irpf = IRPF()

    def test_cadastrar_previdencia_oficial(self):
        self.irpf.cadastrar_previdencia_oficial(700)
        self.assertEqual(700, self.irpf.get_previdencia_oficial())

    def test_cadastrar_previdencia_oficial2(self):
        self.irpf.cadastrar_previdencia_oficial(800)
        self.assertEqual(800, self.irpf.get_previdencia_oficial())

    def test_cadastrar_previdencia_oficial3(self):
        self.irpf.cadastrar_previdencia_oficial(900)
        self.assertEqual(900, self.irpf.get_previdencia_oficial())
