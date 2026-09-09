n = int(input())

numeros = list(map(int, input().split()))

dois = 0
tres = 0
quatro = 0
cinco = 0

for numero in numeros:
    
    if numero % 2 == 0:
        dois += 1
    
    if numero % 3 == 0:
        tres += 1
        
    if numero % 4 == 0:
        quatro += 1
        
    if numero % 5 == 0:
        cinco += 1
        
print(f"{dois} Multiplo(s) de 2")
print(f"{tres} Multiplo(s) de 3")
print(f"{quatro} Multiplo(s) de 4")
print(f"{cinco} Multiplo(s) de 5")
