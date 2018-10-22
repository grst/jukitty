from .kitty_helper import write_chunked

def show_image(data):
    try:
        write_chunked({'a': 'T', 'f': 100}, data['image/png'].strip().encode('ascii'), b64=True)
    except Exception as e:
        print("Error plotting image: " + getattr(e, 'message', repr(e)))
