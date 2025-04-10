G, S, C = (int(i) for i in input().split())
total_cost = G*3+S*2+C*1

output = ""
if total_cost >= 8:
    output += "Province"
elif total_cost >= 5:
    output += "Duchy"
elif total_cost >= 2:
    output += "Estate"

if output:
    output += " or "

if total_cost >= 6:
    output += "Gold"
elif total_cost >= 3:
    output += "Silver"
else:
    output += "Copper"

print(output)
