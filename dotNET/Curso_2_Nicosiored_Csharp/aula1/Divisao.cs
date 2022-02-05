using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Programa01_01
{
    class Divisao : IOperacao
    {
        private double r = 0;

        // Método da interface
        
        public void calcular(double a, double b)
        {
            try
            {
                r = a / b;
            }
            catch
            {
                int v = (b == 0) ? 1 : 0;

                switch (v)
                {
                    case 1:
                        r = -1;
                        Console.WriteLine("Erro! A divisão por Zero não está definida.");
                        break;
                    case 0:
                        r = -1;
                        Console.WriteLine("Erro!");
                        break;
                    default:
                        break;
                }
            }
        }
            public void mostrar()
        {
            Console.WriteLine($"A divição é {r}");
        }
    }
}