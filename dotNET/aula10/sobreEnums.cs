// See https://aka.ms/new-console-template for more information
using System;

class Aula10
{
    enum DiasdaSemana{Domingo, Segunda, Terça, Quarta, Quinta, Sexta, Sábado}

    static void Main()
    {
        DiasdaSemana primeiroDia = DiasdaSemana.Domingo;
        DiasdaSemana ultimoDia = (DiasdaSemana)6;
        int num = (int)DiasdaSemana.Quinta;

        Console.WriteLine("{0} \n{1} \n{2}", primeiroDia, ultimoDia, num);
    }
}