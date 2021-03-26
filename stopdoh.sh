#!/bin/bash
# USAGE: ./stopdoh.sh CONNNAME
# Run after setupdoh.sh
sudo true || exit 1
nmcli con mod --temporary "$1" ipv4.ignore-auto-dns no && nmcli con down "$1" && nmcli con up "$1" || exit 1
sudo pkill socat || exit 1
pkill doh-stub || exit 1
