a = 70
b = 50


for i in range(a):
    print(b, "x", i+1, "=", (i+1) * b)   #stops the loop
    if (i == 9):
        break
print("Y")
    
for z in range(15):
    if (z == 9):        #skips the iteration
       continue
    print(z)

for m in range(a-b):
    print(m)
    if (m >= 10):
        break