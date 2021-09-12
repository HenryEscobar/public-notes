
# Modules

"""
file_structure:
my_app/
   rooms_update.py
   Hotel/    # MODULE
      __init__.py
     available_rooms.py
     total_rooms.py

from Hotel import total_rooms, available_rooms
"""

import the_basics
the_basics.hello_world()

from the_basics import hello_world as hello

