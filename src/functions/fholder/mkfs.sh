while true; do
    disk=$(jq -r '.blockdevices[].name' <<< "$devices" | grep -v "ram" | gum choose --header "On which disk are the partitions would you like to edit?")
    partitions=$(jq -r --arg d "$disk" '.blockdevices[] | select(.name == $d) | .children[]? | select(.type == "part") | .name' <<< "$devices")
    selected_partition=$(printf "%s\n" $partitions | gum choose --header "Which partition would you like to make a filesystem on?")
    findmnt "/dev/$selected_partition" && echo "That partition is already mounted? That should not happen please fix manually" && exit 1
    fs_type=$(gum choose --header="Which FS would you like to use?" ext4 btrfs)
    gum confirm "Would you like to make $selected_partition of filesystem: $fs_type" || continue
    if [[ "$fs_type" == "ext4" ]]; then
        mkfs.ext4 "/dev/$selected_partition"
    elif [[ "$fs_type" == "btrfs" ]]; then
        #REFACTOR
        echo "Placeholder for now"
        # label=$(gum input --prompt="What is the label for your btrfs fs: ")
        # [ -z "$label" ] && continue
        # mkfs.btrfs -L $label "/dev/$selected_partition"
    fi

    gum confirm "Exit?" && break || continue
done
