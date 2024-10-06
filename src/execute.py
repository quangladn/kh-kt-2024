def execute(tokens: list):
    index = 0

    while index < len(tokens):
        if tokens[index] == "PRINT" and type(tokens[index + 1]):
            print(tokens[index + 1].get_value())
            index += 2
