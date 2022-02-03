using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Exercicios_de_Csharp
{
    public class exercicio3
    {
        public static void Exercicio_3()
        {
            /*
             Nesse exercício, devemos pegar o input do usuário e analisá-lo para então devolver as informações
             sobre o valor digitado. Os pontos analisados são:
             - Qual é o tipo primitivo do input? (sempre uma string no C#);
             - Tem espaço?
             - É um número?
             - É alfabético?
             - É alfanumérico?
             - Está em maiusculas?
             - Está em minusculas?
             - Está capitalizada?
            */
            Console.Write("Digite alguma coisa: ");
            var valor = Console.ReadLine();
            // Pergunta 1: 
            Console.WriteLine("É uma string.");

            // Pergunta 2:
            var valorCopia = valor;
            int espaço = valorCopia.IndexOf(" ");
            List<int> qtdEspacos = new List<int>();

            if (espaço == -1)
            {
                Console.WriteLine("Não há nenhum espaço no que foi digitado.");
            }
            else
            {
                while (espaço != -1)
                {
                    qtdEspacos.Add(espaço);
                    valorCopia = valorCopia.Remove(espaço, 1);
                    espaço = valorCopia.IndexOf(" ");
                }
                Console.WriteLine($"Há {qtdEspacos.Count()} espaços no valor digitado.");
                foreach (int i in qtdEspacos)
                {
                    Console.WriteLine($"O {qtdEspacos.IndexOf(i) + 1}º espaço foi o {i + qtdEspacos.IndexOf(i) + 1}º valor digitado.");
                }
            }

            // Pergunta 3:
            bool isalpha = Regex.IsMatch(valorCopia ,@"^[a-zA-Z]+$");
            bool isnumeric = Regex.IsMatch(valorCopia, @"^[0-9]+$");
            bool isalphanum = Regex.IsMatch(valorCopia, @"^[a-zA-Z0-9]+$");

            if (isalpha)
            {
                Console.WriteLine("A expressão é alfabética.");
            }
            else if (isnumeric)
            {
                Console.WriteLine("A expressão é numérica.");
            }
            else
            {
                Console.WriteLine("A expressão é alfanumerica.");
            }

            bool soMaiuscula =  Regex.IsMatch(valorCopia, @"^[A-Z]+$");
            bool soMinuscula = Regex.IsMatch(valorCopia, @"^[a-z]+$");
            string primeira_letra = Convert.ToString(valorCopia[0]);
            bool capitalizado = Regex.IsMatch(primeira_letra, @"^[A-Z]+$");

            if (soMaiuscula)
            {
                Console.WriteLine("Todas as letras estão em maiusculas.");
            }
            else if (soMinuscula)
            {
                Console.WriteLine("Todas as letras estão em minusculas.");
            }
            if (capitalizado)
            {
                Console.WriteLine("Está capitalizado.");
            }

            Console.ReadLine();
        }
    }
}
