from cx_Freeze import setup, Executable # pyright: ignore[reportUnknownVariableType, reportMissingTypeStubs]

# sticking with cx_Freeze for now but ill likely switch to PyInstaller later


build_exe_options = { # pyright: ignore[reportUnknownVariableType]
    "packages": ["src", "easyttuimenus"], # at a loss as to whether or not these are necessary
    "excludes": ["tkinter", "unittest", "email", "http", "xmlrpc"],
    "include_files": [("assets/", "assets/")], 
    "optimize": 2,
    "include_msvcr": True
} # what do you do exactly?

base = None 

setup(
    name = "Despair",
    version = "0.0.1",
    description = "A Game About Debt",
    options = {"build_exe": build_exe_options},
    executables = [Executable(
        "src/main.py",
        base = base,
        target_name = "despair"
    )]
)