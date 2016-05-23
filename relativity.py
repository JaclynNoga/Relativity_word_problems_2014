import math
import picture

LC_list = [] #length contraction list, each element is a new run
TD_list = [] #time dialation list, each element is a new space trip

class Relativity(): 	#makes relativity class that solves for gamma,
                        #which will be used in both time dilation and length
                                           #contraction

    def __init__(self,velocity):	#using the velocity that the user has input, it solves for gamma,
                                    #a value used in both length contraction
                                                                    #and time dilation calculations
        self.velocity = velocity
        self.gamma = float(math.sqrt(1 - (velocity) ** 2)) #solves for gamma
     
    def length(self):   #uses gamma to find contracted length
        final_length = 100 * self.gamma #multiplies gamma by length
        return final_length

    def time(self): 	#uses gamme to find dilated time
        final_time = 6 * self.gamma #multiplies gamma by time
        return final_time



def length_contraction_calculation():  	#Asks the user for velocity of Jackie's spaceship.
                                        #Then solves for dilated time and inputs both velocity and
                                        #dilated time into a list.  Finally returns dilated time.
                                                                                 
    #Present the user with the word problem that deals with length contraction
    print()
    print("Nora is training for a marathon.")
    print("She jogs past a fence that is 100 meters long on her training route each day.")
    print("Today, she is wearing her rocket shoes that propel her to a velocity near the speed of light.")
    print("The fence appears shorter to Nora. How much shorter is it?")
    print()

    #FOR LENGTH CONTRACTION
    #exception handling in case the user inputs something that is not a decimal
    #between .6 and .99
    done = False    
    while not done:
        try:
            decimal = eval(input("What fraction of the speed of light would you like her to travel? Please enter a decimal between 0.6 and 1: "))
             
            if decimal >= .6 and decimal < 1 and isinstance(decimal, float):    #checks that input is between .6 and 1 and is a decimal
                x = Relativity(decimal) 	#creates relativity object
                a = int(x.length() * 100) / 100 	#finds contracted length and converts to 2 significant figures max
                done = True
            else:
                print("Error with input.") #Throws error message
        except:
            print("Error with input.") #Throws error message

    LC_list.append((decimal,a)) #appends information about the run into a list
    return a #returns contracted length
def length_contraction(a):	#takes in a, the contracted length of the fence, and shows the user how much
                          	#the fence has contracted with a picture
     
    print("When Nora looks at the fence, it is contracted to",a,"meters.")

    #####makes canvas for length contraction
    pic = picture.Picture(600, 800)
    pic.setFillColor(20, 60, 160)
    pic.drawRectFill(0, 0, 600, 800)

    #draws 100 m fence
    pic.setFillColor(255,255,255)
    for i in range(5):
        pic.drawRectFill(100 + i * 100,100,25,200) #draws vertical slats of fence
        pic.setOutlineColor(225,225,225)
        pic.drawPolygonFill([(100 + i * 100,100),(112.5 + i * 100,90),(125 + i * 100,100)]) 
        #draws triangles that make up the top of each verticle slat
     
    pic.setFillColor(255,255,255)
    pic.setOutlineColor(0,0,0)
    pic.drawRectFill(100,125,425,25) #draws horizontal slats on fence
    pic.drawRectFill(100,230,425,25) #draws horizontal slats on fence

    #draws length contracted fence
    for i in range(5):
        pic.drawRectFill(100 + (i * 100) * (a / 100),500,25 * (a / 100),200) #draws shortened vertical slats of fence, a is the length of the shorter fence
        pic.setOutlineColor(225,225,225)
        pic.drawPolygonFill([(100 + (i * 100) * (a / 100),500), ((100 + (i * 100) * (a / 100)) + ((a / 100) * 25) / 2,490), 
                             ((100 + (i * 100) * (a / 100)) + 25 * (a / 100),500)]) 
        #draws triangles that make up the top of each verticle slat while accounting
                                                                                                                                                                                   #for length contraction

    pic.setFillColor(255,255,255)
    pic.setOutlineColor(0,0,0)
    pic.drawRectFill(100,525,425 * (a / 100),25) #draws shortened horizontal slats on fence
    pic.drawRectFill(100,630,425 * (a / 100),25) #draws shortened horizontal slats on fence

    pic.display() #displays picture of normal and contracted fence.  The normal fence is on top,
                  #the length contracted fence on the bottom
    input()

