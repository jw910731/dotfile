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
    env -i LANG=zh_TW.UTF-8 LC_ALL="zh_TW.UTF-8" LANGUAGE="zh_TW:zh" code
    export EDITOR="$(which code) --wait"
    export VISUAL="$(which code)"
else
    export EDITOR="$(which joe)"
    export VISUAL=${EDITOR}
fi

