# Leveraging A-priori Knowledge in Predictive Business Process Monitoring

## Synopsis

At the top of the file there should be a short introduction and/ or overview that explains **what** the project is. This description should match descriptions added for package managers (Gemspec, package.json, etc.)

## Code Example

Show what the library does as concisely as possible, developers should be able to figure out **how** your project solves their problem by looking at the code example. Make sure the API you are showing off is obvious, and that your code is short and concise.

## Motivation

A short description of the motivation behind the creation and maintenance of the project. This should explain **why** the project exists.

## Running the project

The project was written in Python (ver: 2.7.12), with Pycharm IDE. Also, for LTL formula check module you
will need to run Java code in background (tested on JDK ver: 1.8).

## Tests

In order to use the scripts few steps need to be performed.

0. Before running any inference algorithms you need to run the java service from the LTLCkeckForTraces folder.

1. The historical log should be converted into the supported format.
In order to do so, csv file can be processed by the script csv_converter.py.
Just feed the full csv log, and specify where the case ID, activity ID, and timestamps are.

Put the file in the data folder.

2. In the file shared variables, write the paths to the files you will use.

3. In the file experiment_runner.py you can following:

3.1. Use function 'train' to train the model

3.2. Use either of the functions

_6_evaluate_beseline_SUFFIX_only.runExperiments(logNumber,formula_used)
_9_cycl_SUFFIX_only.runExperiments(logNumber,formula_used)
10_cycl_back_SUFFIX_only.runExperiments(logNumber,formula_used)
_11_cycl_pro_SUFFIX_only.runExperiments(logNumber,formula_used)

In order to run corresponding algorithms for predictions.

4. Run calculate_accuracy_on_next_event.py file in order to run evaluation of the algorithms.
The results will be displayed in console as well as the table-like file will be created.

## Contributors


The code based on the original repository.

## License



