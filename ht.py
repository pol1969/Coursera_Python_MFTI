import requests
import base64

url = "https://datasend.webpython.graders.eldf.ru/submissions/1/"
headers= {'Authorization': 'Basic YWxsYWRpbjpvcGVuc2VzYW1l'}
r = requests.post(url, headers=headers)
print(r.text.encode('utf-8').decode('unicode-escape'))
d = eval( r.text.encode('utf-8').decode('unicode-escape'))
url1 = url[0:-14] + d['path']
l = d['login']
p = d['password']

data = {'login':l, 'password':p}
auth_str = '%s:%s' % (l, p)
b64_auth_str = base64.b64encode(auth_str.encode())

headers = {'Authorization': 'Basic %s' % b64_auth_str.decode()}

content_res = requests.put(url1, headers=headers, data=data)
f = eval(content_res.text)
print(f['answer'])

filehandle = open('answer.txt', 'w')  
filehandle.write(f['answer'])  
filehandle.close()  
