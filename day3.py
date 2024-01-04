strTest = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..'''

# All numbers adjacent to symbols are important, add them all up.

# initial idea: 1. solve for all symbols 2.when one is encountered, mark all affected indexes with h.
# 3. A number is important if it has an h somewhere within it.
# 4. Solve for numbers with h touching them, go left until a dot or a symbol is encountered, go right until
# a dot or a symbol is encountered, add all those numbers together

data: str = strTest
data = data.split('\n')
shape = [len(data[0])-1,len(data)-1]

marks = []

for i, o  in enumerate(data):
    data[i] = list(o)
    marks.append([])
    for x in data[i]:
        marks[i].append(0)
'''

5x5, 3,3 is hit
affected are : 3:, :3, 1 1, 2 2, 3 3, 4 4, 5 5, 1 5, 2 4, 3 3, 4 2, 5 1

10 x 10

2 5 is hit

affected are: 2:, :5, 1 4, 3 6, 4 7, 5 8, 6 9, 7 10
                    , 1 6, 3 4, 4 3, 5 2, 6 1
                    
affected.append(y, x)
for distance in range(1, max(shape))
    affected.append(y+distance, x+distance) add [] for all
    affected.append(y-distance, x-distance)
    affected.append(y+distance, x-distance)
    affected.append(y-distance, x+distance)
    
for i,o in enumerate(affected):
    if o[0] > shape[0] or o[1] > shape[1]:
        affected.pop(i)
# Filter?


'''

def markAffected(y,x):
    startingPoint = y,x
    # ONLY DIAGS AFFECTED
    # Calculate affected indices
    # x all, y all, diag x directions until shape limit hit
    affected = []
   
    #for distance in range(1, max(shape)):
    for distance in range(1,2):
        affected.append([y+distance, x])
        affected.append([y, x+distance])
        affected.append([y-distance, x])
        affected.append([y, x-distance])
        
        affected.append([y+distance, x+distance])
        affected.append([y-distance, x-distance])
        affected.append([y+distance, x-distance])
        affected.append([y-distance, x+distance])
    
    """
    for i,o in enumerate(affected):
        if o[0] > shape[0] or o[1] > shape[1] or o[0] < 0 or o[1] < 0:
            affected.pop(i)
    """
    affected = [o for o in affected if o[0] <= shape[0] and o[1] <= shape[1] and o[0] >= 0 and o[1] >= 0]
    
    for o in affected:
        if marks[o[0]][o[1]] != 1:
            marks[o[0]][o[1]] = 1
            #data[o[0]][o[1]] = 'h' + data[o[0]][o[1]]
    return

def getNum(y,x):
    result = []
    while str(data[y][x]).isdigit():
        x-=1
    x+=1
    while str(data[y][x]).isdigit():
        result.append(str(data[y][x]))
        data[y][x] = 0
        x+=1
    res = "".join(result)
    return int(res)
        


for y, line in enumerate(data):
    for x, symbol in enumerate(line):
        if not symbol.isalnum() and symbol != "h." and symbol != ".":
            markAffected(y,x)

    
    

    
# count and analyze
result = 0
for y, line in enumerate(marks):
    #for x, symbol in enumerate(line):
    #    if symbol.find('h') == -1 and not symbol.isdigit():
    #        line[x] = " "
    #data[y] = "".join(line)
    for x, tagged in enumerate(marks[y]):
        if marks[y][x] == tagged and str(data[y][x]).isdigit():
            result += getNum(y,x)
        

        
'''
    continue
if symbol.isdigit():
    continue
else:
    data[y][x] = " "

'''
print(result)