using System;

namespace Genéricos
{
    public class ComparaClass<TipoA, TipoB>
    {
        public void Compara(TipoA p1, TipoB p2)
        {
            bool resultado;
            resultado = p1.Equals(p2);
            Console.WriteLine("Os Parâmetros são iguais? {0}", resultado);
        }
    }
}