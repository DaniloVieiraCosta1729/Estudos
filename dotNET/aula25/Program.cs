using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class aula25
{
    static void Main(string[] args)
    {
        int f8 = 8;
        fib(ref f8);
        System.Console.WriteLine(f8);
    }

    static int fib(ref int n)
    {
        return n *= 2;
    }
}