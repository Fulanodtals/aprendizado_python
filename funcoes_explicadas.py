# aprendizado_python
explicacoes do uso de varias funcoes em python.
(alguns scripts nao foram revisados por isso podem
nao funcionar corretamente.)




# print e input
'''
nome = input('digite seu nome: ')
print('é um prazer te conhecer, {}!'.format(nome))
#só usa o input quando for digitar algo que n nessecite de valor

no print em vez de criar varios prints pode se colocar no lugar
que quiser quebrar a linha um \n ou \r e para colocar na mesma
linha coloca no final(, end=' ') assim as linhas de cima e de
cima e de baixo e a de cima.
'''





# int e format
'''
a = int(input('digite um valor: '))
b = int(input('digite outro valor: '))
print('a soma entre {} + {} = {}'.format(a, b, a+b))
#format é a msm coisa que %i só que melhor
'''





# type
'''
type sao os tipos de numero que sao:
int == numeros inteiros, positivos e negativos
float == numeros com vigula
bool == True e False / verdadeiro e falso
str == letras ou palavras que estao em aspas ''/""

tambem o tipo primitivo e tem eles por exemplo print(n.isnumeric())
ai ele verifica se a variavel é numerico, a lista de traducao é
.isnumeric() == se tem numero
.isalpha == se tem letra
.isalnum == se tem letra e numero
.isupper == se tem só letra maiuscula
.islower == se só tem letra minuscula
.isprintable == se pode ser impresso
.isspace == se tem espaco 

um exemplo:

a = input('digite uma palavra')
print('o tipo primitivo desse valor é', type(a))
print('tem espaços? ', a.isspace())
print('é um numero? ', a.isnumeric())
print('é alfabetico? ', a.isalpha())
print('é alfanumerico?', a.isalnum())
print('esta em maiuscula? ', a.isupper())
print('esta em minuscula? ', a.islower())
print('esta capitalizada?', a.istitle())

assim aparecera em bool(True/False)
'''





# operadores aritmeticos, ordem de precedencias e funcionalidades

'''
+ == adicao | 5 + 2 == 7
- == subtracao | 5 - 2 == 3
* == multiplicacao | 5 * 2 == 10
/ == divisao | 5 / 2 == 2,5
** == potencia | 5 ** 2 == 20 (5 x 5 (duas vezes))
// == divisao inteira (sem numero quebrado) | 5 // 2 == 2 (sem virgula)
% == resto da divisao | 5 % 2 == 1 (numero quebrado, depois da virgula)

#na 'biblioteca' math(matematiaca) tem as funcoes:
ceil == arredindamento para cima
floor == arredondamento para baixo
trunc == elimina o numero da virgula pra frente sem arredondar
pow == potencia, parecido com a utilidade dos **
sqrt == calcular raiz quadrada
factorial == para calcular o fatorial

1º == () contas que devem ser calculadas primeiro
2º == ** potencias
3º == * > / > // > % sao as sequencias dos que vao ser somadas
4º == + e -
ex:5 + 3 * 2 esta errado pois a multiplicacao estaa cima ou seja
a maneira certa seria 2 * 3 + 5.
com os parenteses a conta tem mais certeza como: 3 * 5 + 4 ** 2 == 31
com parenteses ficaria mais certo na soma pois ela esta depois da * 
assim: 3 * (5 + 4) ** 2 == 243 seria a maneira correta

desafio:
#antecessor e sucessor j
n = int(input('digite um numero: '))
print('o numero sucessor de {} é {} e seu sucessor é {}'.format(n, n - 1, n + 1))
#triplo e dobro:j
n = int(input('digite um numero: '))
print('o dobro de {} é {}, o triplo é {} e a raiz quadrada \n é {:.2f}'.format(n, n*2, n*3, n**n))

#mediaj
n = int(input('digite sua nota do primeiro bimestre: '))
a = int(input('do segundo: '))
s = int (input('do terceiro:'))
d = int(input('e por ultimo do quarto:'))
print('sua media desse ano foi {:.1f} !'.format((n + a + s + d)/4))

conversao:j
m = int(input('digite os mettros que serao convertidos:'))
print('{} metros tem {} centimetros e {} milimetros.'.format(m, m / 100, m / 1000))

#taboada:j
n = int(input('digite um numero inteiro:'))
print('a taboada de {} é')
print('{} x 1 = {}'.format(n, n))
print('{} x 2 = {}'.format(n, n*2))
print('{} x 3 = {}'.format(n, n*3))
print('{} x 4 = {}'.format(n, n*4))
print('{} x 5 = {}'.format(n, n*5))
print('{} x 6 = {}'.format(n, n*6))
print('{} x 7 = {}'.format(n, n*7))
print('{} x 8 = {}'.format(n, n*8))
print('{} x 9 = {}'.format(n, n*9))
print('{} x 10 = {}'.format(n, n*10))

#3,27 convertidos:j
n = float(input('quanto voce tem na carteira? '))
print('voce pode obter us{} dolares'.format(n / 3.27))

#area e litros de tinta:j
l = int(input('qual a largura da parede? '))
h = int(input('qual a altura da parede? '))
a = l * h
print('a parede tem uma area de {} metros² e sera \n gasto {} litros de tinta para pintala'.format(a, a / 2))

#5% de desconto:j
n = int(input('digite o valor do produto: '))
a = (n * 5) / 100
print('a loja oferece 5% de desconto entao ficara R${} '.format(n - a))

#15% de almento:j
n = int(input('digite o valor do seu salario:'))
a = (n * 15) / 100
print('voce recebera um desconto de 15%! \n seu novo salario é de {}'.format(n + a))

'''





