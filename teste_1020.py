
I = input()

anos = int(I) // 365
meses = (int(I) - (anos*365))//30
dias = int(I) - (anos*365) - (meses*30)

print(f'{anos} ano(s) \n{meses} mes(es) \n{dias} dia(s)', end="")
