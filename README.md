# weather_cli

A simple command-line interface for querying the current weather forecast for 
any entered city. 

### usage

To use, ensure that you have python3 installed, and then use pip to install 
`geopy` and `requests`:

```
$ pip install geopy 
$ pip install requests
```

To run the "app":

```
$ python3 weather_cli.py
```
and then enter a city name when prompted. If the city name is left blank and 
"Enter" is pressed, the program defaults to displaying the weather of Eugene,
Oregon. To quit, enter "quit".

### future improvements
This was really just a small simple thing that I wanted to build, and honestly 
it did not take much effort, but it was fun to get back into the groove of 
building something, even something as small as this. Whether I actually improve
it in the future is a very hand-wavy ordeal. 

Currently, it only works with cities in the U.S. (that I have found, at least), 
and it will need some improvements to work for any country on earth. 

### credits

This was partly based on [this](https://www.howtogeek.com/how-i-built-my-own-command-line-weather-app-with-python/) 
project, though I really only used their instructions to figure out what python 
packages to use, and what API to call. I did my best to figure the rest out on 
my own. 
