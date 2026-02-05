file=open("data.txt", 'w')
file.write("Hello, World!")
file.close()
file=open("data.txt", 'r')
content=file.read() 
print(content)
file.close()
#with open("data.txt", 'a') as file:
# #file.write("\nThis is an appended line.")   
