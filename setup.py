from cx_Freeze import setup, Executable

base = None    

executables = [Executable("LimpaURL.py", base=base)]

packages = ["idna", "pyperclip", "time", "pyautogui"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Limpa URL",
    options = options,
    version = "0.04",
    description = '*Copie o texto que deseja e deixe o programa rodar sem interferências.',
    executables = executables
)

# In the prompt, type 'python setup.py build'