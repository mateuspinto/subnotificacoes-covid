from numba import jit, prange
import numpy as np
import pandas as pd


@jit(nopython=True, cache=True)
def __n_way_column_map(target, source, xs, ys):
    for i in prange(target.shape[0]):
        for j in range(xs.shape[0]):
            if source[i] == xs[j]:
                target[i] = ys[j]


def n_way_column_map(target_column, source_column, original_values, new_values):
    target = target_column.to_numpy()
    source = source_column.to_numpy()
    xs = np.array(original_values)
    ys = np.array(new_values)

    __n_way_column_map(target, source, xs, ys)


def unoptimzed_n_way_column_map(target_column, source_column, original_values, new_values):
    target = target_column.to_numpy()
    source = source_column.to_numpy()
    xs = np.array(original_values)
    ys = np.array(new_values)

    for i in range(target.shape[0]):
        for j in range(xs.shape[0]):
            if source[i] == xs[j]:
                target[i] = ys[j]


@jit(nopython=True, cache=True)
def __n_way_column_filter(target, source, f, default):
    for i in prange(target.shape[0]):
        if f(source[i]):
            target[i] = default
        else:
            target[i] = source[i]


def n_way_column_filter(target_column, source_column, filter_func, default_value):
    target = target_column.to_numpy()
    source = source_column.to_numpy()
    f = jit(filter_func, nopython=True, cache=False)

    __n_way_column_filter(target, source, f, default_value)


@jit(nopython=True, cache=True)
def __fill_column(target, x):
    for i in prange(target.shape[0]):
        target[i] = x


def fill_column(target_column, default_value):
    target = target_column.to_numpy()

    __fill_column(target, default_value)


def filter_dates(source_column):
    return pd.to_datetime(source_column, errors='coerce', dayfirst=True)


def new_blank_dataframe(length):
    df = pd.DataFrame()

    df['cad_dt_nascimento'] = np.full(length, np.datetime64(
        'Nat', 'ns'), np.datetime64('Nat', 'ns'))
    df['cad_dt_notificacao'] = np.full(length, np.datetime64(
        'Nat', 'ns'), np.datetime64('Nat', 'ns'))

    df['cad_cod_cidade'] = np.full(length, np.nan, float)
    df['cad_sexo'] = np.full(length, np.nan, float)

    df['fr_asma'] = np.full(length, np.nan, float)
    df['fr_cardiopatia'] = np.full(length, np.nan, float)
    df['fr_diabetes'] = np.full(length, np.nan, float)
    df['fr_doenca_renal'] = np.full(length, np.nan, float)
    df['fr_gestante'] = np.full(length, np.nan, float)
    df['fr_hematologia'] = np.full(length, np.nan, float)
    df['fr_hepatia'] = np.full(length, np.nan, float)
    df['fr_imunodepressao'] = np.full(length, np.nan, float)
    df['fr_neuropatia'] = np.full(length, np.nan, float)
    df['fr_obesidade'] = np.full(length, np.nan, float)
    df['fr_pneumopatia'] = np.full(length, np.nan, float)
    df['fr_puerpera'] = np.full(length, np.nan, float)
    df['fr_snd_down'] = np.full(length, np.nan, float)

    df['sint_dfc_respiratorio'] = np.full(length, np.nan, float)
    df['sint_diarreia'] = np.full(length, np.nan, float)
    df['sint_dispneia'] = np.full(length, np.nan, float)
    df['sint_dor_abdominal'] = np.full(length, np.nan, float)
    df['sint_dor_garganta'] = np.full(length, np.nan, float)
    df['sint_fadiga'] = np.full(length, np.nan, float)
    df['sint_febre'] = np.full(length, np.nan, float)
    df['sint_prd_olfato'] = np.full(length, np.nan, float)
    df['sint_prd_paladar'] = np.full(length, np.nan, float)
    df['sint_saturacao'] = np.full(length, np.nan, float)
    df['sint_tosse'] = np.full(length, np.nan, float)
    df['sint_vomito'] = np.full(length, np.nan, float)

    df['vac_covid'] = np.full(length, np.nan, float)
    df['vac_gripe'] = np.full(length, np.nan, float)

    df['evo_internacao'] = np.full(length, np.nan, float)
    df['evo_obito'] = np.full(length, np.nan, float)
    df['evo_uti'] = np.full(length, np.nan, float)
    df['evo_ventilacao'] = np.full(length, np.nan, float)

    df['dg_covid'] = np.full(length, np.nan, float)
    return df
