# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 10:03:21 2020

@author: Gianl
"""


from scipy.optimize import curve_fit
import numpy as np
import argparse
import pandas as pd
import Plot
import os
#Define the data to be fit with some noise:

def func_ale (x, wn_x, wn_y, eta_x, eta_y, k_x, k_y):

    #la funzione è ok
    return np.sqrt(((1-(x/wn_x)**2)/(((1-(x/wn_x)**2)**2+eta_x**2)*k_x)+(-eta_y/(((1-(x/wn_y)**2)**2+eta_y**2)*k_y)))**2+((-eta_x/(((1-(x/wn_x)**2)**2+eta_x**2)*k_x))+(-(1-(x/wn_y)**2)/(((1-(x/wn_y)**2)**2+eta_y**2)*k_y)))**2)

def set_p0_rule(x_value, parameters,tolerance):
    #usare x_data per settarli
    wn_x = np.max(x_value) - tolerance/100*np.max(x_value)
    wn_y = np.max(x_value) + tolerance/100*np.max(x_value)
    Eta_x = parameters[0]
    Eta_y = parameters[1]
    K_x = parameters[2]
    K_y = parameters[3]
    return np.array([wn_x, wn_y, Eta_x, Eta_y, K_x, K_y], dtype = float)

def main(directory_p, parameters, tolerance):
    element = os.listdir(directory_p) #guardo tutti gli elementi nella directory
    #DA COMPLETARE LA RICERCA DEI FILE CSV OCCHIO ALLA VARIABILE I IN SAVEFIG
    #IMPLEMENTARE ANCHE IL SETTAGGIO DEI PARAMETRI INIZIALI
    for i in element:
        if i.split(".")[1] == "xls": #seleziono il primo file .csv
            folder_picture = os.path.join(directory_p,i.split(".")[1])
            os.mkdir(folder_picture)
            df = pd.read_excel(r"{}/{}".format(directory_p,i), encoding = "utf-8", header = 0)
            column = df.columns
            col = 1
            x_data = df.filter(regex="Frequenza")
            y_data = df.filter(regex="Ampiezza")
            for x,y in zip(x_data, y_data):
                x_value = x_data[x].dropna()
                y_value = y_data[y].dropna()
                p0 = set_p0_rule(x_value, parameters, tolerance) #IMPOSTARE BENE!!
                try:
                    popt, pcov = curve_fit(func_ale, x_value, y_value, p0, method='lm', maxfev = 2000)
                    Plot.draw(x_value, y_value, func_ale, "fit curve vs normal points", folder_picture + str(col)+".png", popt) #libreria nostra!
                except:
                    print ("{}, {} non converge".format(x,y))
                    pass
                col += 1

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument ("-d", "--directory", help = "Directory of .csv file", required = True)
    parser.add_argument ("-p", "--parameters", nargs = 4 ,help = "values of: Eta_x, Eta_y, K_x, K_y", required = True, type = float)
    parser.add_argument ("-t", "--tolerance", help = "% tolerance for wn_x and wn_y", required = False, default = 5, \
    type = float)
    args = parser.parse_args()
    directory_p = args.directory
    print ("{} {} {}".format(directory_p, args.parameters, args.tolerance))
    main(directory_p, args.parameters, args.tolerance)
