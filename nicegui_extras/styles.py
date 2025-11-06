from nicegui import ui
from contextlib import contextmanager


def link_button(text: str, url: str, new_tab: bool = False):
    """Create a link styled as a button."""
    classes = 'q-btn q-btn-item non-selectable no-outline q-btn--flat q-btn--rectangle'
    return ui.link(text, url, new_tab=new_tab).classes(classes)

@contextmanager
def menu_row(height: str = '60px', side: str = 'left'):
    """
    Create a sticky top menu bar that stays fixed and aligns items from one side.
    
    Args:
        height (str): menu height (e.g. '50px', '4rem')
        side (str): alignment side, either 'left' or 'right'
    """
    justify = 'justify-start' if side == 'left' else 'justify-end'
    menu_style = f'''
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #222;
        color: white;
        padding: 10px;
        z-index: 1000;
        height: {height};
    '''
    with ui.row().style(menu_style).classes(f'items-center {justify}') as row:
        yield row
    ui.space().style(f'height: {height};')

# link_btn = 'q-btn q-btn-item non-selectable no-outline q-btn--flat q-btn--rectangle'

animated_dialog = 'backdrop-filter="blur(8px) brightness(20%)"'