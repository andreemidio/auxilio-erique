import json
import base64
from io import StringIO
import io
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

URL =  '  CORRIGIR ISSO'

headers={'Content-Type': 'multipart/form-data'}

files = {'file': ('foto.jpg', open('foto.jpg', 'rb'),
                  'body':{
            'speed':'Aooba'
         }


try:
    res =  requests.post(url, files=file, headers = headers)

except Exception as e:
    print("Erro ao enviar dados")