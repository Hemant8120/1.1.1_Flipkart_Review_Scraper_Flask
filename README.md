Flipkart Review WebScraping Project using Flask

Command Prompt Shell:

To Clone a Repository from Github:
git clone "GitHub_URL"

conda create -n env_3.6.0 python=3.6.0 -y

To activate this environment, use:
conda activate env_3.6.0

To deactivate an active environment, use:
conda deactivate env_3.6.0

To Check Python Version:
python --version

pip install -r requirements.txt
python app.py
python application.py

Git Bash Commands:
git config --global user.email "hemant8120g@gmail.com"
git config --global user.name "Hemant8120"
git config --global --list

How to Create Git Repository from VS Code:
git init
git add .
git status
git commit -m "First Commit"
git branch -M main
git remote add origin https://github.com/Hemant8120/0.1.1_Flipkart_Review_Scraper_Flask.git
git push -u origin main

error: remote origin already exists:

git remote --verbose
git remote -v

git clone https://github.com/Hemant8120/0.1.1_Flipkart_Review_Scraper_Flask.git

git remote set-url origin1 https://github.com/Hemant8120/0.1.1_Flipkart_Review_Scraper_Flask1.git
git remote add origin1 https://github.com/Hemant8120/0.1.1_Flipkart_Review_Scraper_Flask.git

Github remote permission denied:
git config --global --unset core.excludesfile
git config --global user.email "hemant8120g@gmail.com"
git config --global user.name "Hemant8120"
git config --global --list

Go the Folder in Local Machine:
C:\Users\Hemant_PC\.ssh

Delete the files if any exist

To Generate a New Key:
Go to Terminal with Local Repository: (D:\Python Projects Blog\Project-0_Web_Scraping\0.1_iNeuron_Scraper\0.1.1_Flipkart_Review_Scraper_Flask)
Type the command:
ssh-keygen

PROMPT:
Enter file in which to save the key (C:\Users\Hemant_PC/.ssh/id_rsa): "PRESS 1st-ENTER" "PRESS 2nd-ENTER" "PRESS 3rd-ENTER"

Go to Github/setting/ SSH and GPG Key/SSH keys:
Click on: New SSH Key
Title: Windows
Key:

//powershell
Go to the Local Repository(C:\Users\Hemant_PC), where SSH Key has generated:
Open it with Powershell, and type the command:
Get-Content ~/.ssh/id_rsa.pub | Set-Clipboard

By doing this, SSH Key has copied into my PC's Clipboard
Go to Github/setting/ SSH and GPG Key/SSH keys:
Key: "PASTE IT HERE"

Click on: Add SSH Key

fatal: unable to access 'https://github.com/Hemant8120/0.1.1_Flipkart_Review_Scraper_Flask.git/': The requested URL returned error: 403
Go to Github/Settings/Developer Settings/Persona access tokens/Tokens(classic)
Click on: Generate new token / Generate new token(classic)

Note: authentication

Select scopes:
repo (Ckeck it)
workflow (Ckeck it)
write:packages
delete:packages
admin:org
admin:public_key
admin:repo_hook
admin:org_hook
gist
notifications
user (Ckeck it)
delete_repo
write:discussion (Ckeck it)
admin:enterprise (Ckeck it)
audit_log
codespace
copilot
project
admin:gpg_key (Ckeck it)
admin:ssh_signing_key

Click on: Generate token
Personal access tokens (classic): "SAVE THE KEY IN SAFE PLACE"

How do I change/switch user credentials used by git command line? (Windows 10, Git 2.9.2):
PATH: Control Panel\User Accounts\Credential Manager:
Select option: git:https://github.com: REMOVE

ALL DONE!
