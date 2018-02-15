#file does not meet custom format requirements
class FileFormatError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
