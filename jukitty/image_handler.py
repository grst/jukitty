import base64
import sys
from subprocess import call
import tempfile

protocol_start = b'\033_Gf=100;'
protocol_end = b'\033\\'

stdbout = getattr(sys.stdout, 'buffer', sys.stdout)

def show_image(data):
    png = base64.b64decode(data['image/png'])
    with tempfile.NamedTemporaryFile(delete=False) as f:
       f.write(png)
       f.flush()
    call(['kitty', 'icat', f.name])
    # stdbout.write(protocol_start + png + protocol_end)
    # stdbout.flush()

