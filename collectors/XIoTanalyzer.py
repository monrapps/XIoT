#!/usr/bin/env python
import sys
from os import listdir
from os.path import isdir, join
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from cycler import cycler  

"""

exemplo para executar o script
python ./collector_Python36.py <Path_of_Result> <Path_To_Save_Results>

"""

def convertNumbers(dataframe):
     dataframe['cpu'] = dataframe['cpu'].str.replace('%','')
     dataframe['cpu'] = dataframe['cpu'].astype(float)
     dataframe['net I'] = dataframe['net I'].str.replace('k','000')
     dataframe['net I'] = dataframe['net I'].str.replace('M','000000')
     dataframe['net I'] = dataframe['net I'].str.replace('B','')
     dataframe['net I'] = dataframe['net I'].str.replace('.','')
     dataframe['net I'] = dataframe['net I'].astype(float)
     dataframe['net O'] = dataframe['net O'].str.replace('k','000')
     dataframe['net O'] = dataframe['net O'].str.replace('M','000000')
     dataframe['net O'] = dataframe['net O'].str.replace('B','')
     dataframe['net O'] = dataframe['net O'].str.replace('.','')
     dataframe['net O'] = dataframe['net O'].astype(float)
     dataframe['time'] = dataframe['time'].astype(float)

     return dataframe

# def plotCPUGraph(item, dir, dataframe):
#     #print('plotting CPU graph ' + item)
#     fig  = plt.figure() 
#     ax0 = fig.add_subplot(111)
    

#     Time = np.array(dataframe['time'])
#     CPU = []

#     for index, row in dataframe.iterrows():
#         CPU.append(row['cpu'])
#     CPU = np.array(CPU)
#     ax0.plot(Time, CPU)
#     #ax0.errorbar(inputSamples, input3FIXP, yerr = input3FIXPIC, label='3 FIXPs Switches', fmt='o')

#     ax0.set_xlabel('Time', loc = 'center')
#     ax0.set_ylabel('CPU', loc = 'center')
#     #ax0.set_xlim(0,1400)
#     #ax0.set_ylim(160,260)
#     ax0.set_box_aspect(1)
#     ax0.grid(True,linestyle='-.')



#     #fig.tight_layout()
#     #legend = ax0.legend(loc = 'lower left', shadow=True, fontsize=10)

#     fig.savefig(dir+item+' CPU.png', format='png')
#     plt.close(fig) 
#     del fig
#     plt.clf()
    

# def plotThroughput(item, dir, dataframe):
#     #print('plotting throughput ' + item)
#     fig, (ax1,ax2) = plt.subplots(2)

#     Time = np.array(dataframe['time'])
#     Input = []
#     Output = []
#     for index, row in dataframe.iterrows():
#         #print(row['time'])
#         #print(row['net I'])
#         #print(row['net O'])
#         #print('Resultado I: ' + str(row['net I']/row['time']))
#         #print('Resultado O: ' + str(row['net O']/row['time']))
        
#     Input = np.array(Input)
#     Output = np.array(Output)

#     ax1.plot(Time, Input, label='Input')
#     ax2.plot(Time, Output, label='Output')
#     #ax1.set_ylim(0,600)
#     #ax2.set_ylim(0,600)
#     #ax0.errorbar(inputSamples, input3FIXP, yerr = input3FIXPIC, label='3 FIXPs Switches', fmt='o')

#     ax1.set_xlabel('Time', loc = 'center')
#     ax1.set_ylabel('Input Throughput', loc = 'center')
#     ax2.set_ylabel('Output Throughput', loc = 'center')
#     #ax0.set_xlim(0,1400)
#     #ax0.set_ylim(160,260)
#     ax1.set_box_aspect(1)
#     ax1.grid(True,linestyle='-.')
#     ax2.set_box_aspect(1)
#     ax2.grid(True,linestyle='-.')


#     #fig.tight_layout()
#     legend = ax1.legend(loc = 'upper right', shadow=True, fontsize=10)
#     legend = ax2.legend(loc = 'upper right', shadow=True, fontsize=10)

#     fig.savefig(dir+item+' Throughput.png', format='png')
#     plt.close(fig) #where f is the figure
#     del fig
#     plt.clf()
    

