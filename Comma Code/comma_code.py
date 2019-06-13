def commaCode(list):
    result = ''
    for listValue in range(len(list)-1):
        result=result + list[listValue] + ', '
    result=result + 'and ' + list[-1]

    return result

print("Enter list items (Enter nothing to stop)")
list=[]

while True: 
    listItem=input()
    if (listItem==''):
        break
    list=list+[listItem]

result=commaCode(list)
print(result)