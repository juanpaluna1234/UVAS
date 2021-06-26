"""
Juan Pablo Luna Mejia
11357 ENSURING TRUTH
"""
from sys import stdin

def main():
    casos = int(stdin.readline())
    while casos:
        cadena = stdin.readline().strip()
        if division(cadena):
            print("YES")
        else:
            print("NO")
        casos -= 1
"""
La funcion Main lo que hace es recibe la entrada y para cada formula que entre se llamada a division
la cual retorna si es satisfacible o no. Por eso esta el if donde imprime YES si lo es y NO si no lo es
"""
def division(cadena):
    cadena = cadena[1:len(cadena)-1]
    formula = cadena.split(")|(")
    i = 0
    res = False
    while i < len(formula) and not(res):
        res = res or evaluar(formula[i])
        i += 1
    return res
"""
La funcion division lo que hace es dividir la formula en subformulas que esta separadas por el or(|) y quita
los parentesis. Lo que hace es que para cada subformula llama a evaluar para determinar si esa sub formula
es satisfacible o no. Basta con que una sola cadena sea satisfacible por la naturaleza del or(|). El resultado
de este es retornado.
"""
def evaluar(formula):
    neg = []
    noNeg = []
    val = formula.split("&")
    res = True
    i = 0
    while i < len(val) and res:
        if val[i][0] == '~':
            temp = (val[i][1])
            if temp in noNeg:
                res = False
            neg.append(temp)
        else:
            temp = (val[i])
            if temp in neg:
                res = False
            noNeg.append(temp)
        i += 1
    return res
"""
La funcion evaluar lo que revibe es una formula con variables y negaciones separadas por and(&). Lo que se hace es
dividir la foruma por & y tenes una lista con todos las variables. Aqui existen dos posibilidades que la variable
este sola o este negada. Cuando esta sola entra a la lista noNeg y si esta negada entra a la lista de neg. En caso
de que una variable exista en ambas listas la expresion no es satisfacible y retorna False de lo contrario retorna
True
"""
main()

"""
Código de honor: Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
a seguir los más altos estándares de integridad académica.
"""
