using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Programa01_01
{
    class Soma : IOperacao
    {
        private double r = 0;
        private ArrayList resultados = new ArrayList();

        // Métodos da INTERFACE IOperacao
        public void calcular(double a, double b)
        {
            r = a + b;
        }

        public void mostrar()
        {
            Console.WriteLine($"a soma é {r}");
            resultados.Add(r);
        }

        // Método próprio da classe.
        public void mostrarResultados()
        {
            foreach (double r in resultados)
            {
                Console.WriteLine(r);
            }
        }
    }
}