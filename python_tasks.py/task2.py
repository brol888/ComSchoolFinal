# #2 პროგრამა "21" ქულა
# ---------------------
# წესები:
# - დასტა შედგება 52 კარტისაგან - 4 ვარიანტი ("ყვავი" "ჯვარი" "გული" "აგური")
# - 2-დან 10-მდე + Jack + Queen + King + Ace
# - კარტების ღირებულება - 2-10მდე = თავისივე მნიშვნელობა (ანუ 3 = 3, 7 = 7 და ა.შ.)
# ; J,Q,K = 10 ; Ace = 11 (მარტივი ვარიანტი, უდრის მხოლოდ 11-ს)
# - მოთამაშე და კომპიუტერი იღებენ კარტებს (თავდაპირველად 2-2,
# შემთხვევითობის პრინციპით)
# - მოთამაშეს შეუძლია აირჩიოს "add" (დამატება) ან "stop" (გაჩერდეს)

# - კომპიუტერი თავის მხრივ იღებს კარტებს მანამ, სანამ ქულა < 17
# - ვინც 21-ს მიუახლოვდება, მაგრამ არ გადააჭარბებს, ის იგებს
# თუ მოთამაშე მოიგებს გამოგვაქვს "თქვენ მოიგეთ" თუ კომპიუტერი "თქვენ
# წააგეთ" ფრეზე ვარიგებთ ხელახლა.
# შეგიძლიათ გამოიყენოთ:
# ------------------------
# 1. ციკლები
# 2. პირობითი ოპერატორები
# 3. ფუნქცია
# 4. მოდულები
from dataclasses import dataclass
from random import shuffle

@dataclass
class Card:
    suit: str
    rank: str
    value: int

class DeckBlackJack:

  


    
    def create_standard_deck(self):
        suits = ["ყვავი", "ჯვარი", "გული", "აგური"]

        ranks = [
            ("2", 2),
            ("3", 3),
            ("4", 4),
            ("5", 5),
            ("6", 6),
            ("7", 7),
            ("8", 8),
            ("9", 9),
            ("10", 10),
            ("Jack", 10),
            ("Queen", 10),
            ("King", 10),
            ("Ace", 11)
        ]

        cards = []

        for suit in suits:
            for rank, value in ranks:
                cards.append(Card(suit, rank, value))

        self.deck = cards
        return cards
    @staticmethod
    def score(cards):
        total = 0

        for card in cards:
            total += card.value

        return total
    



while True:
    decks = DeckBlackJack()
    decks.create_standard_deck()
    input_first = input('start game Y / N : ')
    computer_scores = []
    user_scores = []
    shuffle(decks.deck)
    if input_first == 'y':
        for _ in range(2):
            computer_scores.append(decks.deck.pop())
            user_scores.append(decks.deck.pop())

    
    while True:
        print("Your card:", user_scores)
        print("score:", DeckBlackJack.score(user_scores))

        if DeckBlackJack.score(user_scores) > 21:
            print('you loose')
            break

        choice = input("add / stop: ").lower()

        if choice == "add":
            user_scores.append(decks.deck.pop())
        elif choice == "stop":
            if comp > 21 and user > 21:
                print('play again ! equal ')

            elif  user < comp <= 21 :
                print('comp won')

            elif comp < user <= 21 :
                print('u won')

            elif comp == user:
                print('equal')
            break
    
    while DeckBlackJack.score(computer_scores) < 17:
        computer_scores.append(decks.deck.pop())



    comp = DeckBlackJack.score(computer_scores)
    user = DeckBlackJack.score(user_scores)

    if comp > 21 and user > 21:
        print('play again ! equal ')

    elif  user < comp <= 21 :
        print('comp won')

    elif comp < user <= 21 :
        print('u won')

    elif comp == user:
        print('equal')

    
  






