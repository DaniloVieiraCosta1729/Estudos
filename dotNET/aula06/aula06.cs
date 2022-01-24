// See https://aka.ms/new-console-template for more information
using System ;
class aula06
{
    static void Main()
    {
        int n1, n2, n3;
        n1 = 1; n2 = 2; n3 = 3;
        Console.WriteLine("{0}, {1}, {2}", n1, n2, n3);
        Console.WriteLine("{0, 15}\n{1, 10}\n{2, 5}", n1, n2, n3);
        Console.WriteLine("{0, 5:c}\n{1, 10:p}\n{2, 15:c}", n1, n2, n3);
    }
    static string explicando()
    {
        string a = "Para começar um projeto dotNET pelo terminal devemos usar o comando: ";
        a = a + " dotnet new \nDepois de digitar esse comando podemos incluir alguns recursos que queremos ";
        a = a + "usar, por exemplo,\n por exemplo, qual linguagem de programação usaremos.\n";
        a = a + "Antes de criar um projeto, podemos ver uma lista de templates, com o comando: \n";
        a = a + "dotnet new --list";
        return a;
    }
}
