# projeto FlyFood

def main():
    routers = definePoints(openFile("rotas.txt"))
    r, routers = originAndPoints(routers)
    print(r)
    print(routers)
    print(distance(['C', 2, 5], ['B', 3, 2]))
    print(distance(['D', 0, 5], ['B', 3, 2]))
    print(distance(['D', 0, 5], ['C', 2, 5]))

def openFile(x):
    with open (x,"r") as file:
        routes = file.readlines()
        return routes

def definePoints(routes):
    routes = routes[1:]
    finalRoutes = []
    count = 0
    for i in routes:
        internalCount = 1
        for j in i:
            if j not in [" ", "0","\n"]:
                finalRoutes.append([j,count,internalCount])
            elif j == "0":
                internalCount += 1

        count += 1

        print(i)
    return finalRoutes

def permutation(listp):

    if len(listp) == 0:
        return []
    
    if len(listp) == 1:
        return [listp]
    
    finalList = []

    for i in listp:
        currentList = listp[:]
        currentList.remove(i)

        for j in permutation(currentList):
            finalList.append([i] + (j))
        
    return finalList

def originAndPoints(listp):
    for i in listp:
        if i[0] == "R":
            listp.remove(i)
            return (i,listp)

def distance(point1,point2):
    y = abs(point1[1] - point2[1])
    if y == 0:
        y += 1
    x = abs(point1[2] - point2[2])
    if x == 0:
        x += 1
    return (x + y - 1)


main()