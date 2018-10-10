# Coding assignment

You have a file containing a long list of words. Write a function that, given any two words, finds the shortest
distance between them in terms of numbers of words in between.
For example, if this was the content of the file:
“We do value and reward motivation in our development team. Development is a key skill for a DevOp.”
The value of find_shortest_distance(‘motivation’, ‘development’) should be 2 (“in our”).
It can be case insensitive.

Requirements
1. Use Python 3.6 or higher
2. Include tests and a short documentation on how to run it
3. (bonus) commit your code to GitHub and, ideally, keep it in 2-4 commits so that we can see the history
(don’t squash everything in one)

# Solution

I am assuming the input file can live in one machine and doesn't necessarily fit into memory.

We have three main parts
- First we need to get the words from the file. For this I have used generators, so we don't need
to load the file into memory and therefore can read bigger files. We use a regex and take into account
that many words can be in one line of the file.
- Data needs to be cleaned. As we saw in the example file, we could have dots (.), commas (,) or other
non alpha numeric characters that need to be removed as they are not really parts of the words. Also
because we are working in a case insensitive fashion, all the data is lowercased. This is an expensive
operation in terms of time complexity.
- The search itself. Once we have a stream of words, and using the counter variable as a sentinel, we count
the amount of words sitting between the first word and the second word.

# Setup to run the tests

I recommend to use pyenv to manage multiple virtualenvs. If you follow this recommendation, these are the steps:

## Setup virtual environment

```
pyenv install 3.7.0  # in case you haven't done it yet
pyenv virtualenv 3.7.0 coding-assignment
pyenv local coding-assignment
```

## Install requirements

```
pip install -r requirements-dev.txt
```

## Run the tests

```
./run_tests.sh
```
