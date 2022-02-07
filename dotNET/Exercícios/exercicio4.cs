using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exercicios_de_Csharp
{
    public class exercicio4
    {
        public static void Exercicio_4()
        {
            Console.Write("Digite um número natural menor que 250: ");

            byte k = Convert.ToByte(Console.ReadLine());

            // Testando a biblioteca de matemática do C#
            Console.WriteLine($"O quadrado de {k} é {Math.Pow(k, 2)}");
            Console.WriteLine($"A raiz quadrada de {k} é {Math.Sqrt(k)}");
            Console.WriteLine($"O logaritmo natural de {k} é {Math.Log(k)}");
            Console.WriteLine($"seno({k}) = {Math.Sin(k)}");
        }
    }
}