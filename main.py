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

def maquina_turing(estados, func_transition, w):
    estado_actual = "q0"
    input_actual = 1
    flag = False
    print()
    print("Transiciones:")

    while estado_actual != "R":
        if estado_actual == "q6":
            flag = True
            break
        else:
            transition = func_transition[(estado_actual, w[input_actual])]
            print(estado_actual, w[input_actual],"->", transition)
            estado_actual = transition[0]
            w[input_actual] = transition[1]
            if transition[2] == "R":
                input_actual += 1
            else:
                input_actual -= 1
    
    print()
    print("Estado final:", estado_actual)
    print("Cadena final:", w)
    if flag:
        print("La cadena w fue aceptada")
    else:
        print("La cadena w no fue aceptada")

def main():
    w = list("B" + input("Enter a number: ") + "B")

    estados = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "R"]

    func_transition = {
        ("q0", "1"): ("q1", "B", "R"),
        ("q0", "0"): ("q4", "B", "R"),
        ("q0", "B"): ("q6", "B", "R"),
        ("q1", "1"): ("q1", "1", "R"),
        ("q1", "0"): ("q1", "0", "R"),
        ("q1", "B"): ("q2", "B", "L"),
        ("q2", "B"): ("q6", "B", "R"),
        ("q2", "0"): ("R", "0", "R"),
        ("q2", "1"): ("q3", "B", "L"),
        ("q3", "1"): ("q3", "1", "L"),
        ("q3", "0"): ("q3", "0", "L"),
        ("q3", "B"): ("q0", "B", "R"),
        ("q4", "1"): ("q4", "1", "R"),
        ("q4", "0"): ("q4", "0", "R"),
        ("q4", "B"): ("q5", "B", "L"),
        ("q5", "B"): ("q6", "B", "R"),
        ("q5", "1"): ("R", "1", "R"),
        ("q5", "0"): ("q3", "B", "L")
    }

    maquina_turing(estados, func_transition, w)

main()