# Simple Python Logger

I'm a master of forever programming the same code so I need an easy way to review.
This is a Python model of a system I used before in other code projects.

Basiaclly it replaces the console logging using the print(variable) with l.variable.
This fixed a disagvantage of the print() funtion by thelling you the app name (including imported) and line number.

You do not need to remove the l.variable if you do not want debugging, it just is switched on and off elsewhere.
This is no replacement for the sophisticated many optioned Python debugger and logging options available on GitHub etc, however l.var_name is simple to use and easy to control and back-track.

## Features
- Simple to use, less typing
- Unlike print(var) l.var also tells the TYPE of the var
- Does not truncate longer answers and formats the data more readable
- makes a log file with TIME stamps, APP name, LINE number, TYPE and VALUE
- print to screen and log to file are concurrent but independantly created
- can be switched ON or OFF anywhere in the code
- can be left in the code and revived anytime later 

## Setup is Easy

Add to the current directory of your Python a file called logger.py with the code.

In your code as below import the file called logger.py containing the class _logger_, and make lazy logging.

~~~
from logger import Logger
l = Logger()
~~~

That will work, making the default log file called _app.log_

It will print on the screen ie:

## Basic Example of var z
~~~
z = 22
l.z <= tell the logger to report the var z
#  RESULT ON SCREEN
z: Type: int Value: 22
#  RESULT IN APP.LOG FILE
[2024-11-28 20:13:26] c:\users\cc\desktop\_pysites\test.logger.py:15 - z: Type: int Value: 22
~~~
## A bigger variable called config
~~~
config = {"key1": "value1", "key2": "value2"}
l.config
#  RESULT ON SCREEN
config: Type: dict Value: {
  "key1": "value1",
  "key2": "value2"
}
#  RESULT IN APP.LOG FILE
[2024-11-28 20:13:26] c:\users\cc\desktop\_pysites\test.logger.py:61 - config: Type: dict Value: {
  "key1": "value1",
  "key2": "value2"
}
~~~

# Switching on and off in your code

### Turn off console logging but keep file logging
l.print(0)

### Enable console and file logging
l.print(1)  # Turn on console output
l.save(1)   # Turn on file output

# More detailed setup
Replace the l = Logger() with the following code.  It is now documenting the function and options.
~~~
l = Logger(log_to_file=True, log_file_name="app.log", print_to_console=True)
~~~
I like to use 0 and 1 for false and true

## Notes (Append Log File Option)
It overwrites the last log file, so everytime you run you Python app it will get a clean file. To append the log instead ..
~~~
# Clear the log file at the start of the run
        if self.log_to_file:
            with open(self.log_file_name, 'w') as file: <==== CHANGE THE 'w' to 'a' FOR APPEND
                file.write(f"--- Logging started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
~~~

By using the ON/OFF feature of logging and the APPEND funtion described all instances and values in one place in the code / AND / OR / MAYBE others can be monitored.

~~~
l.save(1)   # Turn on file output
l.my_important_variable # MONITOR ONLY THIS VARIABLE
l.save(0)   # Turn off file output
~~~
## Print text feature
~~~
print("another positional message with")
l.p("any message") 
~~~

## Decerator Feature Option
~~~
from logger import log
@log
def add(a, b):
     return a + b
add returned 8
#  becomes Calling add with arguments (3, 5) and {}
~~~

Cool bananas - I'm possibly contactable for any miss-fit reason.
Likely to grow legs this is a good start, and I will update this with my use comments in time.
It currently passes the whole var when confronted with l.fruits('name'), that is it will show all the fruits dictionary.
Happy hacking.








