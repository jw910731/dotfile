# This Repository Is No Longer Used and Maintained
I uses nix and the related file are placed here: [https://github.com/jw910731/nixfile](https://github.com/jw910731/nixfile).

# Intro
This is my dot files for my working Linux and Mac OS X desktop environment. Including zsh config, gnupg config, i3 config (for Linux) and some utils for daily use.

Note that the dotfiles is force to run in locale zh_TW.UTF-8 on Linux when using i3wm as window manager.

# Required Packages
These packages are needed for the dotfiles to work properly.
On macOS only *CLI* and *Recommended tools* are strongly required. (Cause there's no user interface config for macOS in this repo)

On Linux you need to satisfy all requirements to gain a consistant experience in i3wm with my custom settings. Or use KDE Plasma as alternative windows manager. These dotfile are meant to be work on KDE Plasma, though experience consistancy is not guaranteed on KDE Plasma.
## CLI
- **chezmoi**
- zsh
- fish *(alternative with light settings)*
- git
- fzf
- most
- joe
- lsd
- bat *(optional)*
- code *(optional)*
### Yubikey & gpg
- yubikey-manager
    Remember to enable `pcscd.service` systemd service
- gnupg
- pinentry *(For pacman)*
- pinentry-mac *(For hombrew mac)*

# Linux X11 environment
Most of these are Arch Linux AUR or package name. You will need to find alternatives if you are not using Arch Linux.
- i3wm-gaps **(i3wm is deprecated and is not compatible with this dot file)**
- Xresources (pacman: `xorg-xrdb`)
- xrandr
- python3
- rofi
- rofi-calc
- dunst
- polybar
- dbus-python
- noto-fonts-cjk
- siji-git
- playerctl
- nitrogen
- dex
- polkit-kde-agent
- xidlehook *(optional)*
- numlockx *(optional)*
- ddcutil *(optional)*
- picom *(optional)*
## IME
- hime-git
- libchewing

# Wayland
Plan to migrate to sway. But HiDPi support of Xwayland is bad and the migration is suspended.
*Working in progress*

## Recommended util programs
The dotfiles is meant to be work with these programs.
- Terminal: kitty or iTerm2 (on mac)
- Editor: joe & Visual Studio Code
- VCS: git
- Yubikey 5

# Thank list
I must give these repository and their author a big thank for being a reference of my dotfile
- [Birkhoff's Dotfile](https://github.com/BirkhoffLee/dotfiles)
- [i3 Starterpack](https://github.com/addy-dclxvi/i3-starterpack)
