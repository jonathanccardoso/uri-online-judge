while True:
  try:
    password=int(input())
    if(password==2002):
      print("Acesso Permitido")
      break
    else:
      print("Senha Invalida")
  except:
    break