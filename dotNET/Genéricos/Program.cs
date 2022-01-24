using System;
using System.Collections.Generic;

namespace Genéricos
{
    class Program
    {
        static void Main(string[] args)
        {
            int i1 = 2;
            int i2 = 2;

            float f1 = 2;
            float f2 = 2;

            string s1 = "2";
            string s2 = "2";

            Compara(i1, i2);
            Compara(f1, f2);
            Compara(s1, s2);
            Compara(s2, i1);

            Console.ReadKey();
        }
        /*
        static void Compara(int p1, int p2)
        {
            bool resultado;
            resultado = p1.Equals(p2);
            Console.WriteLine("Os parametros são iguais? {0}", resultado);
        }

        // Para usar float no método Compara, é preciso copiar e colar o médoto Compara, mudando apenas o tipo 
        // de entrada. (Na verdade isso deve ser resolvido com os Generics)
        
        static void Compara(float p1, float p2)
        {
            bool resultado;
            resultado = p1.Equals(p2);
            Console.WriteLine("Os parametros são iguais? {0}", resultado);
        }

        static void Compara(string p1, string p2)
        {
            bool resultado;
            resultado = p1.Equals(p2);
            Console.WriteLine("Os parametros são iguais? {0}", resultado);
        }
        */

        // Ao invés disso, podemos usar os generics! Isso substitui a necessidade de se copiar o mesmo método
        // várias vezes.
        
        static void Compara<TipoGenericoA, TipoGenericoB>(TipoGenericoA p1, TipoGenericoB p2)
        {
            bool resultado;
            resultado = p1.Equals(p2);
            Console.WriteLine("Os parametros são iguais? {0}", resultado);
        }
    }   
}