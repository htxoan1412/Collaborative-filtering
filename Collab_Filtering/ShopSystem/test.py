import numpy as np
import pandas
from joblib.numpy_pickle_utils import xrange
import read_data_func
import collab_filtering

if __name__ == '__main__':
    rate_train = read_data_func.get_dataframe_views_base('ub.base')
    rate_test = read_data_func.get_dataframe_views_base('ub.test')
    rate_train[:, :2] -= 1
    rate_test[:, :2] -= 1
    cf_rs = collab_filtering.CF(rate_train, k=30, uuCF=1)
    cf_rs.fit()

    n_tests = rate_test.shape[0]
    SE = 0  # squared error
    for n in xrange(n_tests):
        pred = cf_rs.pred(rate_test[n, 0], rate_test[n, 1], normalized=0)
        SE += (pred - rate_test[n, 2]) ** 2

    RMSE = np.sqrt(SE / n_tests)
    print("User-user CF, RMSE =", RMSE)