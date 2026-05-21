#!/usr/bin/env bash

if ! curl -fsS https://www.google.com/generate_204 >/dev/null then
clear
iw_footer
iwctl

fi

declare -A pkgs=(
    [tput]="ncurses"

    [gum]="gum"
)

for bin in "${!pkgs[@]}"; do
    if ! command -v "$bin" >/dev/null 2>&1; then
        echo "Installing package for $bin: ${pkgs[$bin]}"
        sudo pacman -S --noconfirm "${pkgs[$bin]}"
    fi
done

iw_footer() {
    tput sc
    tput cup $(($(tput lines)-1)) 0
    tput el
    echo -n "station list=get stations | station <station> scan=scan for networks && station <station> get-networks=get networks from scan | station <station> connect <network_name>=connect to network"
    tput rc
}
fdisk_footer() {
    tput sc
    tput cup $(($(tput lines)-1)) 0
    tput el
    echo -n "n=new partition | t=change parition type | w=write | d=delete | m=help | q=quit"
    tput rc
}
tmux 
tmux set-option status on

while true; do
    clear

    echo "Select a disk:"
    choice=$(lsblk -dn -o NAME | grep -v zram | gum choose --limit 1)

    if [[ -z "$choice" ]]; then
        echo "No device selected. Exiting."
        break
    fi

    if gum confirm "Do you want to edit /dev/$choice?"; then
        sudo fdisk "/dev/$choice"
    fi

done