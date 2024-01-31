import random
#Generating  random number between 0 to 100
num = random.randint(0,100)

#Getting input from user
boy_name = input("Write your name: ")
girl_name = input("Write her name: ")

#Calculating the value of love LOL!!
if boy_name == "Atharv" and girl_name == "Payal":
    print("Love between Atharv and Payal is 100%")

if boy_name == "Waggy" and girl_name == "Kenny":
    print("Love between Waggy and Kenny is 100%")

else: 
    print("love between " + boy_name + " and " + girl_name + " found to be " + str(num) + "%")