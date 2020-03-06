# a basic routine for how to analyse and making graphics for the date
# example date: Versuch 26092019 FCT

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

Versuch_2909 = pd.read_excel('Versuch_26092019_FCT.xlsx',sep=';')
Versuch_2909.head()

# get a general information of the date
Versuch_2909['Volume (%)'].describe()


# plot a Qualitaetsregelkarte
Versuch_2909_mean = 1.170840e+02
plt.figure(figsize=(12,8))

x = np.arange(1037953,1,-1)

plt.title('Qualitätsregelkarte bzgl. der Transfereffizienz für den Versuch 7, FCT')

plt.plot(x,Versuch_2909['Volume (%)'],color='limegreen',label='Transfereffizienz(%)')

plt.xlabel('Nummer der Pads', fontsize=13)
plt.ylabel('Transfereffizienz(%)', fontsize=13)

plt.axhline(xmin=0,xmax=103000,y=Versuch_2909_mean,color='navy',label='Mittelwert')

plt.legend()

#plt.savefig('png/QRK_vor_preprocessing.png',dpi=300)
#plt.savefig('svg/QRK_vor_preprocessing.svg',dpi=300)


# see different pads using different conditions
Versuch_2909_TE_0 = Versuch_2909[Versuch_2909['Volume (%)']==0]
Versuch_2909_TE_0['Pad ID'].to_excel('gleich_0_Pads.xlsx')
Versuch_2909_TE_0['PCBIndex'].to_excel('gleich_0_PCB.xlsx')


Versuch_2909_klein_10 = Versuch_2909[Versuch_2909['Volume (%)']<=10]
Versuch_2909_klein_10['Pad ID'].to_excel('klein_10_Pads.xlsx')
Versuch_2909_klein_10['PCBIndex'].to_excel('klein_10_PCB.xlsx')

Versuch_2909_klein_20 = Versuch_2909[Versuch_2909['Volume (%)']<=20]
Versuch_2909_klein_20['Pad ID'].to_excel('klein_20_Pads.xlsx')
Versuch_2909_klein_20['PCBIndex'].to_excel('klein_20_PCB.xlsx')

Versuch_2909_klein_30 = Versuch_2909[Versuch_2909['Volume (%)']<=30]
Versuch_2909_klein_30['Pad ID'].to_excel('klein_30_Pads.xlsx')
Versuch_2909_klein_30['PCBIndex'].to_excel('klein_30_PCB.xlsx')

Versuch_2909_gross_700 = Versuch_2909[Versuch_2909['Volume (%)']>=700]
Versuch_2909_gross_700['Pad ID'].to_excel('gross_700_Pads.xlsx')
Versuch_2909_gross_700['PCBIndex'].to_excel('gross_700_PCB.xlsx')


Versuch_2909_gross_600 = Versuch_2909[Versuch_2909['Volume (%)']>=600]
Versuch_2909_gross_600['Pad ID'].to_excel('gross_600_Pads.xlsx')
Versuch_2909_gross_600['PCBIndex'].to_excel('gross_600_PCB.xlsx')


Versuch_2909_gross_500 = Versuch_2909[Versuch_2909['Volume (%)']>=500]
Versuch_2909_gross_500['Pad ID'].to_excel('gross_500_Pads.xlsx')
Versuch_2909_gross_500['PCBIndex'].to_excel('gross_500_PCB.xlsx')

Versuch_2909_gross_400 = Versuch_2909[Versuch_2909['Volume (%)']>=400]
Versuch_2909_gross_400['Pad ID'].to_excel('gross_400_Pads.xlsx')
Versuch_2909_gross_400['PCBIndex'].to_excel('gross_400_PCB.xlsx')

Versuch_2909_gross_300 = Versuch_2909[Versuch_2909['Volume (%)']>=300]
Versuch_2909_gross_300['Pad ID'].to_excel('gross_300_Pads.xlsx')
Versuch_2909_gross_300['PCBIndex'].to_excel('gross_300_PCB.xlsx')

Versuch_2909_gross_250 = Versuch_2909[Versuch_2909['Volume (%)']>=250]
Versuch_2909_gross_250['Pad ID'].to_excel('gross_250_Pads.xlsx')
Versuch_2909_gross_250['PCBIndex'].to_excel('gross_250_PCB.xlsx')

