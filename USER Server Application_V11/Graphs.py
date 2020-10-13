import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import time

def spider_graph(saq, seq, scq, sdq, svq, u_id, datt, time_accessed = ''):

    t = time_accessed

    df = pd.DataFrame({
    'group': [i for i in range(len(saq))],
    'saq': [i for i in saq],
    'seq': [i for i in seq],
    'scq': [i for i in scq],
    'sdq': [i for i in sdq],
    'svq': [i for i in svq]
    })
    
    
    
    # ------- PART 1: Create background
    
    # number of variable
    categories=list(df)[1:]
    N = len(categories)
    
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)
    
    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories)
    
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([-3.50, -3, -2, -1, 0, 1, 2, 3], ["-3.50","-3","-2","-1", "0","1","2", "3"], color="black", size=7)
    plt.ylim(-3,3)
    
    
    # ------- PART 2: Add plots
    
    # Plot each individual = each line of the data
    # I don't do a loop, because plotting more than 3 groups makes the chart unreadable
    
    # Ind1
    for i in range(len(saq)):
        values=df.loc[i].drop('group').values.flatten().tolist()
        values += values[:1]
        if t == "":
            ax.plot(angles, values, linewidth=1, linestyle='solid')
        else:
            ax.plot(angles, values, linewidth=1, linestyle='solid', label=t[i])
        ax.fill(angles, values, 'b', alpha=0.1)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    if t == "":
        ax.set_title('Average Daily Score of '+str(u_id) + " on "+ str(datt))
    else:
        ax.set_title('Daily Score of ' + str(u_id) + " on "+ str(datt))
    saq = []
    seq = []
    scq = []
    sdq = []
    svq = []
    return ax, str(u_id) + str(datt)#plt.show()
