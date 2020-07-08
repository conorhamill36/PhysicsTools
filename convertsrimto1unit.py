#program takes SRIM output and converts to units of micrometer and MeV
#C. B. Hamill September 2018


import math
import matplotlib.pyplot as plt
import sys
def unit_conversion_energy(energy,energy_unit): #converts to MeV
    # print(energy)
    # print(energy_unit)
    if energy_unit == "keV":
        energy=energy/1000.0
    # print(energy)
    return energy


def unit_conversion_distance(distance,distance_unit): #converts to micrometer (10^-6)
    # print(distance)
    if distance_unit == "mm":
        distance = distance*1000.0

    if distance_unit == "m": # 10^0
        distance = distance*1000000.0

    if distance_unit == "km":
        distance = distance*1000000000.0

    if distance_unit == "A": #10^-10
        distance = distance/10000.0


    # print (distance)
    return distance


def main():
    #           First prompt for file and open it
    # filename = input("Input file : ")

    #test
    test_string = "     hello"
    test_string.strip()
    # print(test_string.strip())
    # print(type(test_string))




    filename=sys.argv[1] #takes in command line argument as input file in " "
    output_filename = filename[:-3] + 'dat'
    print(output_filename)
    filein = open(filename,"r")
    fileout = open(output_filename,"w")
    input_data = filein.readlines()    # Read in whole file
    data_flag=0
    for line in input_data:
        # print(line)
        # print("data flag value is:")
        # print (data_flag)


        if line.startswith ("-----") :
            # print()
            print("reached end of data")
            break

        if data_flag == 1:
            # line=line.strip()
            token = line.split(" ") # Split on blank space
            #splitting on blank space results in lots of empty arrays that can just be hard coded around
            token=filter(None,token)
            # print(token)

            # print(line)
            # print(token)
            # print(token[1])
            #Each column is broken into an element
            token[0]=float(token[0])
            token[2]=float(token[2])
            token[3]=float(token[3])
            token[4]=float(token[4])
            token[6]=float(token[6])
            token[8]=float(token[8])

            # print(type(token[0]))
            #Functions called to convert to appropriate unit
            token[0]=unit_conversion_energy(token[0],token[1])
            token[4]=unit_conversion_distance(token[4], token[5])
            token[6]=unit_conversion_distance(token[6], token[7])
            token[8]=unit_conversion_distance(token[8], token[9])
            # for i in range(0,10):
                # print (i,token[i]) #for checking
                #convert units to keV
                # print(token[2])
            # print(token)
            # print "value is {}".format(value)
            #Values written to output file
            fileout.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(token[0],token[2],token[3],token[4],token[6],token[8]))

        if line.startswith  ("  --------------"): #Line before data appears
            data_flag = 1
            print("data flag set to 1")

        # print(type(token[0]))
    filein.close()         # Good practice
    fileout.close()
    #SRIM structure: (element number, variable)
    #0 - energy
    #1 - energy units
    #2 - dE/dx Elec - not to be converted
    #3   - dE/dx Nuclear - not to be converted
    #4  - Projected Range
    #5  - Projected Range Units
    #6   -Long Stragg
    #7   -Long Stragg unit
    #8   -Lateral Straggling
    #9   -Lateral Straggling unit

main()
