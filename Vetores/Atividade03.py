A = [0] * 10
B = [0] * 10

for i in range(len(A)):
    A[i] = float(input(f"Digite o {i + 1}º número: "))
    B[i] = A[i]** 2

print(f"Número: {A}")
print(f"Quadrado dos números: {B}")