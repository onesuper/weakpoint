

import sys
from weakpoint.core import WeakPoint
from weakpoint.exceptions import WeakPointException






def main():
    try:
        WeakPoint()
    except WeakPointException as e:
        print e
        return e.code
    return 0


if __name__ == "__main__":
    sys.exit(main())
