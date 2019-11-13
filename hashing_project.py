'''Login system with Hashing '''

import hashlib


def encode_data(string):

    hs = hashlib.sha512()
    hs.update(string.encode("UTF"))
    hs = hs.hexdigest()
    return hs


def test_data(string, hs):
    if encode_data(str(string)) == hs:
        return True
    else:
        return False


def regis(login, pack):
    login = str(login)
    pack = encode_data(str(pack))
    file = open('data', 'a')
    file.write("\n"+login+"\n"+pack)
    file.close()


print('''1.Registration \n2.login''')

op = int(input(">>>"))
if op == 1:
    userName = input("Username: ")
    passWord = input("password: ")
    passConf = input("password: ")
    if passWord == passConf:
        try:
            regis(userName, passWord)
            print("success")
        except:
            print("\n;-; Fail... Try again\n")
else:
    userName = input("\nUsername: ")+"\n"
    passWord = input("Password: ")
    with open ("data ", 'r') as data:
        loginAndPass = data.readlines()
        if userName in loginAndPass:
            position = loginAndPass.index(userName)
            if position % 2 != 0:
                if test_data(passWord, loginAndPass[int(position)+1]):
                    print("SUccessful !!")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
