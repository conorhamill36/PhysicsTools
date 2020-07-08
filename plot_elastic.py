#program takes main output data from fresco, plots first reaction in output (used for elastic reactions)

import sys
import matplotlib.pyplot as plt
import math


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

angle_list=[]
cross_section_list=[]

ruth_angle_list=[]
ruth_cross_section_list=[]

ratio_angle_list=[]
ratio_cross_section_list=[]

def main():
    filename=sys.argv[1] #takes in command line argument as input file in " "
    # D=2.157*pow(10,-15) #25Mg
    D=1.420 * pow(10,-14) #197Au

    for angle in range(1,181):
        ruth_angle_list.append(angle)
        angle=math.radians(angle)
        ruth_cross_section=(D*D)/(16*math.pow( (math.sin(angle/2.0)), 4))
        ruth_cross_section=ruth_cross_section*pow(10,28)
        ruth_cross_section=ruth_cross_section*1000
        ruth_cross_section_list.append(ruth_cross_section)

    print(ruth_angle_list[29])
    print(ruth_cross_section_list[29])

    print(ruth_angle_list[30])
    print(ruth_cross_section_list[30])


    output_filename = filename[:-3] + 'dat'
    # print(output_filename)
    filein = open(filename,"r")
    fileout = open(output_filename,"w")
    input_data = filein.readlines()    # Read in whole file

    data_flag=0

    for line in input_data: #reading in data loop begins



        if line.startswith(" Finished all xsecs"):
            data_flag=0
            print("Cross-section data reached, data flag set to 0")
            # print(line)
            print("End of one reaction reached")


            for i in range(1,180):
                ratio=(cross_section_list[i])/(ruth_cross_section_list[i])
                ratio_cross_section_list.append(ratio)
                print(ratio)

            ratio_cross_section_list.append(ratio) #bluffing the ratio lists so can plot

            # plt.plot(angle_list,cross_section_list)
            # plt.plot(ruth_angle_list,ruth_cross_section_list)
            print(ruth_angle_list[29])
            print(cross_section_list[29])
            print(ruth_cross_section_list[29])

            plt.plot(ratio_angle_list,ratio_cross_section_list)
            plt.xlim(0,180)
            plt.ylim(0,2.0)
            plt.ylabel('cross section [mb/sr]')
            plt.xlabel('angle/degrees')
            ax = plt.subplot()
            # ax.set_yscale('log')
            plt.grid()
            angle_list[:]=[]
            cross_section_list[:]=[]#resetting arrays to be empty
            plt.show()


        if data_flag==1:
            # print(line)
            token=line.split(" ")
            token=filter(None,token)

            # print(token)
            if hasNumbers(token[0]): #checking if first element actually contains a number, to avoid conversion error

                token[0]=float(token[0])
                token[4]=float(token[4])
                fileout.write("{}\t{}\n".format(token[0],token[4]))
                angle_list.append(token[0])
                cross_section_list.append(token[4])
                ratio_angle_list.append(token[0])





        if line.startswith (" CROSS SECTIONS FOR OUTGOING 2H "):
            data_flag=1
            print("Cross-section data reached, data flag set to 1")
            # print(line)





    filein.close()         # Good practice
    fileout.close()





main()
