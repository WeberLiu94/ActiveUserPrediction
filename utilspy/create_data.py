import pandas as pd
from dataprocesspy.create_feature_v3_nonp import processing

if __name__=="__main__":
    # print("begin to load the testset")
    # train_set52 = processing(trainSpan=(1, 30), label=False)
    # train_set52.to_csv("data/testing_eld1-30_r.csv", header=True, index=False)
    # train_set52 = pd.read_csv("data/training_eld1-23.csv", header=0, index_col=None, usecols=use_feature)
    # print(train_set52.describe())
    # print("begin to load the trainset52")
    # train_set52 = processing(trainSpan=(1, 23), label=True)
    # train_set52.to_csv("data/training_rld1-23_r.csv", header=True, index=False)
    # # train_set52 = pd.read_csv("data/training_eld1-23.csv", header=0, index_col=None, usecols=use_feature)
    # print(train_set52.describe())
    # print("begin to load the trainset51")
    # train_set51 = processing(trainSpan=(1, 22), label=True)
    # train_set51.to_csv("data/training_rld1-22.csv", header=True, index=False)
    # # train_set5 = pd.read_csv("data/training_eld1-22.csv", header=0, index_col=None, usecols=use_feature)
    # print(train_set51.describe())
    # print("begin to load the trainset5")
    # train_set5 = processing(trainSpan=(1, 21), label=True)
    # train_set5.to_csv("data/training_rld1-21.csv", header=True, index=False)
    # # train_set5 = pd.read_csv("data/training_eld1-21.csv", header=0, index_col=None, usecols=use_feature)
    # print(train_set5.describe())
    print("begin to load the trainset41")
    train_set41 = processing(trainSpan=(1, 20), label=True)
    train_set41.to_csv("../data/data_v4/training_rld1-20.csv", header=True, index=False)
    # train_set41 = pd.read_csv("data/training_eld1-20.csv", header=0, index_col=None, usecols=use_feature)
    print(train_set41.describe())
    print("begin to load the trainset4")
    train_set4 = processing(trainSpan=(1, 19), label=True)
    train_set4.to_csv("../data/data_v4/training_rld1-19.csv", header=True, index=False)
    # train_set4 = pd.read_csv("data/training_eld1-19.csv", header=0, index_col=None, usecols=use_feature)
    print(train_set4.describe())
    print("begin to load the trainset2")
    train_set2 = processing(trainSpan=(1, 15), label=True)
    train_set2.to_csv("../data/data_v4/training_rld1-15.csv", header=True, index=False)
    # train_set2 = pd.read_csv("data/training_eld1-15.csv", header=0, index_col=None, usecols=use_feature)
    print(train_set2.describe())
    print("begin to load the trainset21")
    train_set21 = processing(trainSpan=(1, 16), label=True)
    train_set21.to_csv("../data/data_v4/training_rld1-16.csv", header=True, index=False)
    # train_set21 = pd.read_csv("data/training_eld1-16.csv", header=0, index_col=None, usecols=use_feature)
    print(train_set21.describe())
    print("begin to load the trainset3")
    train_set3 = processing(trainSpan=(1, 17), label=True)
    train_set3.to_csv("../data/data_v4/training_rld1-17.csv", header=True, index=False)
    # train_set3 = pd.read_csv("data/training_eld1-17.csv", header=0, index_col=None, usecols=use_feature)
    print(train_set3.describe())
    print("begin to load the trainset31")
    train_set31 = processing(trainSpan=(1, 18), label=True)
    train_set31.to_csv("../data/data_v4/training_rld1-18.csv", header=True, index=False)
    # train_set3 = pd.read_csv("data/training_eld1-18.csv", header=0, index_col=None, usecols=use_feature)
    print(train_set31.describe())