# modulos import e From
'''
no python temos a bibliotecas como math(matematica) e podemos
usar suas funcionalidades usando o import:
ex:
import math - vai importar todas as funcionalidades
from math import sqrt - vai inporta apenas uma
from math import sqrt, ceil - com virgula pode adicionar mais.
from math import * - importaera tudo da biblioteca math

pratica:
import math
#podemos colocar tb - from math import sqrt ...
n = int(input('digite um numero: '))
raiz = math.sqrt(n)
#vai pegar da biblioteca math o calculo de raiz quadrada
#se importar a funcao antes se coloca apenas - raiz = sqrt(n)
print(' a raiz de {} é igual a {:.2f}'.format(n, math.ceil(raiz)))
#assim adicionamos o arredondamento na raiz ou x do programa

#portanto se quiser importar outro tipo de biblioteca consulte aula#08

desafio:
#parte inteira:j
from math import ceil
n = float(input('digite um numero:'))
a = ceil(n)
print('a parte inteira do numero {} é {} '.format(n, a-1))

#comprimento da hiótenusa sem o inport:x 
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('a hipotenusa vai medir {:.2f}'.format(hi))

#com o import fica mais facil:x
from math import hypot
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))

#seno coseno e tangente sem from
import math
an = float(input('digite o angulo que voce deseja'))
seno = math.sin(math.radians(an))
print('o angulo de {} tem seno de {:.2f}'.format(an, seno))
cos = math.cos(math.radians(an))
print('o angulo de {} tem cosseno de {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print('o angulo de {} tem congente de {:.2f}'.format(an, tan))

#agora com o from:
from math import radians, sin, cos, tan
an = float(input('digite o angulo que voce deseja'))
seno = sin(radians(an))
print('o angulo de {} tem seno de {:.2f}'.format(an, seno))
cos = cos(radians(an))
print('o angulo de {} tem cosseno de {:.2f}'.format(an, cos))
tan = tan(radians(an))
print('o angulo de {} tem congente de {:.2f}'.format(an, tan))

#escolhe com str:
import random
#ou from random import choice, e apaga o choice abaixo
a = str(input('digite o nome do primeiro aluno: '))
b = str(input('digite o nome do segundo aluno: '))
c = str(input('digite o nome do terceiro aluno: '))
d = str(input('digite o nome do quarto aluno'))
lista = [a, b, c, d]
escolhido = random.choice(lista)
print('o aluno escolhido é {}'.format(escolhido))

#embaralhar srt
import random
# ou from random import shuffle
a = str(input('primeiro aluno: '))
b = str(input('segundo aluno: '))
c = str(input('terceiro aluno:'))
d = str(input('quarto aluno: '))
lista = [a, b, c, d]
random.shuffle(lista)
print(lista)
'''





# cadeias de caracteres

