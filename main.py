import json
import base64
from io import StringIO
import io
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

URL =  '  CORRIGIR ISSO'


multipart_data = MultipartEncoder(
    fields={
            'file': ('foto.jpg', open('foto.jpg', 'rb'), 'image/jpeg'),
            'body':{
            'speed':'Aooba'
            }
           }
    )


try:
    res =  requests.post(URL, data=multipart_data,
                  headers={'Content-Type': multipart_data.content_type})

except Exception as e:
    print("Erro ao enviar dados")