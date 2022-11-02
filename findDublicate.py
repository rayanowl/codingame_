# Input :5 5 3 2 1 1 1
# Output: 5



n=input().split()
print(sum((n.count(c)==2)*int(c)for c in n)//2)





n=input().split()
print(sum([int(a)for a in set(n)if n.count(a)==2]))




n=input().split()
print(int(sum(int(i)/2 for i in n if n.count(i)==2)))



n=input().split(" ")
print(sum([int(x) for x in n if n.count(x)==2])//2)