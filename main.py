
import json

#Función para leer archivos json con la estructura del autómata
def read_afd(filename):
    with open(filename, 'r') as file:
        afd = json.load(file)
    
    # Leer los datos del autómata
    estados = afd.get('Q', [])
    simbolos = afd.get('Σ', [])
    estado_inicial = afd.get('q0', '')
    estados_aceptacion = afd.get('F', [])
    transiciones = afd.get('δ', [])

    return estados, simbolos, estado_inicial, estados_aceptacion, transiciones



#Función transition

def transition(state, char, transitions):
    if char not in alphabet or state not in states:
        return False
    else:
        next_state = next((transition["q_prime"] for transition in transitions if transition["q"] == state and transition["a"] == char))
        return next_state
    
#Función final state

def final_state(state, word, transitions):
    for i in word:
        state = transition(state, i, transitions)

    return state


#Función derivation

def derivation(state, word, transitions):
    register = []
    for i in word:
        register.append([state, i])
        state = transition(state, i, transitions)
        register[len(register)-1].append(state)

    return register


#Función de aceptación

def accepted(state, word, finalStates, transitions):
    result = final_state(state, word, transitions)
    if result in finalStates:
        return True
    else:
        return False
    

cond = True
filename = input("Ingresa el nombre del archivo en donde está el autómata: ")
states, alphabet, estado_inicial, estados_aceptacion, transiciones = read_afd(filename)

while cond:
    print()
    print("1. Usar la función transición")
    print("2. Determinar el estado final dada una cadena")
    print("3. Obtener las transiciones dada una cadena")
    print("4. Determinar si una cadena es aceptada")
    print("5. Salir")

    opt = int(input("¿Qué deseas hacer?"))

    if opt == 1:
        q = input("Ingresa el estado: ")
        char = input("Ingresa el caracter: ")
        print(transition(q, char, transiciones))
    if opt == 2:
        q = input("Ingresa el estado: ")
        cadena = input("Ingresa la cadena: ")
        print(final_state(q, cadena, transiciones))

    if opt == 3:
        q = input("Ingresa el estado: ")
        cadena = input("Ingresa la cadena: ")
        register = derivation(q, cadena, transiciones)
        for i in register:
            print(f"Desde {i[0]} con caracter {i[1]} hasta el estado {i[2]}")

    if opt == 4:
        q = input("Ingresa el estado: ")
        cadena = input("Ingresa la cadena: ")
        resultado = accepted(q, cadena, estados_aceptacion, transiciones)
        if resultado == True:
            print(f"La cadena {cadena} es aceptada ")
        else:
            print(f"La cadena {cadena} no es aceptada ")

    if opt == 5:
        cond = False






