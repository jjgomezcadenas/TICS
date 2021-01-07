import numpy as np
import pandas as pd
from pandas import DataFrame
from typing import Tuple, List
from typing import TypeVar
from typing import Union

NN = np.nan
idx = pd.IndexSlice
Columns  = TypeVar('Columns', str, Tuple[str, str], None)

def get_index_slice_from_multi_index(df     : DataFrame,
                                     i      : int,
                                     unique : bool = True)->np.array:
    """
    Given a DataFrame df with multiindex, return an array
    containing a view (with just the unique elements if specified) of
    index i
    """
    vi = df.index.values
    if unique:
        return np.unique(list(zip(*vi))[i])
    else:
        return list(zip(*vi))[i]


def select_on_condition(df : DataFrame, var, cond=True)->DataFrame:
    """
    Return a DataFrame selected if variable var equals condition cond

    """
    return df[df[var] == cond]


def slice_and_select_df(df     : DataFrame,
                       slices  : Tuple[slice],
                       columns : Columns = None)->Union[pd.Series, pd.DataFrame]:

    """
    The slice type is of the form slice(start, stop, step).
    Notice that slice(stop) is valid and slice(start, stop) is also valid
    Very importantly, notice that in pandas, the slicing follows a different
    convention than in python
    (which is very convenient), e.g, the slice includes start and stop

    """
    if columns == None:
        return df.loc[slices, :]
    else:
        return df.loc[slices, columns]
