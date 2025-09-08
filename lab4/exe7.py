H0 = float(input())
g = 9.8
t = 0
H = H0

while H >= 0:
    print(f"t = {t}")
    print(f"h = {H:.1f}")
    t += 1
    H = H0 - 0.5 * g * t**2