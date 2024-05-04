opcion= int(input("Ingrese un 1(UNO) si desea cambiar de Celsius a Fahrenheit, o un 2(DOS) de Fahrenheit a Celsius: "))

if opcion == 1:
    celsius = float (input("Ingrese la Temperatura en Grados Celsius: "))
    fahrenheit =  (celsius * 9/5) + 32
    print ("La Temperatura es Igual a ", fahrenheit, "° Fahrenheit")

if opcion == 2:
    fahrenheit = float(input("Ingrese la Temperatura en Grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print ("La Temperatura es Igual a ", celsius, "° Celsius")


