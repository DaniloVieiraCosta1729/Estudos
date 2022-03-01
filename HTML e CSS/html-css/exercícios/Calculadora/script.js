function insert(n)
{
    var num = document.getElementById('resultado').innerHTML;

    if (num == "0")
    {
        document.getElementById('resultado').innerHTML = "";
    }

    if (num[0] == "0")
    {
        num = num.replace('0','');
    }

    document.getElementById('resultado').innerHTML = num + n;
}

function back()
{
    var num = document.getElementById('resultado').innerHTML;

    num = num.substring(0, num.length - 1);

    document.getElementById('resultado').innerHTML = num;
}

function clean()
{
    document.getElementById('resultado').innerHTML = '0';
}

function igual() 
{
    var expressao = document.getElementById('resultado').innerHTML;

    try {
        if (expressao != '') {
            document.getElementById('resultado').innerHTML = eval(expressao);
        }
    } catch (error) {
        console.alert('Houve um erro. Por favor, formate o valor de entrada para uma expressão valida.');
    }
}