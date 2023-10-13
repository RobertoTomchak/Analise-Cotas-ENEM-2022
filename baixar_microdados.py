# esse código baixa os dados do enem 2022
# caso já tenha a pasta microdados_enem_2022/ em seu diretório,
# não é necessário executar

import requests, zipfile, io
import os

dir = "microdados_enem_2022/"
if not os.path.exists(dir):
    os.makedirs(dir)
    zip_file_url = "https://download.inep.gov.br/microdados/microdados_enem_2022.zip"
    r = requests.get(zip_file_url, verify=False)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(dir)
