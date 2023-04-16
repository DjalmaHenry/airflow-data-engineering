#!/usr/bin/env bash

TAG=$1

if (( EUID != 0 )); then
    echo "Please run command as root."
    exit
fi

DOWNLOADER="https://raw.githubusercontent.com/astronomer/astro-cli/main/godownloader.sh"
curl -sL -o- ${DOWNLOADER} | bash -s -- -b /usr/local/bin "$TAG"
