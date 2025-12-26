from nicegui import ui 
from nicegui_extras.styles import ccolumn

# gruvbox_theme()

with ccolumn(style='border:1px solid;'):
    ui.label('salam')
    ui.button('salam')

ui.run()