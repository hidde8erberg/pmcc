import numpy as np  # voor wiskundige aspecten (zoals een wortel)
import matplotlib.pyplot as plt  # voor het plotten van de coordinaten

# de x en y waarden voor de coordinaten
x = [100.25, 100.31, 100.34, 100.66, 100.76, 100.88, 101.02, 101.09, 101.15, 101.5, 101.45, 102.86, 103.18, 103.29, 103.36, 103.29, 104.06, 104.44, 104.45, 104.53, 104.94, 104.93, 105.31, 105.64, 105.69]
y = [608, 617, 591, 565, 603, 612, 599, 587, 557, 528, 517, 484, 514, 510, 495, 458, 509, 504, 489, 471, 456, 425, 413, 388, 424]
# test data (de bovenste arrays maar dan shuffled)
yTest = [514, 591, 509, 489, 617, 599, 603, 608, 565, 456, 510, 557, 504, 424, 458, 484, 528, 388, 495, 517, 471, 425, 413, 587, 612]
xTest = [101.09, 102.86, 104.94, 100.25, 103.29, 103.29, 101.5, 100.31, 104.93, 100.88, 101.02, 103.18, 105.69, 103.36, 101.45, 105.64, 100.76, 104.45, 100.34, 104.06, 100.66, 104.53, 104.44, 105.31, 101.15]


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


def line(x):  # functie voor y-coordinaat bij invoeren van x-coordinaat
    return rc * x + yinterc


# de uiteindelijke correlatie coefficient
r = pmcc(x, y)
print(r)  # print de correlatie coefficient naar het scherm


# rc en punt waar y=0
sdX, xmean = sd(x)
sdY, ymean = sd(y)
rc = r * (sdY / sdX)
yinterc = ymean - (rc * xmean)


# een plot van de coordinaten
plot = plt.figure()
plt.plot(x, y, "ro")
plt.plot([100, 106], [line(100), line(106)])
plt.title("pmcc = " + str(r))
plt.xlabel("fastfood en afhaalmaaltijden (in indexcijfers, met 2015 als basis)")
plt.ylabel("werkloosheid omvang (x1000)")
plt.show()

# Grafiek opslaan als bestand
plot.savefig("correlationGraph.pdf")  # plot.savefig("correlationGraph.png")
