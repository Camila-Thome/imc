# condicionais / imc.py
'''
Solicite para o usuario informar:
-Nome
-Altura (cm)
-Peso (kg)
Com base nestes dados realize o calculo para descobrir
qual o IMC (indice de massa corporea) da pessoa.
Para o calculo utilize a tabela padrão do IMC.
abaixo de 18,5 Abaixo do Peso (Pegue suplementos do Cariani)
entre 18,6 e 24,9 Peso Ideal (Para Bens)
entre 25,0 0 29,9 Sobrepeso
entre 30,0 e 34,9 Obesidade Grau 1
entre 35,0 e 39,9 Obesidade Grau 2
acima de 40,0 Obesidade Grau 3 (Dr. Nowzaradan te espera)
formula IMC peso / altura
'''
nome = input('digite seu nome: ')
altura = float(input('digite sua altura em cm: '))
altura2 = altura / 100
peso = float(input('digite seu peso em kg: '))
IMC = peso / (altura2 * altura2)

if IMC <= 18.4:
    result = "está abaixo do peso"

elif IMC >= 18.6 and IMC <= 24.9:   
    imc = "esta com o peso ideal"

elif  IMC >= 25.0 and IMC <= 29.9:
    result = "esta com sobrepeso"

elif IMC >= 30.0 and IMC <= 34.9:
    result = "obesidade grau 1"

elif IMC >= 35.0 and IMC <=39.9:
    result = "obesidade grau 2"

else: 
 result = "obesidade grau 3, a morte lhe espera"
print (f'o IMC eh {result}')

