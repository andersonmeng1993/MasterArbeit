import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# read the date
FTP = pd.read_csv('../2008_FTP/Versuch_2008_FTP.CSV',sep=';')
# just seperate the date of one single PCB
FTP_1039 = FTP[FTP['PCBIndex']==1039]


fig,ax = plt.subplots(figsize=(48,30))

ax.scatter(FTP_1039['PosX'],FTP_1039['PosY'],s=FTP_1039['Size Area (um2)'].values/10000,marker='s',color='green')

x = FTP_1039['PosX']
y = FTP_1039['PosY']
n = FTP_1039['Pad ID']

for i, txt in enumerate(n):
        ax.annotate(txt,(x[i],y[i]))
        
plt.savefig(fname='FTP_1_green.png',dpi=200)