'''
sao frazes que sao colocadas em '',  
e quando colocamos em uma variavel por exemplo
fraze = 'oi seu lindo' e o python guarda a frase
como caracteres tipo o = 0, i = 2, espaco conta tb
espaco = 4 s = 5 e = 6 u = 7 e por ai vai.
fraze = 'sou lindo demais nossa'

#tecnica de fatiamento é pegar a  letra da frase 
do mesmo jeito q for i in range funciona por exemplo
fraze [9] - vai mostrar o caracter nove
fraze[9:15] - vai mostra as letras do caractere 9.
-
ao 14
fraze [9:15:2] vai ir do dove ao 15 caractere pulando
de dois em dois ent ficaria (lindo) l n o
assim podemos dizer que [comeco, final, vezes puladas]
frase[:5] - assim ele comeca do caractere 0 pois esta dps
dos dois pontos, ent vai do 0 ao 4 caractere.
frase[15:] - ele vai comecar do 15 caractere e vai até
o ultimo, sem fim.
fraze[9::3] - ira comecar do nove caractere e ira até
o final pulando de 3 em 3 

#analise
pra saber informacoes da frase:
len(fraze) - o total de caracteres na frase
fraze.count('letra escolhida') - pede pra conatar quantas
veses derivada letra aparecera na frase
fraze.count('letra', 0, 13) - assim utilizamos fatiamento,
mostrara quantas derivada letra aparecera do 0 ao 12 caractere
fraze.find('abc') - assim ele procura derivara palavra ou 
letra e mostra o caractere de cada letra.
fraze.find('android') - se colocar dentro do find algo que
nao existe aparecera -1 que n foi encontrado
'curso' in fraze - ele fala se tem a palavra curso na fraze

#transformacao
fraze.replace('palavra da frase','palavra q substituira') - 
ele vai subtitui a palavra por otra
fraze.upper() - ele na fraze vai fazer todas as letras que estao 
em minuscula virarem maiuscula
fraze.lower() - faz o contrario do upper
fraze.capitalize() - vai trasformar todas as letras em minuscula
menos a primeira que ira ficar em maiucula.
fraze.title() - fara o mesmo que captalize so que em todas as palavras
fraze.strip() - ele remove os espacos antes e depois da frase
que serao inuteis.
fraze.rtrip() - remove apenas os espacos depois da frase
fraze.lstrip() - remove apenas os espacos antes da frase
fraze.split() - ele faz cada palavra reiniciar o processo de 
contacao e cada palavra vai ser - oi=0 seu=1 e lindo=2

juncao:
'-'.join(fraze) - ele vai fazer com que todos os espaco da fraze
se separem(nos espacos) tranformarem em tracos

pratica:
fraze = '  oi seu lin do e gostoso  '
print(fraze[:9:2])

print(''usando as aspas triplas
podemos escrever  o que quisermos e o python 
assimilara como um texto deixando melhor
do que se usaçe varios prints'')

desafio:
#funcoes
n = str(input('digite seu nome completo: ')).strip()
#com o strip assim ele ja vai fatiar as palavras
print('seu nome apenas com letras minuscula é {}'.format(n.upper()))
print('seu nome apenas com letras minusculas sao {}'.format(n.lower()))
print('seu nome tem no total {} letras'.format(len(n) - n.count(' ')))
#com o len ele conta as letras junto com os espacos, menos os espacos (- n.count)
#para saber a quantidade de letras na primeira palava fazemos:
#n.find(' ') e parara de ler no primeiro espaco
print('a primeira letra do seu nome é {}'.format(n.find(' ')))
#mas pode fazer assim tb
separa = n.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

#u d c m:
n = int(input('digite um numero: '))
print('analizando o numero {}'.format(n))
print('unidade: {}'.format(n % 10))
print('dezena: {}'.format((n // 10)% 10))
print('centena: {}'.format((n // 100) % 10))
print('milhar: {}'.format((n // 1000) % 10))

#cidade:
cid = str(input('em que cidade voce nasceu: ')).strip()
print(cid[:5] == 'SANTO')

#procurar nome dentro da frase
n = str(input('digite seu nome')).strip()
print('seu nome tem silva? {}'.format('silva' in n.lower()))

#achar informacoes:
f = str(input('digite uma frase: ')).lower().strip()
f = f.strip()
print('a letra A apareceu {} vezes na frase.'.format(f.count('a')))
print('a primeira letra a apareceu na posicao {}'.format(f.find('a')+1))
print('a ultima letra a aparecel a posicao {}'.format(f.rfind('a')+1))

#primeiro e ultima palavra:
n = str(input('digite seu nome completo: ')).lower()
print('muito prazer em te conhcer!')
a = n.split()
print('seu primeiro nome é {}'.format(a[0]))
print('seu ultimo nome é {}'.format(a[len(a)-1]))
'''


