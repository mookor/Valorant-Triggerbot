from pystray import Icon, MenuItem, Menu
from PIL import Image
from os import _exit

# Создаем функцию для отображения/скрытия окна
def exit_window(icon, item):
    icon.stop()
    icon.visible = False
    _exit(0)

def start_app(img_path):
    image = Image.open(img_path)  # Замените 'icon.png' на путь к вашей иконке
    menu_items = [MenuItem('Exit', exit_window)]
    menu = Menu(*menu_items)
    icon = Icon('V', image, menu=menu)
    icon.run()