def time_dilation_calculation():    	#Asks the user for the velocity of Nora's rocket shoes.  Then solves for
                                    	#the contracted length and inputs velocity and contracted length into a
                                    	#list.  Finally returns contracted length.

    #Presents the user with the word problem that deals with time dilation
    print()
    print("Jackie goes on a space mission on a rocket ship that travels at a velocity near the speed of light.")
    print("Nora notices that it is noon on Earth when Jackie leaves.")
    print("When she returns, Nora notices that it is 6 o'clock.")
    print("How much time has passed for Jackie?")

    print()
    #exception handling in case the user inputs something that is not a decimal
    #between .6 and .99
    done = False
    while not done:
        try:
            decimal2 = eval(input("What fraction of the speed of light would you like her to travel? Please enter a decimal between 0.6 and .99: "))
             
            if decimal2 >= .6 and decimal2 < .99 and isinstance(decimal2, float):    
                #checks that input is between .6 and .99 and is a decimal
                y = Relativity(decimal2)	#creates relativity object
                b = int(y.time() * 100) / 100   #finds dilated time and converts to 2 significant figures max
                done = True
            else:
                print("Error with input.") #Throws error message
        except:
            print("Error with input.") #Throws error message

    print("When Jackie returns to Earth, she believes that",b,"hours have passed.")

    TD_list.append((decimal2,b)) #appends information about the run into a list
    return b #returns the dilated time
