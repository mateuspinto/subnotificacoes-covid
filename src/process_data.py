#!/usr/bin/python3

# Date: 08/08/2021
# Turn raw data files to processed

from common.path import *
from common.data_processing import *


def process_y09_12(input_filename):
    raw = pd.read_csv(RAW_DATA_DIR / (input_filename + '.csv'), delimiter=';', encoding='iso-8859-1', usecols=['CS_SEXO', 'ID_MUNICIP', 'DT_NASC', 'DT_NOTIFIC', 'PUERPERA', 'CARDIOPATI', 'SIND_DOWN', 'HEPATICA', 'METABOLICA', 'NEUROLOGIC', 'PNEUMOPATI', 'IMUNODEPRE', 'RENAL', 'OBESIDADE', 'FEBRE', 'TOSSE', 'GARGANTA', 'DISPNEIA', 'DESC_RESP', 'SATURACAO', 'DIARREIA', 'VACINA', 'HOSPITAL', 'UTI', 'EVOLUCAO', 'CS_GESTANT', 'SUPORT_VEN'])

    processed = new_blank_dataframe(len(raw))

    processed.cad_dt_nascimento = filter_dates(raw.DT_NASC)
    processed.cad_dt_notificacao = filter_dates(raw.DT_NOTIFIC)

    unoptimzed_n_way_column_map(processed.cad_sexo_feminino, raw.CS_SEXO, ['F', 'M'], [1, 0])
    n_way_column_filter(processed.cad_cod_cidade, raw.ID_MUNICIP, lambda x: x < 100000 or x > 999999, np.nan)

    n_way_column_map(processed.fr_cardiopatia, raw.CARDIOPATI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_diabetes, raw.METABOLICA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_doenca_renal, raw.RENAL, [1, 2], [1, 0])
    n_way_column_map(processed.fr_gestante, raw.CS_GESTANT, [1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 0, 0])
    n_way_column_map(processed.fr_hepatia, raw.HEPATICA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_imunodepressao, raw.IMUNODEPRE, [1, 2], [1, 0])
    n_way_column_map(processed.fr_neuropatia, raw.NEUROLOGIC, [1, 2], [1, 0])
    n_way_column_map(processed.fr_obesidade, raw.OBESIDADE, [1, 2], [1, 0])
    n_way_column_map(processed.fr_pneumopatia, raw.PNEUMOPATI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_puerpera, raw.PUERPERA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_snd_down, raw.SIND_DOWN, [1, 2], [1, 0])

    n_way_column_map(processed.sint_dfc_respiratorio, raw.DESC_RESP, [1, 2], [1, 0])
    n_way_column_map(processed.sint_diarreia, raw.DIARREIA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_dispneia, raw.DISPNEIA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_dor_garganta, raw.GARGANTA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_febre, raw.FEBRE, [1, 2], [1, 0])
    n_way_column_map(processed.sint_saturacao, raw.SATURACAO, [1, 2], [1, 0])
    n_way_column_map(processed.sint_tosse, raw.TOSSE, [1, 2], [1, 0])

    fill_column(processed.vac_covid, 0)
    n_way_column_map(processed.vac_gripe, raw.VACINA, [1, 2], [1, 0])

    n_way_column_map(processed.evo_internacao, raw.HOSPITAL, [1, 2], [1, 0])
    n_way_column_map(processed.evo_obito, raw.EVOLUCAO, [1, 2, 3], [0, 1, 1])
    n_way_column_map(processed.evo_uti, raw.UTI, [1, 2], [1, 0])
    n_way_column_map(processed.evo_ventilacao, raw.SUPORT_VEN, [1, 2], [1, 0])

    fill_column(processed.dg_covid, 0)
    return processed


