# will use the pyscreenshot library
# install the library
# pip install pyscreenshot

import pyscreenshot

# To capture the screen
image = pyscreenshot.grab()

# Display the image
image.show()

# Save the image
image.save("BB")

