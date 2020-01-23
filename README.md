# Feature-Engineering-Toolkit
A feature engineering toolkit for data so that data scientists can easily apply different transforms to their data, then use this data to train their models, to see if the new features (transformed data) improve their model's performance. 

### MAIN FEATURES
The main features of the toolkit are highlighted below:

- **Extensibility** It is a highly extensible toolkit with the ease of adding new feature engineering techniques by implemeting abstract class "FeatureTransfomer".
- **Pipeline** More often, a data scientist would want to create a sequence of transformations on the data. Using this toolkit one can build the pipelines very intuitively to apply seqyential transforms.
- **Validate Pipeline** Every Pipeline is validated before the transforms can be applied and inituitive error message are shown to data scientist to fix the validations. This saves data scientist lot of time in fixing the issues and create pipelines quickly.
- **Pipeline Comparison** This toolkit lets you easily compare two different feature engineering pipelines against standard pre-defined scikit-learn models and metrics.
- **CSV Loader** The CSV Loader takes cares of different encodings of CSV and loads your data as a `pandas` dataframe seemlessly for processing.
- **Demo Notebooks** Most often in toolkits, data scientists struggle with documentation and easy to use examples. This toolkit comes with demo Jupyter notebooks thats lets users play with toolkit and use its different techniques easily. A sample notebook has been used to demo some of the toolkit capabilities.

### TOOLS ALREADY AVAILABLE
There are other open source toolkits which have similar motivation such as [featuretools](https://www.featuretools.com/), [autosklearn](https://automl.github.io/auto-sklearn/master/), and [H2O](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/faq/python.html). While many of the feature engineering and trasnformation functions could be borrowed from these toolkits, I have majorly focussed on pproviding the overall solution architecture (given time constraints)

### WITH MORE TIME
If given more time, I would make following enhancements to the toolkit (with decreasing order of priority):
* Add more feature engineering tecnhiques by borrowing from above mentioned toolkits as well as by implemeting some SOTA research papers.
* Add auto-recommendation pipeline to be applied with basic transforms. Based on your dataset's quality, make recommendations for transforms which would improve model's performance.
* For now, the focus is on structured data, but it can be easily extended for time-series data feature engineering techniques as well.
* Improve the validation for various techniques before feature enginnering could be applied.
* Make the feature engineering transforms more rich by adding more configurable parameters to the transforms (Vanilla versions with minimum configurations has been implemented as of now. FOr example: There are numerous techniques for Imputation but as of now only few have been implemted, remaining techniques can be easily added by making them as parameters in the __init__ function of each Transformation class )
* Build a graphical user interface for ease of use, API/pip library for easy consumption, and dockers for scalability
