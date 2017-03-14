# Leveraging A-priori Knowledge in Predictive Business Process Monitoring

## Synopsis

It is the source code to support experiments performed for the article "Leveraging A-priori Knowledge in Predictive Business Process Monitoring" by Chiara Di Francescomarino and Chiara Ghidini and Fabrizio Maria Maggi and Giulio Petrucci and Anton Yeshchenko

Code can be used to train LSTM models to predict sequences of next events. Also, different prediction techniques available:

0. Baseline
1. Prediction with NoCycle - algorithm that prevents the loops in the output trace. It is useful when the training log contains more than 0.5 cycles per trace.
2. Prediction with Apriori knowledge - algorithm that exploits Apriori knowledge (states as LTL formula), in order to make more accurate, compliant predictions.



## Running the project

The project was written in Python (ver: 2.7.12), with Pycharm IDE. Also, for LTL formula check module you
will need to run Java code in background (JDK ver: 1.8).

Keras (ver: 1.1.2) is used alongside with Tensorflow (ver: 0.12.0-rc0) backend.

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

Supplementary:
S1. The properties_of_logs.py can be run in order to collect general information about the log (that are numbe rof cycles, alphabet size e.c.)
S2. graph_results.py used to generate graphs on results

## Contributors

This code is supported by Anton Yeshchenko (anton.yeshchenko@gmail.com)


The code based on the original repository (github.com/verenich/ProcessSequencePrediction)




