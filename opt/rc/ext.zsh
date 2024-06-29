
# Incremental completion on zsh: 实时补全
source $ZSH_CUSTOM/plugins/incr/incr.zsh

# 关闭自动更新
zstyle ':omz:update' mode disabled

# 解决zsh粘贴卡慢问题
pasteinit() {
  OLD_SELF_INSERT=${${(s.:.)widgets[self-insert]}[2,3]}
  zle -N self-insert url-quote-magic # I wonder if you'd need `.url-quote-magic`?
}

pastefinish() {
  zle -N self-insert $OLD_SELF_INSERT
}
zstyle :bracketed-paste-magic paste-init pasteinit
zstyle :bracketed-paste-magic paste-finish pastefinish


############################################################
export TERM xterm
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8

export BASE_OPT_DIR=/wine/devbox/opt

export PATH=$PATH:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/go/bin:$BASE_OPT_DIR/devc/bin

############################################################

alias runc="make -f Makefile.runc" 
alias runs="make -f Makefile.runs"

alias rinh="make -f Makefile.rinh"
alias rinc="make -f Makefile.rinc"
alias rind="make -f Makefile.rind"
alias rinv="make -f Makefile.rinv"

alias jopt="cd ${BASE_OPT_DIR}" 
alias jdevc="cd ${BASE_OPT_DIR}/devc" 
alias jroam="cd ${BASE_OPT_DIR}/roam" 
alias jwork="cd ${BASE_OPT_DIR}/work" 
alias jrc="cd ${BASE_OPT_DIR}/rc" 


