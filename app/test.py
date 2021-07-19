import json

import pandas as pd


def test_pandas():
    a = pd.__version__
    df1 = pd.read_csv('./test.csv')
    df2 = pd.read_csv('./test2.csv')

    df = df2.merge(df1[['C', 'D']])
    df.to_csv('./res.csv', index=False, sep=',')
    a = df.to_json()
    with open("./test.json", 'w') as f:
        json.dump(a, f)
    print(list('ABC'))


def list_test():
    list1 = [['a', 1, 255, 100, '03'], ['a', 2, 481, 50, '06'], ['a', 47, 255, 500, '03'], ['b', 3, 1, 50, '11']]
    df1 = pd.DataFrame(list1, columns=["名字", "ID", "颜色", "数量", "类型"])
    list2 = [['a', '03', 255, 1], ['a', '06', 481, 2]]
    df2 = pd.DataFrame(list2, columns=["名字", "类型", "颜色", "ID"])
    df = pd.merge(df2, df1, how='inner', on=["名字", "类型", "颜色"])
    df.sort_index(inplace=True)
    print(df)
