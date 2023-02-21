cat_hat = {}

# set each cat without a hat
for cat in range(1,101):
    cat_hat[cat] = "off"

# walk around that cat circle 100 times (set round 1)    
rounds = 1
while rounds <= 100:
    # for each new round start at 'round' continuing to 100 adding a hat
    # at each stop.  For round 1 we will stop at each cat
    for i in range(rounds, 101, rounds):
        if cat_hat[i] == 'off':
            cat_hat[i] = 'on'
        else:
            cat_hat[i] = 'off'
    rounds += 1
for cat in cat_hat:
    if cat_hat[cat] == 'on':
        print(f"Cat {cat} has a hat!")
    else:
        print(f"Cat {cat} has no hat!")
