#!/bin/bash
# USAGE: ./stopdoh.sh CONNNAME
# Run after setupdoh.sh
cp /etc/resolv.conf.ctebak /etc/resolv.conf || exit 1
sleep 60 || exit 1
pkill socat || exit 1
pkill doh-stub || exit 1
