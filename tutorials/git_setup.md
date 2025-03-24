# 2. Git Setup

```{image} images/Git-Icon-1788C.png
:alt: Git Logo
:width: 100px
:align: center
```

```{note} If you use MacOS or Windows and prefer to work in a GUI (not the terminal), download and install [GitHub Desktop](https://desktop.github.com/download/). GitHub Desktop is not yet supported on Linux.
```

GUI - Graphical User Interface

&nbsp;

How you download and install Git depends on your operating system.

- MacOS  
Choose one:

**GUI** - Download and install [GitHub Desktop](https://desktop.github.com/download/)  
**Terminal** - From the [Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) section of _Pro Git_

```{image} images/GitInstall_MacOS_1.png
:alt: 
:scale: 75
:align: center
```

&nbsp;

```{image} images/GitInstall_MacOS_2.png
:alt: 
:scale: 75
:align: center
```

&nbsp;

- Windows  
Choose one:

**GUI** - Download and install [GitHub Desktop](https://desktop.github.com/download/)

**Terminal** _Git BASH_ - Download and and install [Git for Windows](https://gitforwindows.org/). Git BASH is a terminal emulator that comes with Git for Windows. Although Git for Windows is not maintained by the Git developers, they recommend using it.

**Terminal** _PowerShell_

```{warning} This is not recommended. Too many things to download and install. Unless you are a die hard Windows user and a PowerShell Wizard, do not bother. Also, we have not tried this setup and cannot help troubleshoot.
```

1. Download and install the [WinGet tool](https://learn.microsoft.com/en-us/windows/package-manager/winget/).

In the PowerShell command line, type:

```
winget install --id Git.Git -e --source winget
```

2. Download and install [posh-Git](https://github.com/dahlbyk/posh-git)

Please read the posh-Git README file and follow the instructions.

&nbsp;

- Linux  
From the [Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) section of _Pro Git_  

```{image} images/GitInstall_Linux.png
:alt: 
:scale: 75
:align: center
```

&nbsp;

## GitHub Desktop - linking with Git



## Configure Git - Terminal addition

The first time you start Git on your computer you have to [configure your Git environment](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

Git comes with a `git config` tool that lets you control the configuration of many variables, including:

- Setup your user name and email address. Git uses this information to uniquely identify you in your commits
- Assign your text editor

You can view all your settings and where they come from using:

```
git congif --list --show-origin
```

You will probably have to hit `Enter` or the space bar to scroll through the list if your terminal is not large enough to see all the output on one screen. Type `q` to exit once you are at the end of the list.

If the output looks like a lot of gobbledygook to you, try:

```
git config -l
```

Again, you might have to hit `Enter` or the space bar to scroll through the list. Type `q` to exit when you are at the end of the list.

You! (Your identity)
_These settings have to be set for you to interact with GitHub._

1. Set your user name.

```
git config --global user.name "John Doe"
```

Replace _John Doe_ with your user name.  

2. Set your email.

```
git config --global user.email johndoe@example.com
```

Replace _johndoe@example.com_ with the email linked to your GitHub account.

```{note}Your Git username and GitHub username do not have to match, but your _Git user email has to be linked to your GitHub account_.
```
