#!/usr/bin/env bash

echo Installing CLI stuff.

# install prezto (disabled for now)

#if [ ! -e "${ZDOTDIR:-$HOME}/.zprezto" ]; then
#  git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"
#  git clone --recurse-submodules https://github.com/belak/prezto-contrib "${ZDOTDIR:-$HOME}/.zprezto/contrib"
#fi

# install zinit

if [ ! -e "$HOME/.zinit" ]; then
    mkdir ~/.zinit
    git clone https://github.com/zdharma-continuum/zinit.git $HOME/.zinit/bin
    zsh -i -c "zinit self-update"
fi

if [ ! -d "$HOME/dev" ]; then
    mkdir "$HOME/dev"
fi

# zsh compaudit
echo "Fixing dot file permission"
zsh -i -c "compaudit | xargs chmod g-w" || true

# install spacemacs
if [ ! -d "$HOME/.emacs.d" ]; then
    git clone https://github.com/syl20bnr/spacemacs "$HOME/.emacs.d"
fi
