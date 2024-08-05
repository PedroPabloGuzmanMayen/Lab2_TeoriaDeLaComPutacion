
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

# Ruta del archivo JSON
filename = 'afd.json'
states, alphabet, estado_inicial, estados_aceptacion, transiciones = read_afd(filename)

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
        state = transition(state, i, transitions )

    return state


print(final_state("q0", "abaa", transiciones))

