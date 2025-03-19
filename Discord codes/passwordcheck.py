password = input('Enter your password: ')
if len(password)<8 or password.isdigit or password.islower or password.isupper or password.isalpha:
  print('password too weak')
else:
  print('password approved')