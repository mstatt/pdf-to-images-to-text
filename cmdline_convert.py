#Using subprocess command with "CONVERT"
import os
import subprocess

subprocess.check_output(['convert','-density', '500','PATH/NAME.pdf','PATH/NAME.jpg'])