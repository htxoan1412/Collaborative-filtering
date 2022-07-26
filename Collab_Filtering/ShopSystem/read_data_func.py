import pandas
import pandas as read_csv

def get_dataframe_views_base(text):
    r_cols = ['user_id', 'item_id', 'views', 'unix_timestamp']
    views = pandas.read_csv(text,  sep='\t', names=r_cols, encoding='utf-8')
    views = views.drop(columns='unix_timestamp')
    Y_data = views.values
    print("data", Y_data)
    return Y_data