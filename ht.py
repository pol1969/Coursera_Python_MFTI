import requests

url = "https://datasend.webpython.graders.eldf.ru/submissions/1/"
headers= {'Authorization': 'Basic YWxsYWRpbjpvcGVuc2VzYW1l'}
r = requests.post(url, headers=headers)
print(r.text)
print (type(r.text))
#print(r.text.get('instructions'))
print(r.text.encode('utf-8').decode('unicode-escape'))
 

