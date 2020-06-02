## @package licenser
# Main package

from engine import Engine
import sys
e = Engine("settings",sys.argv[1])
e.license()
