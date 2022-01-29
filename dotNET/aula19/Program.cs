// See https://aka.ms/new-console-template for more information
using System;
using System.Text;
using System.Collections.Generic;
using System.Linq;

class aula19
{
    static void Main()
    {
        string esp = "-------------------------";
        System.Console.WriteLine(esp + "Sequência de Fibonacci " + esp);
        System.Console.Write("Digite até qual termo você deseja ver: ");
        int termo = Convert.ToInt32(System.Console.ReadLine());
        int[] fib = new int[termo];
        fib[0] = 0;
        fib[1] = 1;

        for (var i = 2; i <= termo - 1; i++)
        {
            fib[i] = fib[i-1] + fib[i-2];
        }

        for (var j = 0; j < fib.Count(); j++)
        {
            System.Console.WriteLine(fib[j]);
        }
    }
}