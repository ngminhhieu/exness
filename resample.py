import os
import pandas as pd

path = './data'

for root, dirs, files in os.walk(path):
    if root == path:
        continue
    for index, file in enumerate(files):
        print("Resampling ", file)
        data_frame = pd.read_csv(root+"/"+file, usecols=["Symbol", "Timestamp", "Bid"])
        data_frame[['Timestamp', 'z']] = data_frame['Timestamp'].str.split(".", expand=True)
        data_frame = data_frame.drop(['z'], axis=1)
        data_frame['Timestamp'] = data_frame['Timestamp'].str.replace("-", ':')
        data_frame[['date', 'time']] = data_frame['Timestamp'].str.split(" ", expand=True)
        data_frame['Timestamp'] = pd.to_datetime(data_frame['Timestamp'], format='%Y:%m:%d %H:%M:%S')
        
        # resample
        data_bid = data_frame.set_index(['Timestamp'])
        data_bid = data_bid['Bid'].resample('60Min').ohlc()
        data_bid = data_bid.round(3)
       
        # add column volume
        data_bid['volume'] = 100
        data_bid.reset_index(inplace = True)
        data_bid[['date', 'time']] = data_bid['Timestamp'].astype(str).str.split(" ", expand=True)
        data_bid['date'] = data_bid['date'].str.replace("-", ".")
        data_bid = data_bid[['date', 'time', 'open', 'high', 'low', 'close', 'volume']]
        data_bid.to_csv("{}/{}_1hour.csv".format(root, file.split(".")[0]), header=False, index=False)