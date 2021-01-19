# Customizing your Terminal

- [Homebrew](#install-homebrew)
- [iTerm2](#Install-iTerm2)
- [Oh My Zsh](#install-oh-my-zsh)
- [Intro to vim](#Brief-intro-to-vim)
- [Auto-suggestions & Syntax highlighting](#Set-Up-Auto-suggestions-&-Syntax-highlighting)
- [Select Your Theme](#select-your-theme)
- [Starship Theme](#install-starship-theme)

Life can be easier if you become accustomed to using terminal. 
By pimping your terminal, you boost the appearance and get cool features that make your work more efficient.


## Install [Homebrew](https://brew.sh) 

Homebrew is a free and open-source package management system available for macOS and (now also) Linux. You can install it directly from the terminal.

* Paste the following (withouth the $ sign) at the Terminal prompt.

```sh
  $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

If you're a Linux user you can also use homebrew. But if you are familiar with using another tool to manage your packages or run into an issue when using homebrew, feel free to use an alternative. Depending on your Linux distribution you can use e.g. `apt-get` instead of `brew`.

You will find a nice blogpost describing how to customize your Terminal with Oh my Zsh on Ubuntu (not using brew) [here](https://caffeinedev.medium.com/customize-your-terminal-oh-my-zsh-on-ubuntu-18-04-lts-a9b11b63f2).


## Install [iTerm2](https://www.iterm2.com/)
iTerm2, an alternative to the Terminal on Mac, is equipped with a bunch of nice features that make your life easier. 

* Install iTerm2 by entering the following line at the command prompt in your Terminal: 

```sh
  $ brew install --cask iterm2
```


## Install [Oh My Zsh](https://github.com/robbyrussell/oh-my-zsh)

Oh My Zsh allows you to customize the appearance of your terminal.

* Install it by copy pasting each line to your Terminal:

```sh
  $ brew install zsh
  $ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```


## Brief Intro to vim

Before we will install cool plugins like auto-suggestion or syntax highlighting here is short introduction to Vim. Vim is a text editor you can use from a command-line interface and it is usually set as the default editor in the Terminal. So if you type a command that will in some way open an editor, it will usually open Vim. Since navigating through Vim is not intuitive, it is good to know some basics:

* Moving inside the editor works with the arrow keys. 
* Vim has different modes:
  - To survive at the beginning you should know the **insert mode** and **command mode**. You can switch to the insert mode by pressing `i`. If you are in the insert mode the word **-- INSERT --** will appear in the lower left corner. Like the name already implies you can now insert text into the file. 
  - To change from insert mode to the **command mode** you can press `ESC` and the **-- INSERT --** will disappear. In this mode you can save the file, abort the changes and exit Vim. (Acutally you can do a lot more, but let's keep it simple for now.)
  To save and exit Vim write `:wq` (write & quit). It will appear in the lower left corner. Click enter to execute. Only saving your changes works with `:w`. To trash all changes and exit Vim you can use `:q!`.

If you want to learn more about Vim you can use the command `vimtutor` to start a tutorial directly in the command-line interface. 



## #Set Up Auto-suggestions & Syntax highlighting)

A. Auto-suggestion allows you to save time typing repeated commands, by suggesting strings from your history that you can select by just using the right arrow and tab keys in sequence.  To install it, paste the following line at the terminal prompt:

```sh
  $ brew install zsh-autosuggestions
```
B. Syntax highlighting will display text in different colors and fonts according to the category of terms.  To install syntax hightlighting, paste the following line at the terminal prompt:

```sh
  $ brew install zsh-syntax-highlighting
```

C. In order to activate both auto-suggestion and syntax highlighting you have to modify the .zshrc file. 
You can open the file with the following command:

```sh
  $ ~/.zshrc
```
The (by default) vim editor will open and you can append the following lines at the end of the file. (Make sure that only the first line will start with an `#`. The other lines have to start directly with `source`.)

```sh
# additional zsh plugins 
source /usr/local/share/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```

D. For the changes to take effect you have to reload your .zshrc file with the following command or restart your Terminal:

```sh
  $ source ~/.zshrc
```


## Select Your Theme 

Now you are using the (default) Robby Russell theme... but you can try different ones: [ZSH Themes](https://github.com/robbyrussell/oh-my-zsh/wiki/Themes)

To change for example from "robbyrussel" to the "cloud" theme all you have to do is open the .zshrc file (you will find the command above) and change value of the ZSH_Theme attribute as follows:

from

```sh
ZSH_THEME="robbyrussell"
```
to 

```sh
ZSH_THEME="cloud"
```

## Install [Starship Theme](https://starship.rs/)

There is a plethora of different Terminal themes. Depending on the tasks you are doing some themes are better suited than others. For our purpose the starship theme is a good choice. 

You can install the starship theme with the following command: 

```
  $ curl -fsSL https://starship.rs/install.sh | bash
```

In order to activate it, open the .zshrc file and paste the following line

```
eval "$(starship init zsh)"
```

after the line ZSH_THEME="robbyrussell". 
(Don't forget to run the source command or restart your Terminal.)
