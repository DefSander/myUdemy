#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      localadmin
#
# Created:     05.04.2018
# Copyright:   (c) localadmin 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a, b = 0, 1
while b < 1000:
	print(b, end=',')
	a, b = b, a+b

# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
print(text)