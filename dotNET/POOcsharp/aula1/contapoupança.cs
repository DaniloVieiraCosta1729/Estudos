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
    }
}