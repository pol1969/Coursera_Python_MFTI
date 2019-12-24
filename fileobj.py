import os.path
import uuid
import tempfile

class File:
    """ Класс для работы с файлом """
    
    def __init__(self, path):
        self.path = path
        self.cur_pos = 0
 
        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def write(self, content):
        with open(self.path, 'w') as f:
            return f.write(content)
 
    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __iter__(self):
        return self

    def __add__(self, obj):
        np = os.path.join(
       #     os.path.dirname(self.path),
            tempfile.gettempdir(),
            str(uuid.uuid4().hex)
        )
        f = File(np)
        f.write(self.read() + obj.read())
        return f

    def __str__(self):
        return self.path

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.cur_pos)

            line = f.readline()
            if not line:
                self.cur_pos = 0
                raise StopIteration('EOF')

            self.cur_pos = f.tell()
            return line
                


