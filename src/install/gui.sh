#!/usr/bin/env bash

if [ -z "$TMUX" ]; then
tmux
tmux set-option status on
fi


if ! curl -fsS https://www.google.com/generate_204 >/dev/null; then
clear
iwctl
fi

timezone=$(curl http://ipapi.co/timezone || curl http://ip-api.com/line/?fields=timezone)
if [ ! -z "$timezone" ] && [ "$timezone" ]



mt() {
while true; do
    devices=$(lsblk -P -o NAME,MOUNTPOINT,TYPE)
    clear

    echo "Choose which folder you would like to mount:"

    fdlr=$(gum choose $(find /mnt/ -type d))

    devi=$(gum choose $(
         echo "$devices" |
        awk '$3 ~ /part/ {
            gsub(/NAME=|"/, "", $1)
            print "/dev/"$1
        }'
    ))
  fs=$(lsblk -pnro NAME,FSTYPE | awk -v dev="$devi" '$1 == dev {print $2}')
  if [ -z "$fs" ]; then
    echo "no filesystem found"
    mfs=$(gum choose --header="What filesystem would you like for $devi?" ext4 btrfs)
    mkfs."$mfs" "$devi"
  fi
    gum confirm "Would you like to mount /dev/$devi to $fdlr?" || continue

    mount "$devi" "$fdlr" || continue
    mountedevs=$(df -Th)
    gum confirm "Done with mounts? Currently mounted devices:\n$mountedevs\n" && exit || continue
done
}

while true; do
    clear

    echo "Select a disk:"
    choice=$(lsblk -dn -o NAME | grep -v zram | gum choose --limit 1)

    if [[ -z "$choice" ]]; then
        echo "No device selected. Exiting."
        break
    fi

    if gum confirm "Do you want to edit /dev/$choice?"; then
        fdisk "/dev/$choice"
    fi
done
