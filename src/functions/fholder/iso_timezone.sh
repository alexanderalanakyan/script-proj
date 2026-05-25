
timezone=$(curl -fsS https://ipapi.co/timezone | sed 's/$/\n/' \
    || curl -fsS http://ip-api.com/line/?fields=timezone)

gum confirm "Your timezone is $timezone correct?" \
    || timezone=$(gum input --prompt="Input your timezone: ")

while true; do
    if timedatectl list-timezones | grep -Fxq "$timezone"; then
        timedatectl set-timezone "$timezone"
        break
    else
        echo "Invalid timezone: $timezone"
        timezone=$(gum input --prompt="Try again: ")
    fi
done
echo "Timezone set to $timezone"