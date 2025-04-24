class MethodError(Exception):
    def __init__(self, message):
        self.message = message


class DirectoryNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
