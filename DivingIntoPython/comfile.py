import os
import tempfile
from  fileobj import File

storage_path = os.path.join(tempfile.gettempdir(),'storage.data')
first = os.path.join(tempfile.gettempdir(), 'first')
second = os.path.join(tempfile.gettempdir(),'second')


obj = File(storage_path)
print('Инициация ',obj)

obj.write('line\n')
print('Запись строки ', obj)

obj1 = File(first)
obj1.write('line obj1')

obj2 = File(second)
obj2.write('line obj2')



new_obj = obj1 + obj2 
#print('Операция сложения ', new_obj)
print('new_obj ', new_obj)

for line in File(storage_path):
    print(line)

print(obj)