# condicoes:
'''sao estruturas com if e else
if condicao:
    bloco True
else condicao:
    bloco False

assim podemos fazer dois programas em um
e adicionando variavel:

tempo = int(input('quandtos anos tems seu carro')
if tempo <=3:
    print('carro novo')
else:
    print('carro velho')
print('--fim--')

podemos fazer tambem uma condicao simplificada:
tempo = int(input('quantos anos tem seu carro? ')
print('carro novo') if tempo<=3 else'carro velho')
print('fim')
porem essa maneira nao é tao recomendada por causa 
da leitura que pode ser mais complicada.
porem ela é compacta e algo q custaria muitas linhas
em apenas uma se resolve:

distancia = int(input('qual a distancia da viagem: '))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('o preco da sua passagem sera de {}'format(preço))

pratica:
n = int(input('qual seu nome? ')
if n == 'joao':
    print('que nome lindo!')
else:
    print('seu nome é tao normal')
print('bom dia, {}'.format(n)

desafios:
#descubra o numero:

import random
n = random.randint(0,5)
print('vou pensar em um numero entre 0 e 5. tente adivinhar... \n')
a = int(input('em que numero eu pensei'))
if a == n:
    print('voce ganhou o numero era {}!'.format(n))
else:
    print('voce perdeu, o numero era {} e nao {}'.format(n, a))

#multa de transito
v = int(input('qual a velocidade atual do carro: '))
m = (v - 80) * 7
if v > 80:
    print('vc foi multado, sua multa é de {}, temnha mais cuidado'.format(m))
print('ok, dirija com cuidado')

#par ou impar:
n = int(input('digute um nmero: '))
a = n % 2
if a == 0:
    print('o numero {} é par'.format(n))
else:
    print('o numero {} pe impar'.format(n))
  
ano:
from datetime import date
ano = int(input('digite o ano que quer analizar: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é bixesto'.format(ano))
else:
    print('o ano {} nao é bixesto'.format(ano))
  
maior e menor simplificado:
a = int(input ('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
menor = a
if b < a and b <  c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('o menor valor é {}'.format(menor))
print('o maior valor é {}'.format(maior))

#desconto e almento:
n = float(input('qual o valor do salario do funcionario? '))
if n <= 1250:
    a = (n * 15) / 100
else:
    a = (n * 10) / 100
print('seu salario q era de {} e com o almento ficara R${}'.format(n, a))

#é triangulo?
a = int(input('digite o valor do primeiro lado: '))
b = int(input('digite o valor do segundo lado: '))
c = int(input('digite o valor do terceiro lado: '))

if a < (b + c) and b < (a + c) and c < (a + b):
    print('os seguimento a cima podem formar um triangulo')
else:
    print('os seguimentos a cima nao podem formar um triangulo')
'''





#cores no terminal:

'''
nos podemos aplicar cores nas palavras no python
usando o codigo ansi para cores, assim:
\033[m
e dentro desse codigo podemos colocar o codigo 
da cor, entre o ponchete e o m podemos colocar 3 codigos
\033[style:text:backm 
style é o estilo da fonte como negrito
text cor do texto
back cor de fundo
\033[0:33:44m
'da mesma maneira que funciona as cadeias de caracteres'

style:
0 = nada - none
1 = negrito - bold
4 = sublinhado - underline
7 = trocar a cor da letra com a do fundo - negative
'exitem muito mais'

text:
30 = branco
31 = vermelho
32 = verde
33 = amarelo 
34 = azul
35 = rosa
36 = ciano
37 = cinza

'se quiser mais apenas importe uma biblioteca'

back:
40 = branco
41 = vermelho
42 = verde
43 = amarelo 
44 = azul
45 = rosa
46 = ciano
47 = cinza

podemos colocar a letra preda usando isto:
\033[7:30m
como colocamos sete ele trocara o fundo preto para a letra
deixandoa preta :)

entao no print ela fica assim
print('\033[0:30:45molá mundo!\033[m')
utilize o \033[m para fechar 

etc funcoes.
'''






