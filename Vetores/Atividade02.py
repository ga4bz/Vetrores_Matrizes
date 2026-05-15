A = [0] * 6

for i in range(len(A)):
    num = input(f"Digite o {i+1}º número: ")
    while not num.isdigit():
         num = input(f"Digite o {i+1}º número novamente: ")
    num = int(num)
    A[i] = num

print(A)