#Program that take the output of a TALYS file and finds the compound contribution for relevant states before outputting toa  text file
#Input: talys_output_file.txt

#Output: "talys_outputs_ex_energy_talys.dat"


import matplotlib
import matplotlib.pyplot as plt
import math



def main():
    # ex_energy_list = ["9.559", "10.349"]
    # ex_energy_list = ["0.00", "1.809", "2.938", "3.588", "3.942", "4.319", "4.333",\
    # 	"4.350", "4.835", "4.901",	"4.972", "5.292", "5.474", "5.691", "5.716", "6.125",\
    #     "6.256", "6.623", "6.745", "6.876", "6.978", "7.061", "7.100", "7.261", "7.283", "7.349"]
    ex_energy_list = ["9.111", "9.169", "9.20600", "9.239", "9.261", "9.428", "9.714", "9.857", "10.040", "10.1025"]

    counter = 0 # integer for iterating through list
    # for i in ex_energy_list:
    for i in range (0,9): #Iterating over list of energy levels
        ex_energy = float(ex_energy_list[counter])

        print("excitation energy is {}".format(ex_energy))

        # talys_in = open("talys_output_shortened","r")
        talys_in = open("nashville_test_3.txt","r")
        talys_input = talys_in.readlines()
        even_talys_cross_sections = []
        even_talys_angles = []
        talys_cross_sections = []
        talys_angles = []


        energy_level_flag = 0
        energy_level_found_flag = 0
        angular_distributions_flag = 0
        level_ang_flag = 0
        energy_level_list_flag = 0
        new_counter = 0

        for line in talys_input:
            if ("   (d,p)   cross sections:" in line): #start of exc list
                print(line)
                energy_level_flag = 1
                print("energy level section found")

            if (" Discrete    (d,p)  :" in line): #end of exc list
                print(line)
                energy_level_flag = 0
                print("end of energy level section found")

            if (energy_level_flag == 1): #searching through list of energies
                # print(line)
                token = line.split(" ")
                token = filter(None,token)
                if(len(token) > 7 and token[1]!='Energy'):
                    energy_level_list_flag = 1
                    # print(token)
                if len(token) > 7 and token[1]!='Energy':
                    current_exc = round(float(token[1]),3) #rounding to 3 decimal places
                    # print("current exc is {}".format(current_exc))
                    # print("energy_level_flag {} , energy_level_list_flag {} , ex_energy_list[counter] {} , current_exc {} ".format(\
                    # energy_level_flag, energy_level_list_flag, ex_energy_list[counter], current_exc))
                    if(ex_energy == current_exc):
                        print("match! \n level of energy {} is {} \n\n\n".format(ex_energy,token[0]))
                        level_number = token[0]
                        energy_level_found_flag = 1

            if ("(d,p) angular distributions" in  line and energy_level_found_flag == 0):
                print("No energy level found")
                break

            if ("(d,p) angular distributions" in  line): #start of (d,p) angular cross-sections
                print(line)
                level_string = "Level  " + level_number + " "
                print("d,p angular distributions found, now searching for ''{}''".format(level_string))
                angular_distributions_flag = 1

            if (level_ang_flag == 1 and "180.0" in line):
                print("Reached angle 180.0 in angular distribution for {}, so level ang flag turned off".format(level_string))
                level_ang_flag = 0


            if(angular_distributions_flag == 1): #Level in angular distributions
                # print(new_counter)
                new_counter = new_counter + 1
                token = line.split(" ")
                token = filter(None,token)
                if(len(token) == 2):
                    token[-1] = token[-1].strip()
                    # print(token)
                    if(level_number == token[1]):
                        print("match for level {} found, now dissecting lines for angle and xs".format(level_number))
                        level_ang_flag = 1
                        angular_distributions_flag = 0

            if level_ang_flag == 1: #dissecting line to get out cross sections
                # print("dissecting line")
                token = line.split(" ")
                # print(len(token))
                token = filter(None,token)
                if len(token) > 3 and token[0]!="Angle":
                    # print(len(token))
                    # print(token[10])
                    # print(token)
                    # print(token[0])
                    # print(token[2])

                    # talys_angles.append(float(token[0])-1)
                    even_talys_angles.append(float(token[0]))
                    even_talys_cross_sections.append(float(token[3])*1.0) #compound cross section is 4th component
                    # talys_cross_sections.append(float(token[3])/6.076)
                # cs = token[10]
                # print(cs    )


        for m in range(0,88):
            angle_value = even_talys_angles[m] + 1.0
            cs_value_1 = even_talys_cross_sections[m]
            cs_value_2 = even_talys_cross_sections[m+1]
            cs_value = (cs_value_1+cs_value_2)/2.0
            # print(cs_value_1,cs_value_2,cs_value)
            talys_angles.append(even_talys_angles[m])
            talys_angles.append(angle_value)
            talys_cross_sections.append(even_talys_cross_sections[m])
            talys_cross_sections.append(cs_value)

            # print(angle_value,cs_value)


        print("loop ended")
        plt.plot(talys_angles, talys_cross_sections)
        plt.xlim(0,180)
        plt.ylim(0,1.0)
	plt.xlabel('angle/degrees')
	plt.ylabel('cross section [mb/sr]')
        plt.grid()
	plt.show()

        output_filename = "talys_outputs/" + str(ex_energy) + "_talys.dat"
        print(output_filename)
	fileout = open(output_filename,"w")
        for m in range (0,len(talys_angles)):
            fileout.write("{}\t{}\n".format(talys_angles[m],talys_cross_sections[m]))
        fileout.close()

        # print(talys_angles,talys_cross_sections)
        # del talys_cross_sections[0:90]
        talys_in.close()
        counter = counter + 1
        print("End of loop for energy level {} \n\n\n\n".format(ex_energy))
main()
