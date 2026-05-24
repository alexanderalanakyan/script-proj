#!/usr/bin/env bash
set -euo pipefail
# if ! curl -fsS https://www.google.com/generate_204 >/dev/null; then
# clear
# ../bin/impala
# fi
# cd ../ && source ../setup.sh && cd install
export PATH="$PWD/bin:$PATH"
# timezone=$(curl -fsS https://ipapi.co/timezone \
#     || curl -fsS http://ip-api.com/line/?fields=timezone)

# gum confirm "Your timezone is $timezone correct?" \
#     || timezone=$(gum input --prompt="Input your timezone: ")

# while true; do
#     if timedatectl list-timezones | grep -Fxq "$timezone"; then
#         timedatectl set-timezone "$timezone"
#         break
#     else
#         echo "Invalid timezone: $timezone"
#         timezone=$(gum input --prompt="Try again: ")
#     fi
# done
# echo "Timezone set to $timezone"
while true; do
    disk=$(lsblk -adn -o NAME | grep -v "ram" | gum choose)
    udevadm trigger && udevadm settle lsblk -fo NAME,FSTYPE,SIZE,MOUNTPOINTS /dev/"$disk"
    # gum confirm "Would you like to edit $disk?" || gum confirm "Would you like to exit?" && break || continue

   # fdisk "/dev/$disk"
done
