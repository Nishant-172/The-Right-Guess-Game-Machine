import random #this is a module used for getting a random value 
number = random.randint(1,100) #used to get a random number b/w 1 to 100
a =-1 # we have give the value -1 taki jo loop ki condition ho hardam true rhe and ye innfinite loop ho
Your_Guess = 1 #default VALUE 1 di hai KYUKI 1 GUESS TO LETI HI HAI KOI CHEEZ
while(a != number): #if a is not equal to number
    a = int(input("Guess the number: ")) #for taking the input value from user
    
    if(a >number):
        print("Lower Number Please")
        Your_Guess +=1 # ye line is likh rha hu taki pta chle ek aadmi kitne times guess kiya hai shi answer ke liye

    elif(a<number):
        print("higher number please")
        Your_Guess +=1 # ye line is likh rha hu taki pta chle ek aadmi kitne times guess kiya hai shi answer ke liye


print(f"you guessed the right number {number} in {Your_Guess}attempts")
if(Your_Guess>5):
    print("Kaafi kharab khela hai aapne😂🤣")
else:
    print("Kaafi accha khela hai aapne , aapko milte hai 7 Crore🤑💲")       