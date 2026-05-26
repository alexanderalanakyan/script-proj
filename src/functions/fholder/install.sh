#!/usr/bin/env bash
set -euo pipefail

gum confirm "Your BIOS is in $(cat /sys/firmware/efi/fw_platform_size) mode is this correct?" || $(echo "Refer to your motherboard manual" && exit 1)
while ! curl -fsS https://www.google.com/generate_204 >/dev/null; do
    [[ $? -gt 0 ]] && break || continue
    clear
    ../bin/impala
done



# Get all other libs:
source ./iso_timezone.sh
source ./setup.sh

export PATH="$PWD/bin:$PATH"

# skip=$(gum choose "Setup on your own" "Default Values")
# if [[ "$skip" == "Default Values" ]]; then
#     skip=""
# fi

# if [ -n "$skip" ]; then
    #   gum confirm "Would you like to make partitions?" && echo $(lsblk -adno NAME,SIZE,MOUNTPOINTS,FSTYPE | grep -v "ram") && source ./fdisk.sh && source ./swap.sh && source ./mkfs.sh && source ./mount.sh

# else
#     source ./fdisk.sh
#     source ./swap.sh
#     source ./mkfs.sh
#     source ./mount.sh
# fi
