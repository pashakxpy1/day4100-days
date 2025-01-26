# пробуем написать перекодування тексту в print


def preprint(atext):
  """ перекодувати мнемокоди кольорів {red}, {blue} в специфічні коди, які розуміє print
      Для пошуку мнемокоду використаємо функцію find https://www.geeksforgeeks.org/python-string-find/
      s = "Welcome to GeekforGeeks!"
      index = s.find("GeekforGeeks")
      print(index)
      
      Для заміни мнемокоду використаємо функцію Replace https://www.geeksforgeeks.org/python-string-replace/
      s = "Hello World! Hello Python!"

      # Replace "Hello" with "Hi"
      s1 = s.replace("Hello", "Hi")

      print(s1)

  """
  # задам коди кольорів
  color_default = "0"
  color_black = "30"
  color_red = "31"
  color_green = "32"
  color_yellow = "33"
  color_blue = "34"
  color_purple = "35"
  color_cyan = "36"
  color_white = "37"
  color_pref = "\033["
  color_suff = "m"
  # Вихідній змінній присвоїмо значення вхіднох (а раптом мнемокодів немає)
  result = atext

  # тепер почергово обробляємо кожний колір
  if result.find("{red}") >= 0:
    result = result.replace("{red}", color_pref + color_red + color_suff)

  if result.find("{default}") >= 0:
    result = result.replace("{default}",
                            color_pref + color_default + color_suff)

  if result.find("{black}") >= 0:
    result = result.replace("{black}", color_pref + color_black + color_suff)

  if result.find("{green}") >= 0:
    result = result.replace("{green}", color_pref + color_green + color_suff)

  if result.find("{yellow}") >= 0:
    result = result.replace("{yellow}", color_pref + color_yellow + color_suff)

  if result.find("{blue}") >= 0:
    result = result.replace("{blue}", color_pref + color_blue + color_suff)

  if result.find("{purple}") >= 0:
    result = result.replace("{purple}", color_pref + color_purple + color_suff)

  if result.find("{cyan}") >= 0:
    result = result.replace("{cyan}", color_pref + color_cyan + color_suff)

  if result.find("{white}") >= 0:
    result = result.replace("{white}", color_pref + color_white + color_suff)
  # повертаємо результат
  return result


# тестуємо різні варіанти виклику функції
mytext = "{red}Просто  самий {default} {blue} простий {cyan} вивід, що дізнатис {default} а воно взагалі працює?"
bprint = preprint(mytext)
print(bprint)

mytext = "{green}Тут {default} кілька {red}разів викорситовуємо{green} один і той {default}же колір {green}green{default}"
bprint = preprint(mytext)
print(bprint)

mytext = "Тут немає жодного кольору"
bprint = preprint(mytext)
print(bprint)

anytext = input("А тут можна ввести бульякий текст  з мнемокодами кольорів: ")
bprint = preprint(anytext)
print(bprint)
