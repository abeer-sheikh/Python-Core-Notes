f = open("notes.txt" , "w")
f.write("python" + "\n")
f.write("javascript" + "\n")
f.write("java" + "\n")
f.write("c++" + "\n")
f.close()
f = open("notes.txt" , "r")
content = f.read()
search_word = input("What language do you search write here : ")
if(search_word in content):
    print("Found")
else:
    print("Not Found")
f.close()        