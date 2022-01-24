// See https://aka.ms/new-console-template for more information
using System;

class Aula11
{
    static void Main()
    {
        // Conversões seguras
        int a = 4;
        float b = a;
        Console.WriteLine(b);

        // Conversão não segura
        /*
        float c = 5f;
        int d = c;
        Console.WriteLine(d);
        */

        // Operação de TypeCast
        float c = 5.333f;
        int d = (int)c;
        Console.WriteLine(d);

        float e = 3.1415f;
        short pi = (short)e;
        Console.WriteLine(pi);
    }
}