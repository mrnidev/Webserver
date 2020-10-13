from flask import Flask, render_template, request
import numpy as np
import pandas
#from bokeh.embed import components
import matplotlib.pyplot as plt
import time
from formula_implementation import score_measure
from Graphs import spider_graph

def Data_Ret():
	global users_id, temp_dates
	data = pandas.read_excel('Visualize_users_ID.xlsx')
	headers = data.columns
	ids = data.iloc[:, 0]
	users_id = np.unique(ids)
	date_time = data.iloc[:, 6]
	mix_date = [d.date() for d in date_time]
	temp_dates = np.unique(mix_date)
	return users_id, temp_dates

def index_value(u_index, d_index):
	#print(indx_id)
	#print(dat_id)
	u_id = users_id[u_index]
	d_id = temp_dates[d_index]
	SAQ, SEQ, SCQ, SDQ, SVQ, usr_id, da_id, time_arr = score_measure(u_id, d_id)
	#figure_1 = spider_graph(SAQ, SEQ, SCQ, SDQ, SVQ, usr_id, da_id)
	figure_2, U_Id = spider_graph(SAQ, SEQ, SCQ, SDQ, SVQ, usr_id, da_id, time_arr)
	path_1 = 'static/'+ str(U_Id) + '.png'
	plt.savefig(path_1)
	plt.clf()
	return 0, U_Id


	