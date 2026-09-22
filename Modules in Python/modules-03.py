import datetime #ye ek module hai datetime ke name se 

now = datetime.datetime.now() #datetime ek module hai or datetime.now ek class hai or in ko humney variable now mein store kara hai
print(now) #now ko print kara hai or yahan har cheez print hojayegi date time year day etc


now1 = now.year # yahan humney year store kara hai now1 variable mein or now.year ek function hai jo year deta hai
print(now1)
now2 = now.month #yahan humney month store kara hai now2 variable mein or now.month ek function hai jo month deta hai
print(now2)
now3 = now.day #yahan humney day store kara hai now3 variable mein or now.day ek function hai jo day deta hai
print(now3)


now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y")) #now.strftime ke andar ye jo code hai na ye neechey bhi mention hai to hum iska format neechey dekh saktey hein.




# %d = day
# %m = month
# %Y = year
# %H = hour
# %M = minute
# %S = second
# %B = full month name
# %A = full day name