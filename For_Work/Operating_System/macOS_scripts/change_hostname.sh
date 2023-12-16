#!/bin/bash

# m1 / m2 - не работает

hostname="HOSTNAME"

sudo scutil --set HostName $hostname
sudo scutil --set LocalHostName $hostname
sudo scutil --set ComputerName $hostname
