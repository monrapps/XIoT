#!/usr/bin/env python
import sys
from os import listdir, path, mkdir
from os.path import isdir, join
import pandas as pd
import xlsxwriter

# DIR="/Users/monra/Desktop/Z68X-UD3-B3"
# DIR = "/Users/monra/Desktop/MonRanaonda"
# DIR="/mnt/d/logs/Z68X-UD4-B3"

"""

exemplo para executar o script
sudo ./collector /home/alberti/Desktop/XID2b/

"""


def main(dir, architecture):
    print("Length, Gateways, GatewayRouters, Clients, ClientRouters, TotalDelay, LostPackets, UDPDelay, LostUDPPackets, XIADelay, CPU, TotalTestTime")
    results = pd.DataFrame()
    subdirs = [f for f in listdir(dir)]
    if architecture == 'IPv6':
        subdirs = [f for f in subdirs if f[0] == 'i']
    elif architecture == "XIAIPv6":
        subdirs = [f for f in subdirs if f[0] == 'x']

    for s in subdirs:
        l = s.split(" ")

        # abre cada arquivo e extrai os dados
        # print "#", s
        with open(join(join(dir, s), "clientslog.csv")) as f:
            lines = f.readlines()

            tmean = 0
            okcnt = 0
            tcnt = 0
            ecnt = 0

            for li in lines:
                data = li.split(";")
                tcnt = tcnt + 1
                if data[7][0] != 's':
                    ecnt = ecnt + 1
                else:
                    tmean = tmean + int(data[6])
                    okcnt = okcnt + 1
            f.close()

        # abre cada arquivo e extrai os dados
        # print "#", s

        with open(join(join(DIR, s), "running-stats.csv")) as f:
            lines = f.readlines()

            cpu_tmean = 0
            cpu_tcnt = 0
            cpu_end = int(lines[-1].split(";")[-2])

            for li in lines:
                data = li.split(";")
                cpu_tcnt = cpu_tcnt + 1
                cpu_tmean = cpu_tmean + int(data[-1].split(".")[0])
            f.close()

        if(architecture == 'XIAIPv6'):
            with open(join(join(dir, s), "gatewayslog.csv")) as f:
                lines = f.readlines()

                gw_tmean = 0
                gw_okcnt = 0
                gw_tcnt = 0
                gw_ecnt = 0

                for li in lines:
                    data = li.split(";")
                    gw_tcnt = gw_tcnt + 1
                    if data[6][0] != 's':
                        gw_ecnt = gw_ecnt + 1
                    else:
                        gw_tmean = gw_tmean + int(data[5])
                        gw_okcnt = gw_okcnt + 1
                f.close()


# xia d 30 r 10000 l 8 m 9 g 1 G 1 c 1 C 1
# Length,Gateways,GatewayRouters,Clients,ClientRouters

        if architecture == 'XIAIPv6':
            print(f'{l[6]}, {l[10]}, {l[12]}, {l[14]}, {l[16]}, {tmean/okcnt}, {ecnt*100/tcnt}, {gw_tmean/gw_okcnt}, {gw_ecnt*100/gw_tcnt}, {(tmean/okcnt) - (gw_tmean/gw_okcnt)}, {cpu_tmean/cpu_tcnt}, {cpu_end}')

            results = results.append({'Length': l[6], 'Gateways': l[10], 'GatewayRouters': l[12], 'Clients': l[14], 'ClientRouters': l[16],
                                      'Total Delay': (tmean / okcnt), 'Lost Packets': ecnt*100/tcnt, 'UDPDelay': (gw_tmean/gw_okcnt), 'Lost UDP Packets': (gw_ecnt*100/gw_tcnt),
                                      'XIA Delay': ((tmean/okcnt) - (gw_tmean/gw_okcnt)), 'CPU': cpu_tmean/cpu_tcnt, 'CPU End': cpu_end}, ignore_index=True)
        elif architecture == 'IPv6':
            print(
                f'{l[6]}, {l[10]}, {l[12]}, {l[14]}, {l[16]}, {tmean/okcnt}, {ecnt*100/tcnt}, {cpu_tmean/cpu_tcnt}, {cpu_end}')
            results = results.append({'Length': l[6], 'Gateways': l[10], 'GatewayRouters': l[12], 'Clients': l[14], 'ClientRouters': l[16], 'Latency Mean': tmean /
                                      okcnt, 'Lost Packets': ecnt*100/tcnt, 'CPU': cpu_tmean/cpu_tcnt, 'CPU End': cpu_end}, ignore_index=True)

    if(architecture == 'XIAIPv6'):
        spreadsheetWriter = pd.ExcelWriter(
            './Results/XIAIPv6.xlsx', engine='xlsxwriter')

    elif(architecture == 'IPv6'):
        spreadsheetWriter = pd.ExcelWriter(
            './Results/IPv6Results.xlsx', engine='xlsxwriter')

    results.to_excel(spreadsheetWriter,
                     sheet_name='Filtered Packets', index=False)
    spreadsheetWriter.close()


if __name__ == "__main__":
    if(len(sys.argv) > 2):
        DIR = sys.argv[1]
        Architecture = sys.argv[2]
        if Architecture == 'IPv6' or Architecture == 'XIAIPv6':
            if not path.exists('./Results/'):
                mkdir('./Results/')
                print('Created Results path')
            main(DIR, Architecture)
        else:
            print('Invalid Architecture for now')
        # if Architecture == 'IPv6':
        #    mainIPv6(DIR)
        # elif Architecture == 'XIAIPv6':
        #    mainXIAIPv6(DIR)

    else:
        print("Invalid number of input parameters: <path_to_analyze> <Architecture: IPv6 or XIAIPv6>")
