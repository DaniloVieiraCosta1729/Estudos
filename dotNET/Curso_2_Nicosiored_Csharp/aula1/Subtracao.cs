using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Programa01_01
{
    class Subtracao : IOperacao
    {
        private double r = 0;

        // Métodos da interface
        public void calcular(double a, double b)
        {
            r = a - b;
        }

        public void mostrar()
        {
            Console.WriteLine($"A subtração é {r}");
        }
    }
}