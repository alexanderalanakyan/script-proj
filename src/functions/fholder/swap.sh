choice=$(gum choose --header="Choose between swap partition, and zram" zram spart)
if [[ "$choice" = "zram" ]]; then
    #REFACTOR
    echo "Not implemented yet"
else
    disk=$(jq -r '.blockdevices[].name' <<< "$devices" | grep -v "ram" | gum choose --header "On which disk are the partitions would you like to enable swap on/make a swap file on")
    partitions=$(jq -r --arg d "$disk" '.blockdevices[] | select(.name == $d) | .children[]? | select(.type == "part") | .name' <<< "$devices")
    selected_partition=$(printf "%s\n" $partitions | gum choose --header "Which partition would you like to edit swap on?")
    gum confirm "Make $selected_partition swap?" && mkswap "/dev/$selected_partition"
fi
