# Automation Move Mouse - Python
Simple application python. Open program mac and move mouse for specific time


## Table of content
1. [Overview](https://https://github.com/daviidco/AutomationMoveMouse/#Overview)  
3. [Requirements](https://github.com/daviidco/AutomationMoveMouse/#Requirements)
2. [Download](https://github.com/daviidco/AutomationMoveMouse/#Download)
4. [Configure Project with Alias MAC](https://github.com/daviidco/AutomationMoveMouse/#ConfigurePoc)
5. [Run from terminal](https://github.com/daviidco/AutomationMoveMouse/#RunPoc")

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

## ⚙️ Configure Project with Alias MAC
Create alias MAC. From terminal: 
```nano ~/.zshrc```

set alias:

```alias movemouse='source /Users/NameUser/Documents/projects//ove_mouse/venv/bin/activate; python3 /Users/NameUser/Documents/projects/move_mouse/main.py'```

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


  

