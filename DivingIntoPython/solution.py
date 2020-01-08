class FileReader:
    def __init__(self, path):
        try:
            with open(path, 'r') as f:
               self.data = f.read()
  #              print(data)
        except FileNotFoundError:
            self.data = ''
   #         print('')
    def read(self):
        return self.data







