using System;
using System.Collections.Generic;
using System.Text;

namespace aula1
{
    public class ContaPoupança : Conta // os dois pontos informam que a nossa classe é "filha" de "Conta".
    {
        // usar os dois pontos e depois escrever base() copia o construtor da classe base.
        public ContaPoupança(int numero, double limite) : base(numero, limite)
        {
        }

        // Vamos alterar o método saca() da classe ContaPoupança. Quero cobrar uma taxa de 6 reais por saque.
        // Porém não podemos simplemente usar o "override" pois o método saca() não é abstrato.
        // Nesse caso nós devemos ir até a classe Conta e usar uma recurso chamado de "virtual".
        // O virtual, nós permitirá sobrescrever o método.

        public override bool saca(double x)
        {
            bool deuCerto = base.saca(x);

            if (deuCerto)
            {
                this.saldo -= 6;
            }

            return false;
        }
    }
}