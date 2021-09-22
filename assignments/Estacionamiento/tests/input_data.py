# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test Case 1
    (
        ["-1"],
        ["Horas: ", 'Error en los datos'],
        ["Revisa las condiciones y mensajes cuando son datos inválidos"]
    ),
    # Test Case 2
    (
        ["0", "80"],
        ["Horas: ", "Minutos: ", 'Error en los datos'],
        ["Revisa las condiciones y mensajes cuando son datos inválidos"]
    ),
    # Test Case 3
    (
        ["0", "14"],
        ["Horas: ", "Minutos: ", 'Total a pagar: 10'],
        ["Revisa las condiciones cuando es la primer hora o fracción"]
    ),
    # Test Case 4
    (
        ["1", "24"],
        ["Horas: ", "Minutos: ", 'Total a pagar: 14'],
        ["Revisa las condiciones cuando es más de una hora"]
    ),

    # Test Case 5
    (
        ["2", "30"],
        ["Horas: ", "Minutos: ", 'Total a pagar: 22'],
        ["Revisa las condiciones cuando es más de una hora"]
    )
]
