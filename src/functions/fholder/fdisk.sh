
devices=$(lsblk -aJo NAME,SIZE,MOUNTPOINT,TYPE,FSTYPE)
while true; do
    disk=$(jq '.blockdevices[].name' <<< "$devices" | grep -v "ram" | gum choose --header "Which disk would you like to make partitions?")
    [[ -z "$disk" ]] && break

   udevadm trigger
   udevadm settle

    disk_data=$(lsblk -adno FSTYPE,SIZE,MOUNTPOINTS "/dev/$disk")

    msg=$(printf "Would you like to edit %s?\n\n%s" "$disk" "$disk_data")

    if gum confirm "$msg"; then
        fdisk "/dev/$disk"
        continue
    fi

    if gum confirm "Exit?"; then
        break
    fi
done