def plotGraphs(item, dir, dataframe):
    #print('plotting throughput ' + item)
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig1  = plt.figure() 
    ax0 = fig1.add_subplot(111)

    Time = np.array(dataframe['time'])
    InputTraffic = []
    OutputTraffic = []
    InputThroughput = []
    OutputThroughput = []
    CPU = []

    for index, row in dataframe.iterrows():
        #print(row['time'])
        #print(row['net I'])
        #print(row['net O'])
        #print('Resultado I: ' + str(row['net I']/row['time']))
        #print('Resultado O: ' + str(row['net O']/row['time']))
        InputTraffic.append((row['net I'])/8.0)
        OutputTraffic.append((row['net O'])/8.0)
        InputThroughput.append((row['net I']/row['time'])/8.0)
        OutputThroughput.append((row['net O']/row['time'])/8.0)
        CPU.append(row['cpu'])
    
    InputTraffic = np.array(InputTraffic)
    OutputTraffic = np.array(OutputTraffic)
    InputThroughput = np.array(InputThroughput)
    OutputThroughput = np.array(OutputThroughput)
    CPU = np.array(CPU)
    

    ax1.plot(Time, InputTraffic, label='InputTraffic')
    ax2.plot(Time, OutputTraffic, label='OutputTraffic')
    ax3.plot(Time, InputThroughput, label='InputThroughput')
    ax4.plot(Time, OutputThroughput, label='OutputThroughput')
    ax0.plot(Time, CPU, label='CPU')
    #ax0.errorbar(inputSamples, input3FIXP, yerr = input3FIXPIC, label='3 FIXPs Switches', fmt='o')

    #ax0.set_xlim(0,1400)
    #ax0.set_ylim(160,260)
    
    #ax1.set_ylim(0,600)
    #ax2.set_ylim(0,600)
    #ax0.errorbar(inputSamples, input3FIXP, yerr = input3FIXPIC, label='3 FIXPs Switches', fmt='o')

    ax1.set_xlabel('Time', loc = 'center')
    ax1.set_ylabel('Input Traffic', loc = 'center')
    ax2.set_xlabel('Time', loc = 'center')
    ax2.set_ylabel('Output Traffic', loc = 'center')
    ax3.set_xlabel('Time', loc = 'center')
    ax3.set_ylabel('Input Throughput', loc = 'center')
    ax4.set_xlabel('Time', loc = 'center')
    ax4.set_ylabel('Output Throughput', loc = 'center')
    ax0.set_xlabel('Time', loc = 'center')
    ax0.set_ylabel('CPU', loc = 'center')
   
    #ax0.set_xlim(0,1400)
    #ax0.set_ylim(160,260)
    ax1.set_box_aspect(1)
    ax1.grid(True,linestyle='-.')
    ax2.set_box_aspect(1)
    ax2.grid(True,linestyle='-.')
    ax3.set_box_aspect(1)
    ax3.grid(True,linestyle='-.')
    ax4.set_box_aspect(1)
    ax4.grid(True,linestyle='-.')
    ax0.set_box_aspect(1)
    ax0.grid(True,linestyle='-.')

    #fig.tight_layout()
    legend = ax1.legend(loc = 'best', shadow=True, fontsize=10)
    legend = ax2.legend(loc = 'best', shadow=True, fontsize=10)
    legend = ax3.legend(loc = 'best', shadow=True, fontsize=10)
    legend = ax4.legend(loc = 'best', shadow=True, fontsize=10)
    legend = ax0.legend(loc= 'best', shadow=True, fontsize=10)

    fig.savefig(dir+item+' Network.png', format='png')
    fig1.savefig(dir+item+' CPU.png', format='png')
    plt.close(fig) #where f is the figure
    del fig
    plt.close(fig1) #where f is the figure
    del fig1
    plt.clf()
    

def main(dir):
 with open(dir+'running-stats.csv') as f:
     data = f.read().replace('/',';')

 #print(data)
 with open(dir+'newfile.csv', 'w') as f:
    f.write(data)

 try:
     df = pd.read_csv(dir+'newfile.csv',sep=";", engine='python', header=None, names=['component', 'cpu', 'ram', 'ram I', 'ram O', 'ram avg','net I', 'net O', 'disk I', 'disk O', 'time', 'cpu avg'])
 except:
    print('there is no running-stats.csv')
    return None
 #print(df)

 df = convertNumbers(df)

 df = df.sort_values(by=['component', 'time'])
 grouped = df.groupby(df['component'])
 #print(df)
 #print(df['component'].unique())

 for item in df['component'].unique():
     #print(item)
     groupDataFrame = grouped.get_group(item)
     #print(groupDataFrame)
     print('plotting graphs for '+ item)
     plotGraphs(item, dir, groupDataFrame)
     #plotThroughput(item, dir, groupDataFrame)

     

if __name__ == "__main__":
    if(len(sys.argv) > 1):
        DIR = sys.argv[1]
        main(DIR)
        #if Architecture == 'IPv6':
        #    mainIPv6(DIR)
        #elif Architecture == 'XIAIPv6':
        #    mainXIAIPv6(DIR)

    else:
        print("Invalid number of input parameters: <path_to_analyze>")
    