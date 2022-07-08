# Week 3 - Query understanding

### Two ways of understanding intent
1. Relate query to content taxonomy or content facets
2. Relate query to "higher-level" intent, e.g., known-item vs exploratory search
	- Can determine what metrics to use, e.g., known item search should focus on P@1, exploratory should use a more general metric

### Query rewriting
- Generally to increase recall and precision
- **increasing recall:** Retrieve a larger set of relevant results
	- query expansion: add additional tokens or phrases to keyword search on
		- Very popular to user synonyms for this 
		- Synonyms come from: 1. manual entry, 2. thesaurus, 3. query logs (e.g., users first search "couch", then "sofa"), 4. content mining
		- need to consider context in synonyms (e.g., "glasses" synonym for "eyeglasses" but searcher could want wine glasses)
	- query relaxation: remove tokens from query
		- helpful for overspecified queries
		- if not clear which tokens are important, can use ES minimum_should_match parameter
- **increasing precision**: good for pruning large, heterogenus result sets
	- query segmentation: make phrases from within queries
		- can treat the problem of figuring out query boundaries as a machine learning problem (conditional random fields (CRFs) and long short-term memory (LSTM) neural networks), or can use PMI for pairs 
		- OR maintain a list of known phrases
	- entity recognition: determine entity type for each query segment 
		- common approach is to classify queries into categories, then find entities within each category

### Query Classification
- can do manual but has diminishing returns for less common queries
- heuristic: find some regex based rule
	- can also see if you can transform a less common query into a more common one with a few simple rules (e.g., get rid of adjectives, change a character, etc.)
- machine-learned
	- need to watch out for bias between more common and less common queries
	- need to include negative/ unclassifiable examples 
- dealing with hierarchy:
	- aggregate leaf-level probabilities (probability of being in parent category is sum of children's probabilities)
	- cascade probabilities upward: set a threshold probability (50%) and go up the tree with the aggregation method above until there's a category that exceeds the threshold
	- collection of classifiers for each level of tree (rather than one mapping queries to leaf level categories) -- THEN cascade 

### Using query classification
- To improve precision: use category as filter (may hurt recall) or boost 
	- if user explicitly sorts then boost may be problematic (so switch to filter?) 
- Improving faceting: choose "facets" for classes of results (e.g., "cases", "screen size", "model") and let users refine based on these
	- can define what facets are important per category
