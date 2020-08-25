def imc(cliente):
    p = cliente['peso']
    a = cliente['altura']
    imc = p / (a * a)
    return imc

pessoa = {
    'nome': 'Lucas Alexandre Virginio',
    'idade': 18,
    'peso': 67,
    'altura': 1.72
}

print(imc(pessoa))
