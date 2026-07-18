# #3 ATM Machine--------------
# პროგრამა მუშაობს როგორც ბანკომატი:
# - მომხმარებელს აქვს ანგარიშზე X თანხა რომელსაც წინასწარ ვინახავთ
# - მომხმარებელს შეუძლია შეამოწმოს ბალანსი (ბრძანებით)
# - მომხმარებელს შეუძლია თანხის: "გატანა", "შემოტანა", ბალანსის ნახვა
# - აუცილებელი ვალიდაციები: ვერ უნდა გაიტანოს იმაზე მეტი რაც ანგარიშზე აქვს
# და ასევე ერთჯერადად ვერ უნდა შეიტანოს 1000ზე მეტი
# - ბანკომატი მუშაობს მხოლოდ ლარზე
# - ყველა ოპერაცია უნდა ჩაიწეროს ლოგერში და შეიხანოს ლოგ ფაილში (გატანა,
# შემოტანა)
# - მომხმარებელს ყოველთვის შემოჰყავს


import logging

logging.basicConfig(
    filename="atm.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


class ATMMachine:
    def __init__(self, balance):
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            logging.info(f'user withdraw { amount}')
            print('წარმატებით გაიტანეთ თანხა')
        else:
            print('არასწორი მოქმედება')
            logging.error('ვერ გაიტანა თანხა იუზერმა')
    
    def deposit(self, amount):
        if 0 < amount <= 1000:
            self.__balance += amount
            logging.info(f'უზერმა შემოიტანა { amount}')

        else:
            logging.error('უზერმა ვერ შემოიტანა თანხა')
            print('არასწორი მოქმედება')
        

user1 = ATMMachine(5000)

