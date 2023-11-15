"""
Entrada: (En archivo .txt, .json, .ml, etc)
    ∗ conjunto de estados Q,
    ∗ alfabeto input Σ,
    ∗ alfabeto de cinta Γ,
    ∗ estado inicial q0,
    ∗ conjunto de estados de aceptaci ́on F ,
    ∗ tabla de transiciones (o en su defecto, el listado de 4-tuplas).
• cadena input w (o cadenas) necesarias para iniciar la simulaci ́on.

Salida:
• derivacion, paso a paso, de la lectura de w. Para ello puede elegir entre presentarla como derivacion o como secuencia deconfiguraciones instantaneas (visual o desplegado en pantalla). X
• estado final X
• cadena final escrita sobre la cinta X
• flag que indique si w es aceptada o no. X
"""

def read_file():
    # Open the file in read mode ('r')
    estados = []
    alfabeto_entrada = []
    alfabeto_cinta = []
    func_transition = {}
    estado_inicial = ""
    sim_blanco = ""
    estados_aceptacion = []

    with open('machine.txt', 'r') as file:
        contador = 0
        for line in file:
            # Split the line at the '=' character
            if "=" not in line:
                line = line.strip().replace('(', '').replace(')', '').replace(' ', '')
                value = [tuple(filter(None, v.split(','))) for v in line.split('->')]
                try:
                    func_transition[value[0]] = value[1]
                except IndexError:
                    print()
                continue
            key, value = line.split('=')
            key = key.strip()
            value = value.strip()

            # Remove the curly braces and split the values at the ',' character
            if '{' in value and '}' in value:
                value = value.replace('{', '').replace('}', '').replace(' ', '')
                value = value.split(',')

            # Store the key-value pair in the dictionary
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

    # Now 'variables' is a dictionary that contains all the variables and their values

    return estados, alfabeto_entrada, alfabeto_cinta, func_transition, estado_inicial, sim_blanco, estados_aceptacion


def maquina_turing(estados, alfabeto_entrada, alfabeto_cinta, func_transition, estado_inicial, sim_blanco, estados_aceptacion, w, starter):
    input_actual = starter
    flag = False
    print()
    print("Transiciones:")

    while estado_inicial != "R":
        if estado_inicial in estados_aceptacion:
            flag = True
            break
        else:
            transition = func_transition[(estado_inicial, w[input_actual])]
            print("(" + estado_inicial + ", " + w[input_actual] + ")","->", transition)
            estado_inicial = transition[0]
            w[input_actual] = transition[1]
            if transition[2] == "R":
                input_actual += 1
            else:
                input_actual -= 1
    
    print()
    print("Estado final:", estado_inicial)
    print("Resultado de cinta:", w)
    if flag:
        print("La cadena w es un palíndromo")
    else:
        print("La cadena w no es un palíndromo")


def main():
    estados, alfabeto_entrada, alfabeto_cinta, func_transition, estado_inicial, sim_blanco, estados_aceptacion = read_file()

    input_user = input("Enter a number: ")

    for i in input_user:
        if i not in alfabeto_entrada:
            print("Input no es una cadena binaria")
            return
        
    blank_number = 5
    w = list(sim_blanco * blank_number + input_user + sim_blanco * blank_number)

    maquina_turing(estados, alfabeto_entrada, alfabeto_cinta, func_transition, estado_inicial, sim_blanco, estados_aceptacion, w, blank_number)

main()