#!/usr/bin/env python
import sys
from os import listdir, mkdir, path
from os.path import isdir, join
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from cycler import cycler


def plotGraphs(item, dataframe, componentType):
    print('plotting throughput ' + item + ' ' + componentType)
    fig1 = plt.figure()
    ax0 = fig1.add_subplot(111)

    Time = np.array(dataframe['time'])
    OutputTraffic = []
    line = 1
    for index, row in dataframe.iterrows():
        if(row['time'] > 1):
            OutputTraffic.append((8.0*8.0*line)/row['time'])
            line += 1
            # print(8.0*8.0*line)
            # print(row['time'])
        else:
            OutputTraffic.append(0.0)

    OutputTraffic = np.array(OutputTraffic)

    ax0.plot(Time, OutputTraffic, label='Throughput')

    ax0.set_xlabel('Time', loc='center')
    ax0.set_ylabel('Throughput [bits/sec]', loc='center')

    ax0.set_box_aspect(1)
    ax0.grid(True, linestyle='-.')

    # fig.tight_layout()
    legend = ax0.legend(loc='best', shadow=True, fontsize=10)

    fig1.savefig('./Graphs/'+item+componentType +
                 ' Throughput.png', format='png')
    plt.close(fig1)  # where f is the figure
    del fig1
    plt.clf()


def main(dir):
    # Loop through IP folders
    # print(dir)
    subdirs = [f for f in listdir(dir)]
    subdirsIPv6 = [f for f in subdirs if f[0] == 'i']

    # print(len(subdirsIPv6))
    if len(subdirsIPv6) > 0:
        for s in subdirsIPv6:
            # print(s)
            df = pd.DataFrame()
            try:
                df = pd.read_csv(dir+s+'/clientslog.csv', sep=";", engine='python', header=None, names=[
                    'src_client', 'src_clientrouter', 'dst_mote', 'dst_gateway', 'dst_gatrouter', 'time', 'latency', 'status'])
            except:
                print('there is no clientslog.csv')
                return None
            # print(df)
            if len(df) > 0:
                df.loc[df['status'] == 'success']
                df = df.sort_values(by=['time'])
                # print(df)

                print('plotting graphs for ' + s)
                plotGraphs(s, df, 'Client')

    # Loop through XIA folders

    subdirsXIA = [f for f in subdirs if f[0] == 'x']

    if len(subdirsXIA) > 0:
        for s in subdirsXIA:
            print(s)
            dfClient = pd.DataFrame()
            dfGateway = pd.DataFrame()
            try:
                dfClient = pd.read_csv(dir+s+'/clientslog.csv', sep=";", engine='python', header=None, names=[
                    'src_client', 'src_clientrouter', 'dst_mote', 'dst_gateway', 'dst_gatrouter', 'time', 'latency', 'status'])
            except:
                print('there is no clientslog.csv')
                return None

            try:
                dfGateway = pd.read_csv(dir+s+'/gatewayslog.csv', sep=";", engine='python', header=None, names=[
                    'MOTE', 'gateway', 'GATEWAYROUTER', 'REQ', 'time', 'latency', 'status'])
            except:
                print('there is no gatewayslog.csv')
                return None

            print('plotting graphs for ' + s)
            if len(dfClient) > 0:
                dfClient.loc[dfClient['status'] == 'success']
                dfClient = dfClient.sort_values(by=['time'])
                plotGraphs(s, dfClient, 'Client')
            if len(dfGateway) > 0:
                dfGateway.loc[dfGateway['status'] == 'success']
                dfGateway = dfGateway.sort_values(by=['time'])
                plotGraphs(s, dfGateway, 'Gateway')


if __name__ == "__main__":
    if(len(sys.argv) > 1):
        if not path.exists('./Graphs/'):
            mkdir('./Graphs/')
            print('Created Graphs path')
        DIR = sys.argv[1]
        main(DIR)

    else:
        print("Invalid number of input parameters: <path_to_analyze>")
