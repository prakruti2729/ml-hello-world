import platform
import os
import psutil

print("Hello, ML World from Jenkins!")
print(f"Python Version: {platform.python_version()})
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"CPU Cores: {os.cpu_count()}")
print(f"Total RAM: {round(psutil.virtual_memory().total/(1024**3),2)}GB")