# condicoes aninhadas
'''
quando usamos o if e o else temos apenas duas opcoes
porem quando temos tres ou mais opcoes utilizamos o elif
que preferencialmente descarta o else, o utilizamos quantas
quiser:

nome = str(input('qual o seu nome: '))
if 'anta' in nome:
    print('que nome lindo')
elif name == 'pedro' or nome == 'maria':
    print('tem cara de gtz')
elif 'maria' in name:
    print('madalena?')
else:
    ('nome normat, aff')
print('bom dia {}'.format(nome))
dessa maneira ulilizamos o elif:)


#desafio:
#imprestimo pra casa
a = int(input('digite o primeiro valor: '))
b = int(input('digite o segundo numero: '))
if a > b:
    print('{} é maior que {}'.format(a, b))
elif a < b:
    print('{} é maior que {}'.format(b, a))
elif a == b:
    print('{} é igual a {}'.format(a, b))

#alistamento:
i = int(input('digite a sua idade:'))
if i < 18:
    print('voce ainda é muito novo para se alistar, falta {} anos'.format(18 - i))
elif i == 18:
    print('ja ta na hr de se alistar')
elif i > 18:
    print('voce deveria ter se alistado antes, se passou {} anos da data'.format(i - 18))

#nota:
n = float(input('digite sua primeira nota: '))
no = float(input('digite a segunda nota: '))
nota = (n + no) / 2
if nota < 5:
    print('voce foi reprovado, seu burro')
elif nota > 5 and nota < 6.9:
    print('voce esta de recuperacao')
elif nota >= 7:
    print('voce foi aprovado')

categorias:
i = int(input('digite a idade para obter sua categoria: '))
if i <= 9:
    print('sua categoria é mirim')
elif i > 9 and i < 14:
    print('sua categoria é infantil')
elif i >= 14 and i < 19:
    print('sua categoria é junior')
elif i == 19:
    print('sua categoria é senior')
elif i == 20:
    print('sua categoria é master')

#imc: 
p = float(input('digite seu peso: '))
a = float(input('digite sua altura: '))
imc = p / (a * 2)
if imc < 18.5:
    print('voce esta abaixo do peso ideal')
elif imc > 18.5 and imc < 25:
    print('voce esta com o peso ideal')
elif imc > 25 and imc < 30:
    print('voce esta com sobrepeso')
elif imc > 30 and imc < 40:
    print('voce esta obeso')
elif imc > 40:
    print('voce esta com obesidade morbita')

#condicao de pagamento:
p = float(input('digite o valor do produto'))
print('qual meio voce deseja usar:')
print('1 = a vista em dinheiro/cheque (10% de desconto)
2 = a vista no cartao(valido a 5% de desconto)
3 = 2x no cartao.
4 = 3x ou mais no cartao (20% de juros)
')
r = int(input('qual meio voce qué? '))
if r == 1:
    print('sua compra ficom com um valor de R${} '.format(p - ((p * 20) / 100)))
elif r == 2:
    print('sua compra ficou com um valor de R${} '.format(p - ((p * 5) / 100)))
elif r == 3:
    print('sua compra ficou com um valor de R${}',format(p))
elif r == 4:
    print('sua compra ficou com um valor de R${}'.format(p + ((p * 20) / 100)))

#pedra papel e tesoura
print('pedra papel e tesolra')
import random
n = random.randint(1,3)
print('1 = pedra
2 = papel
3 = tesoura \n')
import time
c = int(input('o que voce escolhe: '))
print('vamos la!')
time.sleep(1)
print('pedra')
time.sleep(0.5)
print('papel')
time.sleep(0.4)
print('tesoura!')
time.sleep(0.7)
if n == c:
    print('PARABENS! voce ganhou')
else:
    print('ha eu ganhei, sinto muito perdedor')

#conversoes:
n = int(input('digite um numero inteiro'))
print(''escolha uma das bases bara comversao
1 - converter para binario
2 - coponverter para octal
3 - converter ára hexadecimal'')
opcao = int(input('qual a sua opcao: '))
if opcao == 1:
    print('{} convertido para binario é igual a {}'.format(n, bin(n)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(n, oct(n)[2:]))
elif opcao == 3:
    print('{} convertido para octal é {}'.format(n, hex(n)[2:]))
else:
    print('opcao invalida, tente novamente!')

#continuacao do exercicio 35:
a = int(input('digite o valor do primeiro lado: '))
b = int(input('digite o valor do segundo lado: '))
c = int(input('digite o valor do terceiro lado: '))

if a < (b + c) and b < (a + c) and c < (a + b):
    print('os seguimento a cima podem formar um triangulo ', end='')
    if a == b == c:
        print('equilatero')
    if a != b != c != a:
        print('escaleno')
    else:
        print('isoceles')
else:
    print('os seguimentos a cima nao podem formar um triangulo')

'''





