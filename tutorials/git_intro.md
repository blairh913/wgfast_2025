# Git Instructions for Beginners

[Git](https://git-scm.com)

## What is Git?
[Git](https://git-scm.com/) is a free and open source distributed version control system for working on group projects. Originally designed for developers to work collaboratively on large software projects, Git has been repurposed by many scientific communities to manage the evolution of projects in a structured and reproducible way.

With Git, all files related to a project (images, documents, code, etc.) and their change histories are stored in a single repository. Repositories support a hierarchical directory structure, meaning folders and subfolders are allowed. The WGFAST repository is hosted on GitHub in the ICES-eg workspace.

The power of Git comes from its distributed version control system (DVCS). Unlike local and centralized version control systems, in DVCSs users (clients - you) are able to fully mirror all files and folders in the project (repository) and see the project's full history from all users. Think of DVCS as the Track Changes feature in Microsoft Word on steroids.

We are only going to use a few core commands in Git, but if you want to dive deeper into Git and DVCSs, there are many tutorials online, including [vidoes, books, and external links](https://git-scm.com/doc) on the Git website. The _Getting Started_ and _Git Basics_ chapters from the [Pro Git](https://git-scm.com/book/en/v2) book (free online) is also a good place to start.

---
# To Do
1. Download Git
Download Git from the Git website. [Git Download](https://git-scm.com/downloads)

2. Install Git
How you install Git depends on your operating system.

- Linux
From the [Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) section of _Pro Git_
- MacOS
From the [Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) section of _Pro Git_
- Windows
From the [Getting Started - Installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) section of _Pro Git_

3. Configure Git
The first time you start Git on your computer you have to [configure your Git environment](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

Git comes with a `git config` tool that lets you control the configuration of many variables, including:

- Setup your user name and email address. Git uses this information to uniquely identify you in your commits
- Assign your text editor

You can view all your settings and where they come from using:
```
$ git congif --list --show-origin
```

You will probably have to hit `Enter` or the space bar to scroll through the list if your terminal is not large enough to see all the output on one screen. Type `q` to exit once you are at the end of the list.

If the output looks like a lot of gobbledygook to you, try:
```
$ git config -l
```

Again, you might have to hit `Enter` or the space bar to scroll through the list. Type `q` to exit when you are at the end of the list.


You! (Your identity)
*These settings have to be set for you to interact with GitHub.*

1. Set your user name.

```
$ git config --global user.name "John Doe"
```
Replace _John Doe_ with your user name.  

2. Set your email.
```
$ git config --global user.email johndoe@example.com
```
Replace _johndoe@example.com_ with the email linked to your GitHub account.

WARNING: Your Git username and GitHub username do not have to match. *Your Git user email has to be linked to your GitHub account*.

{empty} +

# Terminology
The [Git Glossary](https://git-scm.com/docs/gitglossary) is the technical glossary of all Git terms and commands.

These are a few Git and GitHub terms you should be familiar with before starting.

***Git*** - A type of version control system (software).  
***GitHub*** - An online (in the cloud) hosting service for Git repositories.  
***Repository*** - Also called a "repo".  A repository is a permanent record of a project's development. It tracks all changes made to files in a project over time. Initializing a repository for a project creates a `.git` folder that stores the project's history. If you delete the `.git` folder, you delete the project's record of development.  
***Clone*** (n.) / *_Cloning a repo_* (v.) - A clone of a repository is a complete (files and change histories) copy of a repository. You usually clone a repository from GitHub (hosting service) to your computer to work on project files locally.  
***Fork*** (n.) / *_Forking a repo_* (v.) - This is a special term used by GitHub and a few other hosting services. It is not a Git command. A fork is a cloned repository owned by someone else that you manage in your GitHub account. You are going to fork the `ices-eg/wg_WGFAST` repository to your own GitHub account to work on files independently before submitting any changes back to the `ices-eg/wg_WGFAST` repository.  
***Upstream repository*** - The repository you fork from.  
***Remote repository*** - A repository on GitHub or another hosting service.  
***Local repository*** - A repository on your computer.  
***Branch*** - Branches of a repository are isolated development areas. You create a branch to work on part of a project without affecting the entire project. Every repository has one default branch, usually called `master`, and can have multiple other branches. You merge branches using a pull request.  
***Checkout*** - "Checkout a branch" is to switch to a different branch in the repository.  
***Staging area*** - The staging area stores changes and additions for the next commit. The first time you add a file to the staging area allows Git to start tracking changes to that file. Staging is the step before committing a file, or changes to a file, to a repository. You can continue to edit files that have been staged.  
***Commit*** - Save all staged changes to your local repository.  
***Push*** - Move changes (commits) from your local repository to a remote repository.  
***Fetch*** - Retrieve changes from a remote repository without merging the changes into your local repository.  
***Merge*** - Incorporate the commits and files from a source repository to a target repository into a unified history. You can also merge branches within a repository.  
***Pull*** - Fetch and merge in one step.  
***Pull Request*** - Also called a "PR". A pull request tells others about the changes you have made (all the commits) to the project. It is called a pull request because you are asking to pull the changes from a source to a target. You can create a pull request between branches of a single repository or between branches of different repositories.  


image:Git_GitHub_workflow.png[]
