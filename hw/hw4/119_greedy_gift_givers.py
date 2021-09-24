import sys

def get_input():
    return next(sys.stdin)

first = True
try:
    while True:
        n = int(get_input())
        if first:
            first = False
        else:
            print()
        all_names = get_input().split()
        totals = dict((name, 0) for name in all_names)
        for i in range(n):
            giver, amount, people, *names = get_input().split()
            amount = int(amount)
            people = int(people)
            amount = 0 if people == 0 else amount//people
            totals[giver] -= amount * people
            for receiver in names:
                totals[receiver] += amount
        for key, value in totals.items():
            print(key, value)
except StopIteration:
    quit()