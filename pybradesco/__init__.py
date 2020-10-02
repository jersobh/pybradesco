import json
import socket
import os
import OpenSSL
import requests


class BradescoBoleto(object):

    def __init__(self, environment, cert_path, cert_passwd, sdk_ver="1.5.0"):
        self.environment = environment
        if os.path.isfile(cert_path):
            self.cert = OpenSSL.crypto.load_pkcs12(open(cert_path).read(), passphrase=cert_passwd)
            self.cert_info = self.cert.get_certificate()
        else:
            raise Exception("Error: Certificate file path not found")
        self.cert_passwd = cert_passwd
        self.sdk_ver = sdk_ver
        self.host = socket.gethostname()
        self.headers = {
            'Content-Type': 'application/json',
            'User-Agent': f'Bradesco-API-PHP/{self.sdk_ver};{self.host}'
        }
        if environment == 'production':
            self.base_url = 'https://cobranca.bradesconetempresa.b.br/ibpjregistrotitulows/registrotitulo'
        elif environment == 'sandbox':
            self.base_url = 'https://cobranca.bradesconetempresa.b.br/ibpjregistrotitulows/registrotitulohomologacao'

        self.session = requests.Session()


    def get_request_api(self):
        try:
            self.session.get()
        except:
            raise Exception('Error')

    def post_request_api(self):
        try:
            self.session.post()
        except:
            raise Exception('Error')

    def response(self):
        try

