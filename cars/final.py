import pickle
import os
import pandas as pd
import numpy as np
import warnings
from matplotlib import pyplot as plt

warnings.filterwarnings('ignore')


def reduce_mem_usage(df):
    """ iterate through all the columns of a dataframe and modify the data type
        to reduce memory usage.
    """
    start_mem = df.memory_usage().sum()
    print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum()
    print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
    return df


sample_feature = reduce_mem_usage(pd.read_csv('data_for_tree.csv'))
continuous_feature_names = [x for x in sample_feature.columns if x not in ['price']]

# 线性模型
sample_feature = sample_feature.dropna().replace('-', 0).reset_index(drop=True)
sample_feature['notRepairedDamage'] = sample_feature['notRepairedDamage'].astype(np.float32)
train = sample_feature[continuous_feature_names + ['price']]

train_X = train[continuous_feature_names]
train_y = train['price']

# 对标签进行log（X+1变换），使其更贴近正态分布
train_y_ln = np.log(train_y + 1)

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

LinearRegressionModel = LinearRegression(normalize=True)
LinearRegressionModel = LinearRegressionModel.fit(train_X, train_y_ln)

RidgeModel = Ridge(normalize=True)
RidgeModel = RidgeModel.fit(train_X, train_y_ln)

LassoModel = Lasso().fit(train_X, train_y_ln)

# 非线性模型

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

DecisionTreeModel = DecisionTreeRegressor().fit(train_X, train_y_ln)
RandomForestModel = RandomForestRegressor().fit(train_X, train_y_ln)
GradientBoostingModel = GradientBoostingRegressor().fit(train_X, train_y_ln)

f = open('./models/LinearRegressionModel.pkl', 'xb')
pickle.dump(LinearRegressionModel, f)
f.close()

f = open('./models/RidgeModel.pkl', 'xb')
pickle.dump(RidgeModel, f)
f.close()

f = open('./models/LassoModel.pkl', 'xb')
pickle.dump(LassoModel, f)
f.close()

f = open('./models/DecisionTreeModel.pkl', 'wb')
pickle.dump(DecisionTreeModel, f)
f.close()

f = open('./models/RandomForestModel.pkl', 'wb')
pickle.dump(RandomForestModel, f)
f.close()

f = open('./models/GradientBoostingModel.pkl', 'wb')
pickle.dump(GradientBoostingModel, f)
f.close()

print('Done')
