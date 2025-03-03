num1 = float(input("Ingrese el primer valor: "))
operador = input("""operador:
    >  /
    >  *
    >  +
    >  -
seleccione: """)
num2 = float(input("Ingrese el segundo valor: "))


if operador == "-":
    resultado = num1 - num2
elif operador == "+":
    resultado = num1 + num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 and num1 != 0:
        resultado = num1 / num2
    else:
        resultado = "no se puede divir por 0"
else:
    resultado = "Operacion invalida"

print (f"Resultado de ({num1} {operador} {num2}) = {resultado}")