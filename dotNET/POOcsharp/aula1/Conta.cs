using System;
using System.Collections.Generic;
using System.Text;

namespace aula1
{
    public abstract class Conta : IConta // Esses : não significa herança, mas sim implementação, pois tratá-se de uma interface.
    {
        // Construtor
        public Conta(int x, double y = 300)
        {
            this.numero= x;
            this.limite = y;
            Conta.totalContasCriadas++;
        }

        // O nosso modelo de conta terá apenas três ATRIBUTOS: saldo, limite e número.
        public double saldo {get; protected set;} // criando o atributo "saldo";
        // a palavra get indica que o valor desse atributo pode ser acessado.
        // a palavra set indicia que podemos adicionar algum valor para o atributo saldo.
        public double limite {get; private set;} // criando o atributo "limite";
        public int numero {get; private set;}
        public static int totalContasCriadas {get; set;} // Perceba que esse atributo pertence a classe e não ao objeto 
        // que é instaciado pelo classe, portanto, dizemos que ele é ESTÁTICO. Para declarar um atributo ou método
        // estático, usamos a palavra chave "static".

        // vamos criar um MÉTODO para que seja possível fazer depositos.
        public void deposita(double x)
        {
            this.saldo += x; // a palavra "this" é equivalente ao self do Python. Ele refere-se ao objeto que está
            // utilizando o método.
        }

        public virtual bool saca(double x)
        {
            double saldoDisponivel = this.consultaSaldoDisponivel();
            if (x > saldoDisponivel)
            {
                System.Console.WriteLine($"Saque indisponível. \nO seu saldo é R$ {this.consultaSaldoDisponivel()}");
                return false;
            }
            else if(0 > x)
            {
                System.Console.WriteLine("O saque deve ser positivo.");
                return false;
            }
            else
            {
                this.saldo -= x;
                System.Console.WriteLine($"Saque bem sucedido! Você sacou R$ {x}");
                return true;
            }
        }

        public double consultaSaldoDisponivel()
        {
            return this.saldo + this.limite;
        }

        public void adicionarLimite(double x)
        {
            this.limite = x;
        }
    }
}