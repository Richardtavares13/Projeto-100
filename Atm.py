class Atm:
    def __init__(self,account,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.Account = account
     

    def check_balance(self):
        print("Seu saldo é: -")
        print("CLOUD CASH = 500")
        print("CLOUD COIN = 750")
        print("CLOUD MB = 900")

    def withdrawl1(self,CLOUD_CASH):
        new_amount = 100 - CLOUD_CASH
        print("Você retirou o valor "+str(CLOUD_CASH) + ". Seu saldo restante é "+ str(new_amount))

    def withdrawl2(self,CLOUD_COIN):
        new_amount = 200 - CLOUD_COIN
        print("Você retirou o valor "+str(CLOUD_COIN) + ". Seu saldo restante é "+ str(new_amount))

    def withdrawl3(self,CLOUD_MB):
        new_amount = 300 - CLOUD_MB
        print("Você retirou o valor "+str(CLOUD_MB) + ". Seu saldo restante é "+ str(new_amount))        


def main():
    print("Bem Vindo(a) CLOUD'S Bank! :)  !")
    Account = input("Digite o número da sua conta: ")
    Card_number = input("Insira o número da sua chave:- ")
    pin_number  = input("Digite o número do seu pin:- ")

    new_user =  Atm(Account,Card_number,pin_number)

    print("Escolha sua atividade ")
    print("1.Seu saldo  2.Retirada")
    activity = int(input("Digite o número da atividade:- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        print("1. CLOUD CASH")
        print("2. CLOUD COIN")
        print("3. CLOUD MB")
        choose = int(input("1. Add CLOUD CASH  2. Add CLOUD COIN 3. Add CLOUD MB: "))
        if (choose == 1):
           CLOUD_CASH = int(input("Digite o valor:- "))
           new_user.withdrawl1(CLOUD_CASH)
        if (choose == 2):
           CLOUD_COIN= int(input("Digite o valor:- "))
           new_user.withdrawl2(CLOUD_COIN)    
        if (choose == 3):
           CLOUD_MB = int(input("Digite o valor:- "))
           new_user.withdrawl3(CLOUD_MB)
    else:
        print("Digite um número valido")

if __name__ == "__main__":
    main()