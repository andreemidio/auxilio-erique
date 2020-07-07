import json
import base64
from io import StringIO
import io
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

URL =  '  CORRIGIR ISSO'


#referência
#https://stackoverflow.com/questions/22567306/python-requests-file-upload
headers={'Content-Type': 'multipart/form-data'}


files = {'file': ('foto.jpg', open('foto.jpg', 'rb')}

values = {
    'body':{
            'speed':'Aooba'
}


try:
    res =  requests.post(url, files=files, data=values, headers = headers)
    print(res.status_code)

except Exception as e:
    print("Erro ao enviar dados")