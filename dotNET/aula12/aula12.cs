// See https://aka.ms/new-console-template for more information
using System;

class Aula12
{
    static void Main(string[] args)
    {
        Console.WriteLine("Digite a nota: ");
        var valor = Console.ReadLine();
        int nota = Convert.ToInt32(valor);
        Console.WriteLine(passou(nota));
    }

    static string passou(int nota)
    {
        if (nota >= 60)
        {
            return "Você Passou!";
        }
        else
        {
            return "Você não passou. =(";
        }
    }
}