def converter_moeda(valor, moeda_origem, moeda_destino):
    taxas_cambio = {
        ('USD', 'BRL'): 5.30,
        ('BRL', 'USD'): 0.19,
        ('EUR', 'BRL'): 6.20,
        ('BRL', 'EUR'): 0.16,
        ('USD', 'EUR'): 0.85,
        ('EUR', 'USD'): 1.18
    }

    if (moeda_origem, moeda_destino) in taxas_cambio:
        taxa = taxas_cambio[(moeda_origem, moeda_destino)]
        valor_convertido = valor * taxa
        return valor_convertido
    else:
        return None

valor_original = float(input("Digite o valor a ser convertido: "))
moeda_origem = input("Digite a moeda de origem (ex: USD, BRL, EUR): ").upper()
moeda_destino = input("Digite a moeda de destino (ex: USD, BRL, EUR): ").upper()

resultado = converter_moeda(valor_original, moeda_origem, moeda_destino)

if resultado is not None:
    print(f"{valor_original} {moeda_origem} equivale a {resultado:.2f} {moeda_destino}")
else:
    print("Desculpe, não é possível fazer essa conversão.")
