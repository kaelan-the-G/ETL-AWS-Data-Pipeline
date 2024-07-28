import os
import sys
from os.path import dirname
from pathlib import Path
dir = dirname(__file__)
dir = Path(dir).parent.absolute()/'src'
print(dir)
sys.path.append(dir)
 