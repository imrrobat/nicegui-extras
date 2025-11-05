from nicegui import ui

def link_button(text: str, url: str, new_tab: bool = False):
    """Create a link styled as a button."""
    classes = 'q-btn q-btn-item non-selectable no-outline q-btn--flat q-btn--rectangle'
    return ui.link(text, url, new_tab=new_tab).classes(classes)

menu_row = '''
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #222;
    color: white;
    padding: 10px;
    z-index: 1000;
'''

# link_btn = 'q-btn q-btn-item non-selectable no-outline q-btn--flat q-btn--rectangle'

animated_dialog = 'backdrop-filter="blur(8px) brightness(20%)"'