file = open("hello.txt","w")

file.write("Hello, Shiwansh!")
file.write("bye, shiwansh")
line = file.readline()
print(line)
file.close()
