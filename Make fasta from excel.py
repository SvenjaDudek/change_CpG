#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 10:07:57 2023

@author: admin
"""

'''write fasta'''
import pandas as pd

from tkinter import filedialog as fd
filename = fd.askopenfilename()

df=pd.read_excel(filename)

def write_fasta(df,name):
    with open(name, 'w') as f:
    
        for row in df.itertuples():
            f.write(">" + row[1] + "\n" + row[2] + "\n")

write_fasta(df, 'Final_selection_RNA_fasta.txt')

#test