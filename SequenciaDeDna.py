import re

# entrada
dna = input("Digite a sequencia de DNA: ")

# processamento

# filtra sequencias invalidas e as remove da analise
dna = re.sub('[^ACTGactg]', '', dna)

dna = dna.upper()

# uso do método de tradução (maketrans) para substituir cada letra pela sua complementar
traducao = str.maketrans('ATCG', 'TAGC')
dna_complementar = dna.translate(traducao)

# saida
print("A cadeia complementar é: " + dna_complementar)