
f = open("demofile1.txt", "a")
f.write("Now the file has more content! ")
f.close()


f = open("demofile1.txt","r")
print(f.read())
