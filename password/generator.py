import random
import string

print("welcome to our random password generator")
def main():

    length=int(input("enter the length of password you want: "))
    lowerD=string.ascii_lowercase

    upperD=string.ascii_uppercase
    digitD=string.digits

    symbolD= string.punctuation
    combine=lowerD+upperD+digitD+symbolD
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    main()


main()