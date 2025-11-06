from nicegui import ui 
from nicegui_extras.styles import menu_row

with menu_row():
    ui.button('Home')
    ui.button('About')
    ui.label('salam')


ui.label('Hello world!')

ui.run()