#estrutura de repeticao - for in range:
'''
utilizamos esse laco de repeticao controlavel quando
percebemos que um comando se repete e para encurtalo
ou melhoralo usamos as estruturas de repeticao como o 
for n in range(1, 10, 0) - laco n no intervalo(de 1 a 10, interacao )
olhe a demonstracao:
for n in range(0,10):
    print('oi')
print('bye')
dessa maneira aparecera 10x oi na tela e no final, bye
entao tudo oq aparecer dentro do for in range sera repetido
como uma pergunta:
for n in range(0, 5):
    n = int(input('digite o numero: ')
e aparecera 5 vezes a pergunta

fazemos calculos com os ciclos:
calc = 0 
for i in range(0, 3):
    n = int(input('digiete o numero: ')) 
    calc += 1
print('o calculo de todos os numeros é {}'.format(calc))
dessa maneira faremos os cauculos.

 
desafios:
#contagem regresiva:
from time import sleep
print('vamos para a contagem regresivaa')
sleep(1.5)
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('FELIZ ANO NOVO')

#pares entre 1 e 50:
print('os numeros pares entre 1 a 50 sao:')
for i in range(1, 51, 2):
    print(i - 1)

#soma impar tres:
a = 0
for c in range(1, 500, 2):
    if (c % 3) == 0:
        a += c
print(a)

#taboada:
n = int(input('qual numero voce deseja ver a taboada: '))
for i in range(1, 11,):
    print('{}x = {}'.format(i, i * n))
    
#soma só os par:
soma = 0
for i in range(0, 6):
    n = int(input('digite um numero inteiro: '))
    if (n % 2) == 0:
        soma += n

if soma > 0:
    print('a soma dos numeros pares é {}'.format(soma))
else:
    print('nao tem numero par')

#maior ou menor d 21:
from datetime import date
ano = date.today().year
cont = 0
ant = 0
for i in range(0,7):
    nasc = int(input('em que ano a {}ª pessoa nasceu'.format(i + 1)))
    idade = ano - nasc
    if idade >= 21:
        cont += 1
    elif idade < 21:
        ant += 1
print('{} pessoas sao de maior\n{} pessoas sao de menor'.format(cont, ant))


#pa 
cmc = int(input('digite o primeiro termo: '))
raz = int(input('digite a razao'))
dec = cmc + (10 - 1) * raz
for i in range(cmc, dec + raz, raz):
    print('{} '.format(i), end=' - ')
print('fim')

#primo ou n:
n = int(input('digite um numero inteiro:'))
vez = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end=' ')
        vez += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(i), end=' ')

print('\no numero {} foi divisivel {} vezes'.format(n, vez))
if vez == 2:
    print('e por isso é primo')
else:
    print('e por isso n é primo')
    
#palindromo:
frase = str(input('digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] / ''
#for letra in range(len(junto)-1, -1, -1)
print('o inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('temos um palindromo')
else:
    print('a frase nao é um palindromo')
    
#maior e menor:
maior = 0
menor = 0
for p in range(0,5):
    peso = float(input('digite o peso da {}ª pessoa'.format(p + 1)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso lido é de {}'.format(maior))
print('o menor peso lido é de {}\n'.format(menor))

#estrator de dados:
ida, ma, mn, mu = 0, 0, 0, 0   
for i in range(0, 4):            
    print('   {}ª pessoa'.format(i + 1))      
    nome = str(input('nome: ')).strip()    
    idade = int(input('idade: '))       
    sexo = str(input('sexo(m/f): ')).strip()             
    ida += idade            
    if i == 1 and sexo in 'Mm':           
        ma = idade          
        nm = idade    
    if sexo in 'Mm' and idade > ma: 
        ma = idade            
        nm = nome       
    if sexo in 'Ff' and idade < 20:             
        mu += 1      
print(ma)            
print(nm)          
print(ida / 4)    
print('a media de idade do grupo é de {} anos'.format(ida
print('o homem mais velho tem {} anos e se chama {}'.form
print('tem {} mulheres com menos de 20 anos '.format(mu))
'''