def process_y13_18(input_filename):
    raw = pd.read_csv(RAW_DATA_DIR / (input_filename + '.csv'), delimiter=';', encoding='iso-8859-1', usecols=['CS_SEXO', 'ID_MUNICIP', 'DT_NASC', 'DT_NOTIFIC', 'PUERPERA', 'CARDIOPATI', 'SIND_DOWN', 'HEPATICA', 'METABOLICA', 'NEUROLOGIC', 'PNEUMOPATI', 'IMUNODEPRE', 'RENAL', 'OBESIDADE', 'FEBRE', 'TOSSE', 'GARGANTA', 'DISPNEIA', 'DESC_RESP', 'SATURACAO', 'DIARREIA', 'VACINA', 'HOSPITAL', 'UTI', 'EVOLUCAO', 'CS_GESTANT', 'SUPORT_VEN'])

    processed = new_blank_dataframe(len(raw))

    processed.cad_dt_nascimento = filter_dates(raw.DT_NASC)
    processed.cad_dt_notificacao = filter_dates(raw.DT_NOTIFIC)

    unoptimzed_n_way_column_map(processed.cad_sexo_feminino, raw.CS_SEXO, ['F', 'M'], [1, 0])
    n_way_column_filter(processed.cad_cod_cidade, raw.ID_MUNICIP, lambda x: x < 100000 or x > 999999, np.nan)

    n_way_column_map(processed.fr_cardiopatia, raw.CARDIOPATI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_diabetes, raw.METABOLICA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_doenca_renal, raw.RENAL, [1, 2], [1, 0])
    n_way_column_map(processed.fr_gestante, raw.CS_GESTANT, [1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 0, 0])
    n_way_column_map(processed.fr_hepatia, raw.HEPATICA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_imunodepressao, raw.IMUNODEPRE, [1, 2], [1, 0])
    n_way_column_map(processed.fr_neuropatia, raw.NEUROLOGIC, [1, 2], [1, 0])
    n_way_column_map(processed.fr_obesidade, raw.OBESIDADE, [1, 2], [1, 0])
    n_way_column_map(processed.fr_pneumopatia, raw.PNEUMOPATI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_puerpera, raw.PUERPERA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_snd_down, raw.SIND_DOWN, [1, 2], [1, 0])

    n_way_column_map(processed.sint_dfc_respiratorio, raw.DESC_RESP, [1, 2], [1, 0])
    n_way_column_map(processed.sint_diarreia, raw.DIARREIA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_dispneia, raw.DISPNEIA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_dor_garganta, raw.GARGANTA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_febre, raw.FEBRE, [1, 2], [1, 0])
    n_way_column_map(processed.sint_saturacao, raw.SATURACAO, [1, 2], [1, 0])
    n_way_column_map(processed.sint_tosse, raw.TOSSE, [1, 2], [1, 0])

    fill_column(processed.vac_covid, 0)
    n_way_column_map(processed.vac_gripe, raw.VACINA, [1, 2], [1, 0])

    n_way_column_map(processed.evo_internacao, raw.HOSPITAL, [1, 2], [1, 0])
    n_way_column_map(processed.evo_obito, raw.EVOLUCAO, [1, 2, 3], [0, 1, 1])
    n_way_column_map(processed.evo_uti, raw.UTI, [1, 2], [1, 0])
    n_way_column_map(processed.evo_ventilacao, raw.SUPORT_VEN, [1, 2, 3], [0, 1, 1])

    fill_column(processed.dg_covid, 0)
    return processed


def process_y19(input_filename):
    raw = pd.read_csv(RAW_DATA_DIR / (input_filename + '.csv'), delimiter=';', encoding='iso-8859-1', usecols=['CS_SEXO', 'CO_MUN_NOT', 'DT_NASC', 'DT_NOTIFIC', 'PUERPERA', 'CARDIOPATI', 'HEMATOLOGI', 'SIND_DOWN', 'HEPATICA', 'ASMA', 'DIABETES', 'NEUROLOGIC', 'PNEUMOPATI', 'IMUNODEPRE', 'RENAL', 'OBESIDADE', 'FEBRE', 'TOSSE', 'GARGANTA', 'DISPNEIA', 'DESC_RESP', 'SATURACAO', 'DIARREIA', 'VOMITO', 'VACINA', 'HOSPITAL', 'UTI', 'EVOLUCAO', 'CS_GESTANT', 'SUPORT_VEN'])

    processed = new_blank_dataframe(len(raw))

    processed.cad_dt_nascimento = filter_dates(raw.DT_NASC)
    processed.cad_dt_notificacao = filter_dates(raw.DT_NOTIFIC)

    unoptimzed_n_way_column_map(processed.cad_sexo_feminino, raw.CS_SEXO, ['F', 'M'], [1, 0])
    n_way_column_filter(processed.cad_cod_cidade, raw.CO_MUN_NOT, lambda x: x < 100000 or x > 999999, np.nan)

    n_way_column_map(processed.fr_asma, raw.ASMA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_cardiopatia, raw.CARDIOPATI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_diabetes, raw.DIABETES, [1, 2], [1, 0])
    n_way_column_map(processed.fr_doenca_renal, raw.RENAL, [1, 2], [1, 0])
    n_way_column_map(processed.fr_gestante, raw.CS_GESTANT, [1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 0, 0])
    n_way_column_map(processed.fr_hematologia, raw.HEMATOLOGI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_hepatia, raw.HEPATICA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_imunodepressao, raw.IMUNODEPRE, [1, 2], [1, 0])
    n_way_column_map(processed.fr_neuropatia, raw.NEUROLOGIC, [1, 2], [1, 0])
    n_way_column_map(processed.fr_obesidade, raw.OBESIDADE, [1, 2], [1, 0])
    n_way_column_map(processed.fr_pneumopatia, raw.PNEUMOPATI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_puerpera, raw.PUERPERA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_snd_down, raw.SIND_DOWN, [1, 2], [1, 0])

    n_way_column_map(processed.sint_dfc_respiratorio, raw.DESC_RESP, [1, 2], [1, 0])
    n_way_column_map(processed.sint_diarreia, raw.DIARREIA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_dispneia, raw.DISPNEIA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_dor_garganta, raw.GARGANTA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_febre, raw.FEBRE, [1, 2], [1, 0])
    n_way_column_map(processed.sint_saturacao, raw.SATURACAO, [1, 2], [1, 0])
    n_way_column_map(processed.sint_tosse, raw.TOSSE, [1, 2], [1, 0])
    n_way_column_map(processed.sint_vomito, raw.VOMITO, [1, 2], [1, 0])

    fill_column(processed.vac_covid, 0)
    n_way_column_map(processed.vac_gripe, raw.VACINA, [1, 2], [1, 0])

    n_way_column_map(processed.evo_internacao, raw.HOSPITAL, [1, 2], [1, 0])
    n_way_column_map(processed.evo_obito, raw.EVOLUCAO, [1, 2, 3], [0, 1, 1])
    n_way_column_map(processed.evo_uti, raw.UTI, [1, 2], [1, 0])
    n_way_column_map(processed.evo_ventilacao, raw.SUPORT_VEN, [1, 2, 3], [1, 1, 0])

    fill_column(processed.dg_covid, 0)
    return processed


