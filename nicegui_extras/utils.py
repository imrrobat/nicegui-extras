from nicegui import ui 

def farsi_rtl():
    ui.add_head_html("""
        <link href="https://cdn.jsdelivr.net/npm/vazir-font@30.1.0/dist/font-face.css"
              rel="stylesheet" type="text/css" />

        <style>
        body, .q-layout, .q-page-container, .q-page {
            direction: rtl !important;
            text-align: right !important;
            font-family: Vazir, sans-serif !important; 
        }

        .q-btn, .q-input, .q-field__native, .q-table, .q-card, .q-toolbar {
            font-family: Vazir, sans-serif !important;
        }
        </style>
    """)

def no_scroll():
    ui.add_head_html('<style>body { overflow: hidden; }</style>')