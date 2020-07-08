#Program to parse an NNDC HTML for a certain isotope to extract excitation energies and Jpi assignments

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import webbrowser
import os

import matplotlib.pyplot as plt


def plot_ex_levels_func(plot_list, ex_list): #Function to plot excited states
    plt.plot(plot_list, ex_list, '_', markersize = 200)
    plt.xlabel(' ')
    plt.ylabel('Ex [keV]')
    plt.show()



def main():

    #Defining lists
    ex_list = []
    ex_uncert_list = []
    plot_list = []



    print("hello world")
    print("What isotope do you want?")
    isotope = input()
    isotope = isotope.upper()
    #Change so can do lower case/numbers wrong way round
    # isotope = '13C'


    #Getting webpage
    driver = webdriver.Chrome
    URL = 'https://www.nndc.bnl.gov/nudat2/getdataset.jsp?nucleus=' + isotope + '&unc=nds'
    # URL = 'https://www.nndc.bnl.gov/nudat2/getdataset.jsp?nucleus=36CL&unc=nds'
    # URL = 'https://www.nndc.bnl.gov/nudat2/getdataset.jsp?nucleus=26MG&unc=nds'
    page = requests.get(URL)
    #Checking page has opened correctly
    if(page.status_code == 200):
        print("Page status code is 200, so read in correctly")
    else:
        print("Page not found, make sure you've typed in isotope in 26SI format")
        return 0

    #Making BS object
    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup)
    try:
        print(soup.prettify())
    except:
        print("Something seems to have gone wrong with opening the NNDC page \
        for this isotope, try looking at the webpage: {}".format(URL))
        webbrowser.open(URL, new=2)
        return 0
        #Some isotopes not working: 208Pb, 35/36Cl

    # for i in range (0,20):
    #     print(i)
    #     print(list(soup.children)[i])
    #     print("\n")
    #     print(type(list(soup.children)[i]))
    #     print("\n\n\n\n")

    print(len(list(soup.children)))

    #Finds mainTable, which contains level information
    main_table_result = soup.find(id="mainTable")


    # print(main_table_result)
    print(type(main_table_result))

    # print(main_table_result.prettify())



    if main_table_result is None:
        raise Exception('Not sure if this isotope exists. \nMake sure isotope is in format 208PB\n')


    single_level_iterable = main_table_result.find_all('tr')
    single_level_lower = single_level_iterable[1].find('tr')

    # print(single_level_lower)
    # print("\n\n\n\n")
    # print(single_level_lower.find('td', class_="header"))
    # print("\n\n\n\n")
    # single_level_lower = single_level_iterable[14].find('tr')
    # print(single_level_lower.find('td', class_="header"))
    #

    cell_level = single_level_lower.find('td', class_="cell elvl")
    # print(cell_level)
    # print(cell_level.text)
    #Outputting prettified main table for debugging
    output_file = open("NNDC_prettified.txt", "w")
    # output_file.write(single_level_lower.prettify())
    output_file.write(main_table_result.prettify())

    #
    # print(single_level_iterable[14].find('td', class_="cell elvl"))
    # print(single_level_iterable[15].find('td', class_="cell elvl"))
    # print(single_level_iterable[16].find('td', class_="cell elvl"))



    #Iterating over all the energy levels
    for i in range(0, len(single_level_iterable)):
        # print(single_level[i])

        # single_level_lower = single_level_iterable[i].find('tr')
        # if single_level_lower is None:
        #     print("No level found at {}".format(i))
        #     print(single_level_iterable[i].text)
        #     # output_file.write(single_level_iterable[i].text)
        #     continue
        #
        #
        # print(i)
        cell_level = single_level_iterable[i].find('td', class_="cell elvl")
        if cell_level is None:
            print("No level found at {}".format(i))
            continue


        print(type(cell_level))
        print(cell_level.text)

        # single_level_elem = single_level[i].find('td')
        token = cell_level.text.split(" ")
        #
        print(token)
        if(len(token)>0):

            # print(token[0].strip(),"\n", token[1].strip())
            #Adding levels to list

            #Issue with ground level being added to lists!
            token[0] = token[0].strip()
            #NNDC has ? where Ex and Ex uncert aren't definite, so exceptions remove this
            try:
                ex_list.append(float(token[0]))
            except:
                try:
                    token[0] = token[0][:-1] #removes ? at end
                    ex_list.append(float(token[0].strip()))
                except:
                    print("At index {}, ex couldn't be converted in to float".format(i))
                    ex_list.append(0)
            try:
                ex_uncert_list.append(float(token[1].strip()))
            except:
                print("At index {}, ex uncert couldn't be converted in to float".format(i))
                ex_uncert_list.append(0)

            plot_list.append(0.5)


        #Working on finding J pi
        cell_jpi = single_level_lower.find('td', class_="cellc jpi")
        # print(cell_jpi)
        cell_jpi_a = cell_jpi.find('a')
        # print("printing a:")
        # print(type(cell_jpi_a))
        # if(type(cell_jpi_a) != bs4.element.Tag):
        #     print("No Jpi listed")
        # else:
        #     print(cell_jpi_a.text)
        #Shall write exception for .text conversion
        print("\n\n\n\n\n")

    print(ex_list)
    print(ex_uncert_list)
    print(len(ex_list))
    print(len(ex_uncert_list))
    print(len(plot_list))
    print(len(single_level_iterable))


    #Make plot showing energy levels
    plot_ex_levels_func(plot_list, ex_list)

    output_file.close()

    #Checking if directory exists, creating if not

    if(os.path.isdir('NNDC_excited_states')):
        print("Directory already exists")
    else:
        print("Creating directory NNDC_excited_states/")
        os.makedirs("NNDC_excited_states")

    exc_output_file_name ="NNDC_excited_states/" + isotope + "_NNDC_states.txt"
    exc_output_file = open(exc_output_file_name,"w")

    for i in range (0, len(ex_list)):
        # exc_output_file.write("{} {}\n".format(ex_list[i], ex_uncert_list[i]))
        exc_output_file.write("{} ".format(ex_list[i]/1000.0))
    exc_output_file.close()
    print("Files outputted to {}".format(exc_output_file_name))


main()
