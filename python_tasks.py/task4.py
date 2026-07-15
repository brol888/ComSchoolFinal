# #4 ლატარიის სიმულატორი
# --------------------------
# - კომპიუტერი ირჩევს 6 შემთხვევით რიცხვს 1–დან 49-მდე
# - მოთამაშეს შეჰყავს 6 რიცხვი
# - ითვლება, რამდენი დაემთხვა
# - წინასწარ გაწერილია გასათამაშებელი თანხა
# - logging ინახავს ყველა გათამაშებას და შედეგს
# - მომხმარებელს ყოველთვის შემოჰყავს სწორი მნიშვნელობები--------------------------------------------------------
# ლოგიკა:
# 1. 6-6 დამთხვევის შემთხვევაში თამაშდება JACKPOT
# 2. 6-5 დამთხვევის შემთხვევაში JACKPOT-ის თანხას ვაკლებთ 40%-ს
# 3. 6-4 დამთხვევის შემთხვევაში JACKPOT-ის თანხას ვაკლებთ 60%-ს
# 4. 6-3 დამთხვევის შემთხვევაში JACKPOT-ის თანხას ვაკლებთ 80%-ს
# 5. 6-2 და 6-1 დამთხვევის შემთხვევაში მოთამაშე ვერაფერს ვერ იგებს


from random import sample
import logging

logging.basicConfig(filename='loto.at', 
                    level=logging.INFO,
                     format="%(asctime)s - %(levelname)s - %(message)s",
                    encoding="utf-8"   )

computer_numbers = sample(range(1,49), 6)
print(computer_numbers)

number = []

for _ in range(6):
    number_user = int(input('შეიყვანეთ რიცხვი :'))
    number.append(number_user)

jackpot = 1000

matches = 0 

for i in number:
    if i in computer_numbers:
        matches += 1 

    
if matches == 6:
    prize = jackpot

elif matches == 5:
    prize = jackpot * 0.60

elif matches == 4:
    prize = jackpot * 0.40

elif matches == 3:
    prize = jackpot * 0.20

else:
    prize = 0

print(prize)

logging.info(f'მომხმარებელმა მოიგო : {prize}')