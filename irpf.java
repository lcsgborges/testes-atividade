package app;

import java.util.ArrayList;
import java.util.List;

public class IRPF {

    public static final float VALOR_DEDUCAO_POR_DEPENDENTE = 189.59f;

    private float totalRendimentos;
    private float contribuicaoPrevidenciaria;
    private final List<String> dependentes;

    public IRPF() {
        this.dependentes = new ArrayList<>();
    }

    public void cadastrarRendimento(float valor) {
        this.totalRendimentos += valor;
    }

    public float getTotalRendimentos() {
        return this.totalRendimentos;
    }

    public void cadastrarPrevidenciaOficial(float valor) {
        this.contribuicaoPrevidenciaria = valor;
    }

    public float getPrevidenciaOficial() {
        return this.contribuicaoPrevidenciaria;
    }

    public void cadastrarDependente(String nome) {
        this.dependentes.add(nome);
    }

    public float getDeducaoDependentes() {
        return this.dependentes.size() * VALOR_DEDUCAO_POR_DEPENDENTE;
    }
}
