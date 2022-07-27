from cx_Freeze import setup, Executable

base = None    

executables = [Executable("LimpaURL.py", base=base)]

packages = ["idna", "pyperclip"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Limpa URL",
    options = options,
    version = "0.1",
    description = 'Executável para limpar uma string para um padrão de URL.',
    executables = executables
)