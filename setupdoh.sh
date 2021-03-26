#!/bin/bash
# Usage ./setupdoh.sh DOHRESOLV CONNNAME
# Requires Fedora/RH nmcli
# Uses port 53531 on local system
sudo true || exit 1
~/.local/bin/doh-stub --domain "$1" --listen-port 53531 --listen-address 127.0.0.1 &
sudo socat UDP4-RECVFROM:53,fork,bind=127.0.0.1 UDP4-SENDTO:127.0.0.1:53531 &
nmcli con mod --temporary "$2" ipv4.dns 127.0.0.1 && nmcli con mod --temporary "$2" ipv4.ignore-auto-dns yes && nmcli con down "$2" && nmcli con up "$2"
