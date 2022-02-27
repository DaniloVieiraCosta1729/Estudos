using System;
using System.Text;
using System.Collections.Generic;

class aula26
{
    static void Main()
    {
        System.Console.Write("Digite um número: ");
        int a = Convert.ToInt32(Console.ReadLine());
        System.Console.WriteLine("Digite o segundo número: ");
        int b = Convert.ToInt32(Console.ReadLine());
        Console.Clear();
        System.Console.WriteLine("=============================================== Algoritmo de Euclides ===============================================");
        // int r;
        // int q = divide(a, b, out r);
        // System.Console.WriteLine($"{a} = {b} x {q} + {r}");
        Euclides(a, b);
    }

    static int divide(int a, int b, out int resto)
    {
        int quociente = a / b;
        resto = a % b;
        return quociente;
    }

    static void Euclides(int a, int b)
    {
        int r;

        do
        {
            int q = divide(a, b, out r);
            System.Console.WriteLine($"{a} = {b} x {q} + {r}");
            a = b;
            b = r;
        } while (r != 0);
    }
}