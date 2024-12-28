peca1 = []
peca2 = []

peca1.append(int(input()))
peca1.append(int(input()))
peca1.append(float(input()))

peca2.append(int(input()))
peca2.append(int(input()))
peca2.append(float(input()))

print(f"VALOR A PAGAR: R$ {(peca1[1]*peca1[2]+peca2[1]*peca2[2]):.2f}")