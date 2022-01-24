// See https://aka.ms/new-console-template for more information
using System;

namespace Aula09
{
    class Aula09
    {
        static void Main()
        {
            // Operador de bitwise (muliplica por 2 (<<) ou divide por dois (>>).)
            int num = 10;
            num = num << 1;
            int number = num >> 2;
            Console.WriteLine("{0}\n{1}", num, number);
        }
    }
}
