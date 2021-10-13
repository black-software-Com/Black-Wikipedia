#!/usr/bin/sh
# Black Wikipedia

if [[ "$(id -u)" -ne 0 ]];
then
  echo "Please, Run This Program as Root!"
  exit
fi
function main() {
    printf '\033]2;Black-Wikipedia\a'
    clear
    echo "Installing Wikipedia..."
    chmod a+x black.py
    chmod +x install.py
    sleep 2
    apt install python
    apt install python3
    apt install python3-pip
    pip3 install --upgrade pip
    sleep 1
    echo "
Finish...

Usage:
     python black.py
"
    exit
}
main