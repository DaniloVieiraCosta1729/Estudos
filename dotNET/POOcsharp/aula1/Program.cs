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
            AnalistaDeTI analistaDeTI = new AnalistaDeTI();

            // analistaDeTI.nome = "Galo Cego";
            analistaDeTI.adicionarNome("Galo", "Cego");
            analistaDeTI.adicionarSalario(1000);
            analistaDeTI.reajustar();

            // analistaDeTI.salario = 4000;

            Console.WriteLine($"O novo salário de {analistaDeTI.nome} é R$ {analistaDeTI.salario}");

            // ContaPoupança contaP = new ContaPoupança(001, 0);
            // ContaCorrente contaC = new ContaCorrente(001, 100);

            // contaP.deposita(500);
            // contaC.deposita(200);
            // contaP.saca(50);

            // Console.WriteLine($"Conta Poupança - Saldo: {contaP.consultaSaldoDisponivel()}");
            // Console.WriteLine($"Conta Corrente - Saldo: {contaC.consultaSaldoDisponivel()}");


            // AnalistaDeTI analistaDeTI = new AnalistaDeTI();
            // Gerente gerente = new Gerente();
            // GerenteDeAgencia gerenteDeAgencia = new GerenteDeAgencia();
            // GerenteDeTI gerenteDeTI = new GerenteDeTI();

            // analistaDeTI.nome = "Nal do Canal";
            // analistaDeTI.salario = 3000;

            // System.Console.WriteLine($"O salário de {analistaDeTI.nome} é R$ {analistaDeTI.salario}");

            // analistaDeTI.reajustar();

            // System.Console.WriteLine($"Agora o salário de {analistaDeTI.nome} é de R$ {analistaDeTI.salario}");

            // System.Console.WriteLine($"======================================================================");
            
            // gerente.nome = "Chosen Undead";
            // gerente.salario = 8000;

            // System.Console.WriteLine($"O salário de {gerente.nome} é R$ {gerente.salario}");

            // gerente.reajustar();

            // System.Console.WriteLine($"Agora o salário de {gerente.nome} é de R$ {gerente.salario}");

            // System.Console.WriteLine($"======================================================================");
            
            // gerenteDeAgencia.nome = "Nanami Kento";
            // gerenteDeAgencia.salario = 8000;

            // System.Console.WriteLine($"O salário de {gerenteDeAgencia.nome} é R$ {gerenteDeAgencia.salario}");

            // gerenteDeAgencia.reajustar();

            // System.Console.WriteLine($"Agora o salário de {gerenteDeAgencia.nome} é de R$ {gerenteDeAgencia.salario}");

            // System.Console.WriteLine($"======================================================================");
            
            // gerenteDeTI.nome = "Chosen Undead";
            // gerenteDeTI.salario = 8000;

            // System.Console.WriteLine($"O salário de {gerenteDeTI.nome} é R$ {gerenteDeTI.salario}");

            // gerenteDeTI.reajustar();

            // System.Console.WriteLine($"Agora o salário de {gerenteDeTI.nome} é de R$ {gerenteDeTI.salario}");

            // ContaPoupança contaP1 = new ContaPoupança(123, 700);
            // contaP1.deposita(3500);

            // System.Console.WriteLine($"O saldo da sua conta poupança é {contaP1.consultaSaldoDisponivel()}");

            // Conta conta1 = new Conta(123, 500);
            // Conta conta2 = new Conta(456, 800);
            // Conta conta3 = new Conta(789, 900);

            // System.Console.WriteLine($"Até o momento foram criadas {Conta.totalContasCriadas} contas.");

            // Criando um objeto de cada classe.
            // CartaoDeCredito	cartao1 = new CartaoDeCredito();
            // Cliente cliente1 = new Cliente();

            // Adicionando nome do cliente.
            // cliente1.nome = "Pu-kemon! Eu vou lhe achar Pikemon.";

            // Adicionando número e data de validade do cartão de credito.
            // cartao1.numero = "1123581321";
            // cartao1.dataDeValidade = "02/2025";
            // cartao1.cliente = cliente1;

            // System.Console.WriteLine($"O nome do cliente é {cartao1.cliente.nome}");
            // System.Console.WriteLine($"O número do cartão é {cartao1.numero}");
            // System.Console.WriteLine($"A data de validade do cartão é {cartao1.dataDeValidade}");

            // Para criarmos um objeto, nós precisamos criar uma instância da class Conta
            // Conta conta1 = new Conta(001); // é dessa forma que instaciamos a classe Conta. Acabamos de criar um objeto.
            // Conta conta2 = new Conta(002);

            // conta1.saldo = 1500; // O "set" nos permite atribuir um valor a esse atributo do objeto "conta1" =D
            // conta1.limite = 500;
            // conta1.numero = 123;

            // conta2.saldo = 200;
            // conta2.limite = 600;
            // conta2.numero = 456;

            // conta1.deposita(50);
            // conta1.deposita(2000);
            // conta1.deposita(7121);
            // conta1.adicionarLimite(1500);
            // conta1.saca(50000);
            // conta1.saca(1300);

            // System.Console.WriteLine($"O seu saldo disponível é {conta1.consultaSaldoDisponivel()}");

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

            // System.Console.WriteLine($"Seu limite é {conta1.limite}");
            // System.Console.WriteLine($"O número da sua conta é: {conta1.numero}");
            // System.Console.WriteLine($"O limite de conta2 é {conta2.limite}");
        }
    }
}
