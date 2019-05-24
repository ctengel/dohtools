#!/usr/bin/env python3

import dohresolver
import requests
import sys

session = dohresolver.doh_session()
blasession = requests.session()

print(session.get(sys.argv[1]).text)
print(blasession.get(sys.argv[1]).text)
