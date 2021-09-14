import math
import time

tpi = math.pi
n = int(input("How many terms to generate? "))
print("\n")
nt = n / 10000
perc = 0
d = 0
s = 0
t1 = time.time()
for i in range(n):
    d = d + 1
    f = (1 / (d**2))
    s = s + f
    if (i + 1) % nt == 0:
        perc = perc + 0.01
        print(f"Computing... {round(perc, 2)}%      ", end="\r")
    else:
        pass

cpi = math.sqrt((s * 6))
pererr = ((tpi - cpi)/tpi)*100

t2 = time.time()
hour = int(math.floor((t2 - t1) / 60 / 60))
minute = int(math.floor(((t2 - t1) / 60) % 60))
second = int(math.floor((t2 - t1) % 60))
t3 = f"{hour:02d}:{minute:02d}:{second:02d}"
print(f"Time Elapsed:  {t3}\n"
      f"Highest Term:  1/({d}^2)\n"
      f"Calculated pi: {cpi:.30f}\n"
      f"True pi:       {tpi:.30f}\n"
      f"% Error:       {pererr:.30f}%\n")
input("Press ENTER to close...")
