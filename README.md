# neurolab-mongo-python

![image](https://user-images.githubusercontent.com/57321948/196933065-4b16c235-f3b9-4391-9cfe-4affcec87c35.png)

### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

'''
wget
'''

editing in neurolab


Git Commands :-

If you are starting a project and you want to use git in your project
'''
git init
'''
This is going to initialize git in your source code.

OR 

You can clone existing github repo 
'''
git clone <github_url>
'''
Note: Clone/ Download Github repo in your system


Add your changes made in file to git stageing are
'''
git add file_name
'''
Note- You can give file_name to add specific file or use '.' to add everything to stageing area


Create commits
'''
git commit -m "message"
'''

'''
git push origin main
'''
Note: origin --> contains url to your github repo
main --> is your branch name

To push your changes forcefully
'''
git push origin main -f
'''


To pull your changes from github repo
'''
git pull origin main
'''


Ubuntu Commands at AWS VM :-
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker