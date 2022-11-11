# Ursina-Projects
Projects of mine that are using the Ursina Engine


## Ursina Installation
Links I referenced:
- https://www.ursinaengine.org/
- https://python-poetry.org/


1. Make sure you are running Python 3.6 or newer.

*I am using pip to install in several instances. If you want to install pip, run the following code:*

`sudo apt-get install python3-pip python-dev`

2. Install ursina

`pip3 install ursina`

If you are getting this error when trying to install ursina:

`    The headers or library files could not be found for zlib,
    a required dependency when compiling Pillow from source.`
    
Try running the following line:

`sudo apt install libjpeg-dev zlib1g zlib1g-dev`

