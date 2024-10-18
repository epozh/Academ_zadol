def count_beautiful_pairs(S, P):
    beautiful_pairs = 0
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            if (S[i] + S[j]) in P:
                beautiful_pairs += 1

    return beautiful_pairs


f = open('input.txt')
s1 = f.readline().split()
n = int(s1[0])
k = int(s1[1])
kamni = f.readline()
good_kamni = []
for i in range(k):
    para = f.readline().rstrip()
    good_kamni.append(para)
with open("output.txt", "w") as file:
    file.write(str(count_beautiful_pairs(kamni, good_kamni)))
