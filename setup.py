from cx_Freeze import setup, Executable

base = None    

executables = [Executable("LimpaURL.py", base=base)]

packages = ["idna", "pyperclip", "time"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Limpa URL",
    options = options,
    version = "0.02",
    description = 'Executável para limpar uma string para um padrão de URL.',
    executables = executables
)

# In the prompt, type 'python setup.py build'