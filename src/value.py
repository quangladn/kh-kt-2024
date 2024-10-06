from const import *


class Value:
    def __init__(self, value) -> None:
        self.value = value
        self.type = TYPE_UNKNOWN
        self.update_type()

    def update_type(self):
        try:
            eval(self.value)
            self.type = TYPE_NUMBER
        except SyntaxError:
            if type(self.value) == str:
                self.type = TYPE_STRING

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value
