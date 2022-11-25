import os
import sys
import pandas as pd
import datetime

dir_path = "./"
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
            if validate_date(line_split[0]):
                out_lists.append(line_split)

    # for out_list in out_lists:
    #     print(out_list)

    df = pd.DataFrame(out_lists)
    return df


for (root, directories, files) in os.walk(dir_path):
    empty_df = pd.DataFrame()

    for file in files:
        file_path = os.path.join(root, file)
        if os.path.getsize(file_path) > 0:
            df = change_df(file_path)
            print(df.size)
            if df.size >0:
                empty_df = empty_df.append(df)

    # df.to_csv(empty_df)
