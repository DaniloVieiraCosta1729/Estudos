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

            string espaço = "                                          ";
            string linha1 = espaço + "Digite a opção desejada:";
            string linha2 = espaço + "1 - Criar Conta";
            string linha3 = espaço + "2 - Entrar com CPF e senha";
            string separador = espaço + "==============================";

            Console.WriteLine($"{linha1}\n{separador}\n{linha2}\n{separador}\n{linha3}");

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