'''Generators are iterators that allow you to iterate over a sequence of values without the need to 
store the entire sequence in memory at once. They use the yield statement to produce values one at a 
time and maintain their state between yields.

Lazy Evaluation: Generators compute their values on-the-fly, which saves memory. They don’t generate all the values at once, making 
them suitable for large datasets or infinite sequences.
State Retention: A generator retains the execution state of the function between calls, allowing it to resume where it left off.
Simpler Code: Generators simplify code related to iterations, making it cleaner than managing state manually with iterators.


Imagine you are working with a large log file that records events from a server. You want to analyze this log file to extract error messages for reporting purposes.

If the log file is too large to fit into memory, using a generator can help process each line one at a time without overwhelming your system’s memory.
'''

#Define a Generator for Reading Log Files
def read_log_lines(file_path):
    """Generator to read log file line by line."""
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()  # Use yield to return each line

# Usage of the generator
log_file_path = 'server.log'  # path to your log file

for line in read_log_lines(log_file_path):
    print(line)  # Processing each line

'''In this code:

The read_log_lines generator reads a file line by line.
Each line is yielded, allowing the caller to process it immediately without loading the entire file into memory.'''