using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Exercicios_de_Csharp
{
    public class exercicio5
    {
        public static void Exercicio_5()
        {
            // Deve perguntar quantos testes são e incluir quantos alunos o professor desejar;
            // Pede as notas de cada aluno e salva em um array;
            // Faz a média geométrica, aritmética e harmônica dos alunos.
            string tab = "            ";
            string linha = $"{tab}===================================================================================";
            Console.WriteLine(linha);
            Console.WriteLine($"{tab}Sistema de Avaliação");
            Console.WriteLine(linha);

            bool teste = true;
            while (teste == true)
            {
                retorno:
                Console.WriteLine($"{tab}Deseja cadastrar as notas de um novo aluno? [S/N]");
                Console.Write($"{tab}Digite: ");
                string resposta = Console.ReadLine().ToUpper();

                switch (resposta)
                {
                    case "S":
                        Console.Clear();
                        Console.WriteLine(linha);
                        Console.WriteLine($"{tab}Sistema de Avaliação");
                        Console.WriteLine(linha);
                        Console.Write($"{tab}Digite o nome do aluno: ");
                        string nome = Console.ReadLine();
                        Alunos nomeAluno = new Alunos(nome);
                        nomeAluno.AtribuirNotas();
                        nomeAluno.MostrarMedia();
                        Console.WriteLine($"{linha}");
                        break;

                    case "N":
                        teste = false;
                        break;

                    default:
                        Console.WriteLine($"{tab}Entrada invalida. Por favor, digite \"S\" para SIM (sem as aspas) e \"N\" para NÃO.");
                        Console.ReadLine();
                        Console.Clear();
                        goto retorno;
                }
            }
            Console.WriteLine("\n\n\n");
            Console.WriteLine(linha);
            Console.WriteLine($"{tab}Fim do Programa.");
            Console.WriteLine(linha);
        }
    }

    public class Alunos : Escola
    {
        public string Nome { get; set; }
        private double[] Notas { get; set; }

        public Alunos(string nome)
        {
            this.Nome = nome;
        }

        public void AtribuirNotas()
        {
            this.Notas = new double[NumeroTestes];

            for (int i = 0; i < NumeroTestes; i++)
            {
                Console.Write($"{tab}Digite a nota de {this.Nome} no {i + 1}º teste: ");
                this.Notas[i] = Convert.ToDouble(Console.ReadLine());
            }
        }

        public double MediaAritmetica()
        {
            double soma = 0;

            for (int i = 0; i < NumeroTestes; i++)
            {
                soma += this.Notas[i];
            }

            double resultado = soma / NumeroTestes;

            return resultado;
        }

        public double MediaGeometrica()
        {
            double produto = 1;

            foreach (double i in this.Notas)
            {
                produto *= i;
            }

            double resultado = Math.Pow(produto, 1.0 / (double)NumeroTestes);

            return resultado;
        }

        public double MediaHarmonica()
        {
            double soma = 0;

            foreach (var i in this.Notas)
            {
                if (i == 0)
                {
                    soma += 0;
                }
                else
                {
                    soma += 1 / i;
                }
            }

            double resultado = NumeroTestes / soma;

            return resultado;
        }

        public void MostrarMedia()
        {
            Console.WriteLine(linha);
            Console.WriteLine($"{tab}A média aritmética de {this.Nome} é {this.MediaAritmetica()}");
            Console.WriteLine($"{tab}A média geometrica é {this.MediaGeometrica()}");
            Console.WriteLine($"{tab}E a média harmônica é {this.MediaHarmonica()}");
        }
    }

    public class Escola
    {
        public int NumeroTestes = 3;
        public string tab = "            ";
        public string linha = $"            ===================================================================================";
    }
}