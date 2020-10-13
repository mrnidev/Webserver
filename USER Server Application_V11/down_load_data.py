import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import statistics as stat
import datetime
from data_gen import gen_clean_data


def data_down_load():

    all_ids, all_dates, Saq, Seq, Scq, Sdq, Svq = gen_clean_data()

    final_score = pd.DataFrame(all_ids)
    final_score['Date'] = all_dates
    final_score['SAQ'] = Saq
    final_score['SEQ'] = Seq
    final_score['SCQ'] = Scq
    final_score['SDQ'] = Sdq
    final_score['SVQ'] = Svq

    final_score.to_csv("Final_score.csv", index=False)
    return 0