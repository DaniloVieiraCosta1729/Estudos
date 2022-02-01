using System;
using System.Collections.Generic;
using System.Text;

namespace aula1
{
    public abstract class Funcionario // abstract informa que essa é uma classe modelo para as classes concretas
    {
        public string nome {get; set;}
        public double salario {get; protected set;}

        public abstract void reajustar(); // perceba que não implementamos o método abstrato, pois quem deve implementá-lo são
        // as classes concretas (classes que derivam da classe abstrata). Isso está fortemente ligado ao conceito de
        // polimorfismo do POO. Todos os funcionarios podem ter seu salário reajustado, porém esse reajuste acontece de 
        // forma diferente, ou seja, a classe concreta "Professor" implementará o método "reajustar" de forma diferente
        // da classe concreta cozinheiro. P.S.: Classes abstratas não podem ser instaciadas, apenas herdadas.

        public void adicionarNome(string primeiro, string segundo)
        {
            this.nome = $"{primeiro} {segundo}";
        }

        public void adicionarSalario(double salario)
        {
            this.salario = salario;
        }
    }
}