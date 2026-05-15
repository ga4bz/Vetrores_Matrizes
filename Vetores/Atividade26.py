import math

vetor = [float(input(f"vetor[{i+1}]: ")) for i in range(10)]

media = sum(vetor) / len(vetor)

temp = 0
for x in vetor:
    temp += (x - media) ** 2

desvio = math.sqrt(temp/(len(vetor) - 1))

print(f"\nMédia: {media:.4f}")
print(f"Desvio Padrão: {desvio:.4f}")