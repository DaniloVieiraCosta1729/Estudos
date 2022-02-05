using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Programa01_01
{
    class Program
    {
        static void Main(string[] args)
        {
            int opcao = 0;
            double a = 0;
            double b = 0;

            // Olha o polimorfismo abaixo! =D É por isso que as intefaces são úteis!
            IOperacao operacao = new Soma();
            /*
             A interface nos permite criar um objeto que pode ter todas as variações dos 
             métodos que são pedidos pela interface! Melhor dizendo: se a interface tem um método operação, então podemos instaciar
             um objeto de uma das classes que implementam a interface mas enfatizando que esse objeto é "do tipo da interface",
             podendo variar o método "operação" que esse objeto terá, entre o conjunto de métodos operações que foram definidos por cada
             uma das classes, como operação de Soma, operação de Divisão, operação de Multiplicação etc.
            */

            while (opcao != 5)
            {
                Console.WriteLine("1 - Soma; 2 - Multiplicação; 3 - Subtração; 4 - Divisão; 5 - Sair.");
                opcao = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine("Digite o primeiro valor: ");
                a = Convert.ToDouble(Console.ReadLine());

                Console.WriteLine("Digite o segundo valor: ");
                b = Convert.ToDouble(Console.ReadLine());

                // Polimorfismo
                switch (opcao)
                {
                    case 1:
                        operacao = new Soma();
                        break;
                    case 2:
                        operacao = new Multiplicacao();
                        break;
                    case 3:
                        operacao = new Subtracao();
                        break;
                    case 4:
                        operacao = new Divisao();
                        break;
                    default:
                        break;
                }
                // Se as classes não implementassem a interface IOperacao, não seria possível fazer o código assim, pois não poderiamos
                // converter implincitamente o objeto de uma classe em outra.

                operacao.calcular(a, b);
                operacao.mostrar();

                Console.ReadLine();
                Console.Clear();

            }
        }
    }
}