def process_y20(input_filename):
    raw = pd.read_csv(RAW_DATA_DIR / (input_filename + '.csv'), delimiter=';', encoding='iso-8859-1', usecols=['CS_SEXO', 'CO_MUN_NOT', 'DT_NASC', 'DT_NOTIFIC', 'PUERPERA', 'CARDIOPATI', 'HEMATOLOGI', 'SIND_DOWN', 'HEPATICA', 'ASMA', 'DIABETES', 'NEUROLOGIC', 'PNEUMOPATI', 'IMUNODEPRE', 'RENAL', 'OBESIDADE', 'FEBRE', 'TOSSE', 'GARGANTA', 'DISPNEIA', 'DESC_RESP', 'SATURACAO', 'DIARREIA', 'VOMITO', 'DOR_ABD', 'FADIGA', 'PERD_OLFT', 'PERD_PALA', 'VACINA', 'HOSPITAL', 'UTI', 'EVOLUCAO', 'CS_GESTANT', 'SUPORT_VEN', 'CLASSI_FIN'])

    processed = new_blank_dataframe(len(raw))

    processed.cad_dt_nascimento = filter_dates(raw.DT_NASC)
    processed.cad_dt_notificacao = filter_dates(raw.DT_NOTIFIC)

    unoptimzed_n_way_column_map(processed.cad_sexo_feminino, raw.CS_SEXO, ['F', 'M'], [1, 0])
    n_way_column_filter(processed.cad_cod_cidade, raw.CO_MUN_NOT, lambda x: x < 100000 or x > 999999, np.nan)

    n_way_column_map(processed.fr_asma, raw.ASMA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_cardiopatia, raw.CARDIOPATI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_diabetes, raw.DIABETES, [1, 2], [1, 0])
    n_way_column_map(processed.fr_doenca_renal, raw.RENAL, [1, 2], [1, 0])
    n_way_column_map(processed.fr_gestante, raw.CS_GESTANT, [1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 0, 0])
    n_way_column_map(processed.fr_hematologia, raw.HEMATOLOGI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_hepatia, raw.HEPATICA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_imunodepressao, raw.IMUNODEPRE, [1, 2], [1, 0])
    n_way_column_map(processed.fr_neuropatia, raw.NEUROLOGIC, [1, 2], [1, 0])
    n_way_column_map(processed.fr_obesidade, raw.OBESIDADE, [1, 2], [1, 0])
    n_way_column_map(processed.fr_pneumopatia, raw.PNEUMOPATI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_puerpera, raw.PUERPERA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_snd_down, raw.SIND_DOWN, [1, 2], [1, 0])

    n_way_column_map(processed.sint_dfc_respiratorio, raw.DESC_RESP, [1, 2], [1, 0])
    n_way_column_map(processed.sint_diarreia, raw.DIARREIA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_dispneia, raw.DISPNEIA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_dor_abdominal, raw.DOR_ABD, [1, 2], [1, 0])
    n_way_column_map(processed.sint_dor_garganta, raw.GARGANTA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_fadiga, raw.FADIGA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_febre, raw.FEBRE, [1, 2], [1, 0])
    n_way_column_map(processed.sint_prd_olfato, raw.PERD_OLFT, [1, 2], [1, 0])
    n_way_column_map(processed.sint_prd_paladar, raw.PERD_PALA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_saturacao, raw.SATURACAO, [1, 2], [1, 0])
    n_way_column_map(processed.sint_tosse, raw.TOSSE, [1, 2], [1, 0])
    n_way_column_map(processed.sint_vomito, raw.VOMITO, [1, 2], [1, 0])

    fill_column(processed.vac_covid, 0)
    n_way_column_map(processed.vac_gripe, raw.VACINA, [1, 2], [1, 0])

    n_way_column_map(processed.evo_internacao, raw.HOSPITAL, [1, 2], [1, 0])
    n_way_column_map(processed.evo_obito, raw.EVOLUCAO, [1, 2, 3], [0, 1, 1])
    n_way_column_map(processed.evo_uti, raw.UTI, [1, 2], [1, 0])
    n_way_column_map(processed.evo_ventilacao, raw.SUPORT_VEN, [1, 2, 3], [1, 1, 0])

    n_way_column_map(processed.dg_covid, raw.CLASSI_FIN, [1, 2, 3, 4, 5], [0, 0, 0, 0, 1])
    return processed


