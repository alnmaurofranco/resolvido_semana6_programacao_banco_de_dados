from matplotlib import pyplot as plt
from collections import Counter

users = [1, 2, 3, 4, 5, 6, 7, 8]
friends = [5, 10]

plt.bar([2013, 2014], users, 0.2)
plt.xticks(friends)
plt.ylabel('#Numero de amigos')
plt.axis([5, 10, 5, 8])
plt.show()


salarys = [910, 1000, 2300, 800, 600]
exp = lambda grade: grade // 6 * 10

histogram = Counter (exp(salary) for salary in salarys)

plt.bar([
    totals for totals in histogram.keys()
], histogram.values(), 10)

plt.axis([-10, 200,0, 8])
plt.xticks('# Salario total')
plt.show()


payments = ['Clayton', 'José', 'Mariana', 'Celso', 'Soarez']

not_payments = [1, 3, 4, 5]
xs = [i for i, _ in enumerate(payments)]

plt.bar(xs, not_payments)
plt.ylabel('Numeros de não pagantes')
plt.xlabel('Pagantes')
plt.xticks([i for i, _ in enumerate(payments)], payments)
plt.show()

