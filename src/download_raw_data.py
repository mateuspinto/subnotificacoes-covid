#!/usr/bin/python3

# Date: 08/08/2021
# Download required data using wget

from common.path import *
import wget

files = [
    'https://opendatasus.saude.gov.br/dataset/c9a8f286-44bc-444e-94b4-f4ceded3af2c/resource/06a7abd3-412f-47e7-a289-b38f67e9425b/download/influd09_limpo-final.csv',
    'https://opendatasus.saude.gov.br/dataset/c9a8f286-44bc-444e-94b4-f4ceded3af2c/resource/0e9fd20f-dfc1-44e0-8f6e-5bc324c567e6/download/influd10_limpo-final.csv',
    'https://opendatasus.saude.gov.br/dataset/c9a8f286-44bc-444e-94b4-f4ceded3af2c/resource/c368801b-11fe-469a-93f7-cfa61e462126/download/influd11_limpo_final.csv',
    'https://opendatasus.saude.gov.br/dataset/c9a8f286-44bc-444e-94b4-f4ceded3af2c/resource/86a35b29-3778-406b-80ae-e81697f60df0/download/influd12_limpo_final.csv',
    'https://opendatasus.saude.gov.br/dataset/e6b03178-551c-495c-9935-adaab4b2f966/resource/4919f202-083a-4fac-858d-99fdf1f1d765/download/influd13_limpo_final.csv',
    'https://opendatasus.saude.gov.br/dataset/e6b03178-551c-495c-9935-adaab4b2f966/resource/2182aff1-4e8b-4aee-84fc-8c9f66378a2b/download/influd14_limpo-final.csv',
    'https://opendatasus.saude.gov.br/dataset/e6b03178-551c-495c-9935-adaab4b2f966/resource/97cabeb6-f09e-47a5-8358-4036fb10b535/download/influd15_limpo-final.csv',
    'https://opendatasus.saude.gov.br/dataset/e6b03178-551c-495c-9935-adaab4b2f966/resource/dbb0fd9b-1345-47a5-86db-d3d2f4868a11/download/influd16_limpo-final.csv',
    'https://opendatasus.saude.gov.br/dataset/e6b03178-551c-495c-9935-adaab4b2f966/resource/aab28b3c-f6b8-467f-af0b-44889a062ac6/download/influd17_limpo-final.csv',
    'https://opendatasus.saude.gov.br/dataset/e6b03178-551c-495c-9935-adaab4b2f966/resource/a7b19adf-c6e6-4349-a309-7a1ec0f016a4/download/influd18_limpo-final.csv',
    'https://opendatasus.saude.gov.br/dataset/e99cfd21-3d8c-4ff9-bd9c-04b8b2518739/resource/9d1165b3-80a3-4ec4-a6ad-e980e3d354b2/download/influd19_limpo-27.04.2020-final.csv',
    'https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2020/INFLUD-02-08-2021.csv',
    'https://s3-sa-east-1.amazonaws.com/ckan.saude.gov.br/SRAG/2021/INFLUD21-02-08-2021.csv',
    'https://ftp.ibge.gov.br/Pib_Municipios/2018/base/base_de_dados_2002_2009_xls.zip',
    'https://ftp.ibge.gov.br/Pib_Municipios/2018/base/base_de_dados_2010_2018_xls.zip',
]

for count, file in enumerate(files):
    print(f'\n[{count+1}/{len(files)}] Baixando arquivos...')
    wget.download(file, out=str(RAW_DATA_DIR), bar=wget.bar_thermometer)
