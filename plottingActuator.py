import matplotlib.pyplot as plt
import numpy as np

H = ['angleRespect', 'accRespect']

H__ = ['Angle Data', 'Acee Data']

linestyle_str = [
     ('solid', 'solid'),
     ('dotted', 'dotted'),
     ('dashed', 'dashed'),
     ('dashdot', 'dashdot')]

colors = [
     ('red', 'red'),
     ('green', 'green'),
     ('blue', 'blue'),
     ('black', 'black')]

linestyle_tuple = [
     ('loosely dotted',        (0, (1, 10))),
     ('dotted',                (0, (1, 1))),
     ('densely dotted',        (0, (1, 1))),

     ('loosely dashed',        (0, (5, 10))),
     ('dashed',                (0, (5, 5))),
     ('densely dashed',        (0, (5, 1))),

     ('loosely dashdotted',    (0, (3, 10, 1, 10))),
     ('dashdotted',            (0, (3, 5, 1, 5))),
     ('densely dashdotted',    (0, (3, 1, 1, 1))),

     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]

fig, ax = plt.subplots(1, 1, figsize=(48, 32))

ax.set_xticks(np.arange(0, 25, 2))
#ax.set_yticks(np.arange(0, 1., 0.1))

files = []

file_name_list = []

for h in H:
    file_name_list.append(f'{h}.csv')

for file in file_name_list:
    f = open(file, 'r')
    files.append(f)

X = []
Y = []

for f in files:
    x = []
    y = []
    for count, line in enumerate(f):
        if count > 1:
            line = line.strip()
            columns = line.split()
            #print(columns)
            if len(columns) >= 2:
                _x = float(columns[0])
                _y = float(columns[1])
                x.append(_x)
                y.append(_y)
        if len(x) >= 1500:
            break
    X.append(x)
    Y.append(y)


legends = []


for curve in range(len(X)):
    legends.append(f'Actuator {H__[curve]}')
    (name, color) = colors[curve]
    ax.plot(X[curve], Y[curve], linewidth=3, color=color)

plt.legend(legends, prop = {'family': 'Times New Roman', 'size': 40})
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
csfont = {'fontname': 'Times New Roman'}
plt.xlabel('Time (Hour)', csfont, fontsize=40)
plt.ylabel('Acmplitude', csfont, fontsize=40)

plt.grid(color='grey', linestyle='--', linewidth=1)

plt.show()