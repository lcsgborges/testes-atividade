import unittest
from irpf import IRPF

class CadastroRendimentosTest(unittest.TestCase):

    def setUp(self):
        self.irpf = IRPF()

    def test_cadastrar_um_rendimento(self):
        self.irpf.cadastrar_rendimento(5000)
        self.assertEqual(5000, self.irpf.get_total_rendimentos())

    def test_cadastrar_dois_rendimentos_iguais(self):
        self.irpf.cadastrar_rendimento(6000)
        self.irpf.cadastrar_rendimento(6000)
        self.assertEqual(12000, self.irpf.get_total_rendimentos())

    def test_cadastrar_dois_rendimentos_diferentes(self):
        self.irpf.cadastrar_rendimento(5000)
        self.irpf.cadastrar_rendimento(6000)
        self.assertEqual(11000, self.irpf.get_total_rendimentos())
