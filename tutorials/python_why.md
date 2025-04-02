---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# To Python or not to Python?  

## Install Python, conda, mamba, echopype - Miniforge

The very easiest way to get a minimal install of [Conda](https://conda.io/), [Mamba](https://github.com/mamba-org/mamba) and Python, with conda-forge as default channel is to install [Miniforge](https://github.com/conda-forge/miniforge).  
Once Miniforge is installed, you should be able to use ```conda``` and ```mamba``` in your terminal.  

The very easiest way to install Miniforge is to download and run a provided installer for your OS  from [https://conda-forge.org/download/](https://conda-forge.org/download/)  

**Mac & Linux**: Download the installer and run ```bash Miniforge3-$(uname)-$(uname -m).sh```
**Windows**: download and run the Windows installer.  

**Note for Windows users:**  
By default the commands are not added to the path environment (making them available in the default Windows Command Prompt (CMD)). This is a precautious step, to avoid chances of software conflicts.  
*Solutions:*  

* Option 1 (easiest, safest): Use *Anaconda Prompt*, like the freshly installed *Miniforge Prompt*
* Option 2: Initialise conda in the *Anaconda Prompt* by typing ```conda init```. Close your propmpt window and open it again. Now the commands should be available
* Option 3: [Manually add](https://learn.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14)#to-add-a-path-to-the-path-environment-variable) ```C:\Users\myusername\miniforge3\condabin``` to the path environment. This will allow you to use the commands from any prompt, with limited risk of conflicts with other software.  