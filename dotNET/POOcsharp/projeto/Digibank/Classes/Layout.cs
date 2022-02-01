using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;

namespace Digibank.Classes
{
    public class Layout
    {
        private static byte opcao;

        public static void telaPrincipal()
        {
            Console.Clear();

            string linha1 = "Digite a opção desejada:";
            string linha2 = "1 - Criar Conta";
            string linha3 = "2 - Entrar com CPF e senha";
            string separador = "==============================";

            Console.WriteLine($"{linha1, 10}\n{separador, 10}\n{linha2, 10}\n{separador, 10}\n{linha3, 10}");

            opcao = byte.Parse(Console.ReadLine());

            switch (opcao)
            {
                case 1:
                    Console.WriteLine("Opção 1");
                    break;
                case 2:
                    Console.WriteLine("Opção 2");
                    break;
                default:
                    Console.WriteLine("Opção Inválida");
                    break;
            }
        }
    }
}