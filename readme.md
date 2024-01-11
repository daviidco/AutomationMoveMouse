# Automation Move Mouse - Python
Simple application python. Open program mac and move mouse for specific time


## Table of content
1. [Overview](https://github.com/daviidco/AutomationMoveMouse#-overview)  
3. [Requirements](https://github.com/daviidco/AutomationMoveMouse#-requirements)
2. [Download](https://github.com/daviidco/AutomationMoveMouse#%EF%B8%8F-download)
4. [Configure Project with Alias MAC](https://github.com/daviidco/AutomationMoveMouse#%EF%B8%8F-configure-project-with-alias-mac)
5. [Run from terminal](https://github.com/daviidco/AutomationMoveMouse#%EF%B8%8F-run-project-from-terminal)

## 	📜 Overview
Simple application python. Open program mac and move mouse for specific time

## ✅ Requirements

- Python 3.10.5


## ⬇️ Download
Clone project with ssh key:
```
git@github.com:daviidco/AutomationMoveMouse.git
```
or clone project using https:
```
https://github.com/daviidco/AutomationMoveMouse.git
```
## Install python version on Mac (good practice with multiplies versions):
```brew install xz```
```brew install pyenv```
```pyenv global 3.10.5```

## Creates a virtual environment and install necessary pacakges
```python3.10.5 -m venv movemouseenv```
Go to project downloded and search requirements.txt
```pip install -r requirements.txt```


## ⚙️ Configure Project with Alias MAC
Create alias MAC. From terminal: 
```nano ~/.zshrc```

set alias:

```alias movemouse='source /locationvirtualenvironment/bin/activate; python3 /locationproject/AutomationMoveMouse/main.py'```

The alias first activate the environment of project and end with ";" continue with specified the main.py file.

## ▶️ Run Project from terminal
Open terminal Mac, and type the next command:

```movemouse```

The previous command sets for default 15 minutes

If you want specified a range time of 10 minutes:

```movemouse 10```

```movemouse {num_minutes}```

To stop execution use the hotkeys

```control + c```

or 

```command + option + esc```

and kills the process 


  

