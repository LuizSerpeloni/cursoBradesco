notaA = float(input('Informe a primeira nota: '))
notaB = float(input('Informe a segunda nota: '))

# Calcula média:
mediafinal = (notaA + notaB) / 2

# Verificação
if mediafinal >= 7.0:
    print('A média: %.1f - Aprovado ' % mediafinal)
else:
    print('A média: %.1f - Reprovado ' % mediafinal)