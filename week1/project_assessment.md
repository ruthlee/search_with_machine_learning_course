## Project Assessment - Week 1

1. Do you understand the steps involved in creating and deploying an LTR model?  Name them and describe what each step does in your own words.

First, you gather relevance judgements from search logs (whether that's from click data or human judgements). Then, you extract features for each query-document pair in your dataset. These can be query-dependent or independent. Then, you split your data into training and test sets. Then, you train an XGBoost (or other) ranking model on the training set, and use search evaluation metrics like nDCG on the test set to evaluate how you ranked. 

2. What is a feature and featureset?

A feature (in this context) is a value which can provide some information as to how relevant a document is to a query. A featureset is a json file which contains the features to be extracted from query logs. 

3. What is the difference between precision and recall?

Precision: out of all the results returned, what fraction are relevant?

Recall: out of all the possibly relevant results, what fraction were returned? 

4. What are some of the traps associated with using click data in your model?

Different biases: presentation (people will tend to click on the first thing), uncertainty (is 1 impression and 1 click enough to say that your relevance judgement is 1?), and overall data/tracking issues. 

5. What are some of the ways we are faking our data and how would you prevent that in your application?

We faked impressions data. We should probably use real impressions data. 

6. What is target leakage and why is it a bad thing?

When you leak some of the testing data into the training data, causing your model to overfit. 

7. When can using prior history cause problems in search and LTR?

Search patterns can change over time. Past data may not be the best indicator of current search trends. 

Best MRR score: 0.401