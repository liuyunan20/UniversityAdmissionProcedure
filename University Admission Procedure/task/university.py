applicants_num = int(input())
accept_num = int(input())
applicants = [input().split() for x in range(applicants_num)]
applicants.sort(key=lambda x: (-float(x[2]), x[0], x[1]))
print("Successful applicants:")
for x in range(accept_num):
    print(f"{applicants[x][0]} {applicants[x][1]}")
