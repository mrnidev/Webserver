import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import statistics as stat
#from Radar_gr import *
import datetime

start_time = time.time()
data = pd.read_excel('SVQ_data.xlsx')
headers = data.columns
user_ids = data.iloc[:,0]
all_dates = data.iloc[:,1]
mix_date = [d.date() for d in all_dates]
dat_time = pd.to_datetime(all_dates)
time_list = dat_time.dt.time 
only_date = np.unique(mix_date)
id_list = np.unique(user_ids)


E = data.iloc[:, 4]
G = data.iloc[:, 6]
I = data.iloc[:, 8]

R = data.iloc[:, 17]
S = data.iloc[:, 18]
T = data.iloc[:, 19]
U = data.iloc[:, 20]
V = data.iloc[:, 21]
W = data.iloc[:, 22]

AC = data.iloc[:, 28]
AD = data.iloc[:, 29]
AG = data.iloc[:, 32]

AM = data.iloc[:, 38]
AN = data.iloc[:, 39]
AO = data.iloc[:, 40]
AP = data.iloc[:, 41]
AQ = data.iloc[:, 42]
AR = data.iloc[:, 43]


temp = []


""" SAQ Calculation """
for i in range(len(E)):
	if str(E[i]) == 'nan':
		temp.append(1.4)
	else:
		temp.append(E[i])

E_avg = sum(temp)/len(temp)
E_stad = stat.stdev(temp)

G_avg = sum(G)/len(G)
G_stad = stat.stdev(G)

I_avg = sum(I)/len(I)
I_stad = stat.stdev(I)


""" SAQ Calculation"""
K = [(E[i]- E_avg)/E_stad for i in range(len(user_ids))]
L = [(G[i]- G_avg)/G_stad for i in range(len(user_ids))]
M = [(I[i]- I_avg)/I_stad for i in range(len(user_ids))]
P = [(K[i] + L[i] + M[i])/3 for i in range(len(user_ids))]
SAQ = [50 + (P[i]*10) for i in range(len(user_ids))]

""" SEQ Calculation"""
Y = [(R[i]*0.546) + (S[i]*0.403) + (T[i]*0.989) + (U[i]*0.902) + (V[i]*0.932) + (W[i]*0.145) for i in range(len(user_ids))]
Y_avg = sum(Y)/len(Y)
Y_stad = stat.stdev(Y)
AA = [(Y[i] - Y_avg)/Y_stad for i in range(len(user_ids))]
SEQ = [50 + (AA[i] * 10) for i in range(len(user_ids))]

""" SCQ Calculation"""
AE = [AC[i] + AD[i] for i in range(len(user_ids))]
AH = [300 - AG[i] for i in range(len(user_ids))]
AE_avg = sum(AE)/len(AE)
AE_stad = stat.stdev(AE)
AH_avg = sum(AH)/len(AH)
AH_stad = stat.stdev(AH)
AF = [(AE[i]-AE_avg)/AE_stad for i in range(len(user_ids))]
AI = [(AH[i]-AH_avg)/AH_stad for i in range(len(user_ids))]
AK = [(AF[i]+AI[i])/2 for i in range(len(user_ids))]
SCQ = [50 +(10*AK[i]) for i in range(len(user_ids))]


""" SDQ Calculation"""
AM_avg = sum(AM)/len(AM)
AM_stad = stat.stdev(AM)

AN_avg = sum(AN)/len(AN)
AN_stad = stat.stdev(AN)

AO_avg = sum(AO)/len(AO)
AO_stad = stat.stdev(AO)

AP_avg = sum(AP)/len(AP)
AP_stad = stat.stdev(AP)

AQ_avg = sum(AQ)/len(AQ)
AQ_stad = stat.stdev(AQ)

AR_avg = sum(AR)/len(AR)
AR_stad = stat.stdev(AR)

AS = [ AM[i] + AN[i] + AO[i] + AP[i] + AQ[i]+ AR[i]   for i in range(len(user_ids))]
AT = [(AM[i]- AM_avg)/AM_stad for i in range(len(user_ids))]
AU = [(AN[i]- AN_avg)/AN_stad for i in range(len(user_ids))]
AV = [(AO[i]- AO_avg)/AO_stad for i in range(len(user_ids))]
AW = [(AP[i]- AP_avg)- AP_stad for i in range(len(user_ids))]
AX = [(AQ[i]- AQ_avg)/AQ_stad for i in range(len(user_ids))]
AY = [(AR[i]- AR_avg)/AR_stad for i in range(len(user_ids))]

BB = [(AT[i] + AU[i] + AV[i] + AW[i] + AX[i] + AY[i])/6 for i in range(len(user_ids))]
SDQ = [50 + (BB[i] * 10) for i in range(len(user_ids))]
BD = [P[i] + AA[i] + AK[i] + BB[i] for i in range(len(user_ids))]
BE = [BD[i]/4 for i in range(len(user_ids))]

#SAQ_cal = []
#SEQ_cal = []
#SCQ_cal = []
#SDQ_cal = []
#SVQ_cal = []
#time_array = []

def score_measure(idd, d):
	SAQ_cal = []
	SEQ_cal = []
	SCQ_cal = []
	SDQ_cal = []
	SVQ_cal = []
	time_array = []
	for user_id in range(len(user_ids)):
		if user_ids[user_id] == idd and mix_date[user_id]==d:
			SAQ_cal.append((P[user_id]))
			SEQ_cal.append((AA[user_id]))
			SCQ_cal.append((AK[user_id]))
			SDQ_cal.append((BB[user_id]))
			SVQ_cal.append((BE[user_id]))
			time_array.append((time_list[user_id]))
	#avg_saq = [sum(SAQ_cal)/len(SAQ_cal)]
	#avg_seq = [sum(SEQ_cal)/len(SEQ_cal)]
	#avg_scq = [sum(SCQ_cal)/len(SCQ_cal)]
	#avg_sdq = [sum(SDQ_cal)/len(SDQ_cal)]
	#avg_svq = [sum(SVQ_cal)/len(SVQ_cal)]
	#print(len(time_array))
	print(len(SAQ_cal))
	#print(len(avg_seq))
	return SAQ_cal, SEQ_cal, SCQ_cal, SDQ_cal, SVQ_cal, idd, d, time_array

#print(min(P))
#print(min(AA))
#print(min(AK))
#print(min(BB))
#print(min(BE))
#print("*******")
#print(max(P))
#print(max(AA))
#print(max(AK))
#print(max(BB))
#print(max(BE))


#time.sleep(10)

#u_id, datt = score_measure(id_list[2], only_date[1])

#avg_saq = [sum(SAQ_cal)/len(SAQ_cal)]
#avg_seq = [sum(SEQ_cal)/len(SEQ_cal)]
#avg_scq = [sum(SCQ_cal)/len(SCQ_cal)]
#avg_sdq = [sum(SDQ_cal)/len(SDQ_cal)]
#avg_svq = [sum(SVQ_cal)/len(SVQ_cal)]

#print(SAQ_cal)
#print(SEQ_cal)
#print(SCQ_cal)
#print(SDQ_cal)
#print(SVQ_cal)
#time.sleep(10)


#figure = spider_grapth(avg_saq, avg_seq, avg_scq, avg_sdq, avg_svq, u_id, datt)
#plt.show()
#spider_grapth(SAQ_cal, SEQ_cal, SCQ_cal, SDQ_cal, SVQ_cal,  u_id, datt, time_array)






