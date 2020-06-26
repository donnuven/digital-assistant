from contextlib import contextmanager


class AssistantWriter(object):
    '''
    A class that writes information to a chat log file.

    '''

    def __init__(self, file_name):
        self.file_name = file_name

    @contextmanager
    def open_file(self):
        try:
            file = open(self.file_name, 'w')
            yield file
        finally:
            file.close()
