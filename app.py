import numpy as np

x = [100.25, 100.31, 100.34, 100.66, 100.76, 100.88, 101.02, 101.09, 101.15, 101.5, 101.45, 102.86, 103.18, 103.36, 103.29, 104.06, 104.44, 104.45, 104.53, 104.94, 104.93, 105.31, 105.64, 105.69]
y = [3030.25, 100.31, 100.34, 100.66, 100.76, 100.88, 101.02, 101.09, 101.15, 101.5, 101.45, 102.86, 103.18, 103.36, 103.29, 104.06, 104.44, 104.45, 104.53, 104.94, 104.93, 105.31, 105.64, 105.69]

if len(x) != len(y):
    print("Arrays not equal size!")
    quit()

def sd(arr=[]):
    rsum = 0
    for i in arr:
        rsum += i
    arrav = rsum / len(arr)

    arrdif = 0
    for i in arr:
        arrdif += (i - arrav) ** 2

    return np.sqrt(arrdif / len(arr)), arrav


def z(x, arr=[]):
    stddvn, arrav = sd(arr)
    return (x - arrav) / stddvn


def zz(arr1=[], arr2=[]):
    zsum = 0
    for i in range(len(arr1)):
        zsum += z(arr1[i], arr1) * z(arr2[i], arr2)
    return zsum


def pmcc(arr1=[], arr2=[]):
    return zz(arr1, arr2) / len(arr1)


print(pmcc(x, y))
