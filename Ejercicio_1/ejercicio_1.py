def main():
    import random # Libreria para ocupar la funcion random

    # contador de intentos
    num_intentos = 0
    num = random.randint(1, 100) # Retorna un entero aleatorio N (entre 1 y 100)
    print ("Adivina un numero entre 1 a 100")

    # Mientras el numero de intentos sea menor a 10 se realiza el ciclo 
    while num_intentos < 10:
        num_intentos += 1
        estimacion = int(input("Indique el numero que cree que es: "))
        # Si el numero ingresado es menor al numero generado se muestra el mensaje del print
        if estimacion < num:
            print("La estimacion que acaba de realizar es baja.")
        # Si el numero ingresado es mayor al numero generado se muestra el mensaje del print
        if estimacion > num:
            print("La estimacion que acaba de realizar es alta.")
        # Si el numero ingresado es igual al numero generado se paraliza el bucle while
        if estimacion == num:
            break

    # Si el numero ingresado es igual al numero generado se muestra el mensaje del print
    if estimacion == num:
        print("Congratulations. Adivinaste el numero en "+str(num_intentos)+" intentos.")
    # Si no se cumple la condicion del if, se muestra este print
    else:
        print("Failed. El numero en realidad era --> "+str(num)+".")

    return

if __name__ == "__main__":
    main()

