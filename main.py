import random  # Importamos la librería random
# Para implementar puntajes, crearemos una nueva variable llamada "puntaje", la que inicializamos en 0.
import time

puntaje = 0
# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
iniciar_trivia = True  # Iniciamos la variable en True
intentos = 0  # variable que almacenará el número de veces que el usuario intenta nuestra trivia.

print ("\033[34mBienvenido a mi trivia sobre las criaturas del mar\033[39m")
print ("\033[36mPondremos a prueba tus conocimientos\033[39m")
#nueva variable
nombre = input("Cuál es tu nombre?: ")
time.sleep(1)
print ("lindo nombre ...")
time.sleep(1)


while iniciar_trivia == True: #  Mientras iniciar_trivia sea True, repite:
  intentos += 1
  puntaje = 0

  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")

  # Es importante dar instrucciones sobre cómo jugar:
  print ("\n Hola", nombre, "Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n")
  
  # Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable
  
  # Pregunta 1
  print ("\033[33mPregunta 1\033[39m")
  print ("1) ¿Cuál es el pez más rápido?")
  print ("a) tiburon martillo")
  print ("b) Pez vela")
  print ("c) pez espada")
  print ("d) tiburon tigre")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ")
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_1=="b":
    puntaje += 10
    print("Muy bien", nombre, "! (ˆ‿ˆ)\n")
  else: print("Incorrecto\n")
  print(nombre, "llevas", puntaje, "puntos")
  time.sleep(2)
  # Pregunta 2
  print ("\033[33mPregunta 2\033[39m")
  print ("1) ¿Qué especie no puede dejar de nadar?")
  print ("a) morsa")
  print ("b) delfin")
  print ("c) ballena")
  print ("d) tiburon")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_2 = input("\nTu respuesta: ")
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  # Ahora, verificamos su respuesta para mandar un mensaje de acierto o de error
  if respuesta_2 == "a":
    print("Incorrecto!", nombre, "la morsa puede dejar de nadar")
  elif respuesta_2 == "b":
    print("Incorrecto!", nombre, "el delfi puede dejar de nadar")
  elif respuesta_2 == "c":
    print("Incorrecto!", nombre, "la ballena puede dejar de nadar")
  else:
    puntaje +=10
    print("Muy bien", nombre, "! (ˆ‿ˆ)\n")
  print(nombre, "llevas", puntaje, "puntos")
  time.sleep(2)
  
  # Pregunta 3
  print ("\033[33mPregunta 3\033[39m")
  print ("1) ¿cuántos corazones tiene un pulpo?")
  print ("a) 1")
  print ("b) 2")
  print ("c) 3")
  print ("d) 4")
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_3 = input("\nTu respuesta: ")
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  
  if respuesta_3 == "a":
    print ("Totalmente incorrecto! ...")
    puntaje = puntaje / 2
  elif respuesta_3 == "d":
    print ("incorrecto pero te regalaré 5 puntos >_^...")
    puntaje = puntaje + 5
  elif respuesta_3 == "b":
    print ("Incorrecto! ...")
    puntaje = puntaje - 5
  else:
    print ("Correcto! ...")
    puntaje = puntaje * 2
  
  print("Gracias", nombre, "por jugar mi trivia, tienes", puntaje, "puntos")
  
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  # != significa "distinto"
   print("\nEspero que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.