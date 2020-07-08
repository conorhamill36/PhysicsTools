#Program to run multiple front20 programs for a range of energies and Jpi's, to produce multiple outputs for TWOFNR
import os
import subprocess
import twofnr_to_ascii


def main():
    print("hello world")

    file_name = 'input_front20_dwba_3+_2_potentials.txt'
    file_name_input = open(file_name,"r")
    file_name_input_lines = file_name_input.readlines()
    print(file_name_input_lines[0])
    # command_file_name = file_name_input_lines[0][:-4]
    command_file_name = file_name_input_lines[0][:12]
    print(command_file_name)


    front_command = "./front20 < " + file_name
    print(front_command)
    # os.system("./front20 < input_front20_dwba_3+_2_potentials.txt")
    os.system(front_command)


    twofnr_command_file_name = "temp_twofnr_input.txt"
    twofnr_command_file = open(twofnr_command_file_name,"w")
    twofnr_command_file.write("tran."+command_file_name.rstrip())
    twofnr_command_file.close()

    twofnr_command = "./twofnr18 < " + twofnr_command_file_name
    print(twofnr_command)
    os.system(twofnr_command)
    #os.system("./twofnr18 < tran.dwba_potenti")
    twofnr_to_ascii_command = "20." + command_file_name
    print(twofnr_to_ascii_command)
    twofnr_to_ascii.main(twofnr_to_ascii_command)
    #twofnr_to_ascii.main("20.dwba_potenti")
    # os.system("test_file | ./front20")
    file_name_input.close()
main()
