import json
import inspect
from datetime import datetime

# Logging Decorator:
def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

class Logger:
    def __init__(self, log_to_file=True, log_file_name="app.log", print_to_console=True):
        """Initialize the logger with optional file and console logging."""
        self.log_to_file = log_to_file
        self.log_file_name = log_file_name
        self.print_to_console = print_to_console

        # Clear the log file at the start of the run
        if self.log_to_file:
            with open(self.log_file_name, 'w') as file:
                file.write(f"--- Logging started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

    def print(self, flag):
        """Enable or disable console logging."""
        self.print_to_console = bool(flag)

    def save(self, flag):
        """Enable or disable file logging."""
        self.log_to_file = bool(flag)
    
    def p(self,message):
        """Write the log message to the console and/or the log file."""
        # Get the source file and line number
        frame = inspect.currentframe().f_back
        file_name = inspect.getfile(frame)
        line_number = frame.f_lineno

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = (f"{file_name}:{line_number}\n[{timestamp}]: *** {message}***")
        
        if self.print_to_console:
            print(f"Log: {log_line}\n")

        # Log to file if enabled and not a console-only message
        if self.log_to_file:
            with open(self.log_file_name, 'a') as file:
                file.write(f"{log_line}\n")
        

    def log(self, message, console_only=False):
        """Write the log message to the console and/or the log file."""
        # Log to console only if enabled and not a duplicate
        if self.print_to_console and console_only:
            print(message)

        # Log to file if enabled and not a console-only message
        if self.log_to_file and not console_only:
            with open(self.log_file_name, 'a') as file:
                file.write(f"{message}\n")

    def __getattr__(self, name):
        """Intercept attribute access to log variable details."""
        # Use the stack to get the caller's context
        frame = inspect.currentframe().f_back
        local_vars = frame.f_locals

        if name in local_vars:
            value = local_vars[name]
            log_message = self._format_log(name, value)
            # Log to file with full details
            self.log(log_message)
            # Log to console without full details
            self.log(log_message.split(' - ')[-1], console_only=True)
            return value  # Return the variable's value
        else:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")

    def _format_log(self, var_name, value):
        """Format the log entry with variable details."""
        if isinstance(value, (dict, list)):
            value_str = json.dumps(value, indent=2)  # Pretty-print dictionaries and lists
        else:
            value_str = repr(value)  # Default representation for other types

        # Get the source file and line number
        frame = inspect.currentframe().f_back.f_back
        file_name = inspect.getfile(frame)
        line_number = frame.f_lineno

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"[{timestamp}] {file_name}:{line_number} - {var_name}: Type: {type(value).__name__} Value: {value_str}"
