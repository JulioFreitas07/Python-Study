#Strings são coleções de caracteres


# O símbolo de + quando está em contexto de variáveis do tipo String faz a operação de concatenar

country1 = "Brazil"
country2 = "Africa"
print(country2+country1)

# Para saber o tipo da variáveil pode-se usar a função type()
print(type(country2))


#Operações de indexação (indexing) e fatiamento(slicing)

manchete = ("MXRF11, HGLG11, URPR11 e mais 49 FIIs pagam dividendos hoje; retornos chegam a 1,25% ao mês "
            "E mais: dono de livraria vende tudo e se aposenta com dividendo de FIIs; “é preciso disciplina e consistência")

#Para saber a quantidade de string usa-se a função len (len remete ao length do inglês, de comprimento)

print(len(manchete))

#consigo acessar os caracteres das strings por index: (espaço é considerado string)

print(manchete[0])

# podemos expandir o index para fazer busca na string:

print(manchete[0:6]) #o primeiro número é inclusivo, o segundo é exclusivo

#posso pedir para o python trazer o texto de uma posição específica até o último caracter, para fazer isso
# basta não informar no colchete o index exclusivo.
print(manchete[5:])

# para pedir para o python me informar toda string, posso não informar nem o index inclusivo e nem o exclusivo)
print(manchete[:])

#ao colocar o index negativo na posição do index exclusivo, eu estou pedidindo para o python retirar aquela quantidade
#de caracteres da minha String
print(manchete[:-1])
print(manchete[15:-100])

#o terceiro argumento refere-se ao "pulo", ou seja, se você colocar "2" como terceiro argumento, o comando vai percorrer
#sua String pulando de 2 em 2 caracteres. E, se você passar esse argumento como negativo, o comando vai te retornar
#o inverso da sua operação, nesse caso, o index incluso passa a ser o index exclusivo
print(manchete[::-1])
print(manchete[::4])



