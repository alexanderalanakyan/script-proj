choices=$(gum choose --no-limit country latest sort protocol)

mapfile -t options <<< $choices

for i in ${options[@]}; do
    if [[ "$i" == "country" ]]; then

done
