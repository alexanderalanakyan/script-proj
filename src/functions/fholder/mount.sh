
while true; do
    disk=$(jq -r '.blockdevices[].name' <<< "$devices" | grep -v "ram" | gum choose --header "On which disk are the partitions would you like to edit?")
    partitions=$(jq -r --arg d "$disk" '.blockdevices[] | select(.name == $d) | .children[]? | select(.type == "part") | .name' <<< "$devices")
    selected_partition=$(printf "%s\n" $partitions | gum choose --header "Which partition would you like to mount?")
    mountdir=$(gum input --prompt="Which dir would you like to mount $selected_partition to, relative to /: ")
    while [[ ! -d $mountdir ]]; do
        gum confirm "Make dir --affirmative="Make mount directory" --negative="Change mount directory" $mountdir during mount or change mount directory" && mount --mkdir "/dev/$selected_partition" $mountdir && break || mountdir=$(gum input --prompt="Which dir would you like to mount $selected_partition to, relative to /: ") && continue
        [[ $? -gt 0 ]] && break || continue
    done
    gum confirm "Done with mounting?" && break || continue

done