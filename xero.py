from xero import Xero
from xero.auth import PrivateCredentials


def main():
    with open('privatekey.pem') as keyfile:
        rsa_key = keyfile.read()

    credentials = PrivateCredentials('', rsa_key)
    xero = Xero(credentials)

print(xero)


if __name__ == '__main__':
    main()
