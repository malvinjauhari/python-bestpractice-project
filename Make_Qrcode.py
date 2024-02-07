# Import QRCode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngegg.com%2Fen%2Fsearch%3Fq%3Dpikachu&psig=AOvVaw35otVJ7uzMyUUYZkUBitc7&ust=1650499212410000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCJDY7e2qofcCFQAAAAAdAAAAABAD"
  
# Generate QR code
url = pyqrcode.create(s)
  
# Create and save the png file naming "myqr.png"
url.png('qrcode.png', scale = 15)