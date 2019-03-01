import pandas as pd
def send(csv_file):
    data_set=pd.read_csv(csv_file, sep=',')
    """data_set = csv_file.read().decode('utf-8')"""
    img = "C:\\Users\\Hp\\Downloads\\download"

    return data_set,img