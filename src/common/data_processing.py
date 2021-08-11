from numba import jit, prange
import numpy as np

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