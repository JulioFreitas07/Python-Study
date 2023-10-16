# o que pode ter dentro das listas? todos os tipos de dados! a lista por sí só já é um tipo de dado, uma lista
# normalmente as listas são representadas por colchete

#obs: quando eu tenho uma variável com uma string, e atribuo essa string com a função split para outra variavel
# então essa variavel passa a ser do tipo list, conforme exemplo abaixo

fo = 'Lembre-se de substituir nome_do_ramo_origem pelo nome da branch que você deseja mesclar e nome_do_ramo_destino pelo nome da branch em que você deseja fazer o merge. Certifique-se de ter as alterações do repositório atualizadas antes de executar o merge para evitar possíveis conflitos.'

print(type(fo))

po = fo.split()

print(type(po))


#os elementos dentro das listas devem ser separados por vírgula
test_list = ['arroz', False, 'purê de batata', 'bife', True, 'suco de laranja', 3.5, -1555, 2]
precos = [2.65, 7.66]

print(test_list[-1])

#podemos gerar frases com essas informações, não é possível concatenar dados que não sejam str, portanto,
#se formos printar eles, devemos antes formatar os tipos de dados para string com "str()"

print("hoje eu comprei no mercado: " + test_list[0] + " e " + test_list[2] + " e eles custam respectivamente: "
      + "R$" + str(precos[1]) + " e R$" + str(precos[0]))

#Também posso substituir os elementos dentro de uma lista
precos[0] = 0.00

print("hoje eu comprei no mercado: " + test_list[0] + " e " + test_list[2] + " e eles custam respectivamente: "
      + "R$" + str(precos[1]) + " e R$" + str(precos[0]))

#alem disso, também é possível multiplicar uma lista, quando eu multiplico uma lista ela multiplica o tamaho. Por exemplo,
# se eu multiplicar uma lista por dois, cada elemento dentro da lista vai aparecer duas vezes na mesma lista.

print(test_list*3)

#além disso eu também consigo concatenar listas, posso armazená-las em uma nova variável ou apenas exibi-la no terminal.

new_list = precos + test_list #exibindo em uma nova variável
print(new_list)

print(precos + test_list) #printando direto

#parei na aula no minuto 30
