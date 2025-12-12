from cx_Freeze import setup, Executable # pyright: ignore[reportUnknownVariableType, reportMissingTypeStubs]

build_exe_options = { # pyright: ignore[reportUnknownVariableType]
    "packages": ["easyttuimenus"],
    "excludes": ["tkinter", "unittest", "email", "http", "xmlrpc"],
    "include_files": [],
    "optimize": 2,
    "include_msvcr": True
} # what do you do exactly?

base = None # console app (use "WIN32GUI" on Windows GUI apps)

setup(
    name = "Despair",
    version = "0.0.1",
    description = "A Game About Debt",
    options = {"build_exe": build_exe_options},
    executables = [Executable(
        "main.py",
        base = base,
        target_name = "despair"
    )]
)