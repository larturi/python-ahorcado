from operator import le
import os
from palabras import *

# Variables globales
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

# Funciones

def elegir_palabra():
    palabra_elegida = get_word()
    letras_unicas = len(set(palabra_elegida))
    
    return palabra_elegida, letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedrio = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    while not es_valida:
        letra_elegida = input('Elige una letra: ').lower()
        if len(letra_elegida) == 1 and letra_elegida in abecedrio:
            es_valida = True
        else:
            print('Escribe una letra válida')

    return letra_elegida

def mostrar_nuevo_tablero(palabra):
    lista_oculta = []
    
    for l in palabra:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('_')
            
    print(' '.join(lista_oculta))
    
def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False
            
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in letras_incorrectas or letra_elegida in letras_correctas:
        pass
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)

    return vidas, fin, coincidencias
        
def perder():
    print('Perdiste! La palabra era: ' + palabra)
    return True

def ganar(palabra_oculta):
    mostrar_nuevo_tablero(palabra_oculta)
    print('Ganaste! La palabra era: ' + palabra_oculta)
    return True


# Juego
palabra, letras_unicas = elegir_palabra()

while not juego_terminado:
    clear = lambda: os.system('clear')
    clear()
    print('\n')
    print("Ahorcado.py!")
    print("__________________")
    print('LETRAS INCORRECTAS: ' + '-'.join(letras_incorrectas))    
    print(f'VIDAS: {intentos}')
    mostrar_nuevo_tablero(palabra)
    
    print('\n')
    letra = pedir_letra()
    
    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
    
    juego_terminado = terminado