Versuch_2909_gross_225 = Versuch_2909[Versuch_2909['Volume (%)']>=225]
Versuch_2909_gross_225['Pad ID'].to_excel('gross_225_Pads.xlsx')
Versuch_2909_gross_225['PCBIndex'].to_excel('gross_225_PCB.xlsx')

Versuch_2909_gross_200 = Versuch_2909[Versuch_2909['Volume (%)']>=200]
Versuch_2909_gross_200['Pad ID'].to_excel('gross_200_Pads.xlsx')
Versuch_2909_gross_200['PCBIndex'].to_excel('gross_200_PCB.xlsx')

########################################

# and print the graphics special for PCBs or Pads

# klein 20 PCB
PCB_1375 = Versuch_2909[Versuch_2909['PCBIndex']==1375]
PCB_1471 = Versuch_2909[Versuch_2909['PCBIndex']==1471]
PCB_1422 = Versuch_2909[Versuch_2909['PCBIndex']==1422]
PCB_1389 = Versuch_2909[Versuch_2909['PCBIndex']==1389]

# zwei normalen Leiterplatten zum Vergleich

PCB_1396 = Versuch_2909[Versuch_2909['PCBIndex']==1396]
PCB_1368 = Versuch_2909[Versuch_2909['PCBIndex']==1368]

#gross 225 PCB

PCB_1373 = Versuch_2909[Versuch_2909['PCBIndex']==1373]
PCB_1470 = Versuch_2909[Versuch_2909['PCBIndex']==1470]
PCB_1374 = Versuch_2909[Versuch_2909['PCBIndex']==1374]
PCB_1482 = Versuch_2909[Versuch_2909['PCBIndex']==1482]

# klein 20 Pads
Pad_30557 = Versuch_2909[Versuch_2909['Pad ID']==30557]
Pad_30827 = Versuch_2909[Versuch_2909['Pad ID']==30827]
Pad_34118 = Versuch_2909[Versuch_2909['Pad ID']==34118]

# gross 225 Pads

Pad_220356 = Versuch_2909[Versuch_2909['Pad ID']==220356]
Pad_6032 = Versuch_2909[Versuch_2909['Pad ID']==6032]
Pad_6036 = Versuch_2909[Versuch_2909['Pad ID']==6036]


# klein 20 PCB
plt.figure(figsize=(13,13))

plt.subplot(2,2,1)
plt.title('Gauss-Verteilung Transfereffizienz Leiterplatte 1375')
sns.distplot(PCB_1375['Volume (%)'],color='limegreen')
plt.xlabel('Transfereffizienz(%)')

plt.subplot(2,2,2)
plt.title('Gauss-Verteilung Transfereffizienz Leiterplatte 1471')
sns.distplot(PCB_1471['Volume (%)'],color='limegreen')
plt.xlabel('Transfereffizienz(%)')

plt.subplot(2,2,3)
plt.title('Gauss-Verteilung Transfereffizienz Leiterplatte 1396')
sns.distplot(PCB_1396['Volume (%)'],color='limegreen')
plt.xlabel('Transfereffizienz(%)')

plt.subplot(2,2,4)
plt.title('Gauss-Verteilung Transfereffizienz Leiterplatte 1368')
sns.distplot(PCB_1368['Volume (%)'],color='limegreen')
plt.xlabel('Transfereffizienz(%)')


plt.savefig('png/PCB_1375_1471_1396_1368.png',dpi=300)
plt.savefig('svg/PCB_1375_1471_1396_1368.svg',dpi=300)


#gross 225 PCB + klein 20 PCB +2 normal PCB
plt.figure(figsize=(16,11))

plt.subplot(2,3,1)
plt.title('Verteilung Transfereffizienz Leiterplatte 1375')
sns.distplot(PCB_1375['Volume (%)'],color='limegreen')
plt.xlabel('Transfereffizienz(%)')

plt.subplot(2,3,2)
plt.title('Verteilung Transfereffizienz Leiterplatte 1471')
sns.distplot(PCB_1471['Volume (%)'],color='limegreen')
plt.xlabel('Transfereffizienz(%)')


