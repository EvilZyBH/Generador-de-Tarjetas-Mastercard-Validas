from termcolor import colored
import pyfiglet
from faker import Faker
from colorama import Fore, Style
import os

fake = Faker()

# Define las marcas de tarjetas que se pueden generar
marcas = ["mastercard"]

# Define una función para validar la tarjeta utilizando el algoritmo de Luhn
def luhn_algorithm(numero_tarjeta):
    suma = 0
    longitud = len(numero_tarjeta)
    para_multiplicar = (longitud + 1) % 2
    for i, digito in enumerate(numero_tarjeta):
        multiplicador = 1
        if i % 2 == para_multiplicar:
            multiplicador = 2
        resultado = int(digito) * multiplicador
        if resultado > 9:
            resultado -= 9
        suma += resultado
    return suma % 10 == 0

# Define una función para generar una tarjeta
def generar_tarjeta():
    marca = fake.random.choice(marcas)
    if marca.lower() != "mastercard":
        while True:
            tarjeta = fake.credit_card_number(card_type=marca)
            if tarjeta[0] not in ["2", "5"] and not tarjeta.startswith("543913"):
                break
    else:
        tarjeta = fake.credit_card_number(card_type=marca)
    fecha_vencimiento = fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y")
    cvv = fake.credit_card_security_code(card_type=marca)
    return marca, tarjeta, fecha_vencimiento, cvv

os.system('cls' if os.name == 'nt' else 'clear') # limpia la pantalla

print(colored(pyfiglet.figlet_format("Generador de Tarjetas Mastercard"), "magenta"))
print
print
print ("Author   : Evil Bryan Hernandez")
print ("TikTok   : https://www.tiktok.com/@seguidores_del_temach")
print ("github   : https://github.com/EvilZyBH")
print()
print()
while True:
    print("¿Qué deseas hacer?")
    print(colored("1. Generar y guardar tarjetas válidas", "cyan"))
    print(colored("2. Salir", "cyan"))
    opcion = input(colored("Selecciona una opción: ", "yellow"))
    
    if opcion == "1":
        cantidad = int(input(colored("¿Cuántas tarjetas válidas deseas generar y guardar?: ", "yellow")))
        tarjetas_validas = []
        while len(tarjetas_validas) < cantidad:
            marca, tarjeta, fecha_vencimiento, cvv = generar_tarjeta()
            if luhn_algorithm(tarjeta):
                tarjetas_validas.append((marca, tarjeta, fecha_vencimiento, cvv))
        with open("tarjetas_validas.txt", "a") as archivo:
            for marca, tarjeta, fecha_vencimiento, cvv in tarjetas_validas:
                mensaje = "Tarjeta válida\n"
                mensaje += "Marca: " + marca + "\n"
                mensaje += "Tarjeta: " + tarjeta + "\n"
                mensaje += "Fecha de vencimiento: " + fecha_vencimiento + "\n"
                mensaje += "CVV: " + cvv + "\n\n"
                archivo.write(mensaje)
                print(Fore.GREEN + "Tarjeta válida" + Style.RESET_ALL)
                print(Fore.MAGENTA + "Marca:" + Style.RESET_ALL, marca)
                print(Fore.YELLOW + "Tarjeta:" + Style.RESET_ALL, tarjeta)
                print(Fore.BLUE + "Fecha de vencimiento:" + Style.RESET_ALL, fecha_vencimiento)
                print(Fore.WHITE + "CVV:" + Style.RESET_ALL, cvv)
        print(Fore.WHITE + "Se han generado " +  str(len(tarjetas_validas)) + " tarjetas válidas y se han guardado en el archivo tarjetas_validas.txt" + Style.RESET_ALL)
    
    elif opcion == "2":
        print("Hasta luego")
        break
    
    else:
        print("Opción inválida. Intenta de nuevo.")

