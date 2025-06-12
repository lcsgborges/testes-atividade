package tst;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

import app.IRPF;

public class CadastroRendimentosTest {

    private IRPF irpf;

    @Before
    public void setup() {
        irpf = new IRPF();
    }

    @Test
    public void testCadastrarUmRendimento() {
        irpf.cadastrarRendimento(5000f);
        assertEquals(5000f, irpf.getTotalRendimentos(), 0);
    }

    @Test
    public void testCadastrarDoisRendimentosIguais() {
        irpf.cadastrarRendimento(6000f);
        irpf.cadastrarRendimento(6000f);
        assertEquals(12000f, irpf.getTotalRendimentos(), 0);
    }

    @Test
    public void testCadastrarDoisRendimentosDiferentes() {
        irpf.cadastrarRendimento(5000f);
        irpf.cadastrarRendimento(6000f);
        assertEquals(11000f, irpf.getTotalRendimentos(), 0);
    }
}
