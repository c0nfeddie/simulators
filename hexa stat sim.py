import random


def enhance(value, prob):
    if value <= 10:
        value += 1
    return value

def change_rates(rates, stats_0):
    if 3 <= stats_0 <= 6:
        rates = [0.2, 0.4, 0.4]
    elif 6 < stats_0 < 8:
        rates = [0.15, 0.425, 0.425]
    elif 7 < stats_0 < 9:
        rates = [0.1, 0.45, 0.45]
    elif stats_0 >= 9:
        rates = [0.05, 0.475, 0.475]
    return rates

def check_cap(stats_1, stats_2, rates):
    if stats_1 == 10:
        rates[2] = rates[1] + rates[2]
        rates[1] = 0
    if stats_2 == 10:
        rates[1] = rates[1] + rates[2]
        rates[2] = 0
    return rates

def spend_frags(frag, stats_0):
    if stats_0 >= 9:
        frag = frag+50
    elif stats_0 >= 7:
        frag = frag+30
    elif 3 <= stats_0 <= 6:
        frag = frag+20
    elif 0 <= stats_0 < 3: 
        frag = frag+10
    return frag
    
stats = [0, 0, 0]
rates = [0.35, 0.325, 0.325]
iterations = 20
frags = 0

for x in range(iterations):
    frags = spend_frags(frags, stats[0])

    index_to_increase = random.choices([0, 1, 2], weights=rates, k=1)[0]

    stats[index_to_increase] = enhance(stats[index_to_increase], rates[index_to_increase])

    rates = change_rates(rates, stats[0]) 
    rates = check_cap(stats[1], stats[2], rates)
    
    print(f"Roll {x + 1}")
    print("Main Stat:", stats[0])
    print("Sub-stat:", stats[1])
    print("Sub-stat:", stats[2])
    print("Rates:", rates)
    print("Frags spent:", frags)
    print("----")
    