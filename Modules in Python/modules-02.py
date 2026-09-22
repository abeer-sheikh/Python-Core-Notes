import random
#random.randint
dice = random.randint(1,10)
print("Dice number : " , dice)

#random.randint
otp = random.randint(1000, 9999) #random.randint ke andar jo bhi number likhey hein wo unmein se koi bhi random number dedeta hai bas yhi hota hai ranom.randint
print("Your Otp : " , otp)

#random.choice
colors = ["red", "blue", "green", "yellow"] #random.choice kisi bhi list mein se koi bhi random string yan number dedeta hai
winner = random.choice(colors)
print("Winner : " , winner)