def time_dilation(b): #takes in b, the dilated time, to show the user the difference in much time
                      #has passed on Earth and in space using a picture.

    #makes canvas for time dilation
    pic2 = picture.Picture(600, 800)
    pic2.setFillColor(200, 20, 20)
    pic2.drawRectFill(0, 0, 600, 800)


    #########################draws TOP clock without hands.  The tops clock is
    #########################the non relativistic clock
    #draws white circle for top clock
    pic2.setFillColor(255,255,255)
    pic2.drawCircleFill(300,200,150)
    pic2.setPenWidth(5)

    #draws circles to indicate hours on TOP clock.  Draws circles to indicate
    #hours 1,2,4,5,7,8,10,11
    pic2.setOutlineColor(120,120,120)
    pic2.drawCircleFill(421.24355652982143, 270.0,5)
    pic2.drawCircleFill(370.0, 321.2435565298214,5)
    pic2.drawCircleFill(230.00000000000003, 321.24355652982143,5)
    pic2.drawCircleFill(178.75644347017857, 270.0,5)
    pic2.drawCircleFill(178.7564434701786, 130.0,5)
    pic2.drawCircleFill(229.99999999999994, 78.75644347017862,5)
    pic2.drawCircleFill(370.0, 78.7564434701786,5)
    pic2.drawCircleFill(421.2435565298214, 129.99999999999994,5)

    #draws lines to indicate hours on TOP clock.  Draws lines to indicate hours
    #3,6,9,12
    pic2.setPenWidth(10)
    pic2.setPosition(300,55)
    pic2.setDirection(90)
    pic2.drawForward(25)
    pic2.setPosition(300,340)
    pic2.setDirection(270)
    pic2.drawForward(25)
    pic2.setPosition(160,200)
    pic2.setDirection(0)
    pic2.drawForward(25)
    pic2.setPosition(440,200)
    pic2.setDirection(180)
    pic2.drawForward(25)
     

    #####################draws BOTTOM clock without hands
    #draws white circle
    pic2.setPenWidth(1)
    pic2.setFillColor(255,255,255)
    pic2.drawCircleFill(300,600,150)

    #draws circles to incate hours on BOTTOM clock.  Draws circles to indicate
    #hours 1,2,4,5,7,8,10,11
    pic2.setPenWidth(5)
    pic2.setOutlineColor(120,120,120)
    pic2.drawCircleFill(421.24355652982143, 670.0,5)
    pic2.drawCircleFill(370.0, 721.2435565298214,5)
    pic2.drawCircleFill(230.00000000000003, 721.24355652982143,5)
    pic2.drawCircleFill(178.75644347017857, 670.0,5)
    pic2.drawCircleFill(178.7564434701786, 530.0,5)
    pic2.drawCircleFill(229.99999999999994, 478.75644347017862,5)
    pic2.drawCircleFill(370.0, 478.7564434701786,5)
    pic2.drawCircleFill(421.2435565298214, 529.99999999999994,5)

    #draws lines to indicate hours on BOTTOM clock.  Draws lines to indicate
    #hours 3,6,9,12
    pic2.setPenWidth(10)
    pic2.setPosition(300,455)
    pic2.setDirection(90)
    pic2.drawForward(25)
    pic2.setPosition(300,740)
    pic2.setDirection(270)
    pic2.drawForward(25)
    pic2.setPosition(160,600)
    pic2.setDirection(0)
    pic2.drawForward(25)
    pic2.setPosition(440,600)
    pic2.setDirection(180)
    pic2.drawForward(25)

    ####gets variables organized into a list, L, that we will use in animating
    ####the hands of the clocks
    dilated_hours = int(b) #integer value of the shorter time
    decimal_minutes = b - dilated_hours #decimal value of extra minutes after the integer hours have passed
    dilated_minutes = decimal_minutes * 60 #actual number of minutes left after the integer hours have passed
    modthing = 144 / dilated_hours / 2

    L = [dilated_hours, dilated_minutes, modthing] #puts variables organized into a list, L, that we 
                                                   #will use in animating the hands of the relativistic clock

    x = 0 	#variable used for drawing hour hands of the TOP clock so that it only
          	#changes position every 12 frames (30 minutes)
    y = 0 	#variable used for drawing hours hands of the BOTTOM clock so that it only
          	#changes position every 12 frames (30 minutes)

    pic2.setPenWidth(12)
    for i in range(144): 	#moves hands of top clock for every 2.5 minutes, 15 degrees, 144 frames
     
        ###############################draws hands of the TOP clock
        #draws minutes hand of TOP clock
        pic2.setOutlineColor(0,0,0)
        pic2.setPosition(300,200)
        pic2.setDirection(270 + (15 * i)) #hand moves 7.5 degrees every loop
        pic2.drawForward(115)
     
        #draws hour hands of TOP clock.
        if (i % 12) == 0: #Only updates every 12 frames
            x = x + 12 #variable to hold the hour clock in place for 12 frames while minute hand
                       #continues to move.  Used in else statement
            pic2.setPosition(300,200)
            pic2.setDirection(255 + (i / 12) * 15) #moves hour hand 15 degrees every 12 frames aka 30 minutes
            pic2.drawForward(70)
        else: #this else statement keeps the hour hand from being erased.  It redraws the
              #hour hand every frame until it's time to update
            pic2.setPosition(300,200)
            pic2.setDirection(255 + (x / 12) * 15)
            pic2.drawForward(70)   	 
     
        #draws circle in the middle of TOP clock
        pic2.setFillColor(0,0,0)
        pic2.drawCircleFill(300,200,5)
         
        ##############################draws hands of the BOTTOM clock
        #minutes hand of BOTTOM clock
        pic2.setOutlineColor(0,0,0)
        pic2.setPosition(300,600)
        pic2.setDirection(270 + i * ((L[0] * 360 + L[1] * 6) / 144)) #moves hand between 0 and 7.5 degress based on the speed the user defined.
                                                                     #Uses variables in list defined above
        pic2.drawForward(115)
         
        #draws hour hands of BOTTOM clock
        if (i % L[2]) == 0:
            y = y + L[2] #variable to hold the hour clock in place for 12 frames while minute hand
                         #continues to move.  Used in else statement
            pic2.setPosition(300,600)
            pic2.setDirection(270 + (i / L[2]) * 15) #moves hour hand 15 degrees every time the minute hand moves 30 minutes.  Uses
                                                     #variables defined in list above
            pic2.drawForward(70)
        else: #this else statement keeps the hour hand from being erased.  It redraws the
              #hour hand every frame until it's time to update
            pic2.setPosition(300,600)
            pic2.setDirection(270 + (y / L[2]) * 15) 
            pic2.drawForward(70)   	 
         
        #draws circle in the middle of BOTTOM clock
        pic2.setFillColor(0,0,0)
        pic2.drawCircleFill(300,600,5)
         
         
        pic2.delay(50) #delay so that all lines are not drawn and erased in the same frame
        pic2.display()
         
        ################################erases hands of the clocks
        #erases minutes hand of TOP clock.  This is necessary because otherwise
        #black lines would completely fill the clock as the hand moved
        pic2.setOutlineColor(255,255,255)
        pic2.setPosition(300,200)
        pic2.setDirection(270 + i * 15) #erases minute hand
        pic2.drawForward(115)
         
        #erases hour hand of TOP clock
        if (i % 12) == 0:
            pic2.setPosition(300,200)
            pic2.setDirection(255 + (i / 12) * 15) #erases hour hand
            pic2.drawForward(70)
        else:
            pic2.setPosition(300,200)
            pic2.setDirection(255 + (x / 12) * 15) #erases hour hand
            pic2.drawForward(70)   	 
    
        #erases minutes hand of BOTTOM clock
        pic2.setPosition(300,600)
        pic2.setDirection(270 + (i * ((L[0] * 360 + L[1] * 6) / 144))) #erases minute hand
        pic2.drawForward(115)
         
        #erases hour hands of BOTTOM clock
        if (i % L[2]) == 0:
            pic2.setPosition(300,600)
            pic2.setDirection(270 + (i / L[2]) * 15) #erases hour hand
            pic2.drawForward(70)
        else:
            pic2.setPosition(300,600)
            pic2.setDirection(270 + (y / L[2]) * 15) #erases hour hand
            pic2.drawForward(70)   	 
    

    ###############draws final top clock
    #draws final minutes hand of top clock
    pic2.setOutlineColor(0,0,0)
    pic2.setPosition(300,200)
    pic2.setDirection(270)
    pic2.drawForward(115)
    #draws final hour hand of top clock
    pic2.setPosition(300,200)
    pic2.setDirection(90)
    pic2.drawForward(70)
    #draws circle in the middle of top clock
    pic2.setFillColor(0,0,0)
    pic2.drawCircleFill(300,200,5)

    ######draws final hands of the bottom clock
    #minutes hand
    pic2.setOutlineColor(0,0,0)
    pic2.setPenWidth(12)
    pic2.setPosition(300,600)
    pic2.setDirection(270 + (144 * (L[0] * 360 + L[1] * 6) / 144))
    pic2.drawForward(115)
    #hours hand
    pic2.setPosition(300,600)
    pic2.setDirection(270 + 30 * b)
    pic2.drawForward(70)
    #draws circle in the middle of bottom clock
    pic2.setFillColor(0,0,0)
    pic2.drawCircleFill(300,600,5)

    pic2.display()
    input()

def bubbleSort(A):  	#Sorts the list of tuples so that the shortest time or length is first in
                    	#the list.
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(A) - 1):
                if A[i][1] > A[i + 1][1]:
                    A[i],A[i + 1] = A[i + 1],A[i]
                    swapped = True

