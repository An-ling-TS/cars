import pandas as pd
import numpy as np
import pickle


def reduce_mem_usage(df):
    """ iterate through all the columns of a dataframe and modify the data type
        to reduce memory usage.
    """

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

    # end_mem = df.memory_usage().sum()
    # print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    # print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))
    return df


def predict(car):
    f = open('./models/LinearRegressionModel.pkl', 'rb')
    LinearRegressionModel = pickle.load(f)
    f.close()

    f = open('./models/RidgeModel.pkl', 'rb')
    RidgeModel = pickle.load(f)
    f.close()

    f = open('./models/LassoModel.pkl', 'rb')
    LassoModel = pickle.load(f)
    f.close()

    f = open('./models/DecisionTreeModel.pkl', 'rb')
    DecisionTreeModel = pickle.load(f)
    f.close()

    f = open('./models/RandomForestModel.pkl', 'rb')
    RandomForestModel = pickle.load(f)
    f.close()

    f = open('./models/GradientBoostingModel.pkl', 'rb')
    GradientBoostingModel = pickle.load(f)
    f.close()

    # finalResult最终的预测价格
    LinearRegressionPredictPrice = np.exp(LinearRegressionModel.predict(car))
    RidgeModelPredictPrice = np.exp(RidgeModel.predict(car))
    LassoModelPredictPrice = np.exp(LassoModel.predict(car))
    DecisionTreeModelPredictPrice = np.exp(DecisionTreeModel.predict(car))
    RandomForestModelPredictPrice = np.exp(RandomForestModel.predict(car))
    GradientBoostingModelPredictPrice = np.exp(GradientBoostingModel.predict(car))

    finalResult = (
                          LinearRegressionPredictPrice * 0.7 + RidgeModelPredictPrice * 0.7 + LassoModelPredictPrice * 0.7 + DecisionTreeModelPredictPrice * 1.3 + RandomForestModelPredictPrice * 1.3 + GradientBoostingModelPredictPrice * 1.3) / 6
    return finalResult
