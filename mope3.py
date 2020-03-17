import random, math
import numpy as np

x1_min = 10
x1_max = 40
x2_min = 10
x2_max = 60
x3_min = 10
x3_max = 15
y_min = 230
y_max = 238
m = 3
X = [[-1.0, -1.0, -1.0],
     [-1.0, 1.0, 1.0],
     [1.0, -1.0, 1.0],
     [1.0, 1.0, -1.0]]
# матриця У
Y = [[random.randint(230, 238) for y in range(m)] for x in range(4)]
print("Y: ")
for i in range(len(Y)):
    print(Y[i])
print("-------------------------")
# матриця Х
for i in range(len(X)):
    if X[i][0] == -1:
        X[i][0] = x1_min
    else:
        X[i][0] = x1_max
    if X[i][1] == -1:
        X[i][1] = x2_min
    else:
        X[i][1] = x2_max
    if X[i][2] == -1:
        X[i][2] = x3_min
    else:
        X[i][2] = x3_max
print("X: ")
for i in range(len(X)):
    print(X[i])
print("-------------------------")
# середнє по рядках
Ys = []
for i in range(len(Y)):
    Ys.append(sum(Y[i]) / m)
print("Ys: ", Ys)
print("-------------------------")
mx1 = (X[0][0] + X[1][0] + X[2][0] + X[3][0]) / 4
mx2 = (X[0][1] + X[1][1] + X[2][1] + X[3][1]) / 4
mx3 = (X[0][2] + X[1][2] + X[2][2] + X[3][2]) / 4
my = sum(Ys) / 4
print("mx1= {0} \n"
      "mx2= {1} \n"
      "mx3= {2} \n"
      "my= {3} ".format(mx1, mx2, mx3, my))
print("-------------------------")
a1 = ((X[0][0] * Ys[0]) + (X[1][0] * Ys[1]) + (X[2][0] * Ys[2]) + (X[3][0] * Ys[3])) / 4
a2 = ((X[0][1] * Ys[0]) + (X[1][1] * Ys[1]) + (X[2][1] * Ys[2]) + (X[3][1] * Ys[3])) / 4
a3 = ((X[0][2] * Ys[0]) + (X[1][2] * Ys[1]) + (X[2][2] * Ys[2]) + (X[3][2] * Ys[3])) / 4
print("a1= {0} \n"
      "a2= {1} \n"
      "a3= {2} ".format(a1, a2, a3))
print("-------------------------")
a11 = (X[0][0] ** 2 + X[1][0] ** 2 + X[2][0] ** 2 + X[3][0] ** 2) / 4
a22 = (X[0][1] ** 2 + X[1][1] ** 2 + X[2][1] ** 2 + X[3][1] ** 2) / 4
a33 = (X[0][2] ** 2 + X[1][2] ** 2 + X[2][2] ** 2 + X[3][2] ** 2) / 4
print("a11= {0} \n"
      "a22= {1} \n"
      "a33= {2} ".format(a11, a22, a33))
print("-------------------------")
a12 = a21 = ((X[0][0] * X[0][1]) + (X[1][0] * X[1][1]) + (X[2][0] * X[2][1]) + (X[3][0] * X[3][1])) / 4
a13 = a31 = ((X[0][0] * X[0][2]) + (X[1][0] * X[1][2]) + (X[2][0] * X[2][2]) + (X[3][0] * X[3][2])) / 4
a23 = a32 = ((X[0][1] * X[0][2]) + (X[1][1] * X[1][2]) + (X[2][1] * X[2][2]) + (X[3][1] * X[3][2])) / 4
print("a12=a21= {0} \n"
      "a13=a31= {1} \n"
      "a23=a32= {2} ".format(a12, a13, a23))
print("-------------------------")
# розрахунок детермінантів матриці
znamen = np.array([[1, mx1, mx2, mx3],
                   [mx1, a11, a12, a13],
                   [mx2, a12, a22, a32],
                   [mx3, a13, a23, a33]], dtype='float')
ch0 = np.array([[my, mx1, mx2, mx3],
                [a1, a11, a12, a13],
                [a2, a12, a22, a32],
                [a3, a13, a23, a33]], dtype='float')
ch1 = np.array([[1, my, mx2, mx3],
                [mx1, a1, a12, a13],
                [mx2, a2, a22, a32],
                [mx3, a3, a23, a33]], dtype='float')
ch2 = np.array([[1, mx1, my, mx3],
                [mx1, a11, a1, a13],
                [mx2, a12, a2, a32],
                [mx3, a13, a3, a33]], dtype='float')
ch3 = np.array([[1, mx1, mx2, my],
                [mx1, a11, a12, a1],
                [mx2, a12, a22, a2],
                [mx3, a13, a23, a3]], dtype='float')
