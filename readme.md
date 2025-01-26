# Урок 4

Кольоровий вивід

```py
print("\033[99m")

print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")

```

Color	|Value|
------|-----|
Default	|0|
Black	|30|
Red	|31|
Green	|32|
Yellow	|33|
Blue	|34|
Purple	|35|
Cyan	|36|
White	|37|


# А тут своя задачка 


перекодувати мнемокоди кольорів {red}, {blue} в специфічні коди, які розуміє print
Для пошуку мнемокоду використаємо функцію find https://www.geeksforgeeks.org/python-string-find/
s = "Welcome to GeekforGeeks!"
index = s.find("GeekforGeeks")
print(index)

Для заміни мнемокоду використаємо функцію Replace https://www.geeksforgeeks.org/python-string-replace/
s = "Hello World! Hello Python!"

# Replace "Hello" with "Hi"
s1 = s.replace("Hello", "Hi")

print(s1)