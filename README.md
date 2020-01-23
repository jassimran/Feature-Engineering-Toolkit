# Feature-Engineering-Toolkit
A feature engineering toolkit for data so that Data Scientists can easily apply different transforms to their data, then use this data to train their models, to see if the new features impprove their model's performance. Its main features are highlighted below:
* It is a highly extensible toolkit with the ease of adding new feature engineering techniques by implemeting abstract class "FeatureTransfomer".
* It easily compares your models against standard pre-defined metrics on dataset with different feature engineering tecniques applied.
* The CSV Loader takes cares of different encoding of CSV and loads your data in the toolkit seemlessly for processing.

Jupyter notebook can be used to play with toolkit and try different techniques on your data. A sample notebook has been used to demo some of the toolkit capabilities.

If given more time, i would make following enhancements to the toolkit:
* Improve the validation for various techniques before feature enginnering could be applied.
* Make the feature engineering transforms more rich by more configurable parameters to the transforms (Vanilla versions with minimum configurations has been implemented as of now. FOr example: There are numerous techniques for Imputation but as of now only few have been implemted, remaining techniques can be easily added by making them as parameters in the __init__ function of each Transformation class )
* Add auto-recommendation pipeline to be applied with basic transforms. Based on your dataset's quality, make recommendations for transforms which would improve model's performance. 
* Add more feature engineering tecnhiques 
* Build a graphical user interface for ease of use.

Write more...
