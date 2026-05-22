# TODO.md
#### Why are there so many lines here?
##### Just why?
###### This is getting a little out of hand.
---
# Tasks: 

### Refactor all .py files, and convert (most) .sh files to .py for readability
### Add more checking in .py files so as to not mess up the users system:
- Add automatic CPU detection for correct ucode package
- Add automatic GPU detection for correct drivers
- Add automatic SSD/HDD detection so as to not mess with certain settings if they dont work
- Allow user to pick and see what packages are added and for what purpose
### See if certain services can be enabled and that they work as intended
### Do some testing in actual CHROOT
### See if there is some way to add commands to arch-chroot interactivly 

# Services, Packages, and more that are to be added:

> [**kernal-modules-hook**](https://github.com/saber-nyan/kernel-modules-hook) along with  **linux-modules-cleanup.service**
