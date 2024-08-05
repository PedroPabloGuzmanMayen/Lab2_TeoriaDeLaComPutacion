
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
estados, simbolos, estado_inicial, estados_aceptacion, transiciones = read_afd(filename)

#Función transition

def transition(state, char, transitions, alphabet, states):
    if char not in alphabet or state not in states:
        return False
    else:
        next_state = next((transition["q_prime"] for transition in transitions if transition["q"] == state and transition["a"] == char))
        return next_state
    
print(transition("q3", "a", transiciones, simbolos, estados))

