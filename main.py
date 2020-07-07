import requests


URL =  '  CORRIGIR ISSO'


#referência
#https://stackoverflow.com/questions/22567306/python-requests-file-upload
headers={'Content-Type': 'multipart/form-data'}


files = {'file': open('foto.jpg', 'rb')}

values = {
    'body':{
            'speed':'Aooba'
}

try :
    res =  requests.post(url, files=files, data=values, headers = headers)
    print(res.status_code)
except Exception as e:
    print(f"Erro ao enviar dados -->> {e}")