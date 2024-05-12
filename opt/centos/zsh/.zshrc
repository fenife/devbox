
### ZSH HOME
export ZSH_DIR=$HOME/.zsh

### ---- history config -------------------------------------
export HISTFILE=$ZSH_DIR/.zsh_history

# How many commands zsh will load to memory.
export HISTSIZE=10000

# How many commands history will save on file.
export SAVEHIST=10000

# History won't save duplicates.
setopt HIST_IGNORE_ALL_DUPS

# History won't show duplicates on search.
setopt HIST_FIND_NO_DUPS

### ---- PLUGINS & THEMES -----------------------------------
source $ZSH_DIR/plugins/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh
source $ZSH_DIR/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
fpath=($ZSH_DIR/plugins/zsh-completions/src $fpath)

source $ZSH_DIR/themes/spaceship-prompt/spaceship.zsh-theme

### --- Spaceship Config ------------------------------------

SPACESHIP_PROMPT_ORDER=(
  user          # Username section
  dir           # Current directory section
  host          # Hostname section
  git           # Git section (git_branch + git_status)
  hg            # Mercurial section (hg_branch  + hg_status)
  exec_time     # Execution time
  line_sep      # Line break
  vi_mode       # Vi-mode indicator
  jobs          # Background jobs indicator
  exit_code     # Exit code section
  char          # Prompt character
)
SPACESHIP_USER_SHOW=always
SPACESHIP_PROMPT_ADD_NEWLINE=false
SPACESHIP_CHAR_SYMBOL="❯"
SPACESHIP_CHAR_SUFFIX=" "


