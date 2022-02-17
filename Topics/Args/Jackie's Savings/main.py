def final_deposit_amount(*interest, amount=1000):
    earned = amount
    for i in interest:
        earned *= 1 + int(i) / 100
    return round(earned, 2)
