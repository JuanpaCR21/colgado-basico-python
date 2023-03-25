#CODIGO CREADO POR JUAN PABLO ALVARADO GRANADOS COPYRIGHT 2023


#PARA ESTE SISTEMA SE NECESITAN LOS SIGUIENTES COMANDOS EN EL CMD

#python -m pip install colorama
#pip install keyboard


#IMPORTACION DE LAS LIBRERIAS NECESARIAS
import random,sys,os,time,keyboard,audio,config
from colorama import Fore, init, Style

init(autoreset=True)

#LISTA DE LOS COLORES PARA EL TEXTO DEL TITULO (MERAMENTE ESTETICO)
l_colores = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]


#VARIABLE GLOBAL PARA EL PUNTAJE OBTENIDO
v_puntaje = 0

#FUNCIÓN QUE INICIA EL JUEGO
def ingame():
    #LISTA DE POSIBLES PALABRAS
    l_words = ["ventana", "computadora", "bicicleta", "café", "libro", "guitarra", "perro", "reloj", "sol", "nube"]
    v_selectWord = random.choice(l_words)
    global v_puntaje
    l_chars = ["_" for l in v_selectWord]
    v_fallos = 0
    while True:
        os.system("cls")
        print("".join(l_chars))
        print("fallos:",v_fallos)
        v_letra = input("Ingrese una letra: \n")
        if v_letra in v_selectWord:
            audio.play_sound(r'sounds\SF_Point.wav',volumen = config.v_soundVolume)
            for i in range(len(v_selectWord)):
                if v_selectWord[i] == v_letra:
                    l_chars[i] = v_letra
        else:
            v_fallos +=1
            audio.play_sound(r'sounds\SF_Error.wav', volumen = config.v_soundVolume)
            if v_fallos == 6:
                os.system("cls")
                print(Fore.RED + 'Has perdido. La palabra era:', v_selectWord)
                v_puntaje -= 5
                input("Precione cualquier tecla para continuar")
                break
        if "".join(l_chars) == v_selectWord:
            os.system("cls")
            print(Fore.GREEN + 'EXCELENTE, HAS ADIVINADO LA PALABRA. La palabra era:', v_selectWord)
            v_puntaje += 10
            input("Precione cualquier tecla para continuar")
            break

#FUNCIÓN PARA MOSTRAR LAS INSTRUCCIONES DEL JUEGO
def instructions():
        os.system("cls")
        print("Instrucciones: \nAdivina la palabra oculta ingresando una letra a la vez. Tienes 6 intentos antes de perder. ¡Buena suerte!")
        input("Precione cualquier tecla para continuar")


#FUNCIÓN PARA MOSTRAR LAS DIFERENTES CONFIGURACIONES
def configs():
    os.system("cls")
    audio.play_sound(r'sounds\sound1.wav', volumen = config.v_soundVolume)
    print("Configuraciones:")
    print("1-Sonidos del juego (Por default: True):", config.v_musicPlay )
    print("2-Salir")
    v_op = input("Precione el numero de opción para alternar su valor (1/2): \n")
    if v_op == "1":
        audio.play_sound(r'sounds\sound1.wav', config.v_soundVolume)
        if config.v_musicPlay == True:
            config.v_musicPlay = False
        else:
            config.v_musicPlay = True
        configs()
    elif v_op == "2":
        print("")        
    else:
        print("")





#FUNCIÓN PARA EL MENÚ PRINCIPAL
def main_interface():
    os.system("cls")
    global v_puntaje
    if v_puntaje != 0:
        print("Su puntaje actual es de: ", v_puntaje)
    print("Menú Principal")
    print("1-Jugar \n2-Instrucciones \n3-Configuraciones \n4-Salir\nOtras opciones en camino")
    v_op = input("Dijite la opción que desea(1/2) \n")
    if v_op == "1":
        audio.play_sound(r'sounds\sound1.wav', config.v_soundVolume)
        ingame()
        main_interface()
    elif v_op == "2":
        audio.play_sound(r'sounds\sound1.wav', config.v_soundVolume)
        instructions()
        main_interface()
    elif v_op == "3":
        configs()
        main_interface()
    elif v_op == "4":
        audio.play_sound(r'sounds\sound1.wav', config.v_soundVolume)
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
    audio.play_sound(r'sounds\sound1.wav', config.v_soundVolume)
    main_interface()

    
main()