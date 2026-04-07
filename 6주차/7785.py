u_status = {}
enterlist = []
n = int(input())
for i in range(0, n):
    name, status = input().split()
    u_status[name] = status
for key in u_status:
    if u_status[key] == "enter":
        enterlist.append(key)
enterlist.sort(reverse=True)
print(*enterlist, sep= "\n")