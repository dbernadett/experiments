# Importing library
import qrcode
 
# Data to be encoded
SSID="ssid"
PASSWORD="password"
data = f'WIFI:S:{SSID};T:WPA;P:{PASSWORD};;'
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('MyQRCode1.png')
