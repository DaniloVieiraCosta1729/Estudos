// See https://aka.ms/new-console-template for more information
using System;

namespace aula15
{
    class Aula15
    {
        static void Main()
        {
            Console.WriteLine("Belo Horizonte/MG para Vitória/ES");
            Console.Write("Escolha o transporte: [a] Avião, [c] Carro, [o] Ônibus. \nPor favor, digite apenas a letra correspondente.");
            
            int tempo;
            char escolha;
            string opcao = "As arvores somos noses.";
            escolha = Convert.ToChar(Console.ReadLine());

            switch(escolha)
            {
                case 'a':
                    tempo = 50;
                    opcao = "avião";
                    break;
                case 'c':
                    tempo = 480;
                    opcao = "carro";
                    break;
                case 'o':
                    tempo = 660;
                    opcao = "ônibus";
                    break;
                default:
                    tempo = -1;
                    break;
            }

            if (tempo == -1)
            {
                Console.WriteLine("Opção inválida.");
            }
            else
            {
                Console.WriteLine("A viagem de {0} de BH à Vitória dura {1} minutos.", opcao, tempo);
            }
        }
    }
}