import subprocess

packages = [
    "pyautogui",
    "pyperclip"
]

for package in packages:
    try:
        subprocess.check_call(["pip", "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")