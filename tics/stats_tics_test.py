import numpy as np
import pandas as pd
from   pandas import DataFrame
from   typing      import Tuple, List

from tics.stats_tics import bin_data_with_equal_bin_size

def test_bin_data_with_equal_bin_size():
    """
    The test bins the data in increasingly fine arrays, checking that
    the bin edges are correctly calculated

    """
    x = np.array([ 2.8141143e+00,  2.9682205e+00,  3.0682065e+00,  3.2710953e+00,
        3.7205276e+00,  4.2058253e+00,  4.4833355e+00,  4.5922909e+00,
        4.6243653e+00,  4.5973992e+00,  4.4679122e+00,  4.2372832e+00,
        3.9548671e+00,  3.6256325e+00,  3.3081403e+00,  2.8729758e+00,
        2.3658357e+00,  1.7931334e+00,  9.5186341e-01,  1.2763637e-01,
        1.9326104e-02, -4.1853673e-14,  2.4698291e+00,  2.3667533e+00,
        2.2683897e+00,  2.2240682e+00,  2.2948375e+00,  2.3487322e+00,
        2.3467033e+00,  2.2901437e+00,  2.2255528e+00,  2.1227870e+00,
        2.0882895e+00,  2.0404658e+00,  2.0501738e+00,  2.0681076e+00,
        2.0488355e+00,  1.9680529e+00,  1.9035678e+00,  1.8617749e+00,
        1.8494277e+00,  1.8664446e+00,  1.8873806e+00,  1.9099003e+00,
        1.9441431e+00,  1.9677173e+00,  1.9965943e+00,  1.9974265e+00,
        2.0425725e+00,  2.0882130e+00,  2.1322501e+00,  2.1365113e+00,
        2.1056457e+00,  2.0776482e+00,  2.0478256e+00,  2.0211906e+00,
        2.0128164e+00,  2.0101888e+00,  2.0278101e+00,  2.0380580e+00,
        2.0452802e+00,  2.0464013e+00,  2.0703557e+00,  2.0902441e+00,
        2.0900640e+00,  2.0836682e+00,  2.0767059e+00,  2.0698059e+00,
        2.0608964e+00,  2.0525715e+00,  2.0587554e+00,  2.0667362e+00,
        2.0739298e+00,  2.0695913e+00,  2.0751913e+00,  2.0781918e+00,
        2.0758624e+00,  2.0736582e+00,  2.0721989e+00,  2.0698991e+00,
        2.0650682e+00,  2.0644095e+00,  2.0638511e+00,  2.0634425e+00])

    bin_size = 5
    nbins = int((x.max() - x.min()) / bin_size) +1
    xbins = bin_data_with_equal_bin_size([x], bin_size)[0]

    assert nbins == 1
    assert len(xbins) == nbins + 1
    assert np.allclose(xbins[-1], x.max())

    bin_size = 2
    nbins = int((x.max() - x.min()) / bin_size) +1
    xbins = bin_data_with_equal_bin_size([x], bin_size)[0]
    assert nbins == 3
    assert len(xbins) == nbins + 1
    assert np.allclose(xbins[-1], x.max())

    bin_size = 1
    nbins = int((x.max() - x.min()) / bin_size) +1
    xbins = bin_data_with_equal_bin_size([x], bin_size)[0]
    assert nbins == 5
    assert len(xbins) == nbins + 1
    assert np.allclose(xbins[-1], x.max())
   
