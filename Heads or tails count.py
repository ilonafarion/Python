# H for heads
# T for tails
import random
possible_outcomes= ['H','T']
H  = 0
T = 0
for i in range(0,100):
    los = random.choice(possible_outcomes)
    print(los)
    if los == 'H':
        H = H + 1 #counts how many heads there are
    else:
        T = T + 1 #counts how many tails there are

print('heads: ' + str(H)) #shows how many heads there are
print('tails: ' + str(T)) #shows how many tails there are
