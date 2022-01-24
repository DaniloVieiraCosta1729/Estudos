// See https://aka.ms/new-console-template for more information
using System;

namespace aula08
{
    class aula08
    {
        static void Main()
        {
            int a1, a2, a3, soma;

            Console.WriteLine("Digite o primeiro valor: ");
            a1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Digite o segunto valor: ");
            a2 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Digite o terceiro valor: ");
            a3 = Convert.ToInt32(Console.ReadLine());
            soma = a1 + a2 + a3;
            Console.WriteLine("{0} + {1} + {2} = {3}", a1, a2, a3, soma);
        }
    }
}
