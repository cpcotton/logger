# Simple Python Logger

I'm a master of forever programming the same code so I need an easy way to review.
This is a Python model of a system I used before in other code projects.

Basiaclly it replaces the console logging using the print(variable) with l.variable

You do not need to remove the l.variable if you do not want debugging, it just is switched on and off elsewhere.
This is no replacement for the sophisticated many optioned Python debugger and logging options, howere it is simple to use and easy to control.

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

In your code as below import a file caller logger.py containing the class _logger_, a set of funtions to make lazy logging.

~~~
import Logger as l
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
var_name: Type: str Value: 'Hello, Logger!'
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
Replace the l = Logger() WITH
~~~
l = Logger(log_to_file=True, log_file_name="app.log", print_to_console=True)
~~~
I like to use 0 and 1 for false and true

## Notes
It overwrites the last log file, so everytime you run the py app it will get a clean file. To append the log..
~~~
# Clear the log file at the start of the run
        if self.log_to_file:
            with open(self.log_file_name, 'w') as file: <==== CHANGE THE 'w' to 'a' FOR APPEND
                file.write(f"--- Logging started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
~~~


Cool bananas - I'm possibly contactable for any miss-fit reason.
Likely to grow legs this is a good start, and I will update this with my use comments in time.
It currently passes the whole var when confronted with l.fruits('name'), that is it will show all the 'name' dictionary.
Happy hacking.







