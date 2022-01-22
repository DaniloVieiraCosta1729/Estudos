using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            int a = 3;
            int b = 3;
            int c = a + b;
            int d = a * b;
            double e = Math.Sqrt(a * b);
            Console.WriteLine(c);
            Console.WriteLine(d);
            Console.WriteLine(e);
             */
            double a;
            double b;
            Console.WriteLine("Esse código retorna a raiz quadrada de um número positivo. \nDigite um número positivo: ");
            a = double.Parse(Console.ReadLine());
            b = Math.Sqrt(a);
            Console.WriteLine(b);

            Console.ReadLine();
        }
    }
}
