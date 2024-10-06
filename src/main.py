import convert
import lexer
import execute
import sys

SUCCESSFUL_STATUS = 0
ERROR_STATUS = 1


def main():
    try:
        file_name = sys.argv[1]
    except IndexError:
        print("Unknown file error")
        return ERROR_STATUS

    try:
        split_content = convert.do_all_convert(file_name)
    except FileNotFoundError:
        print("File not found error")
        return ERROR_STATUS

    tokens = lexer.lexer(split_content)
    execute.execute(tokens)

    return SUCCESSFUL_STATUS


if __name__ == "__main__":
    main()
