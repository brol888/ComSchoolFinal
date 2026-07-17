user = {
    "email": "nbroladze@mail.com",
    "name": "",
    "username": "nbroladze88",
    "password": "nbroladze123"
}

name = input("შეიყვანეთ სახელი: ")

if name.isdigit():
    print("შემოიყვანეთ სტრინგი მხოლოდ.")

elif not name.isascii() and name.isalpha():
    print("შემოყვანილია სხვა ენა უნდა შემოიყვანოთ ლათინური")

elif name.isascii() and name.isalpha() and not name.islower():
    print("შემოიყვანეთ დაბალი შიფტით")

elif name.isascii() and name.isalpha() and name.islower():
    user["name"] = name

    print("\nრეგისტრაცია წარმატებით დასრულდა!\n")
    print(f"ელ-ფოსტა: {user['email']}")
    print(f"სახელი: {user['name']}")
    print(f"ზედმეტსახელი: {user['username']}")
    print(f"პაროლი: {user['password']}")

elif name.isascii():
    print("შემოყვანილია სიმბოლოები, შემოიტანეთ მხოლოდ string პატარა რეგისტრში.")

else:
    print("არასწორი მნიშვნელობა.")