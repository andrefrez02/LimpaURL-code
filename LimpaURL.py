import pyperclip as clip
import time

texto = input()
texto = texto.lower().replace(" ", "-").replace("_", "-").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("à", "a").replace("è", "e").replace("ì", "i").replace("ò", "o").replace("ù", "u").replace("â", "a").replace("ê", "e").replace("î", "i").replace("ô", "o").replace("û", "u").replace("ã", "a").replace("õ", "o").replace("ñ", "n").replace("ü", "u").replace("ç", "c").replace("!", "").replace('"', "").replace("+", "").replace("'", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("¨", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace("?", "").replace("}", "").replace("{", "").replace("`", "").replace("^", "").replace(":", "").replace(";", "").replace(".", "").replace(",", "").replace("|", "").replace("/", "").replace("\\", "").replace("<", "").replace(">", "").replace("¹", "").replace("²", "").replace("³", "").replace("£", "").replace("¢", "").replace("¬", "").replace("§", "").replace("ª", "").replace("º", "").replace("°", "")
if texto.__contains__("--") == True or texto.__contains__("---") == True:
    texto = texto.replace("---", "-")
    texto = texto.replace("--", "-")
clip.copy(texto)
print(texto)
time.sleep(.75)