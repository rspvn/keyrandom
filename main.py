import random
import string

def generate_random_password(length=12):
    # Bao gồm chữ cái thường, chữ cái viết hoa, số và các ký tự đặc biệt
    characters = string.ascii_letters + string.digits + "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_passwords_to_file(filename='passwords.txt', num_passwords=10, length=12):
    with open(filename, 'w') as file:
        for _ in range(num_passwords):
            password = generate_random_password(length)
            file.write(password + '\n')

# Sử dụng hàm để tạo và lưu 10 mật khẩu vào file 'passwords.txt'
save_passwords_to_file(filename='passwords.txt', num_passwords=10, length=12)
