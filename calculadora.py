print("===============================")
print(f'{'calculadora':-^30}')
print("===============================")
print("     1. Soma")
print("     2. Subtração")
print("     3. Multiplicação")
print("     4. Divisão")
print("     0. Sair")
print("===============================")
n3f =  0
menu =  int(input('opção: '))
while True:
 if menu == 1:
  while True:
     n1 = int(input('digite o numero: '))
     n2 = int(input('digite o segundo numero: '))
     continuar = input('deseja adicionar mais numeros[S/N]: ').upper()
     if continuar == 'N':
        break
     if continuar != 'N':
      while True:
        n3 = int(input('digite o proximo valor: '))
        cont = input('deseja adicionar mais numeros[S/N]: ').upper()
        n3f += n3
        if cont == 'N':
           break
     break
  soma = n1 + n2 + n3f
  print(f'resultado: {soma}')
  break
 if menu == 2:
  while True:
   n1 = int(input('digite o numero: '))
   n2 = int(input('digite o segundo numero: '))
   sub =  n1 - n2
   print(f'resultado: {sub}')
   continuar = input('deseja subtrair mais[S/N]: ').upper()
   if continuar == 'N':
    break
   else:
    while True:
        n3 = int(input('digite o proximo valor: '))
        cont = input('deseja adicionar mais numeros[S/N]: ').upper()
        sub -= n3
        if cont == 'N':
          print(f'resultado: {sub}')
          break
    break
  break
 if menu == 3:
  while True:
    n1 = int(input('digite o numero: '))
    n2 = int(input('digite o segundo numero: '))
    mult = n1 * n2
    print(f'resultado: {mult}')
    cont = input('deseja continuar[S/N]: ').upper()
    if cont == 'N':
      break
    else:
      while True:
        n3 = int(input('digite o proximo numero: '))
        mult *= n3
        cont = input('deseja continuar[S/N]: ').upper()
        if cont == 'N':
          print(f'resultado: {mult}')
          break
    break
  break
 if menu == 4:
  while True:
    n1 = int(input('digite o numero: '))
    n2 = int(input('digite o segundo numero: '))
    div = n1 /  n2
    print(f'resultado: {div}')
    cont = input('deseja continuar[S/N]: ').upper()
    if cont ==  'N':
      break
    else:
      while True:
        n3 = int(input('digite o proximo numero: '))
        div /= n3
        cont = input('deseja continuar[S/N]: ')
        if cont == 'N':
            print(f'resultado: {div}')
            break
      break
  break
 if menu == 0:
  break
 break
print('='*30)
print(f'{'fim do progama':-^30}')
print(f'{'obrigado pelo uso':-^30}')
print('='*30)
