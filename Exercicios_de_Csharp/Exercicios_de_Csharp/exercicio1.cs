using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exercicios_de_Csharp
{
    public class exercicio1
    {
        public static void Exercicio_1()
        {
            Console.WriteLine("Olá. Qual é o seu nome? ");
            string nome = Console.ReadLine();
            Console.WriteLine($"Prazer em te conhecer, {nome}!");
            Console.ReadLine();
        }
    }
}
