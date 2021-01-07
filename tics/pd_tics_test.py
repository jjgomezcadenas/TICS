import numpy as np
import pandas as pd
from pandas import DataFrame
from   typing      import Tuple, List

from tics.pd_tics import get_index_slice_from_multi_index

def test_get_index_slice_from_multi_index(test_df):
    lst = get_index_slice_from_multi_index(test_df, i = 0)
    assert np.all(np.equal(lst, np.array([2013, 2014])))


def test_get_index_slice_from_multi_index_not_unique(test_df):
    lst = get_index_slice_from_multi_index(test_df, i = 1, unique=False)
    assert np.all(np.equal(lst, (1, 2, 1, 2)))
