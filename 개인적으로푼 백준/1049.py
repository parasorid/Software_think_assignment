n, m = map(int, input().split()) # brokenstring, guitarstringbrand
serveral = []
package = []
for i in range(0, m):
    tp, ts = input().split()
    serveral.append(int(ts))
    package.append(int(tp))
cheapest = 0
tempp = min(package)
temps = min(serveral)
while True:
    if n < 6:
        cheapest += min(temps * n, tempp)
        break
    if tempp >= temps * 6:
        cheapest += temps *6
        n -= 6
    else:
        cheapest += tempp
        n-=6


print(cheapest)