#Program that runs fresco for a range of energy levels, changing BE and Ex for 26Mg. Input filename variables and os.system \
#command must be changed whenever changin Jpi or OMP's. fresco_to_ascii_higher.py must also be changed to be used with this program.
#Chanegd to cater for higher energy states
#Inputs: literature_energy_levels/collated_states.txt

import os
import string
import fresco_to_ascii_higher
import subprocess

def main():
  print("hello world")

  ex_list = []
  energy_level_input_file = open("../literature_energy_levels/collated_states.txt")
  energy_level_input_file_input = energy_level_input_file.readlines()

  for line in energy_level_input_file_input:
      # print(line)
      token=line.split("\t")
      # print(token)
      print(float(token[1]))
      ex_list.append(float(token[1])/1000.0) #Converting list from keV to MeV

  energy_level_input_file.close()
  print(ex_list)
  Ex = "7.50" #energy of excited state in MeV
  # BE = 11.093 - Ex #binding energy of 26Mg
  #ex_list = [3.588, 4.972, 6.256, 7.261] #0 + states
  # ex_list = [5.691] #1 + states
  # ex_list = [4.835, 5.292, 6.745, 7.100, 7.371] #2 + states
  # ex_list = [3.942, 4.350, 6.125, 7.246] #3 + states
  # ex_list = [4.319, 4.901, 5.474, 5.716, 6.623] #4 + states
  # ex_list = [6.978] #5+ states
  # ex_list = [7.061] #1 - states
  # ex_list = [7.349] #[6.876]# 7.349] #3 - states
  # ex_list = [7.283] #4 - states

  for i in range(0,len(ex_list)):
      print(Ex)
      Ex=ex_list[i]
      fresco_input_filename = "mg26dp_dwba_3+_bcfec_higher_energy.in"
      new_fresco_input_filename = "mg26dp_dwba_3+_bcfec_higher_energy_temp.in"
      # fresco_input_filename = "mg26dp_dwba_1-_bcfec_higher_energy.in"
      # new_fresco_input_filename = "mg26dp_dwba_1-_bcfec_higher_energy_temp.in"
      print(fresco_input_filename, new_fresco_input_filename)

      fresco_input = open(fresco_input_filename) #cannot be written to so remains unchanged
      new_fresco_input = open(new_fresco_input_filename,"w+")

      #Flags initially set to zero
      Ex_flag = 0
      BE_flag = 0

      #replacing excitation energies and binding energies in fresco file
      for line in fresco_input:
          # print(line)

          token=line.split(" ")
          # print(token)

          if (Ex_flag==1): #finding excitation energy and replacing it
             print(token)
             print(token[2]) #for 0+ states element [2] must be picked
             for j in range (0,len(token)):
                 if "et=" in token[j]:
                     old_Ex = token[j][3:]

             print("Old excitation energy is {} ".format(old_Ex))
             # print(type(old_Ex))
             # print(type(Ex))
             # print(line)
             # line  = string.replace(line,Ex,old_Ex)
             Ex=str(Ex)
             line = line.replace(old_Ex, Ex)
             Ex = float(Ex)
             # print(line)
             # BE = 11.093 - Ex
             # print("Binding energy is {}".format(BE))

          Ex_flag = 0 #flag set to zero so ex energy replacement only happens once


          if(BE_flag == 1): #finding binding energy and replacing it
              # print(token)
              # print(token[3])


              for j in range (0,len(token)):
                  # print(j)
                  temp_string = token[j]
                  # print(temp_string)
                  if "be=" in token[j]:
                      print("BE located")
                      print(token[j])
                      old_BE = token[j][3:]

              # old_BE = token[6][3:]
              BE = 11.093 - Ex #new binding energy is neutron seperation energy of 26Mg less the Ex of state
              if(BE < 0.2):
                  BE = 0.2
                  print("State is weakly bound, so is being artifically bound by {} MeV".format(BE))
              BE = str(BE)
              print("old BE is {}, new BE is {}".format(old_BE, BE))
              print(line)
              line = line.replace(old_BE,BE)
              print(line)

          BE_flag = 0 #flag set to zero so binding energy replacement only happens once

          # if (line.find("copyp=1") == 1):
          #     print("line with excited state found")
          if "copyp=1" in line: #line before line with excitation energy
              print("line with excited state found")
              print(line)
              Ex_flag = 1

          if "kn1=3" in line: #line before line with binding energy
              print("line with binding energy found")
              print(line)
              BE_flag = 1
          new_fresco_input.write(line) #being written to new line



      fresco_input.close()
      new_fresco_input.close()

      os.system("fresco < mg26dp_dwba_3+_bcfec_higher_energy_temp.in > new_test.dat") #new fresco output ran
      # os.system("fresco < mg26dp_dwba_1-_bcfec_higher_energy_temp.in > new_test.dat") #new fresco output ran

      subprocess.call(['python', 'fresco_to_ascii_higher.py', 'new_test.dat']) #other python program called to convert into dat file
      input_variable = "new_test.dat"
      fresco_to_ascii_higher.main(input_variable)
      print("Ex = {}, BE = {}".format(Ex,BE))


main()
