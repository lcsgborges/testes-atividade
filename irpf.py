class IRPF:
    VALOR_DEDUCAO_POR_DEPENDENTE = 189.59

    def __init__(self):
        self.total_rendimentos = 0.0
        self.contribuicao_previdenciaria = 0.0
        self.dependentes = []

    def cadastrar_rendimento(self, valor):
        self.total_rendimentos += valor

    def get_total_rendimentos(self):
        return self.total_rendimentos

    def cadastrar_previdencia_oficial(self, valor):
        self.contribuicao_previdenciaria = valor

    def get_previdencia_oficial(self):
        return self.contribuicao_previdenciaria

    def cadastrar_dependente(self, nome):
        self.dependentes.append(nome)

    def get_deducao_dependentes(self):
        return len(self.dependentes) * self.VALOR_DEDUCAO_POR_DEPENDENTE
