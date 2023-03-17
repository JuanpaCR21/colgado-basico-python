#CODIGO CREADO POR JUAN PABLO ALVARADO GRANADOS COPYRIGHT 2023


#PARA ESTE SISTEMA SE NECESITAN LOS SIGUIENTES COMANDOS EN EL CMD

#python -m pip install colorama
#pip install keyboard
#pip install playsound

#IMPORTACION DE LAS LIBRERIAS NECESARIAS
import random,sys,os,time,keyboard,audio
from colorama import Fore, init, Style

init(autoreset=True)

#LISTA DE LOS COLORES PARA EL TEXTO DEL TITULO (MERAMENTE ESTETICO)
l_colores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]



#FUNCIÓN QUE INICIA EL JUEGO
def ingame():
    #LISTA DE POSIBLES PALABRAS
    l_words = ["ventana", "computadora", "bicicleta", "café", "libro", "guitarra", "perro", "reloj", "sol", "nube"]
    v_selectWord = random.choice(l_words)
    l_chars = ["_" for l in v_selectWord]
    v_fallos = 0
    while True:
        os.system("cls")
        print("".join(l_chars))
        print("fallos:",v_fallos)
        v_letra = input("Ingrese una letra: \n")
        if v_letra in v_selectWord:
            audio.play_sound(r'hangman\sounds\SF_Point.wav')
            for i in range(len(v_selectWord)):
                if v_selectWord[i] == v_letra:
                    l_chars[i] = v_letra
        else:
            v_fallos +=1
            audio.play_sound(r'hangman\sounds\SF_Error.wav')
            if v_fallos == 6:
                os.system("cls")
                print(Fore.RED + 'Has perdido. La palabra era:', v_selectWord)
                input("Precione cualquier tecla para continuar")
                break
        if "".join(l_chars) == v_selectWord:
            os.system("cls")
            print(Fore.GREEN + 'EXCELENTE, HAS ADIVINADO LA PALABRA. La palabra era:', v_selectWord)
            input("Precione cualquier tecla para continuar")
            break


#FUNCIÓN PARA EL MENÚ PRINCIPAL
def main_interface():
    os.system("cls")
    print("Menú Principal")
    print("1-Jugar \n2-salir \nOtras opciones en camino")
    v_op = input("Dijite la opción que desea(1/2) \n")
    if v_op == "1":
        ingame()
        main_interface()
    elif v_op == "2":
        print("Saliendo...")
        sys.exit()
    else:
        print("Opción inválida.")
        time.sleep(1)
        main_interface()
    

#FUNCIÓN PRINCIPAL DEL SISTEMA, ESCRIBE EL TÍTULO
def main():
    enter_pressed = False
    while not enter_pressed:
        os.system("cls")
        t_color = random.choice(l_colores)
        print(t_color + "BIENVENIDO A AHORCADO by Juanpo :p" + Style.RESET_ALL)
        print("Presione shift para comenzar")
        if keyboard.is_pressed('shift'):
            enter_pressed = True
        time.sleep(0.1)
    audio.play_sound(r'hangman\sounds\sound1.wav')
    main_interface()

    
main()