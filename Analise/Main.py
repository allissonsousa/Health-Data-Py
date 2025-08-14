import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import csv


dado = r'C:\Users\allisson.avila\Documents\GitHub\Health-Data-Py\Analise\Mortalidade_Geral_1982.csv'

df = pd.read_csv(dado)

print(df.head())
