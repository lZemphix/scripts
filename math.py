#! /usr/bin/env python
import sys
from typing import Any

def main(argv: str):
    print(eval(str(argv)))

if __name__ == '__main__':
    main(sys.argv[1])
