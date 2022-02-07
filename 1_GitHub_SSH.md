# Adding SSH key to GitHub

During the bootcamp we will use git and GitHub a lot. You will fork and clone repositories from GitHub to your local machine and in the other direction push changes from your local machine to GitHub.  
If you don't want to type your password every time you want to interact with git and github, you can set an SSH key. 


## Create private and public ssh-key

Let's start by creating a new SSH key on your machine. Open the Terminal and run following command. It will ask you to enter several things but you should just *leave all prompts blank and just press **enter*** each time. 

```
$ ssh-keygen
```
Remember - just press *enter* at each prompt!

This will create a hidden folder called **.ssh**. With the command we will copy the contents of the **id_rsa.pub** file into your clipboard. The vertical line in the text below is called a pipe, on a DE keyboard it is made by pressing *option+7*

```
$ cat ~/.ssh/id_rsa.pub | pbcopy
```

This copies key text to your clipboard. If you don't believe us, you can verify this by cmd+v to paste the text somewhere. 

## Adding key to GitHub

Go on GitHub and click in the upper right corner on your profile. Then go to **settings** and select on the left side **SSH and GPG keys**. Click on new SSH key, give it a meaningful name (something like "neuefische bootcamp mac") and paste the copied public-key into the key field. Click on add and you are done! :) 

You can find the GitHub documentation on that topic [here](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).

If you want to test your SSH connection you will find the instructions [here](https://docs.github.com/en/github/authenticating-to-github/testing-your-ssh-connection).
