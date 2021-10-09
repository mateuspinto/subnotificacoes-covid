# Projeto Introdução à Ciência dos Dados - O Brasil em Dados

**Tema:** Análise conclusiva de subnotificações de SRAG provocada por Covid-19 no Brasil

## Integrantes do grupo:

- Daniel Fernandes Pinho (EF02634 - Florestal)
- Mateus Pinto da Silva (EF03489 - Florestal)
- Milena Nobres (ER05164 - Rio Paranaíba)

## Dados utilizados:

- https://opendatasus.saude.gov.br/dataset/bd-srag-2009-a-2012
- https://opendatasus.saude.gov.br/dataset/bd-srag-2012-a-2018
- https://opendatasus.saude.gov.br/dataset/bd-srag-2019
- https://opendatasus.saude.gov.br/dataset/bd-srag-2020
- https://opendatasus.saude.gov.br/dataset/bd-srag-2021

## Dados processados:

É possível baixar os dados processados compactados pelo link (https://drive.google.com/file/d/1knTUgLZHLQcBF9CmCdHWk-WP94AXh2_J/view?usp=sharing). Eles devem ser descompactados e colocados na pasta data/processed/ para correto funcionamento do projeto.

## Como executar:

Note, por favor, que é necessário ter instalado o interpretador do Python 3 com o seu Pip correspondente, além do pacote virtualenv.

### No Linux:

Abra o terminal e digite:

    git clone https://github.com/mateuspinto/subnotificacoes-covid.git
    cd subnotificacoes-covid/
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python src/download_raw_data.py
    python src/process_data.py

Em seguida, execute o Notebook de sua escolha :#

### No Windows:

Abra o Powershell e digite:

    git clone https://github.com/mateuspinto/subnotificacoes-covid.git
    cd subnotificacoes-covid/
    virtualenv venv
    .\venv\Scripts\activate.ps1
    pip install -r requirements.txt
    python src/download_raw_data.py
    python src/process_data.py

Em seguida, execute o Notebook de sua escolha :#
