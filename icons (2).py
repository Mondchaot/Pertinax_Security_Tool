def load_icon(widget):
    try:
        widget.iconbitmap(default="icon.ico")
    except:
        pass  # Icon optional