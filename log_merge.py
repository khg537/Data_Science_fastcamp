import os
import sys
import pandas as pd
import datetime

dir_path = "./log"
out_file = "./out.txt"

def validate_date(date_text):
	try:
		datetime.datetime.strptime(date_text,'%H:%M:%S.%f')
		return True
	except ValueError:
		# print("Incorrect data format({0}), should be YYYY-MM-DD".format(date_text))
		return False

def change_df(file_path):
    out_lists = []
    with open(file_path) as rfile:
        lines = rfile.readlines()
        for line in lines:
            line_split = line.split(' ',1)
            # print(line_split)
            if validate_date(line_split[0]):
                out_lists.append(line_split)

    # for out_list in out_lists:
    #     print(out_list)

    df = pd.DataFrame(out_lists)
    return df

list_df = []
for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.getsize(file_path) > 0:
            df = change_df(file_path)
            print(df.size)
            if df.size >0:
                list_df.append(df)


list_df = pd.concat(list_df)

list_df=list_df.apply(lambda x:x.str.strip(), axis=1)

list_df.columns = ['time', 'value']
print(list_df.head())
list_df['time'] = pd.to_datetime(list_df['time'])
list_df = list_df.sort_values(by='time')
list_df['time'] = list_df['time'].dt.time
list_df.info()
list_df.to_csv('out.txt', sep='\t', index=False)
