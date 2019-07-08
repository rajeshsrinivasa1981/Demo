input = input("Enter the string")
result = ''
for i in range(len(input)-1,-1,-1):
    result = result + input[i]
print(result)


