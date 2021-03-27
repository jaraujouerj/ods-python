from ods import Pilha

p = Pilha()

p.push(3)
p.push(2)
print(p)
print(p.pop())
print(p.pop())
print(p)
print(p.pop())

with open("poema.txt", "r") as f:
    poema = f.read()

linhas = poema.split("\n")

p2 = Pilha()
for lin in linhas:
    p2.push(lin)

while p2.size() != 0:
    print(p2.pop())
