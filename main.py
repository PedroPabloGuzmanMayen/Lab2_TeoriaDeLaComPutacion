
import json

#Función para leer archivos json con la estructura del autómata
def leer_afd(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        afd = json.load(archivo)
    
    # Leer y mostrar los datos del autómata
    estados = afd.get('Q', [])
    simbolos = afd.get('Σ', [])
    estado_inicial = afd.get('q0', '')
    estados_aceptacion = afd.get('F', [])
    transiciones = afd.get('δ', [])
    
    print("Estados:", estados)
    print("Símbolos:", simbolos)
    print("Estado inicial:", estado_inicial)
    print("Estados de aceptación:", estados_aceptacion)
    
    print("Transiciones:")
    for transicion in transiciones:
        print(f"δ({transicion['q']}, {transicion['a']}) = {transicion['q_prime']}")

# Ruta del archivo JSON
ruta_archivo = 'afd.json'
leer_afd(ruta_archivo)
