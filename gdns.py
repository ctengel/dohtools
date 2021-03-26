#!/usr/bin/env python3

import sys
import collections
import dohresolver

# parse args into list of hosts
hosts = sys.argv[1:]
www = ['www.{}'.format(i) for i in hosts]
hosts = hosts + www
hosts = list(set(hosts))

# build a dictionary of IP to hosts
out = collections.defaultdict(list)
for i in hosts:
    trier = dohresolver.doh_resolve(i)
    if trier:
        out[dohresolver.doh_resolve(i)].append(i)

# output
for k, v in out.items():
    print("{}\t{}".format(k, " ".join(v)))
