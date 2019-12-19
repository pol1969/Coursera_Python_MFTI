import json
from functools import wraps

def to_json(func):
    @wraps(func)
    def inner(*args, **kwargs ):
        result = func(*args, **kwargs) 
        res_json = json.dumps(result)
        return res_json
    return inner

@to_json
def get_data():
    return {
            'data':42
            }

if __name__=='__main__':
   s = get_data()
   print(get_data.__name__)
   print(s)


