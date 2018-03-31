import numpy as np
import matplotlib.pyplot as plt

# de x en y waarden voor de coordinaten
x = [100.25, 100.31, 100.34, 100.66, 100.76, 100.88, 101.02, 101.09, 101.15, 101.5, 101.45, 102.86, 103.18, 103.29, 103.36, 103.29, 104.06, 104.44, 104.45, 104.53, 104.94, 104.93, 105.31, 105.64, 105.69]
y = [608, 617, 591, 565, 603, 612, 599, 587, 557, 528, 517, 484, 514, 510, 495, 458, 509, 504, 489, 471, 456, 425, 413, 388, 424]

if len(x) != len(y):  # check dat er voor elk coordinaat een x en een y waarde is
    print("Arrays are not equally sized!", "[", len(x), len(y), "]")
    quit(1)


def sd(arr=[]):  # berekening van de standaard afwijking
    rsum = 0
    for i in arr:
        rsum += i
    arrav = rsum / len(arr)

    arrdif = 0
    for i in arr:
        arrdif += (i - arrav) ** 2

    return np.sqrt(arrdif / len(arr)), arrav


def z(x, arr=[]):  # berekend Zx of Zy
    stddvn, arrav = sd(arr)
    return (x - arrav) / stddvn


def zz(arr1=[], arr2=[]):  # som van Zx*Zy
    zsum = 0
    for i in range(len(arr1)):
        zsum += z(arr1[i], arr1) * z(arr2[i], arr2)
    return zsum


def pmcc(arr1=[], arr2=[]):  # deelt de som van Zx*Zy door n
    return zz(arr1, arr2) / len(arr1)


r = pmcc(x, y)
print(r)  # print de correlatie coefficient naar het scherm

sdX, xmean = sd(x)
sdY, ymean = sd(y)
rc = r * (sdY / sdX)
yinterc = ymean - (rc * xmean)


def line(x):
    return rc * x + yinterc


# een plot van de coordinaten
plt.plot(x, y, "ro")
plt.plot([100, 106], [line(100), line(106)])
plt.show()