def process_y21(input_filename):
    raw = pd.read_csv(RAW_DATA_DIR / (input_filename + '.csv'), delimiter=';', encoding='iso-8859-1', usecols=['CS_SEXO', 'DT_NASC', 'DT_NOTIFIC', 'CO_MUN_NOT', 'PUERPERA', 'CARDIOPATI', 'HEMATOLOGI', 'SIND_DOWN', 'HEPATICA', 'ASMA', 'DIABETES', 'NEUROLOGIC', 'PNEUMOPATI', 'IMUNODEPRE', 'RENAL', 'OBESIDADE', 'FEBRE', 'TOSSE', 'GARGANTA', 'DISPNEIA', 'DESC_RESP', 'SATURACAO', 'DIARREIA', 'VOMITO', 'DOR_ABD', 'FADIGA', 'PERD_OLFT', 'PERD_PALA', 'VACINA_COV', 'VACINA', 'HOSPITAL', 'UTI', 'EVOLUCAO', 'CS_GESTANT', 'SUPORT_VEN', 'CLASSI_FIN'])

    processed = new_blank_dataframe(len(raw))

    processed.cad_dt_nascimento = filter_dates(raw.DT_NASC)
    processed.cad_dt_notificacao = filter_dates(raw.DT_NOTIFIC)

    unoptimzed_n_way_column_map(processed.cad_sexo_feminino, raw.CS_SEXO, ['F', 'M'], [1, 0])
    n_way_column_filter(processed.cad_cod_cidade, raw.CO_MUN_NOT, lambda x: x < 100000 or x > 999999, np.nan)

    n_way_column_map(processed.fr_asma, raw.ASMA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_cardiopatia, raw.CARDIOPATI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_diabetes, raw.DIABETES, [1, 2], [1, 0])
    n_way_column_map(processed.fr_doenca_renal, raw.RENAL, [1, 2], [1, 0])
    n_way_column_map(processed.fr_gestante, raw.CS_GESTANT, [1, 2, 3, 4, 5, 6], [1, 1, 1, 1, 0, 0])
    n_way_column_map(processed.fr_hematologia, raw.HEMATOLOGI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_hepatia, raw.HEPATICA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_imunodepressao, raw.IMUNODEPRE, [1, 2], [1, 0])
    n_way_column_map(processed.fr_neuropatia, raw.NEUROLOGIC, [1, 2], [1, 0])
    n_way_column_map(processed.fr_obesidade, raw.OBESIDADE, [1, 2], [1, 0])
    n_way_column_map(processed.fr_pneumopatia, raw.PNEUMOPATI, [1, 2], [1, 0])
    n_way_column_map(processed.fr_puerpera, raw.PUERPERA, [1, 2], [1, 0])
    n_way_column_map(processed.fr_snd_down, raw.SIND_DOWN, [1, 2], [1, 0])

    n_way_column_map(processed.sint_dfc_respiratorio, raw.DESC_RESP, [1, 2], [1, 0])
    n_way_column_map(processed.sint_diarreia, raw.DIARREIA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_dispneia, raw.DISPNEIA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_dor_abdominal, raw.DOR_ABD, [1, 2], [1, 0])
    n_way_column_map(processed.sint_dor_garganta, raw.GARGANTA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_fadiga, raw.FADIGA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_febre, raw.FEBRE, [1, 2], [1, 0])
    n_way_column_map(processed.sint_prd_olfato, raw.PERD_OLFT, [1, 2], [1, 0])
    n_way_column_map(processed.sint_prd_paladar, raw.PERD_PALA, [1, 2], [1, 0])
    n_way_column_map(processed.sint_saturacao, raw.SATURACAO, [1, 2], [1, 0])
    n_way_column_map(processed.sint_tosse, raw.TOSSE, [1, 2], [1, 0])
    n_way_column_map(processed.sint_vomito, raw.VOMITO, [1, 2], [1, 0])

    n_way_column_map(processed.vac_covid, raw.VACINA_COV, [1, 2], [1, 0])
    n_way_column_map(processed.vac_gripe, raw.VACINA, [1, 2], [1, 0])

    n_way_column_map(processed.evo_internacao, raw.HOSPITAL, [1, 2], [1, 0])
    n_way_column_map(processed.evo_obito, raw.EVOLUCAO, [1, 2, 3], [0, 1, 1])
    n_way_column_map(processed.evo_uti, raw.UTI, [1, 2], [1, 0])
    n_way_column_map(processed.evo_ventilacao, raw.SUPORT_VEN, [1, 2, 3], [1, 1, 0])

    n_way_column_map(processed.dg_covid, raw.CLASSI_FIN, [1, 2, 3, 4, 5], [0, 0, 0, 0, 1])
    return processed


