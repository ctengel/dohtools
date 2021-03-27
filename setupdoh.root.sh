#!/bin/bash
# Usage ./setupdoh.sh DOHRESOLV CONNNAME
# Requires Fedora/RH nmcli
# Uses port 53531 on local system
cp /etc/resolv.conf /etc/resolv.conf.ctebak || exit 1
echo "nameserver 127.0.0.1" > /etc/resolv.conf || exit 1
exec nohup socat UDP4-RECVFROM:53,fork,bind=127.0.0.1 UDP4-SENDTO:127.0.0.1:4130 > /dev/null 2>&1
