def cod(x):
    asc = [ord(char)-64 for char in x]
    return asc

def soma_dig(y):
    digitos=str(y)
    soma=0
    for i in digitos:
        soma += int(i)
    return soma

def soma_impar(s, k):
    resultado = ""
    
    for char in s:
        novo_char = ord(char) + 26
        
        if novo_char > 90:
            novo_char -= 26 
            
        resultado += chr(novo_char) 
    
    return resultado

def soma_par(s, k):
    resultado = ""
    
    for char in s:
        novo_char = ord(char) + 7
        
        if novo_char > 90:
            novo_char -= 26
            
        resultado += chr(novo_char)
    
    return resultado

codigo = 'PLANETAKIXZTLNLKORBITAKOTVNHKRADIACAO'
resultado = len(codigo)
print(f'Resultado: {resultado}')

letra_espaco = "K"

print(f'Letra que corresponde ao espaço: {letra_espaco}')

print(f'Código inicial: {codigo}')

codigo_com_espaco = codigo.replace(letra_espaco, ' ')

print(f'Código final c: {codigo_com_espaco}')

resultado2 = cod(codigo_com_espaco)
print(f'{resultado2}')

valor_codigo_com_espaco = [0 if valor == -32 else valor for valor in resultado2]
print(f'{valor_codigo_com_espaco}')

separados = []

for i in valor_codigo_com_espaco:
    for j in str(i):
        separados.append(int(j))

#separados=[3, 2, 1, 2, 2, 7, 2, 0, 1, 7, 1, 1, 6, 7]

print(f'Separados: {separados}')



soma_digitos_pares = sum(valor for valor in separados if valor % 2 == 0)
print(soma_digitos_pares)
chave_par = (soma_digitos_pares%26)+1
print(f'Chave Par: {chave_par}')

soma_digitos_impares = sum(valor for valor in separados if valor % 2 == 1)
print(f'Soma dos digitos impares: {soma_digitos_impares}')
chave_impar = (soma_digitos_impares%26)+1
print(f'Chave Ímpar: {chave_impar}')

palavras_codigo = codigo_com_espaco.split(' ')
print(f'Palavras do código: {palavras_codigo}')

palavras_codigo.insert(0,'PRIMEIRO')
print(f'Palavras do código: {palavras_codigo}')

#print(palavras_codigo[1])
#print(palavras_codigo[3])

print(f'Soma da palavra {palavras_codigo[1]}: {soma_impar(palavras_codigo[1], chave_impar)}')
print(f'Soma da palavra {palavras_codigo[2]}: {soma_par(palavras_codigo[2], chave_par)}')
print(f'Soma da palavra {palavras_codigo[3]}: {soma_impar(palavras_codigo[3], chave_impar)}')
print(f'Soma da palavra {palavras_codigo[4]}: {soma_par(palavras_codigo[4], chave_par)}')
print(f'Soma da palavra {palavras_codigo[5]}: {soma_impar(palavras_codigo[5], chave_impar)}')

palavras_desc = []

print(palavras_codigo)
for i in range(len(palavras_codigo)):
    if i % 2 == 1:
        palavras_desc.append(soma_impar(palavras_codigo[i], chave_impar))
    else:
        palavras_desc.append(soma_par(palavras_codigo[i], chave_par))

print(palavras_desc)



