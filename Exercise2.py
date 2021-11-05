email=input("Please enter your email: ")
def is_it_email(mail):
    a=0
    b=0
    for i in mail:
        if i == "@":
          a += 1
        elif i == ".":
          b += 1
    if a >= 1 and b >= 1:
       return True
    else:
       return False
print(is_it_email(email))