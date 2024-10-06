import convert
from value import Value
from const import *


def lexer(split_content: list[str]):
    code_sync = ""
    string = ""
    math_value = ""
    mode = NOTHING
    tokens = []

    for letter in split_content:
        code_sync += letter
        if code_sync == " " and (mode == NOTHING or mode == GETTING_MATH_VALUE):
            code_sync = ""
        elif code_sync == "\n" and mode == NOTHING:
            code_sync = ""
        elif code_sync == "\n" and mode == GETTING_MATH_VALUE:
            tokens.append(Value(math_value))

            code_sync = ""
        elif code_sync == "nói":
            tokens.append("PRINT")
            code_sync = ""
        elif code_sync == '"':
            if mode == NOTHING:
                mode = GETTING_STRING
            elif mode == GETTING_STRING:
                mode = NOTHING
                tokens.append(Value(string))
                string = ""
            code_sync = ""
        elif code_sync in MATH_VALUE and mode == NOTHING:
            mode = GETTING_MATH_VALUE
            math_value += code_sync
            code_sync = ""
        elif mode == GETTING_STRING:
            string += code_sync
            code_sync = ""

    return tokens


if __name__ == "__main__":
    test_content = convert.read_file("test/test.txt")
    split_content = convert.split_content(test_content)

    tokens = lexer(split_content)
    print(tokens)
