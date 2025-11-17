from nicegui import ui 
from nicegui_extras.styles import menu_row, floating_button
from nicegui_extras.themes import gruvbox_theme

# gruvbox_theme()

with menu_row():
    ui.button('Home').props('color=green-8')
    ui.button('About')
    ui.label('salam')

floating_button('add')

ui.label('Hello world!')

ui.run()