// See https://aka.ms/new-console-template for more information
using System;

class aula18
{
    static void Main()
    {
        // criando um array
        int[] vetor = new int[5];
        vetor[0] = 0;
        vetor[1] = 1;
        vetor[2] = 2;
        vetor[3] = 3;
        vetor[4] = 4;
        
        int[] v = new int[3]{1, 2, 3};

        System.Console.WriteLine("{0}, {1}", vetor[4], v[2]);

        // criando matrizes
        int[,] matriz = new int[3,3];
        matriz[0,0] = 1;
        matriz[0,1] = 2;
        matriz[0,2] = 3;
        matriz[1,0] = 4;
        matriz[1,1] = 5;
        matriz[1,2] = 6;
        matriz[2,0] = 7;
        matriz[2,1] = 8;
        matriz[2,2] = 9;

        int[,] m = new int[2,2]{{1,2},{3,4}};

        System.Console.WriteLine("{0}, {1}", matriz[2,2], m[1,1]);
    }
}