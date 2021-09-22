# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        # Inputs
        ["-5", "10", "3"],
        # Outputs
        ["Monto: ", "Interés anual: ", "Meses: ", "Error en los datos"],
        # Message in case of failure
        "Revisa los mensajes cuando algún dato es negativo o cero"
    ),
    # Test case 2
    (
        # Inputs
        ["1000", "0", "3"],
        # Outputs
        ["Monto: ", "Interés anual: ", "Meses: ", "Error en los datos"],
        # Message in case of failure
        "Revisa los mensajes cuando algún dato es negativo o cero"
    ),
    # Test case 3
    (
        # Inputs
        ["1550.34", "20.5", "10"],
        # Outputs
        ["Monto: ", "Interés anual: ", "Meses: ", "1836.51"],
        # Message in case of failure
        "Revisa tus cálculos."
    ),
]