b0 = np.linalg.det(ch0) / np.linalg.det(znamen)
b1 = np.linalg.det(ch1) / np.linalg.det(znamen)
b2 = np.linalg.det(ch2) / np.linalg.det(znamen)
b3 = np.linalg.det(ch3) / np.linalg.det(znamen)
b=[]
b.append(b0)
b.append(b1)
b.append(b2)
b.append(b3)
print("b0= {0} \n"
      "b1= {1} \n"
      "b2= {2} \n"
      "b3= {3}".format(b0, b1, b2, b3))
print("-------------------------")
# нормоване рівняння
print("Y={} + {}*x1 + {}*x2 + {}*x3".format(b0, b1, b2, b3))
print("-------------------------")
# перевірка
print("Перевірка: ")
# for i in range(len(X)):
#     for i in range(3):
print(b0 + b1 * X[0][0] + b2 * X[0][1] + b3 * X[0][2], "==", Ys[0])
print(b0 + b1 * X[1][0] + b2 * X[1][1] + b3 * X[1][2], "==", Ys[1])
print(b0 + b1 * X[2][0] + b2 * X[2][1] + b3 * X[2][2], "==", Ys[2])
print(b0 + b1 * X[3][0] + b2 * X[3][1] + b3 * X[3][2], "==", Ys[3])
print("Результат збігається з середніми значеннями")
print("-------------------------")
# перевірка однорідності за Кохреном
# дисперсії по рядках
# дисперсія по рядках
D = []
Summa = 0
for i in range(4):
    for j in range(m):
        Summa += pow((Y[i][j] - Ys[i]), 2)
    D.append(1 / m * Summa)
    Summa = 0
print("D: ", D)
print("-------------------------")
Gp = max(D) / sum(D)
print("Gp= ", Gp)
f1 = m - 1
f2 = N = 4
Gt = 0.7679
if Gp <= Gt:
    print("Дисперсія однорідна")
    print(Gp, "<=", Gt)
else:
    print("Дисперсія не однорідна")
print("-------------------------")
# критерій Стьюдента
S2_b = sum(D) / N
S2_betta = S2_b / (N * m)
S_betta = math.sqrt(S2_betta)
print("S2_b= {0} \n"
      "S2_betta= {1} \n"
      "S_betta= {2}".format(S2_b, S2_betta, S_betta))
print("-------------------------")
Xs = [[1.0, -1.0, -1.0, -1.0],
      [1.0, -1.0, 1.0, 1.0],
      [1.0, 1.0, -1.0, 1.0],
      [1.0, 1.0, 1.0, -1.0]]
betta = []
S = 0
betta0 = (Ys[0] * Xs[0][0] + Ys[1] * Xs[1][0] + Ys[2] * Xs[2][0] + Ys[3] * Xs[3][0]) / 4
betta1 = (Ys[0] * Xs[0][1] + Ys[1] * Xs[1][1] + Ys[2] * Xs[2][1] + Ys[3] * Xs[3][1]) / 4
betta2 = (Ys[0] * Xs[0][2] + Ys[1] * Xs[1][2] + Ys[2] * Xs[2][2] + Ys[3] * Xs[3][2]) / 4
betta3 = (Ys[0] * Xs[0][3] + Ys[1] * Xs[1][3] + Ys[2] * Xs[2][3] + Ys[3] * Xs[3][3]) / 4
betta.append(betta0)
betta.append(betta1)
betta.append(betta2)
betta.append(betta3)
print("betta0= {0} \n"
      "betta1= {1} \n"
      "betta2= {2} \n"
      "betta3= {3}".format(betta0, betta1, betta2, betta3))
# for i in range(4):
#     for j in range(4):
#         S += Ys[i]*Xs[i][j]
#     betta.append(1 / N * S)
#     S = 0
# print("betta: ", betta)
print("-------------------------")
t=[]
for i in range(len(betta)):
    t.append(abs(betta[i])/S_betta)
print("t: ", t)
print("-------------------------")
f3 = f1 * f2
t_tabl = 2.306
for i in range(len(t)):
    if t[i]<t_tabl:
        b[i]=0
y=[]
y.append(b0 + b1 * X[0][0] + b2 * X[0][1] + b3 * X[0][2])
y.append(b0 + b1 * X[1][0] + b2 * X[1][1] + b3 * X[1][2])
y.append(b0 + b1 * X[2][0] + b2 * X[2][1] + b3 * X[2][2])
y.append(b0 + b1 * X[3][0] + b2 * X[3][1] + b3 * X[3][2])
print("y: ", y)
for i in range(len(y)):
    print(y[i], "==", Ys[i])
print("-------------------------")
#критерій Фішера
d=2
f4=N-d
S_ad=0
Sum = 0
for i in range(len(y)):
    Sum += pow((y[i] - Ys[i]), 2)
S_ad=(m/(N-d)) * Sum
print("S_ad= ", S_ad)
Fp=S_ad/S2_b
print("Fp=", Fp)
Ft=4.5
if Fp>Ft:
    print("Рівняння регресії неадекватно оригіналу при рівні значимості 0.05")
else:
    print("Рівняння регресії адекватно оригіналу при рівні значимості 0.05")


