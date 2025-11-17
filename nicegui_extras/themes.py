from nicegui import ui

# Gruvbox color palette as a dictionary
gruvbox_colors = {
    "black": "#282828",
    "red": "#cc241d",
    "green": "#98971a",
    "yellow": "#d79921",
    "blue": "#458588",
    "purple": "#b16286",
    "aqua": "#689d6a",
    "gray": "#928374",
    "white": "#fcfcfc",
}


def gruvbox_theme():
    """Apply the Gruvbox color theme to NiceGUI."""
    c = gruvbox_colors  # shortcut for readability

    ui.add_head_html(f"""
    <style>
        :root {{
            --color-bg: {c["black"]};
            --color-text: {c["white"]};
            --color-muted: {c["gray"]};
            --color-primary: {c["blue"]};
            --color-accent: {c["aqua"]};
            --color-success: {c["green"]};
            --color-warning: {c["yellow"]};
            --color-error: {c["red"]};
            --color-highlight: {c["purple"]};
        }}

        body {{
            background-color: var(--color-bg);
            color: var(--color-text);
        }}

        .q-btn {{
            background-color: var(--color-primary);
            color: var(--color-text);
            border-radius: 8px;
            transition: all 0.3s ease;
        }}

        .q-btn:hover {{
            background-color: var(--color-accent);
        }}

        .q-card {{
            background-color: #32302f;
            color: var(--color-text);
        }}

        .q-input__inner, .q-field__native {{
            background-color: #3c3836;
            color: var(--color-text);
        }}

        .q-toolbar {{
            background-color: var(--color-bg);
            color: var(--color-text);
        }}

        .q-separator {{
            background-color: {c["gray"]};
        }}
    </style>
    """)
