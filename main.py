master_pwd = input("What is the master password: ")

def view():
  with open('passwords.txt','r') as file:
    for line in file.readlines():
      user,passwd = line.rstrip().split(" -> ")

def add():
  name = input("Account name: ")
  pwd = input("Password: ")
  with open('passwords.txt','a') as file:
    file.write(name + " -> "+pwd + "\n")

while True:
  mode = input("Add new password to the list or view passwords ? (Add or View). Press q to quit.").lower()

  if mode == 'q':
    break

  if mode == 'view':
    view()
  elif mode == 'add':
    add()
  else:
    print("Invalid input...")
    continue

