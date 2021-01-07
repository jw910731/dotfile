#!/usr/bin/env zsh

# `.exports` is used to provide custom variables.
#
# This file is used as a part of `.sh_env`

# === General ===

# Language
export LANG=en_US.UTF-8
export LC_ALL="en_US.UTF-8"

# Editor
if (( $+commands[code] )); then
    export EDITOR="$HOME/.shell/editor.zsh"
    export VISUAL="$HOME/.shell/editor.zsh"
else
    export EDITOR="$(which joe)"
    export VISUAL=${EDITOR}
fi

