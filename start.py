from start_test import *
import random


x = 1
answer = []
qwestion_index = []

for question in range(0, 12):
    z = random.randint(0, 18)
    qwestion1 = input("question "+str(x)+" : " +
                      test_list[z])
    answer.append(qwestion1)
    qwestion_index.append(z)
    x = x+1
    
checker_index(qwestion_index)
checker_answer(answer)
print (answer,"\n",qwestion_index)