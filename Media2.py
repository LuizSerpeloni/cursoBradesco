def lernotas():
    n=float(input('Digite uma nota para o aluno(a): '))
    return n

def resultado(n1,n2):
    media = (n1+n2) / 2
    print('Nota 1: ', n1)
    print('Nota 2: ', n2)
    print('Média:', media, 'Resultado: ', end="")
    if media >= 7:
        print('Aprovado')
    else:
        print("Reprovado")

n1 = lernotas()
n2 = lernotas()
resultado(n1,n2)