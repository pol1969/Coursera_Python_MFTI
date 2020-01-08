import os
import tempfile
import argparse
import json
from collections import defaultdict


def createParser():
    parser = argparse.ArgumentParser(prog='ap',
                                     description='Это очень нужная программа ap, она записывает пару ключ:значение в хранилище или выводит значение по ключу',
                                     epilog='Павел Подберезский, 2019,не несет никакой ответственности за использование этой программы')
    parser.add_argument('--key', help='Ключ для записи и получения значения')
    parser.add_argument('--value', help='Значение для ключа')

    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    if os.path.isfile(storage_path) and os.path.getsize(storage_path) > 0:
        with open(storage_path, 'r') as f:
            data = json.load(f)
    else:
        with open(storage_path, 'w') as f:
            data =defaultdict(list)

    if namespace.key is not None and namespace.value is None:
        if namespace.key in data.keys():
            print(*data[namespace.key], sep=', ')  
          #  print(s)
          #  print(data[namespace.key])
        else:
            print('')

    if namespace.key is not None and namespace.value is not None:
        with open(storage_path, 'w') as f:

            if namespace.key in data.keys():
                data[namespace.key].append(namespace.value)
            else:
                data[namespace.key] = []
                data[namespace.key].append(namespace.value)
           
            json.dump(data, f)

            print('')
    if namespace.key is None and namespace.value is  None:
        print('Введите ключ для поиска или ключа и значения для записи')


