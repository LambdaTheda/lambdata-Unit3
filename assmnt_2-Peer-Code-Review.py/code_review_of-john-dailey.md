<!-- 

All of John's files PASSED PEP8 testing: FINAL SCORE 3

Inside the buyholdsell directory, you will find several files, including a blank __init__.py, which helps manage packages (HELPS IMPORT files in that folder).

As is, the package seems thoroughly crafted; these modules are fully functional (well, they run without errors). 

His README.md file is very informative:

"This package is meant specifically for YahooFinance

Historical Data, import, train/test split, feature engineering,

drop Date column and prepare data for predictive modeling.

from buyholdsell import urlcsvsplit

Use urlcsvsplit to prompt a URL CSV input.

Input any Yahoo Finance historical data URL (which are in CSV format).

This import will also automatically perform a 70/30 train/test split.

Instantiate train and test with:

train = urlcsvsplit.train

test = urlcsvsplit.test

from buyholdsell.ttclean import ttclean

Use the ttclean() function to clean train and test time series data frames.

Instantiate clean train and test with: 

train = ttclean(train)

test = ttclean(test)

You can also skip urlcsvsplit and ttclean by just using predprep:

from buyholdsell import predprep

Instantiate:

X_train = predprep.X_train

y_train = predprep.y_train

X_test = predprep.X_test

y_test = predprep.y_test

Now, choose your favorite models and start predictive modeling.

In the spirit of using technical indicators for financial modeling and trading,

Also try:

from buyholdsell.RSI import buyholdsell

buyholdsell(insert number here)

Please choose a number between 1 and 100

and the function in this package will return

whether it would buy, hold, or sell." 

-->
