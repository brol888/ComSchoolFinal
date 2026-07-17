# კლასი Room
# აღწერა: თითო ოთახი სასტუმროში
# Attributes (ატრიბუტები):
# • room_number: int – ოთახის ნომერი
# • room_type: str – ტიპი (Single, Double, Suite)
# • price_per_night: float – ღამეების ფასი
# • is_available: bool – თავისუფალია თუ არა
# • max_guests: int – მაქსიმალური ადამიანების რაოდენობა
# Methods (მეთოდები):
# • book_room(self) – დაჯავშნისას ფლაგი is_available=False
# • release_room(self) – გათავისუფლებისას is_available=True
# • calculate_price(self, nights: int) -> float – ფასი გათვალისწინებით ღამეების
# რაოდენობისა

# • __str__(self) – ოთახის დეტალების სტრინგის სახით დაბრუნება


class Room:
    def __init__(self, room_number : int, room_type: str, 
                 price_per_night: float,  max_guest: int):
        self._room_number = room_number
        self._room_type = room_type
        self._price_per_night = price_per_night
        self._is_available = True
        self._max_guest = max_guest

    def book_room(self):

        self._is_available = False

        return 'წარმატებით დაიჯავშნა'

    def release_room(self):

        self._is_available = True
        print('დაიჯავშნა')

        return 'წარმატებით მოიხსნა ჯავშანი'
    
    def calculate_price(self, nights: int):
        
        price = nights * self._price_per_night
        print(f'price is :{ price}')
        return price

    def __str__(self):
        return (f"""room type : {self._room_type} \n room number: {self._room_number} \n price per night: {self._price_per_night} 
    is_available : {self._is_available} \n max guest: {self._max_guest}""")
        

room1 = Room(room_number=3,room_type='luxery' , price_per_night=132.4, max_guest=5)

