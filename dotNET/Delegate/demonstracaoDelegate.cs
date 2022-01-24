// See https://aka.ms/new-console-template for more information
using System;
using System.Collections.Generic;

namespace demonstracaoDelegate
{
    class Program
    {
        delegate float Funcao(float a, float b);
        static void Main(string[] args)
        {
            Funcao funcao = new Funcao(CalculaMedia);
            float resultado = funcao(2, 8);

            // float resultado = CalculaMedia(2, 8);
            Console.WriteLine("A média entre 2 e 8 é {0}", resultado);

            funcao = new Funcao(Multiplicacao);
            float produto = funcao(2, 8);

            Console.WriteLine("O produto de 2 com 8 é {0}", produto);
            Console.ReadKey();
        }

        static float CalculaMedia(float x, float y)
        {
            float media;
            media = (x + y) / 2;

            return media;
        }

        static float Multiplicacao(float x, float y)
        {
            float produto;
            produto = x * y;

            return produto;
        }
    }
}