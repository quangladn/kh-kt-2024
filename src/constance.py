TYPE_UNKNOWN = 0
TYPE_STRING = 1


class Constance:
    def __init__(self, value) -> None:
        self.value = value
        self.type = TYPE_UNKNOWN
        self.update_type()

    def update_type(self):
        if type(self.value) == str:
            self.type = TYPE_STRING

    def get_value(self):
        return self.value
