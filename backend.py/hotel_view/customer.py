# კლასი Customer
# აღწერა: მომხმარებელი, რომელიც ბილეთებს ან დაჯავშნებს აკეთებს
# Attributes:
# • name: str – მომხმარებლის სახელი
# • budget: float – ბიუჯეტი
# • booked_rooms: list – დაჯავშნილი ოთახების სია
# • reward_points: int – ქულები, რომელიც სისტემა აკლიტებს/ამატებს
# Methods:
# • add_room(self, room: Room) – ოთახის დამატება დაჯავშნაში
# • remove_room(self, room: Room) – ოთახის წაშლა დაჯავშნიდან
# • pay_for_booking(self, total_price: float) -> bool – გადახდა და ბიუჯეტის
# შემოწმება
# • show_booking_summary(self) – სტრინგში დაჯავშნილი ოთახები, ღირებულება


class Customer:
    def __init__(self, name: str, budget: float, reward_points = 0):
        self._name = name
        self._budget = budget
        self._book_rooms = []
        self._reward_points = reward_points

    def add_rooms(self, room):
        self._book_rooms.append(room)
        print(f'room was added sucsesfully : {room}')
        return 'room was added sucsesfully'
    
    def remove_room(self, room):
        self._book_rooms.remove(room)
        print(f'room was sucssefully removed : {room}')
        return f'room was sucssefully removed : {room}'
    
    def pay_for_booking(self, total_price: float):
        print(total_price)
        if self._budget < total_price:
            return 'budget is not enough'
        self._budget -= total_price
        return 'sucessfully paid'
    
    def show_booking_summary(self):
        info_summary = [f'served rooms are {i._room_number} and price {i._price_per_night}' for i in self._book_rooms]
        return "\n".join(info_summary)
            
