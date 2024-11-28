from logger import Logger  # REQUIRED

# Initialize the logger
l = Logger(log_to_file=True, log_file_name="app.log", print_to_console=True) # REQUIRED TO DOUCMENT 
# In python you can say also Logger(log_file_name="another.txt")
# Test variables
var_name = "Hello, Logger!"
config = {"key1": "value1", "key2": "value2"}

z =22
l.z #    < = Now on your console the type and value of z is shown, and put with more detail in the app.log file

# just to show logging works within a function
def says_hell0(t):
    banned_words = set([ 
    "a", "an", "the", "and", "or", "is", "are", "was", "were", "be", "been", 
    "to", "of", "in", "on", "at", "for", "with", "by", "about", "this", "that",
    "it", "from", "as", "but", "if", "not", "can", "will", "do", "does", "did",
    "we", "you", "he", "she", "they", "i", "my", "your", "his", "her", "their",
    "our", "me", "us", "him", "them", "who", "what", "where", "when", "why",
    "how", "which"
])
    other_type = [" a", "an", "the", "and", "or", "is"]
    x = 2 + 3 +t
    l.x
    l.banned_words
    l.other_type
    
    # 
    fruits = ("apple", "banana", "cherry")
    l.fruits
    
    # Represent a record as a dictionary
    employee1 = {"id": 1, "name": "Alice", "position": "Developer", "salary": 70000}
    l.employee1
    # as a list of dictionary
    employees = [
    {"id": 1, "name": "Alice", "position": "Developer", "salary": 70000},
    {"id": 2, "name": "Bob", "position": "Designer", "salary": 65000},
    {"id": 3, "name": "Charlie", "position": "Manager", "salary": 80000}
]
    l.employees
    
    # Log the entire employees list
    l.employees = employees
    
    
    for emp in employees:
        l.emp['name'] #  <== currently displays the full variable container
        print(emp['name'])
    return

# Enable console and file logging < - EXAMPLE BUT ALREADY ON
l.print(1)  # Turn on console output
l.save(1)   # Turn on file outpu

# Log variables dynamically
l.var_name  # Log the details of 'var_name'
l.config    # Log the details of 'config'

says_hell0(z)

# Log variables dynamically
l.var_name  # Log the details of 'var_name'
l.config    # Log the details of 'config'

# Turn off console logging but keep file logging
l.print(0)
l.var_name  # This will only log to the file, not the console

