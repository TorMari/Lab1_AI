import random
import math

def initialization(n):
    return [random.randint(0, n-1) for _ in range(n)]


def random_change(ans):
    new_ans = ans.copy()
    index = random.randint(0, len(ans)-1)
    new_ans[index] = random.randint(0, len(ans)-1)
    #index1, index2 = random.sample(range(len(ans)), 2)
    #new_ans[index1], new_ans[index2] = new_ans[index2], new_ans[index1]
    return new_ans


def evaluateError(ans):
    conflicts = 0
    N = len(ans)
    for i in range(N):
        for j in range(i+1, N):
            if ans[i] == ans[j] or abs(i - j) == abs(ans[i] - ans[j]):
                conflicts += 1
    print(conflicts)
    return conflicts


def copy_ans(ans):
    return ans.copy()


def print_solution(ans):
    #print(ans)
    N = len(ans)
    for i in range(n):
        for j in range(n):
            if ans[j] == i:
                print('Q', end = ' ')
            else:
                print('.', end = ' ')
        print()


def simulated_annealing(n, max, t, coefficient):
    current_ans = initialization(n)
    current_energy = evaluateError(current_ans)
    best_ans = copy_ans(current_ans)
    best_energy = current_energy
    k = 0
    while k < max and current_energy > 0:

        new_ans = random_change(current_ans)
        new_energy = evaluateError(new_ans)

        if new_energy < current_energy or random.random() < math.exp((current_energy - new_energy) / t):
            current_ans = new_ans
            current_energy = new_energy

        if current_energy < best_energy:
            best_ans = copy_ans(current_ans)
            best_energy = current_energy

        t *= coefficient
        k += 1

    return best_ans


n = 30
max = 10000  
t = 10000.0  
coefficient = 0.99  
res = simulated_annealing(n, max, t, coefficient)

print("Розв'язок:")
print_solution(res)
