with open("data.txt" , "w") as f:
    note = input("Enter a note : ")
    f.write(note)
with open("data.txt" , "r") as f:
           n =  f.read()
           print("Saved note : " , n)
