using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exercicios_de_Csharp
{
    public class exercicio2
    {
        public static void Exercicio_2()
        {
            Console.Write("Digite um número: ");
            ushort a = ushort.Parse(Console.ReadLine());
            Console.Write("Digite outro número: ");
            ushort b = ushort.Parse(Console.ReadLine());
            int z = a + b;
            Console.WriteLine($"A soma de {a} com {b} é {z}.");
            Console.ReadLine();
        }
    }
}