STEPS = 7

print(f'[1/{STEPS}] Processando casos de 2009 a 2012')
y09 = process_y09_12('influd09_limpo-final')
y10 = process_y09_12('influd10_limpo-final')
y11 = process_y09_12('influd11_limpo_final')
y12 = process_y09_12('influd12_limpo_final')

print(f'[2/{STEPS}] Processando casos de 2013 a 2018')
y13 = process_y13_18('influd13_limpo_final')
y14 = process_y13_18('influd14_limpo-final')
y15 = process_y13_18('influd15_limpo-final')
y16 = process_y13_18('influd16_limpo-final')
y17 = process_y13_18('influd17_limpo-final')
y18 = process_y13_18('influd18_limpo-final')

print(f'[3/{STEPS}] Processando casos de 2019')
y19 = process_y19('influd19_limpo-27.04.2020-final')

print(f'[4/{STEPS}] Processando casos de 2020')
y20 = process_y20('INFLUD-02-08-2021')

print(f'[5/{STEPS}] Processando casos de 2021')
y21 = process_y21('INFLUD21-02-08-2021')

print(f'[6/{STEPS}] Unindo casos')
casos = pd.concat([y09, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19, y20, y21], ignore_index=True)

casos.dropna(subset=['cad_cod_cidade'], inplace=True)
casos['cad_cod_cidade'] = casos['cad_cod_cidade'].apply(int)
func_column_map(casos.cad_cod_uf, casos.cad_cod_cidade, lambda x: x // 10000)
casos['cad_cod_uf'] = casos['cad_cod_uf'].apply(int)
casos['cad_uf'] = casos['cad_cod_uf'].astype('category').cat.rename_categories({11: 'Rondônia', 12: 'Acre', 13: 'Amazonas', 14: 'Roraima', 15: 'Pará', 16: 'Amapá', 17: 'Tocantins', 21: 'Maranhão', 22: 'Piauí', 23: 'Ceará', 24: 'Rio Grande do Norte', 25: 'Paraíba', 26: 'Pernambuco', 27: 'Alagoas', 28: 'Sergipe', 29: 'Bahia', 31: 'Minas Gerais', 32: 'Espírito Santo', 33: 'Rio de Janeiro', 35: 'São Paulo', 41: 'Paraná', 42: 'Santa Catarina', 43: 'Rio Grande do Sul', 50: 'Mato Grosso do Sul', 51: 'Mato Grosso', 52: 'Goiás', 53: 'Distrito Federal'})
casos.drop(columns=['cad_cod_cidade', 'cad_cod_uf'], inplace=True)
casos.dropna(subset=['cad_dt_nascimento', 'cad_dt_notificacao', 'dg_covid'], inplace=True)
casos['cad_idade'] = (casos.cad_dt_notificacao - casos.cad_dt_nascimento).astype("timedelta64[Y]")

print(f'[7/{STEPS}] Salvando casos')
casos.to_parquet(PROCESSED_DATA_DIR / 'casos.parquet', index=False)
