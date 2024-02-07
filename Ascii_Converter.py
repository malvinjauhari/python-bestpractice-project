import ascii_magic
import argparse
try :
    my_art = ascii_magic.from_image_file('images/together.jpg')
    ascii_magic.to_terminal(my_art)
except Exception as e:
   print('ada aqua',e)
