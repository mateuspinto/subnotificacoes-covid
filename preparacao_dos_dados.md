# Projeto Introdução à Ciência dos Dados - O Brasil em Dados

**Tema:** SRAG e COVID-19 no Brasil: uma análise conclusiva de subnotificações de COVID-19 baseada em parâmetros de diagnóstico dos acometidos por SRAG antes e durante o período de pandemia

## Integrantes do grupo

- Daniel Fernandes Pinho (EF02634 - Florestal)
- Mateus Pinto da Silva (EF03489 - Florestal)
- Milena Nobres (ER05164 - Rio Paranaíba)

## Dados utilizados

- https://opendatasus.saude.gov.br/dataset/bd-srag-2009-a-2012
- https://opendatasus.saude.gov.br/dataset/bd-srag-2012-a-2018
- https://opendatasus.saude.gov.br/dataset/bd-srag-2019
- https://opendatasus.saude.gov.br/dataset/bd-srag-2020
- https://opendatasus.saude.gov.br/dataset/bd-srag-2021
- https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9088-produto-interno-bruto-dos-municipios.html?edicao=29720&t=o-que-e

## Dados processados:

É possível baixar os dados processados compactados pelo link (https://drive.google.com/file/d/1LpwsCS-O2fy7L9TdKi3kIfOoVQDeFxvX/view?usp=sharing). Eles devem ser descompactados e colocados na pasta data/processed/ para correto funcionamento do projeto.

## Como executar:

Note, por favor, que é necessário ter instalado o interpretador do Python 3 com o seu Pip correspondente, além do pacote virtualenv. Ademais, para a correta execução do código, é necessário o arquivo de polígonos das cidades brasileiras. Ele pode ser baixado pelo link (https://drive.google.com/file/d/1HwHSkT_vdKmdKxoYMXK1f1Y0Dc_nGAg7/view?usp=sharing) e deve ser colocado na pasta data/raw/.

### No Linux:

Abra o terminal e digite:

    git clone https://github.com/mateuspinto/subnotificacoes-covid.git
    cd subnotificacoes-covid/
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python src/download_raw_data.py
    python src/process_data.py

### No Windows:

Abra o Powershell e digite:

    git clone https://github.com/mateuspinto/subnotificacoes-covid.git
    cd subnotificacoes-covid/
    virtualenv venv
    .\venv\Scripts\activate.ps1
    pip install -r requirements.txt
    python src/download_raw_data.py
    python src/process_data.py


## Mudanças realizadas

Foi adicionada mais uma base de dados: Produto Interno Bruto dos Municípios (IBGE) juntamente com os polígonos das cidades brasileiras cedidas pelo professor da disciplina. Ela será utilizada para responder algumas perguntas que correlacionam características de qualidade de vida por município e a evolução do caso.

## Objetivo da etapa

Nessa etapa, trataremos todos os dados, escolhendo as colunas a serem utilizadas e gerando dois novos arquivos com casos de SRAG: um com os casos pré-pandemia e o outro com os casos durante a pandemia. Além disso, os dados de PIB por município também serão filtrados e um arquivo deles será gerado.

## Decisões de implementação

Como nossos dados apresentavam tamanhos razoáveis (aproximdamente 10 gigabytes quando carregados em memória principal), optamos por utilizar o Numba, compilador JIT para Python que cria funções inseguras porém rápidas com uso de paralelismo a nível de dados. Não achamos necessário utilizar nada para otimizar o consumo de memória, visto que todos os dados já cabiam em memória principal do computador utilizado para o tratamento (que tem 16 gigabytes de memória principal).

## Dados utilizados nos Dataframes de SRAG

Optamos por definir todas as colunas usadas nos Dataframes de SRAG pré-pandemia e durante a pandemia. Definimos aqui os tipos, e optamos por utilizar sempre float e date por conterem os valor NaN (Not a Number) e valor NaT (Not a Date), o que facilita muito a lidar com os dados faltantes.

| Nome da coluna        | Tipo  | Valores possíveis | Valor padrão | Descrição                                              |
| --------------------- | ----- | ----------------- | ------------ | ------------------------------------------------------ |
| cad_sexo              | float | 0 >= x >= 1       | NaN          | Paciente é do sexo feminino.                           |
| cad_cod_cidade        | float | len(str(x)) == 7  | NaN          | Código da cidade do IBGE.                              |
| cad_dt_nascimento     | date  | YYYY-MM-DD        | NaT          | Data de nascimento do paciente.                        |
| cad_dt_notificacao    | date  | YYYY-MM-DD        | NaT          | Data de notificação do caso.                           |
| fr_gestante           | float | 0 >= x >= 1       | NaN          | Paciente é gestante.                                   |
| fr_puerpera           | float | 0 >= x >= 1       | NaN          | Paciente é puerpera.                                   |
| fr_cardiopatia        | float | 0 >= x >= 1       | NaN          | Paciente tem cardiopatia.                              |
| fr_hematologia        | float | 0 >= x >= 1       | NaN          | Paciente tem hematologia.                              |
| fr_snd_down           | float | 0 >= x >= 1       | NaN          | Paciente tem síndrome de Down.                         |
| fr_hepatia            | float | 0 >= x >= 1       | NaN          | Paciente é hepático.                                   |
| fr_asma               | float | 0 >= x >= 1       | NaN          | Paciente tem asma.                                     |
| fr_diabetes           | float | 0 >= x >= 1       | NaN          | Paciente tem diabetes                                  |
| fr_neuropatia         | float | 0 >= x >= 1       | NaN          | Paciente tem neuropatia.                               |
| fr_pneumopatia        | float | 0 >= x >= 1       | NaN          | Paciente tem pneumopatia.                              |
| fr_imunodepressao     | float | 0 >= x >= 1       | NaN          | Paciente tem imunodepressão.                           |
| fr_doenca_renal       | float | 0 >= x >= 1       | NaN          | Paciente tem doença renal crônica.                     |
| fr_obesidade          | float | 0 >= x >= 1       | NaN          | Paciente tem obesidade.                                |
| sint_tosse            | float | 0 >= x >= 1       | NaN          | Paciente teve tosse.                                   |
| sint_febre            | float | 0 >= x >= 1       | NaN          | Paciente teve febre.                                   |
| sint_dor_abdominal    | float | 0 >= x >= 1       | NaN          | Paciente teve dor abdominal.                           |
| sint_dor_garganta     | float | 0 >= x >= 1       | NaN          | Paciente teve dor de garganta.                         |
| sint_dispneia         | float | 0 >= x >= 1       | NaN          | Paciente teve dispneia.                                |
| sint_dfc_respiratorio | float | 0 >= x >= 1       | NaN          | Paciente teve dificuldade respiratória.                |
| sint_saturacao        | float | 0 >= x >= 1       | NaN          | Paciente teve saturação menor ou igual a 95%.          |
| sint_diarreia         | float | 0 >= x >= 1       | NaN          | Paciente teve diarreia.                                |
| sint_vomito           | float | 0 >= x >= 1       | NaN          | Paciente teve vômito.                                  |
| sint_fadiga           | float | 0 >= x >= 1       | NaN          | Paciente teve fadiga.                                  |
| sint_prd_olfato       | float | 0 >= x >= 1       | NaN          | Paciente teve perda de olfato.                         |
| sint_prd_paladar      | float | 0 >= x >= 1       | NaN          | Paciente teve perda de paladar.                        |
| vac_covid             | float | 0 >= x >= 1       | NaN          | Paciente foi vacinado contra COVID-19.                 |
| vac_gripe             | float | 0 >= x >= 1       | NaN          | Paciente foi vacinado contra gripe na última campanha. |
| evo_internacao        | float | 0 >= x >= 1       | NaN          | Paciente foi internado em leito comum.                 |
| evo_obito             | float | 0 >= x >= 1       | NaN          | Probabilidade do paciente ter ido a óbito.             |
| evo_uti               | float | 0 >= x >= 1       | NaN          | Paciente foi internado em leito UTI.                   |
| evo_ventilacao        | float | 0 >= x >= 1       | NaN          | Paciente recebeu ventilação.                           |
| dg_covid              | float | 0 >= x >= 1       | NaN          | Paciente foi diagnosticado com COVID-19.               |

## Dados utilizados no Dataframe do PIB IBGE

Utilizamos os Dados de PIB de IBGE e dos polígonos das cidades (cedidos pelo professor da disciplina). Utilizamos o mesmo nome de colunas que o próprio IBGE, então não julgamos necessário colocar o dicionário de dados aqui novamente. É possível encontrá-lo na pasta data/raw/dict (além dos dicionários de dados das outras tabelas brutas).

## Documentação da biblioteca de código comum

Para fins de aumento da manutenibilidade, modularidade e reuso, criamos uma simples biblioteca de código comum que abstrai algumas das funções utilizadas por nós neste trabalho. Foi pensada inicialmente como uma forma de encapsular os métodos do Numba. Imaginamos que ela cresça à medida do avanço do trabalho e das eventuais entregas.

\*\* **Note que todos os métodos iniciados por \_\_ são privados e inseguros, portanto não foram citados aqui.**

### common/path.py

Cria constantes globais úteis para caminho de dados de outros códigos utilizando a biblioteca pathlib que é independente de sistema operacional.

**WORK_DIR =** Caminho absoluto para a pasta raiz do projeto.\
**RAW_DATA_DIR =** Caminho absoluto para a pasta de dados brutos.\
**PROCESSED_DATA_DIR =** Caminho absoluto para a pasta de dados processados.

### common/data_processing.py

Funções úteis para o processamento/preparação de dados. Utiliza chamadas seguras a métodos inseguros do Numba, estes focados em paralelismo e eficiência.

**n_way_column_map (target_column, source_column, original_values, new_values):**\
**@target_column: Coluna do Pandas =** Coluna alvo onde serão salvos os novos valores;\
**@source_column: Coluna do Pandas =** Coluna de origem que será referência para os casamentos;\
**@original_values: [Lista] =** Lista de valores a serem testados;\
**@new_values: [Lista] =** Respectivos valores da lista anterior a serem colocados na coluna alvo caso o casamento aconteça;\
**@retorno =** Nada.\
Preenche condicionalmente a coluna alvo baseando-se nos valores da coluna de origem. Necessita de duas listas de valores, sendo a primeira a de valores originais a serem testados e a segunda de novos valores que serão colocados na coluna alvo. Note que as duas listas precisam ter o mesmo tamanho. Caso nenhum valor original case com a coluna de origem, o valor da coluna alvo é mantido. Não suporta colunas com strings.

**unoptimzed_n_way_column_map(target_column, source_column, original_values, new_values):**\
**@target_column: Coluna do Pandas =** Coluna alvo onde serão salvos os novos valores;\
**@source_column: Coluna do Pandas =** Coluna de origem que será referência para os casamentos;\
**@original_values: [Lista] =** Lista de valores a serem testados;\
**@new_values: [Lista] =** Respectivos valores da lista anterior a serem colocados na coluna alvo caso o casamento aconteça;\
**@retorno =** Nada.\
Preenche condicionalmente a coluna alvo baseando-se nos valores da coluna de origem. Necessita de duas listas de valores, sendo a primeira a de valores originais a serem testados e a segunda de novos valores que serão colocados na coluna alvo. Note que as duas listas precisam ter o mesmo tamanho. Caso nenhum valor original case com a coluna de origem, o valor da coluna alvo é mantido. Suporta colunas com strings, porém sacrifica eficiência para tal.

**n_way_column_filter(target_column, source_column, filter_func, default_value):**\
**@target_column: Coluna do Pandas =** Coluna alvo onde serão colados os novos valores;\
**@source_column: Coluna do Pandas =** Coluna de origem a qual os valores serão copiados;\
**@filter_func: f(x) =** Função de um argumento que retorna verdadeiro caso o valor deva ser filtrado e falso caso contrário.\
**@default_value: valor =** Valor a ser colocado na coluna alvo caso o filtro retorne verdadeiro;\
**@retorno =** Nada.\
Copia os valores de uma coluna para outra, aplicando um filtro durante a cópia. Necessita de uma função que é o filtro em si a ser aplicado elemento por elemento, e um valor a ser colocado caso o filtro seja necessário. Não suporta colunas com strings.

**fill_column(target_column, default_value):**\
**@target_column: Coluna do Pandas =** Coluna alvo onde serão salvos os novos valores;\
**@default_value: valor =** Valor a ser colocado em toda a coluna;\
**@retorno =** Nada.\
Preenche toda a coluna alvo com um único valor.

**filter_dates(source_column):**\
**@source_column: Coluna do Pandas =** Coluna origem de datas em string;\
**@retorno: Coluna do Pandas =** Coluna de datas em datetime.\
Filtra datas inválidas e transforma datas de string (no padrão brasileiro com dia na frente) para datetime.

**new_blank_dataframe(length):**\
**@length: Inteiro =** Quantidade de linhas do dataframe do Pandas a ser criado.\
**@retorno: Dataframe do Pandas =** Dataframe padronizado do trabalho em branco.\
Cria um Dataframe do Pandas em branco, ou seja, preenchido com os valores padrão em todas as linhas e colunas.

## Video apresentacao
https://drive.google.com/file/d/1iW2-0zyjtb1Va4jXAyVILVjDwAkr_MrA/view?usp=sharing
