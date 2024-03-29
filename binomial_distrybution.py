from math import comb
import sys

S = (float(eval(input('Probability [%]: '))))/100
T = int(eval(input('Total tries: ')))
resoult = []

for i in range(T+1):
    if (comb(T,i) * (S**i) * (1-S)**(T-i) < 0.001):
        resoult.append(0.0)
    else:
        resoult.append( comb(T,i) * (S**i) * (1-S)**(T-i) )

max_value = resoult[1]
max_index = 1
sec_value = resoult[2]
sec_index = 2

for i in range(len(resoult)):

    if max_value < resoult[i]:

        sec_value = max_value
        sec_index = max_index

        max_index = i
        max_value = resoult[i]

max_value = round(max_value * 100, 2)
sec_value = round(sec_value * 100, 2)
success_chance = round((1-resoult[0]) * 100, 2)

if round(resoult[0], 2) == 0.0:
    if round(resoult[0], 3) == 0.0:
        fail_chance = round(resoult[0]*100, 4)
    else:
        fail_chance = round(resoult[0]*100, 3)
else:
    fail_chance = round(resoult[0]*100, 2)

if len(sys.argv) > 1:
    if str(sys.argv[1]) == "-full":
        print('==========================')
        indi = 0
        for prob in resoult:
            print(str(indi)+" : "+str(prob))
            indi+=1
        print('==========================')
else:
    print('')
    print('Given precentage: ' + str((S*100)) + ' %')
    print('')
    print('========BASE VALUES=======')
    print('')
    print('Total success chance: ' + str(success_chance) + ' %' )
    print('Total failure chance: ' + str(fail_chance) + ' %' )
    print('')
    print('======PRECISE VALUES======')
    print('')
    print('Highest probability of ' + str(max_index) + ' successes in ' + str(T) + ' tries: ' + str(max_value) + ' %')
    print('Second highest probability of ' + str(sec_index) + ' successes in ' + str(T) + ' tries: ' + str(sec_value) + ' %')
    print('Not rounded | 0 successes in ' + str(T) + ' with a probability: ' + str(resoult[0] * 100) + ' %')
    print('')