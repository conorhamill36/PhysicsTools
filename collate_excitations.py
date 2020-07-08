#Reads in all energy levels from all_levels.ods, finds out which energy source has the lowest uncertainty, then saves that energy and associated uncertainty
#Inputs:
#    all_levels.txt
#Outputs:
#   collated_states.txt

def main():
  print("Hello world")
  all_states_input_file = open("all_levels.txt")
  all_states_input = all_states_input_file.readlines()

  exc_array = []
  exc_uncert_array = []
  collated_exc_array = []
  collated_j_pi_array = []
  collated_uncert_array = []

  #Setting up array to link index number with authors
  author_name_array = ["Ota", "Jayatissa", "Hunt", "Lotay","Adsley","Massimi","Adsley_2017","Basunia","Talwar(alpha,alpha')","Talwar(6Li,d)"]
  counter = 0
  for line in all_states_input:
     counter = counter + 1
     # if(counter == 14):
     #     print("number 13")
     # else:
     #     continue
     print(line)
     token = line.split("\t")
     print(token)
     print(len(token)) #length is consistently 36 elements
     j_pi = token[-1]
     print("J pi is: {}".format(j_pi))

	 #Picking out recommended Jpi

	 #Ota (2020)
     if(token[1] != "" and token[3] != ""):
        print("For energy number {}, Ota energy value is {}, with an uncertainty of {}".format(token[0], token[1], token[3]))
        hunt_exc = float(token[1])
        hunt_exc_uncert = float(token[3])
        exc_array.append(float(token[1]))
        exc_uncert_array.append(float(token[1]))
     else:
        exc_array.append(0)
        exc_uncert_array.append(0)

	 #Jayatissa (2020)
     if(token[4] != "" and token[6] != ""):
        print("For energy number {}, Jayatissa energy value is {}, with an uncertainty of {}".format(token[0], token[4], token[6]))
        jayatissa_exc = float(token[4])
        jayatissa_exc_uncert = float(token[6])
        exc_array.append(float(token[4]))
        exc_uncert_array.append(float(token[4]))
     else:
        exc_array.append(0)
        exc_uncert_array.append(0)

	 #Hunt (2020)
     if(token[4] != "" and token[6] != ""):
        print("For energy number {}, hunt energy value is {}, with an uncertainty of {}".format(token[0], token[4], token[6]))
        hunt_exc = float(token[4])
        hunt_exc_uncert = float(token[6])
        exc_array.append(float(token[4]))
        exc_uncert_array.append(float(token[4]))
     else:
        exc_array.append(0)
        exc_uncert_array.append(0)




     #Lotay(2019)
     if(token[10] != "" and token[12] != ""):
        print("For energy number {}, Lotay energy value is {}, with an uncertainty of {}".format(token[0], token[10], token[12]))
        lotay_exc = float(token[10])
        lotay_exc_uncert = float(token[12])
        exc_array.append(float(token[10]))
        exc_uncert_array.append(float(token[12]))
     else:
        exc_array.append(0)
        exc_uncert_array.append(0)


     #Adsley(2018)
     if(token[13] != "" and token[15] != ""):
        print("For energy number {}, Adsley energy value is {}, with an uncertainty of {}".format(token[0], token[13], token[15]))
        adsley_exc = float(token[13])
        adsley_exc_uncert = float(token[15])
        exc_array.append(float(token[13]))
        exc_uncert_array.append(float(token[15]))
     else:
        exc_array.append(0)
        exc_uncert_array.append(0)

     #Massimi(2017/2012)
     if(token[16] != "" and token[18] != ""):
        print("For energy number {}, Massimi energy value is {}, with an uncertainty of {}".format(token[0], token[16], token[18]))
        massimi_exc = float(token[16])
        massimi_exc_uncert = float(token[18])
        exc_array.append(float(token[16]))
        exc_uncert_array.append(float(token[18]))
     else:
        exc_array.append(0)
        exc_uncert_array.append(0)

     #Adsley (2017)
     if(token[21] != "" and token[23] != ""):
        print("For energy number {}, adsley_2017 energy value is {}, with an uncertainty of {}".format(token[0], token[21], token[23]))
        adsley_2017_exc = float(token[21])
        adsley_2017_exc_uncert = float(token[23])
        exc_array.append(float(token[21]))
        exc_uncert_array.append(float(token[23]))
     else:
        exc_array.append(0)
        exc_uncert_array.append(0)


     #Basunia (2016)
     if(token[24] != "" and token[26] != ""):
        print("For energy number {}, basunia 2016 energy value is {}, with an uncertainty of {}".format(token[0], token[24], token[26]))
        basunia_exc = float(token[24])
        basunia_exc_uncert = float(token[26])
        exc_array.append(float(token[24]))
        exc_uncert_array.append(float(token[26]))
     else:
        exc_array.append(0)
        exc_uncert_array.append(0)

     #Talwar (alpha,alpha)
     if(token[27] != "" and token[29] != ""):
        print("For energy number {}, Talwar(alpha,alpha') energy value is {}, with an uncertainty of {}".format(token[0], token[27], token[29]))
        talwar_alpha_exc = float(token[27])
        talwar_alpha_exc_uncert = float(token[29])
        exc_array.append(float(token[27]))
        exc_uncert_array.append(float(token[29]))
     else:
        exc_array.append(0)
        exc_uncert_array.append(0)

     #Talwar (6Li,d)
     if(token[30] != "" and token[32] != ""):
        print("For energy number {}, Talwar (6Li,d) energy value is {}, with an uncertainty of {}".format(token[0], token[30], token[32]))
        talwar_li_exc = float(token[30])
        talwar_li_exc_uncert = float(token[32])
        exc_array.append(float(token[30]))
        exc_uncert_array.append(float(token[32]))
     else:
        exc_array.append(0)
        exc_uncert_array.append(0)








     print(exc_array)
     print(j_pi)
     print(exc_uncert_array)
     #Resetting array to be empty

     #Checking which study has the most accurate value
     lowest_uncert = 1000 # high value to start off search
     lowest_uncert_energy = 0.0
     lowest_uncert_index = 1000
     for i in range(0,len(exc_uncert_array)):
         temp_uncert = exc_uncert_array[i]
         print("temp uncert is {}".format(temp_uncert))
         if (temp_uncert != 0 and temp_uncert < lowest_uncert):
             lowest_uncert = temp_uncert
             lowest_uncert_index = i
             lowest_uncert_energy = exc_array[i]
             # print("Lowest uncert for energy level number {} is now {}, with a value of {}, and an index of {}".format(token[0], lowest_uncert, lowest_uncert_energy, i))

     #if(counter == 11):
	 #	 break
	 #Printing out result of search
     # print("Lowest uncert index is {}".format(lowest_uncert_index))
     if(lowest_uncert_index < 10):
		 print("For energy level number {}, the energy level value is {}, with an uncertainty of {}, from {}".format(token[0], lowest_uncert_energy, lowest_uncert, author_name_array[lowest_uncert_index]))
	 #Adding excitation energies on to the collated lists

     collated_exc_array.append(lowest_uncert_energy)
     collated_j_pi_array.append(j_pi)

     collated_uncert_array.append(lowest_uncert)
     del exc_array[:]
     del exc_uncert_array[:]
  all_states_input_file.close()


  collated_states_output_file = open("collated_states.txt","w")
  for i in range (0,len(collated_exc_array)):
       print("{} Ex: {}+-{}, Jpi: {}".format(i, collated_exc_array[i], collated_uncert_array[i],collated_j_pi_array[i]))
       collated_states_output_file.write("{}\t{}\t{}\t{}\n".format(i, collated_exc_array[i], collated_uncert_array[i], collated_j_pi_array[i]))
  #collated_states_output_file.close()


  #Checking that states plus uncertainties don't overlap
  for i in range (0,len(collated_exc_array) - 1):
      if( (collated_exc_array[i] + collated_uncert_array[i]) > (collated_exc_array[i+1] - collated_uncert_array[i+1]) ):
          print("Overlap at number {}, with energy(+-uncert) of {} {} overlapping with energy(+-uncert) {} {} ".format(i, collated_exc_array[i], collated_uncert_array[i], collated_exc_array[i+1], collated_uncert_array[i+1]))


main()