#estrutura de repeticao - while:
'''
utilizamos while gerealmente para algo que nao temos certeza
do fim pois no for i in range temos o cubiculo () de 0 a n, 
e ai que entra o while, ele é um loop com limite definido ou
nao:
c = 0
while c < 10:
    print(c,end=' ')
    c += 1
print('fim')

dessa maneira o contador ira de 0 ao 9 numerandoo
tambem podemos fazer isso:
r = 'Ss'
while r == 'Ss':
    input('digite um valor')
    r = str(input('quer continuar?(s/n) ')).upper
print('fim')
dessa maneira ira perguntar um valor até o r == n
o que é mais eficas, simples e melhor.

#exercicio:
sexo = str(input('sexo:')).upper()
while sexo != 'M' and sexo != 'F':
    print('tente novamente')
    sexo = str(input('sexo: ')).upper()
print('acesso concebido')

#decobri o numero:
from random import randint
a = randint(0, 10)
print('pensei em um numero de 0 a 10, descubra-o:')
n = int(input('qual vc supoe: '))
cont = 0
while n != a:
    if n < a:
        print('é maior')
    if n > a:
        print('é menor')
    n = int(input('qual vc supoe: '))
    cont += 1
print(f'parabens, voce tentou {cont} vezes')

#menu de coisas
a = int(input('primeiro numero:'))
b = int(input('segundo numero: '))
continua = False
while not continua:
    print(''    [1] somar
    [2] multiplicar
    [3] maior entre
    [4] novo numero
    [5] sair'')
    resp = int(input('>>>>qual a sua opcao?'))
    if resp == 1:
        print(f'a soma é: {a} + {b} = {a + b}')
        print('-=' * 10)
    elif resp == 2:
        print(f'a multiplicacao é: {a} x {b} = {a * b}')
        print('-=' * 10)
    elif resp == 3:
        if a > b:
            print(f'entre {a} e {b} o maior é {a}')
            print('-=' * 10)
        elif a < b:
            print(f'entre {a} e {b} o maior é {b}')
            print('-=' * 10)
    elif resp == 4:
        a = int(input('primeiro numero:'))
        b = int(input('segundo numero: '))
    elif resp == 5:
        print('ok tchau')
        continua = True
    else:
        print('tente novamente:')

#fatorial:
n = int(input('fatorial: '))
cont, na = n, n
while n != 1:
    n -= 1
    cont = n * cont
print(f'o fatorial de {na} é {cont}')
#for in range:
n = int(input('fatorial: '))
na, cont = n, n
for i in range(n, 1, -1):
    n -= 1
    cont *= n
print(f'o fatorial de {na} é {cont}')

#pa 
print('calculo de PA')
pr = int(input('primeiro termo:'))
rz = int(input('razao: '))
termo = pr
cont = 1
while cont <= 10:
    print(f'{termo} - ', end=(''))
    termo += rz
    cont += 1
print(' fim')

#pa 2.0:
print('calculo de PA')
pr = int(input('primeiro termo:'))
rz = int(input('razao: '))
termo = pr
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} - ', end=(''))
        termo += rz
        cont += 1
    print('pausa')
    mais = int(input('\nquantos termos quer a mais? '))
print(f'sua conta acabou com {total} termos, obrigado!')

#sequecia de fibonacci:
n = int(input('quantos termos deseja ver: '))
t1 = 0
t2 = 1
print(f'{t1} - {t2}', end=' - ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'{t3}', end=' - ')
    t1 = t2
    t2 = t3
    cont += 1
print('fim')

#paro no 999;
c, n = 0, 0
while n != 999:
    n = int(input('digite um numero: (999 pra para)'))
    if n != 999:
        c += n 
print(f'proceso finalizado com {c} numeros somados')

#mistura: pft
c = maior = menor = cont = 0
continua = 'S'
while continua in 'Ss':
    n = int(input('digite um numero? '))
    cont += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continua = str(input('deseja continuar? [s/n]')).upper()
media = cont / c
print('o programa encerrou com a soma de {} numeros,\nmedia de {:.2}, o maior foi {} e o menor {}'.format(cont, media, maior, menor))
'''





#enterromendo repetcoes - flag:
'''
quando fazemos uma repetcao inifinita ou finita
utilisamos o break que é um flag(ponto de interropcao
, onde ele podeparar um ciclho de repetcao ou outra 
coisa por exemplo:-

n = s = 0
while true:
#loop infinito
    n = int(input('digite n: '))
    if n == 999:
        break
    s += n

assim em um loop infinito, quando der 999 ele vai parar
e nao contar.
'''





#loginha:
print('loja barata')
continua = 'S'+
total = c = pr = prec = maior = cont = menor = 0
while 'S' in continua:
    nome = str(input('nome do produto: '))
    preco = float(input('preço: '))
    cont += 1
    total += preco
    if preco > 1000:
        c += 1
        pr += preco
    if cont == 1:
        maior = menor = preco
    else:
        if preco > maior:
            maior = preco
        if preco < menor:
            menor = preco
            nm = nome
    continua = str(input('quer continuar? ')).upper().split()[0]
print(f'o total da compra foi R${total}')
print(f'tem {c} produtos custando mais de R$1.000')
print(f'o produto mais barato foi {nm} que custa R${menor}')]

#banco:
print('banco itau meu pau no seu cu')
valor = int(input('qual valor deseja sacar? R$'))
total = valor
cinq = 50
c50 = c20 = c10 = c1 = 0
while total >= cinq:
    total -= 50
    c50 += 1
vint = 20
while total >= vint:
    total -= 20
    c20 += 1
dez = 10
while total >= 10:
    total -= 10
    c10 += 10
um = 1
while total >= 1:
    total -= 1
    c1 += 1
print(f'total de {c50} cedulas de 50 reais')
print(f'total de {c20} cedulas de 20 reais')
print(f'total de {c10} cedulas de 10 reais')
print(f'total de {c1} cedulas de 1 real')
'''





#funcoes importantes(eu acho):
'''
a funcao del que apaga derivada variavel:
variavel = ('joao', 14)
del(variavel)
ai a variavel ira se apagar.

a funcao def que 'define' uma nova funcao
apartir de uma variavel:
a = 5
def forinrange(a):
    for i in range(0, a):
        print(a)
