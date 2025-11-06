# NiceGUI-Extras

**NiceGUI-Extras** is a helper package for [NiceGUI](https://nicegui.io) that provides ready-to-use UI enhancements and utilities to make your NiceGUI apps more beautiful and flexible.

![Downloads](https://static.pepy.tech/personalized-badge/nicegui-extras?period=total&units=international_system&left_color=black&right_color=green&left_text=Downloads)


---

## ✨ Features

✅ Right-to-left (RTL) layout support  
✅ Sticky top navigation menu  
✅ Link-to-button converter  
✅ Animated dialogs  
✅ Scroll disabling utility  

---

## 🚀 Installation

```bash
pip install nicegui-extras
````

---

## 💡 How to Use

### 🧩 In `nicegui_extras.utils`

**Right-to-left Persian layout**

```python
from nicegui_extras.utils import farsi_rtl

farsi_rtl()  # enables RTL and Vazir font automatically
```

**Disable page scrolling**

```python
from nicegui_extras.utils import no_scroll

no_scroll()  # disables scrolling on page
```

---

### 🎨 In `nicegui_extras.style`

**Link as button**

```python
from nicegui_extras.style import link_button

def link_button(text: str, url: str, new_tab: bool = False):
    """Create a link styled as a button."""
    classes = 'q-btn q-btn-item non-selectable no-outline q-btn--flat q-btn--rectangle'
    return ui.link(text, url, new_tab=new_tab).classes(classes)
```

Usage:

```python
link_button('Visit Site', 'https://nicegui.io', new_tab=True)
```

---

### 💬 Animated dialog (CSS class)

For now, you can use this class directly to make a dialog animated and blurred:

```python
animated_dialog = 'backdrop-filter="blur(8px) brightness(20%)"'
```

Example:

```python
ui.dialog().props(animated_dialog)
```

---

حتماً 👍 نسخه جدید آموزش برای منوی چسبیده (Sticky Menu Row) به‌صورت تمیز و کاربردی می‌تونه این شکلی باشه:

---

### 📌 Sticky Menu Row

To create a **sticky top menu** that stays fixed at the top of the page and keeps content visible below it, use the following helper:

```python
from nicegui_extras.layout import menu_row

with menu_row(side='left', height='70px'):
    ui.button('Home')
    ui.button('Docs')
    ui.button('GitHub')
    
ui.label('Page content starts here...')
```

This will create a top menu bar that:

* stays fixed when scrolling
* aligns all items **from the left side**
* automatically adds margin so that other elements do not overlap with the menu

---

## 🧠 Example App

```python
from nicegui import ui
from nicegui_extras.utils import farsi_rtl, no_scroll
from nicegui_extras.style import link_button, menu_row

farsi_rtl()
no_scroll()

with ui.row().style(menu_row):
    ui.label('Main Menu')

link_button('Home', '/home')

ui.run()
```

---

## 🧑‍💻 Author

Created by **Ali Heydari** — a Python developer and NiceGUI enthusiast.
More features like improved dark mode and ready-made themes are coming soon!

---

## 📜 License

MIT License © 2025 Ali Heydari

```

