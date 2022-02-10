score_1 = int(input())
score_2 = int(input())
score_3 = int(input())
score_mean = (score_1 + score_2 + score_3) / 3
print(score_mean)
if score_mean >= 60:
    print("Congratulations, you are accepted!")
else:
    print("We regret to inform you that we will not be able to offer you admission.")
