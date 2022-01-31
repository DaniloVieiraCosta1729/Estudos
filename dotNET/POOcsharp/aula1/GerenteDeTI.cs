using System;
using System.Collections.Generic;
using System.Text;

namespace aula1
{
    public class GerenteDeTI : Gerente
    {
        public override void reajustar()
        {
            this.salario += 2000;
        }
    }
}