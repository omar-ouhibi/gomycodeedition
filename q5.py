str1=input("whats ur name")
result = ""
for i in range(len(str1)):
    if i % 2 == 0:
        result += str1[i]
print (result)    