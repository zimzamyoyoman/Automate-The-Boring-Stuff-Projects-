#! python3
# tablePrinter.py - Prints a list of lists in a formatted table 

def printTable(tableList):
    
    colWidths = [0] * len(tableList)
    length = len(tableList)
    innerLength = len(tableList[0])
    
    for i in range(length):
        temp=tableList[i][0]
        for j in range(1,innerLength):
            if len(temp) < len(tableList[i][j]):
                temp=tableList[i][j]

        colWidths[i]=len(temp)  

    for j in range(innerLength):
        for i in range(length):
            print(tableList[i][j].rjust(colWidths[i]), end=" ")
        print("")

    return None

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)