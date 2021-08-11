from numba import jit, prange
import numpy as np
import pandas as pd

@jit(nopython=True, cache=True)
def __n_way_column_map(source, target, xs, ys):
    for i in prange(target.shape[0]):
        for j in range(len(xs)):
            if source[i] == xs[j]:
                target[i] = ys[j]

def n_way_column_map(source_column, target_column, original_values, new_values):
    __n_way_column_map(source_column.to_numpy(), target_column.to_numpy(), np.array(original_values), np.array(new_values))
    
def new_column(lenght, default_value, dtype):
    return np.full(lenght, default_value, dtype)

def new_raw_dataframe(lenght):
    df = pd.DataFrame()
    df['fr_puerpera'] = new_column(lenght, np.nan, float)
    df['fr_cardiopatia'] = new_column(lenght, np.nan, float)
    df['fr_hematologia'] = new_column(lenght, np.nan, float)
    df['fr_snd_down'] = new_column(lenght, np.nan, float)
    df['fr_hepatia'] = new_column(lenght, np.nan, float)
    df['fr_asma'] = new_column(lenght, np.nan, float)
    df['fr_diabetes'] = new_column(lenght, np.nan, float)
    df['fr_neuropatia'] = new_column(lenght, np.nan, float)
    df['fr_pneumopatia'] = new_column(lenght, np.nan, float)
    df['fr_imunodepressao'] = new_column(lenght, np.nan, float)
    df['fr_doenca_renal'] = new_column(lenght, np.nan, float)
    df['fr_obesidade'] = new_column(lenght, np.nan, float)

    df['st_tosse'] = new_column(lenght, np.nan, float)
    df['st_febre'] = new_column(lenght, np.nan, float)
    df['st_dor_garganta'] = new_column(lenght, np.nan, float)
    df['st_dispneia'] = new_column(lenght, np.nan, float)
    df['st_dfc_respiratorio'] = new_column(lenght, np.nan, float)
    df['st_saturacao'] = new_column(lenght, np.nan, float)
    df['st_diarreia'] = new_column(lenght, np.nan, float)
    df['st_vomito'] = new_column(lenght, np.nan, float)
    df['st_dor_abdominal'] = new_column(lenght, np.nan, float)
    df['st_fadiga'] = new_column(lenght, np.nan, float)
    df['st_prd_olfato'] = new_column(lenght, np.nan, float)
    df['st_prd_paladar'] = new_column(lenght, np.nan, float)
    return df
