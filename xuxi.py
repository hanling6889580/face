import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

def loaddataset(filename):
    datamat=[]
    fr=open(filename)
    for line in fr.readlines():
        curline = line.strip().split('\t')
        fltline = map(float,curline)
        datamat.append(fltline)
    return datamat

loaddataset('C:\Users\Administrator\Desktop\������ʵ��Ԥ��.txt')
