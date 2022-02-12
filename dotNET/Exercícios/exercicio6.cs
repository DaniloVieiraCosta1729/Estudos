using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exercicios_de_Csharp
{
    public class exercicio6
    {
        public static void Exercicio_6()
        {
            string esp = "                        ";
            string linha = "========================";
            string LINHA = $"{esp}{linha}======={linha}";
            Console.WriteLine(LINHA);
            Console.WriteLine($"{esp}{esp}TABOADA{esp}");
            Console.WriteLine(LINHA);

            Console.Write($"{esp}Digite um número natural de 0 a 10: ");
            retorno:
            try
            {
                byte n = Convert.ToByte(Console.ReadLine());

                for (int i = 0; i < 11; i++)
                {
                    Console.WriteLine($"{esp}{n} x {i} = {n * i}");
                }
            }
            catch
            {
                Console.Clear();
                Console.WriteLine(LINHA);
                Console.WriteLine($"{esp}{esp}TABOADA{esp}");
                Console.WriteLine(LINHA);
                Console.Write($"{esp}O valor informado está fora do padrão exigido.\n{esp}Por favor, informe um número de 0 até 10: ");
                
                goto retorno;
            }
        }
    }
}