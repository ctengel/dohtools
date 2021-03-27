#!/bin/bash
# nohup ./setupdoh.sh DOHRESOLV
# Uses port 4130 on local system
exec nohup ~/.local/bin/doh-stub --domain "$1" --listen-port 4130 --listen-address 127.0.0.1 > /dev/null 2>&1