plt.subplot(2,3,3)
plt.title('Verteilung Transfereffizienz Leiterplatte 1373')
sns.distplot(PCB_1373['Volume (%)'],color='limegreen')
plt.xlabel('Transfereffizienz(%)')

plt.subplot(2,3,4)
plt.title('Verteilung Transfereffizienz Leiterplatte 1470')
sns.distplot(PCB_1470['Volume (%)'],color='limegreen')
plt.xlabel('Transfereffizienz(%)')

plt.subplot(2,3,5)
plt.title('Verteilung Transfereffizienz Leiterplatte 1396')
sns.distplot(PCB_1396['Volume (%)'],color='limegreen')
plt.xlabel('Transfereffizienz(%)')

plt.subplot(2,3,6)
plt.title('Verteilung Transfereffizienz Leiterplatte 1368')
sns.distplot(PCB_1368['Volume (%)'],color='limegreen')
plt.xlabel('Transfereffizienz(%)')

plt.savefig('png/PCB_1375_1471_1373_1470_1396_1368.png',dpi=300)
plt.savefig('svg/PCB_1375_1471_1373_1470_1396_1368.svg',dpi=300)




# klein 20 Pads
plt.figure(figsize=(11,11))

'''
Pad_30557 = Versuch_2909[Versuch_2909['Pad ID']==30557]
Pad_30827 = Versuch_2909[Versuch_2909['Pad ID']==30827]
Pad_34118 = Versuch_2909[Versuch_2909['Pad ID']==34118]

'''

x = np.arange(145,1,-1)

plt.title('Vergleich zwischen Pads 30557,30827,34118',fontsize=15)

plt.scatter(x,Pad_30557['Volume (%)'],label='Pad 30557')
plt.scatter(x,Pad_30827['Volume (%)'],label='Pad 30827')
plt.scatter(x,Pad_34118['Volume (%)'],label='Pad 34118')

plt.xlabel('Druckreihenfolge',fontsize=13)
plt.ylabel('Transfereffizienz(%)',fontsize=13)

plt.legend(fontsize=13)

plt.savefig('png/Pads_30557_30827_34118.png',dpi=300)
plt.savefig('svg/Pads_30557_30827_34118.svg',dpi=300)



# gross 225 Pads
plt.figure(figsize=(11,11))


Pad_220544 = df[df['Pad ID']==220356]
Pad_220496 = df[df['Pad ID']==6032]
Pad_5868 = df[Versuch_2909['Pad ID']==6036]



x = np.arange(145,1,-1)

plt.title('Vergleich zwischen Pads 220356,6032,6036',fontsize=15)

plt.scatter(x,Pad_220356['Volume (%)'],label='Pad 220356')
plt.scatter(x,Pad_6032['Volume (%)'],label='Pad 6032')
plt.scatter(x,Pad_6036['Volume (%)'],label='Pad 6036')

plt.xlabel('Druckreihenfolge',fontsize=13)
plt.ylabel('Transfereffizienz(%)',fontsize=13)

plt.legend(fontsize=13)

plt.savefig('png/Pads_220356_6032_6036.png',dpi=300)
plt.savefig('svg/Pads_220356_6032_6036.svg',dpi=300)



## print before and after preprocessing

plt.figure(figsize=(13,7))

plt.subplot(1,2,1)
x1 = np.arange(1037953,1,-1)

plt.title('Vor dem Data-Preprocessing')


plt.plot(x1,Versuch_2909['Volume (%)'],color='limegreen',label='Transfereffizienz(%)')

plt.xlabel('Nummer der Pads', fontsize=13)
plt.ylabel('Transfereffizienz(%)', fontsize=13)

plt.subplot(1,2,2)
#x2 = np.arange(907586,1,-1)

plt.title('Nach dem Data-Preprocessing')


plt.plot(Versuch_2909_preprocessing['Volume (%)'],color='limegreen',label='Transfereffizienz(%)')

plt.xlabel('Nummer der Pads', fontsize=13)
plt.ylabel('Transfereffizienz(%)', fontsize=13)


plt.legend()


plt.savefig('png/QRK_vor_nach_preprocessing.png',dpi=200)
plt.savefig('svg/QRK_vor_nach_preprocessing.svg',dpi=200)
