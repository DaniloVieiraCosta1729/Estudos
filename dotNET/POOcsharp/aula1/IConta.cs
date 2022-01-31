using System;
using System.Collections.Generic;
using System.Text;

namespace aula1
{
    public interface IConta
    {
        void deposita(double x); // As clases que implementarem essa interface devem cumprir um "contrato" que consiste
        // em implementar os métodos presentes na interface.
        // Ao contrário das clases abstratas, as interfaces não têm atributos. Nenhuma classe deriva de uma interface,
        // elas apenas implementam as interfaces. A sintaxe de implementação é a mesmo da de herança. Uma classe pode
        // ser derivada de apenas uma outra classe, porém, pode implementar quantas interfaces quiser.
        bool saca(double x);
        double consultaSaldoDisponivel();
        void adicionarLimite(double x);
    }
}