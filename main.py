"""
    Universidad del Valle de Guatemala
    Teoría de la Computación
    Profesor: Allan Reyes

    Proyecto 3: Máquina de Turing
    Descripción: Implementación de una máquina de Turing que verifica si una cadena binaria es un palíndromo.
    Integrantes:
        - Abner Iván García Alegría - 21285
        - Oscar Esteban Donis Martínez - 21610
        - Adrian Rodriguez Batres - 21691 
"""

def read_file():
    # Variables para guardar los datos del archivo
    estados = []
    alfabeto_entrada = []
    alfabeto_cinta = []
    func_transition = {}
    estado_inicial = ""
    sim_blanco = ""
    estados_aceptacion = []

    # Abrir el archivo
    with open('machine.txt', 'r') as file:
        contador = 0

        # Leer el archivo linea por linea
        for line in file:

            # En caso sea las reglas de la función de transición
            if "=" not in line:
                # Eliminar los espacios en blanco y los paréntesis
                line = line.strip().replace('(', '').replace(')', '').replace(' ', '')
                value = [tuple(filter(None, v.split(','))) for v in line.split('->')]
                try:
                    func_transition[value[0]] = value[1]
                except IndexError:
                    print()
                continue

            # En caso contrario, leer la variable y el valor
            key, value = line.split('=')
            key = key.strip()
            value = value.strip()

            if '{' in value and '}' in value:
                value = value.replace('{', '').replace('}', '').replace(' ', '')
                value = value.split(',')
            
            # Dependiendo de la variable guardamos los datos
            if key == "ESTADOS":
                estados = value
            elif key == "ALFABETO DE ENTRADA":
                alfabeto_entrada = value
            elif key == "ALFABETO DE CINTA":
                alfabeto_cinta = value
            elif key == "ESTADO INICIAL":
                estado_inicial = value
            elif key == "SIMBOLO BLANCO":
                sim_blanco = value
            elif key == "ESTADOS FINALES":
                estados_aceptacion = value

            contador += 1

    return estados, alfabeto_entrada, alfabeto_cinta, func_transition, estado_inicial, sim_blanco, estados_aceptacion


def maquina_turing(estados, alfabeto_entrada, alfabeto_cinta, func_transition, estado_inicial, sim_blanco, estados_aceptacion, w, starter):
    
    # Definimos la posición inicial en la cinta
    input_actual = starter
    flag = False
    print("Transiciones:")

    # Mientras no lleguemos al inicio de la cinta, seguimos iterando
    while input_actual != 0 and input_actual != len(w) - 1:
        # Si el estado actual es un estado de aceptación, entonces la cadena es un palíndromo
        if estado_inicial in estados_aceptacion:
            flag = True
            break
        # Si por caso contrario el estado actual no se encuentra en los estados de aceptación, entonces seguimos moviendono en las reglas de la función de transición
        else:
            # Obtenemos la transición
            transition = func_transition[(estado_inicial, w[input_actual])]
            # Imprimimos la transición
            print("(" + estado_inicial + ", " + w[input_actual] + ")","->", transition)
            # Actualizamos el estado actual y el valor de la cinta
            estado_inicial = transition[0]
            w[input_actual] = transition[1]
            # Actualizamos la posición en la cinta
            if transition[2] == "R":
                input_actual += 1
            else:
                input_actual -= 1
    
    # Imprimimos valores de salida
    print()
    print("Estado final:", estado_inicial)
    print("Resultado de cinta:", w)
    if flag:
        print("La cadena w es un palíndromo")
    else:
        print("La cadena w no es un palíndromo")


def main():
    # Leemos los datos del archivo
    estados, alfabeto_entrada, alfabeto_cinta, func_transition, estado_inicial, sim_blanco, estados_aceptacion = read_file()

    # Pedimos la cadena de entrada
    input_user = input("Enter a number: ")
    print()

    # Verificamos que la cadena de entrada sea binaria
    for i in input_user:
        if i not in alfabeto_entrada:
            print("Input no es una cadena binaria")
            return
    
    # Convertimos la cadena de entrada en una cinta con un número definido de blanks
    blank_number = 5
    w = list(sim_blanco * blank_number + input_user + sim_blanco * blank_number)

    # Le pasamos los datos de la máquina de turing a la función para ejecutarla
    maquina_turing(estados, alfabeto_entrada, alfabeto_cinta, func_transition, estado_inicial, sim_blanco, estados_aceptacion, w, blank_number)

main()