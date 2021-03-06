import os
import pytest
import numpy  as np
import pandas as pd
from   dataclasses import dataclass

from pandas      import DataFrame


@pytest.fixture(scope = 'session')
def FDATA():
    return os.environ['FLEXDATA']


@pytest.fixture(scope='session')
def test_df():
    # hierarchical indices and columns
    index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]],
                                       names=['year', 'visit'])
    columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']],
                                         names=['subject', 'type'])

    # mock some data
    data = np.round(np.random.randn(4, 6), 1)
    data[:, ::2] *= 10
    data += 37

    # create the DataFrame
    health_data = pd.DataFrame(data, index=index, columns=columns)
    health_data
    return health_data
