# Minor Projects

Basic Device_Log Script and an Online Compiler

Device_Log Script
The code uses two libraries, pandas and datetime. After reading the input file, all unique device IDs are taken and then processed one by one. A dictionary is also defined to map the month name with its number. This value can then be further used to calculate time differences.
The given code is valid for just "uam" instrumentation code for now.
Now, for each ID, we first extract the time in the form of month, day, hours, minutes, seconds and milliseconds. Depending on the state, the datetime object is created for each state. A flag for states ON and OFF is also maintained to keep track of their respective occurrences. Using the datetime objects, we find the difference in the ON and OFF states to get the total seconds for which the device was on. 
Finally, the time and the error time stamps are written into a file, data.log.

Online Compiler
React Application: Online Compiler
This project involves creation of a npm package. We tend to use a function call from App.js to Compiler.js which is nothing but the actual source code for the react application.
We get our free API key (Online Judge) and use basic 4 states: Input, Output, Language Input and User Input.
Bootstrap instances were used and index.html file contains its cdn link.
