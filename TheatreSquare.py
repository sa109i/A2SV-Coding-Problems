import math
def numOfFlagstones(n, m, a):
    areaOfTheater = n * m
    areaOfFlagstone = a ** 2
    
    count = math.ceil(areaOfTheater/areaOfFlagstone)
    
    print("Number Of Flagstons: ", count)

n, m, a = [int(i) for i in input("n, m, a saparet them by space").split(" ")]
numOfFlagstones(n, m, a)
