# Regular Expressions

### Regular Expression Characters

|  Character    | Description                                  |
|---------------|----------------------------------------------|
|  .            | any character except line break              |
|  \d           | digit 0-9                                    |
|  \w           | letter(Upper and lower), digit or underscore |
|  \s           | White space character                        |
|  \D           | anything other than Digit                    |
|  \W           | anything other than word character           |
|  \S           | anything other than White space character    |
|  \\.           | A period                                     |


### Regular Expression Quanitifiers

|  Quanitifier  | Description                                      |
|---------------|--------------------------------------------------|
|  +            | One or more Ex: \d+ - Matches one or more digits |
|  {x}          | Exactly x times Ex: {3} - 3 times                |
|  {x, y}       | x to y times Ex: {3, 5} - 3 to 5 times           |
|  {x,}         | x or more times Ex: {4,} - 4 or more times       |
|  *            | 0 or more times                                  |
|  ?            | Once or none (optional)                          |


### Character Classes

|  Character    | Description                                    |
|---------------|------------------------------------------------|
|  [a-z]        | all lower case alphabets                       |
|  [A-Z]        | all upper case alphabets                       |
|  [0-9]        | all digits                                     |
|  [^a-z]       | anything other than Digit lower case alphabets |
|  [^A-Z]       | anything other than Digit upper case alphabets |
|  [^0-9]       | anything other than Digit                      |


### Anchors and boundries

|  Pattern      | Description               |
|---------------|---------------------------|
|  ^            | Start of a string or line |
|  $            | End of a string or line   |
|  \b           | word boundary             |


### Logic

|  Logic      | Description                                    |
|---------------|-------------------------------------------------------------|
|  |            | Alternation / OR operand                                    |
|  ( … )        | Capturing group Ex: A(nt|pple) Apple (captures "pple")      |


### Working with python re module

	>>> import re
	>>>
	>>>
	>>> dir(re)
	['DEBUG', 'DOTALL', 'I', 'IGNORECASE', 'L', 'LOCALE', 'M', 'MULTILINE', 'S', 'Scanner', 'T', 'TEMPLATE', 'U', 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__version__', '_alphanum', '_cache', '_cache_repl', '_compile', '_compile_repl', '_expand', '_locale', '_pattern_type', '_pickle', '_subx', 'compile', 'copy_reg', 'error', 'escape', 'findall', 'finditer', 'match', 'purge', 'search', 'split', 'sre_compile', 'sre_parse', 'sub', 'subn', 'sys', 'template']
	>>>



 ### Why we should used r before the pattern

 In order to getting rid of escape character '\' while writing regex pattern we should use r before the pattern.
