#12/18/14
#Jackie Noga and Nora Rice
#CS 150
#We affirm that we adhered to the honor code on this assignment

from relativity import *

########  LENGTH CONTRACTION #############################
length_contraction(int(length_contraction_calculation())) 	#uses input, relativity class, and functions to print visual representation
                                                          	#of length contraction
LC_count = 1    	#initializes the number of times the user has run the length contraction
                	#function

#allows user the option to continue running length contraction
J = True
while J == True: 
    tacocat = input("Would you like to go on another run? Enter y or n: ") #asks user if they would like to run the problem again
    if tacocat == "n":
        break #if the user enters 'n', the loop will break and move on to the time dilation
              #problem
    elif tacocat == "y":
        length_contraction(int(length_contraction_calculation())) #if the user enters 'y', the problem runs again
        LC_count = LC_count + 1 #updates the count of the number of times the program has run
    else:
        print("Error with input.") #Throws an error if the user inputs anything other than 'y' or 'n'

#prints a summary of the results for all trials of length contraction
print()
print("Summary")
for i in range(len(LC_list)):
    print("Velocity: ",int(LC_list[i][0] * 300000000), "meters per second   Contracted Length: ", LC_list[i][1], "meters") 
    #for each run, this loop prints a summary statement listing the speed at which
    #Nora ran -an actual number rather than a decimal- and the length to which the fence was contracted
                                                                                
bubbleSort(LC_list)

#teaches user the concepts of length contraction
print()
print("The shorted length of the fence was",LC_list[0][1], "when Nora was running", int(LC_list[0][0] * 300000000), "meters per second.")
print("Nora went on ", LC_count, 
      " total runs. Based on the inputs for velocity we can see that the relationship between relativisitic speed and contracted length is inversely proportional.", sep="")


##########  TIME DILATION ############################################
time_dilation(float(time_dilation_calculation()))    	#uses input, relativity class, and functions to print visual
                                                     	#representation of time dilation
TD_count = 1    	#initializes the number of times the user has ran time dilation

#allows user the option to continue running length contraction
K = True
while K == True:
    tacocat = input("Would you like to go on another space mission? Enter y or n: ") #asks user if they would like to run the problem again
    if tacocat == "n": #if the user enters 'n', the loop will break and move on to the time dilation
                       #problem
        break
    elif tacocat == "y": 
        time_dilation(float(time_dilation_calculation())) #if the user enters 'y', the problem runs again
        TD_count = TD_count + 1 #updates the count of the number of times the program has run
    else:
        print("Error with input.") #Throws an error if the user inputs anything other than 'y' or 'n'

#prints a summary of the results for all trials of time dilation
print()
print("Summary")
for i in range(len(TD_list)):
    print("Velocity: ",int(TD_list[i][0] * 300000000), "meters per second   Dilated Time: ", TD_list[i][1], "hours") 
    #for each run, this loop prints a summary statement listing the speed at which
    #Jackie travelled -an actual number rather than a decimal- and the shortened time in decimal form

bubbleSort(TD_list)


######################## SUMMARY ##########################
#teaches user the concept of time dilation
print()
print("The shorted time measured on Jackie's clock was", TD_list[0][1], 
      "when she was traveling", int(TD_list[0][0] * 300000000), "meters per second.")
print("Jackie went on", TD_count, 
      "total trips. Based on the inputs for velocity we can see the relationship between relativistic speed and dilated time is inversely proportional")