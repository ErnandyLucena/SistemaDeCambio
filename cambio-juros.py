def converter_moeda(valor, moeda_origem, moeda_destino, taxas_cambio):
    if (moeda_origem, moeda_destino) in taxas_cambio:
        taxa = taxas_cambio[(moeda_origem, moeda_destino)]
        valor_convertido = valor * taxa
        valor_juros = valor_convertido * 0.10  
        valor_final = valor_convertido + valor_juros
        return valor_final
    else:
        return None

def exibir_taxas_cambio(taxas_cambio):
    print("Taxas de câmbio disponíveis:")
    for (moeda_origem, moeda_destino), taxa in taxas_cambio.items():
        print(f"1 {moeda_origem} = {taxa:.2f} {moeda_destino}")

taxas_cambio = {
    ('USD', 'BRL'): 5.30,
    ('BRL', 'USD'): 0.19,
    ('EUR', 'BRL'): 6.20,
    ('BRL', 'EUR'): 0.16,
    ('USD', 'EUR'): 0.85,
    ('EUR', 'USD'): 1.18
}

exibir_taxas_cambio(taxas_cambio)

valor_original = float(input("Digite o valor a ser convertido: "))
moeda_origem = input("Digite a moeda de origem (ex: USD, BRL, EUR): ").upper()
moeda_destino = input("Digite a moeda de destino (ex: USD, BRL, EUR): ").upper()

resultado = converter_moeda(valor_original, moeda_origem, moeda_destino, taxas_cambio)

if resultado is not None:
    print(f"{valor_original} {moeda_origem} equivale a {resultado:.2f} {moeda_destino} com 10% de juros")
else:
    print("Desculpe, não é possível fazer essa conversão.")
