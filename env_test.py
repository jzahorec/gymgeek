import platform, os

operating_system = platform.system()
python_version = platform.python_version()
virtual_enviroment = os.getenv("VIRTUAL_ENV") or "\u00D7"


print("Operační systém:\t" + operating_system)
print("Verze tohoto pythonu:\t" + python_version)
print("Virtuální prostředí:\t" + virtual_enviroment)
