// See https://aka.ms/new-console-template for more information
using System;
class aula07
{
    static void Main()
    {
        Console.WriteLine("Digite o seu nome: ");
        var nome = Console.ReadLine();
        const double pi = 3.1415;
        Console.WriteLine("Seu nome é {0}\nO valor de pi é: {1,5}", nome, pi);
    }
}