print(forinrange(3))
assim o ciclo ira se repetir 3 vezes
(ira fazer a funcao (3) vezes.

se voce quiser que o seu programa reinicie,
use a biblioteca 'os' e coloque:
os.system('cls') 

'''





#variaveis composta - (tupla):
''''
sao variaveis que podem armazenar varios valores
diferente da simples que armazena a penas um
e tem 3 tipos de variaveis compostas: 
tuplas (), listas[] e dicionario{}, a tupla ela guarda
varios valores porem esses valores nao podem
ser mudados. ela funciona da mesma maneira 
que as cadeias de caracteres(podendo ate mesmo 
usalas) e sua tecnica de fariamento, veremos ela funcionar:

lanche = ('hamburgue', 'suco', 'pizza', 'pudim')
#os parenteses nao sao necesarios
print(lanche[1])
for comida in lanche:
    print(f'vou comer {comida}')

e podemos mostrar os dados com o enumerate:

lanche = ('hamburgue', 'suco', 'pizza', 'pudim')
for pos, comida in enumerate(lanche):
    #o enumerete da o dado e a posicao
    #mas usa só se quiser
    print(f'eu vou comer {comida} da posicao {pos}')    
    
podemos tambem colocar a tupla em ordem alfabetica:
lanche = ('hamburgue', 'suco', 'pizza', 'pudim')
print(sorted(lanche))  

podemos adicionar dados a nossa lista
lista = '1', '2', '3'
e adicionar o 4 assim:
lista += [4]

podemos mudar os valores da lista:
lista = (2, 4, 6 ,8)
e trocaremos o valor 4 por 5:
lista[1] = 5

adicionar valores em uma lista geralmente da erro de
index usamos o metodo append ele adiciona no final da lista
um determinado elemento, usamos ele assim:
lista = []
for i in range(0, 5):
    n = int(input('digite o n: '))
    lista.append(n)
print(lista)



#exercicios:
#media:
soma = 0
vetor = []
for i in range(1, 5):

    n = int(input(f'digite sua {i}ª nota: '))
    vetor.append(n)
    soma += n
print(f'as notas sao: {vetor}')
print(f'a media é {soma // 4}')


#par e impar
vetori = []
vetorp = []
for i in range(1, 21):
    n = int(input(f'digite o {i}º numero'))
    impa = n % 2
    if impa == 0:
        vetorp.append(n)
    else:
        vetori.append(n)
print(f'pares = {vetorp} \nimpares = {vetori}')

#extenco
numeracao = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'trese', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    resposta = int(input('qual numero deseja ver: '))
    if 0 <= resposta >= 20:
        print('tenta dnv...')
    else:
        print(f'{resposta} em extenço é {numeracao[resposta]}')


#tabela de informacoes:
tabela = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print(tabela[0:6])
print(tabela[-4:])
print(sorted(tabela))
print(f'o Flamengo esta na {tabela.index("Flamengo")}ª posicao')

#tupla aleatoria
from random import randint
vetor = []
maior, menor = 0, 0
for i in range(1, 5):
    num = randint(0, 10)
    vetor.append(num)
    if i == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print(f'os valores sorteados foram {vetor}\no maior foi {maior}\no menor foi {menor}')

#analise de dados:
vetor = []
par = []
for i in range(1, 5):
    n = int(input(f'digite o {i}º numero: '))
    vetor.append(n)
    dento = n % 2
    if dento == 0:
        par.append(n)
print(f''
voce digitou os valores {vetor}
o valor 9 apareceu {vetor.count(9)} veses)'')
print(f"o valor 3 apareceu na {vetor.index(3) + 1}ª posicao" if 3 in vetor else print(''))
print('os valores pares digitados foram {par}')

#ver silabas
palavras = ('programar', 'amor', 'amendoa', 'orgalopola')
i = 0
for p in palavras:
    print(f'\nna palavra {palavras[i]} temos ', end=' ' )
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    i += 1
'''





#tecnicas com f strings:

'''
em um print nos podemos ajeitar as formatacoes
de varias maneiras para um melhor estilo, como:
numero = 10
print(f'{codigo:.2f}')
sempre colocamos um ponto final antes do que
queremos fazer e os dois pontos para dizer que 
queremos fazer essas coisas, e dentre elas sao:
'''





#variaveis conpostas - [listas]:

'''
funcionando da mesma maneira que as tuplas
elas guardam valores porem as listas podem ser
adulteradas de varias maneira como:
lanche = [batata, alface, manga]
#para adicionar um valor usamos o append()
lanche.append('maca')
e no final da lista o valor maca sera adicionado
#inserir valores usamos o insert():
lanche.insert(0, 'pao')
e assim na primeira posicao sera colocada o pao

remover um item tem 3 opcoes pelo numero ou pelo
valor:
del lache[3]
deletara a manga
lanche.pop(3)
deletara a manga
lanche.remove('manga')
deletara a manga
 
geralmente usamos o .pop(sem nada) para excluir
o ultimo valor da lista.
'''

