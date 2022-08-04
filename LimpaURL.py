import pyperclip as clip
import pyautogui as auto
import time

time.sleep(.5)
auto.hotkey('ctrl', 'v')
auto.press('enter')
texto = input()
texto = texto.lower().replace(" ", "-").replace("_", "-").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("à", "a").replace("è", "e").replace("ì", "i").replace("ò", "o").replace("ù", "u").replace("â", "a").replace("ê", "e").replace("î", "i").replace("ô", "o").replace("û", "u").replace("ã", "a").replace("õ", "o").replace("ñ", "n").replace("ü", "u").replace("ç", "c").replace("!", "").replace('"', "").replace("+", "").replace("'", "").replace("@", "").replace("#", "").replace("$", "").replace("%", "").replace("¨", "").replace("&", "").replace("*", "").replace("(", "").replace(")", "").replace("?", "").replace("}", "").replace("{", "").replace("`", "").replace("^", "").replace("~", "").replace(":", "").replace(";", "").replace(".", "").replace(",", "").replace("|", "").replace("/", "").replace("\\", "").replace("<", "").replace(">", "").replace("¹", "").replace("²", "").replace("³", "").replace("£", "").replace("¢", "").replace("¬", "").replace("§", "").replace("ª", "").replace("º", "").replace("°", "").replace('"', "").replace("'", "")
if texto.__contains__("--") == True or texto.__contains__("---") == True:
    texto = texto.replace("---", "-")
    texto = texto.replace("--", "-")
print(texto, "\n💾 COPIADO PARA ÁREA DE TRANSFERÊNCIA 📋\nFeche o programa ou aguarde 3 segundos para ser fechado sozinho.")
clip.copy(texto)
time.sleep(3)