#* Welcome to the `lpy-mode' Tutor
#
# `lpy-mode' is a powerful way to interact with a Python REPL.
#
# ATTENTION:
# The commands in the lessons will modify the code. You can always
# revert the file using git.
#
# It is important to remember that this tutor is set up to teach by
# use.  That means that you need to execute the commands to learn
# them properly.  If you only read the text, you will forget the
# commands!
#
# Remember that this is Emacs, you can rebind any binding that you
# don't like. However, a lot of thought has been put into the current
# bindings so don't be surprised if you find stuff inconvenient after
# rebinding without thinking it through.
#
# Your point should now be at beginning of the first line.
# Press =M-<= if it isn't.
#
# Now press =j= to go to Lesson 1.
#
# Press =i= to show/hide the lesson.

#* Lesson 1
# You can press =k= to go back to the introduction.
# Or press =e= to eval the current outline.

#** Python version:
import sys
print(sys.version)

#** Your OS version:
import os
os.uname()
