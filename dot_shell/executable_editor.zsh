#!/usr/bin/env zsh
env -i LANG=zh_TW.UTF-8 LC_ALL="zh_TW.UTF-8" LANGUAGE="zh_TW:zh" $(which code)
env -i LANG=zh_TW.UTF-8 LC_ALL="zh_TW.UTF-8" LANGUAGE="zh_TW:zh" code

$(which code) --wait -- "$@"