# Ursina-Projects
Projects of mine that are using the Ursina Engine


## Ursina Installation

Links I referenced:

*Installing Ursina*

- https://www.ursinaengine.org/

*Installing Poetry*

- https://python-poetry.org/*

*Updating Python version to 3.7

- https://answersdb.com/programming/how-do-i-switch-to-python-37-in-ubuntu.html#:~:text=Upgrade%20Python%203.7%201%20Step%201%3A%20Install%20the,Step%204%3A%20Test%20the%20version%20of%20python%20


1. Make sure you are running Python 3.6 or newer.

*I am using pip to install in several instances. If you want to install pip, run the following code:*

`sudo apt-get install python3-pip python-dev`

2. Install ursina

`pip3 install ursina`


### Potential Errors/Issues You Run Into

If you are getting this error when trying to install ursina:

***`The headers or library files could not be found for zlib,
    a required dependency when compiling Pillow from source.`***
    
Try running the following line:

`sudo apt install libjpeg-dev zlib1g zlib1g-dev`

