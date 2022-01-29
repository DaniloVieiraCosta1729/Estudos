// See https://aka.ms/new-console-template for more information
using System;
using System.Text;
using System.Collections.Generic;

class aula20
{
    static void Main()
    {
        string esp = "-------------------------";
        System.Console.WriteLine(esp + "Sequencia do Quadrado dos Inteiros" + esp);
        System.Console.Write("Deseja ver a sequência até qual termo? ");
        int n = Convert.ToInt32(Console.ReadLine());
        int count = 0;

        int[] vetor = new int[n + 1]; 

        while (count < n + 1)
        {
            int quadrado = count * count;
            vetor[count] = quadrado;
            count++;
        }

        for (var i = 0; i <= n; i++)
        {
            System.Console.WriteLine(vetor[i]);
        }
    }
}