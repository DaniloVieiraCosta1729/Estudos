// See https://aka.ms/new-console-template for more information
using System;
using System.Collections.Generic;
using System.Text;

namespace aula1
{
    class Program
    {
        public static void Main()
        {
            // Para criarmos um objeto, nós precisamos criar uma instância da class Conta
            Conta conta1 = new Conta(001); // é dessa forma que instaciamos a classe Conta. Acabomos de criar um objeto.
            Conta conta2 = new Conta(002);

            // conta1.saldo = 1500; // O "set" nos permite atribuir um valor a esse atributo do objeto "conta1" =D
            // conta1.limite = 500;
            // conta1.numero = 123;

            // conta2.saldo = 200;
            // conta2.limite = 600;
            // conta2.numero = 456;

            conta1.deposita(50);
            conta1.deposita(2000);
            conta1.deposita(7121);
            conta1.adicionarLimite(1500);
            conta1.saca(50000);
            conta1.saca(1300);

            System.Console.WriteLine($"O seu saldo disponível é {conta1.consultaSaldoDisponivel()}");

            /*
                Existe um problema grave com o nosso código. O problema é que o atributo "saldo" é acessivel ao
                programador. Considere a seguinte situação:

                conta1.deposita(2000);
                conta1.deposita(7120);
                conta1.saldo = 10;

                perceba que a última linha de código simplesmente sobrescreve o saldo da conta. Se um programador fizer
                isso ele estará apagando o dinheiro da conta do cliente. Para resolver esse problema de segurança, podemos
                utilizar o modificador de acesso "private" na frente do "set". Assim, não teremos mais permissão de setar
                o valor de saldo.

                public double saldo { get; private set;}

                Ainda, acho que é mais interessante remover a opção de consultar o saldo "puro", i.e, o saldo sem o
                limite, portanto, vou tornar o atributo inteiro em privado.

                private double saldo { get; set;}

                Dessa forma, apenas a propria classe pode pegar (get) e setar (set) esse atributo.

            */

            System.Console.WriteLine($"Seu limite é {conta1.limite}");
            System.Console.WriteLine($"O número da sua conta é: {conta1.numero}");
            System.Console.WriteLine($"O limite de conta2 é {conta2.limite}");
        }
    }
}
