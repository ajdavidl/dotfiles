:set number
:set relativenumber
:set autoindent
syntax enable
set background=dark
colorscheme solarized
:set tabstop=4
:set mouse=a
:set shiftwidth=4
:set softtabstop=4
:set wildmenu

" enable syntax and plugins (for netrw)
syntax enable
filetype plugin on



" FINDING FILES:
" Search down into subfolders
" Provides tab-completion for all file-related tasks
set path+=**
" Display all matching files when we tab complete
" set wildmenu
" NOW WE CAN:
" - Hit tab to :find by partial match
" - Use * to make it fuzzy
" THINGS TO CONSIDER:
" - :b lets you autocomplete any open buffer


let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
    autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin()

Plug 'https://github.com/vim-airline/vim-airline' " Status bar
Plug 'https://github.com/vim-airline/vim-airline-themes'
Plug 'https://github.com/preservim/nerdtree' " nerdtree
Plug 'https://github.com/neoclide/coc.nvim', {'branch': 'release'}

call plug#end()

" airline
let g:airline_theme='solarized'

" coc config
 let g:coc_global_extensions = [
\ 'coc-snippets',
\ 'coc-pairs',
\ 'coc-tsserver',
\ 'coc-eslint', 
\ 'coc-prettier', 
\ 'coc-json', 
\ 'coc-python',
\ ]

" use <tab> for trigger completion and navigate to the next complete item
 function! s:check_back_space() abort
   let col = col('.') - 1
     return !col || getline('.')col - 1][  =~ '\s'
endfunction

inoremap <silent>expr>< <Tab>
     \ pumvisible() ? "\<C-n>" :
     \ <SID>check_back_space() ? "\<Tab>" :
     \ coc#refresh()]

" https://github.com/changemewtf/no_plugins/blob/master/no_plugins.vim
" https://github.com/NeuralNine/config-files/blob/master/init.vim
" https://github.com/josethz00/neovim-like-vscode/blob/main/init.vim
