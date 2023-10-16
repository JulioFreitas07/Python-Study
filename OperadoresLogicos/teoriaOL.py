#OPERADORES ARATIMETICOS

# Soma +
# Subtração -
# Multiplicação *
# Divisão /
# Divisão // "retorna somente a parte inteira"
# Resto das divisões %
# Potência **

# Exemplo: No momento, as ações da PETR4 estão cotadas a 23.07 e as da VALE3 a 85.75. No mesmo dia, você fez duas
# aquisições: 100 de PETR4 e mais 200 de VALE3. Qual o valor que você investiu neste dia.

price_petr4 = 23.07
quantity_petr4 = 100
investment_petr4 = price_petr4*quantity_petr4

price_vale3 = 85.75
quantity_vale3 = 200
investment_vale3 = price_vale3*quantity_vale3

total_invested_day = investment_vale3+investment_petr4
print(total_invested_day)

# sabendo o valor total investido, e o valor de compra da VALE3, quanto foi investido em PETR4?

investment_value_found = (total_invested_day-investment_vale3)
print(investment_value_found)

# sabendo o valor investido em PETR4 e o número de ações compradas, qual era a cotação de PETR4 no momento da compra?

quotation_found_petr4 = investment_petr4/quantity_petr4
print(quotation_found_petr4)

#Suponha que eu tenha R$4000 na carteira. Qunatas ações de VALE3 eu consigo comprar?

account_balance = 4000

quantity_available_vale3_stocks = account_balance//price_vale3 #usado o operador para fazer divisão para retornar sem o resto
print(quantity_available_vale3_stocks)

# vamos utilizar os R$4000 da nossa conta de investimentos para aplicar em sua maioria em papéis de VALE3.
# vamos utilizar o que sobrar para comprar algum outro papel mais barato.
# Quantas ações da MGLU3 nós conseguimos comprar? obs MGLU3 custa R$2.82

price_mglu3 = 2.82

# account_balance_after_purchase = account_balance-(quantity_available_vale3_stocks*price_vale3)
# quantity_available_mglu3_stocks=account_balance_after_purchase//price_mglu3
# print(quantity_available_mglu3_stocks)

# resolvendo o exercício acima usando o sinal de resto da divisão "%"

divide_remainder = account_balance % price_vale3
print(divide_remainder)

quantity_available_mglu3_stocks = divide_remainder // price_mglu3
print(quantity_available_mglu3_stocks)

#potenciação

potenciacao = 2**2
print(potenciacao)

############################################################################################################################

#Operações Lógicas


#Operadores Comparativos
# igualdade == também poder ser usado como 'is'
# diferença != também poder ser usado como 'is not'
# maior >
# menor <
# maior ou igual >=
# menor ou igual

#exemplo: vamos testar se o valor investido na PETR4 foi igual ao investimento feito em VALE3

print(investment_petr4 == investment_vale3)

#exemplo: vamos testar se o valor investido na PETR4 foi diferente ao investimento feito em VALE3
print((investment_petr4 != investment_vale3))

#exemplo: vamos testar se o valor investido na PETR4 foi menor ou igual ao investimento feito em VALE3
print((investment_petr4 <= investment_vale3))

#exemplo: vamos testar se o valor investido na PETR4 foi maior ou igual ao investimento feito em VALE3
print((investment_petr4 >= investment_vale3))

# testando essas condições com strings

stock01 = 'MAGLU3'
stock02 = 'VALE3'

# para Strings podemos usar somente os operadores == e !=

print(stock01 == stock02)
print(stock01 != stock02)


#operadores condicionais

# or (ou)
# and (e)
# not

#utilizando operador and (para dar true, ambos devem ser true)

quantity_maglu3 = 21
quantity_iren3 = 18

print(quantity_petr4 < quantity_vale3 and quantity_maglu3 > quantity_iren3)
print((quantity_petr4 < quantity_vale3) and (quantity_maglu3 > quantity_iren3) and (quantity_maglu3 < quantity_vale3))

#podemos usar o operador and varias vezes e ele pode ser trocado por & que é a mesma coisa

print((quantity_petr4 < quantity_vale3) & (quantity_maglu3 > quantity_iren3) & (quantity_maglu3 < quantity_vale3))


#utilizando operador or (para dar true, somente uma das duas deve ser true

print(quantity_petr4 == quantity_vale3 or quantity_maglu3 != quantity_iren3)

#podemos usar | no lugar de or, mas as operações comparativas devem estar limitadas por parânteses

print((quantity_petr4 == quantity_vale3) | (quantity_maglu3 != quantity_iren3))


