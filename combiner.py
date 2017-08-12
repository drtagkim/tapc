from tkinter import *
from glob import glob
import pandas as pd
#=======================================
#
folder_name="test2"
output_name="test2.xls"
# MAIN PROGRAM =========================
def read_files(folder_name):
    return glob(folder_name+"/*.xls")
def combine_data(files):
    data=pd.DataFrame()
    for file in files:
        a=pd.ExcelFile(file)
        b=a.parse()
        data=data.append(b)
    return data
def export_data(data,fname):
    data.to_excel(fname)

if __name__=="__main__":
    files=read_files(folder_name)
    data=combine_data(files)
    export_data(data,output_name)
