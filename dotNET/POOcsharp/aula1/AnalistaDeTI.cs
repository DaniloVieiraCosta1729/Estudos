using System;
using System.Collections.Generic;
using System.Text;

namespace aula1
{
    public class AnalistaDeTI : Funcionario
    {
        public override void reajustar()
        {
            this.salario += 700;
        }
    }
}