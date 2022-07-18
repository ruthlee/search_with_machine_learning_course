# Week 4 - Vector Search

### Pros and Cons of vector search
**Pros**

- word sense disambiguation: using context to disambiguate different definitions of the same word
- synonyms: if two different words mean the same thing, vector reprentations can take that into account
- better at understanding long queries

**Cons**

- Explainability: not as explainable as TF-IDF
- Task-dependence: single embedding can't capture everything (tho i would argue TF-IDF has the same problem) 
- efficiency: can be slow to compute most similar recipes to a large vector
- ranking: it's not clear where to put the cutoff of similar results from vector similarity, and also how to integrate query-dependent factors 
- filters: can be tough to apply filters to vector results 


### Indexing via nearest-neighbor database
- Once we have embeddings from a model to transform documents, we need a way to quickly index and retrieve them 
- Can use specialized data structure called **nearest-neighbor database**. 
	- [Hierarchical Navigable Small World graph](https://github.com/nmslib/hnswlib). 


### Embedding queries
- If you don't want to use the same space:
- If queries are very different from documents can embed them separately from documents -- **two-tower model**. [Source](https://cloud.google.com/vertex-ai/docs/matching-engine/train-embeddings-two-tower) and [source](https://www.linkedin.com/pulse/personalized-recommendations-iv-two-tower-models-gaurav-chakravorty/).

### Measuring similarity
- Euclidean distance, cosine similarity


### Relevance vs Ranking
* Relevance measures how related a result is to a query (an "objective" metric)
* Ranking takes into account a result's popularity, desirability, quality, etc. More subjective
* For vector retrieval, need to define a threshold or max result number
* For ranking, similarity score can perhaps be used in tandem with query-independent features to rank
* combining vector similarity scores linearly with hand-boosted ES model is probably a bad idea since the scores don't vary linearly in terms of relevance (XGBoost is a good idea since it can handle nonlinearity of features)

### Exact vs Approximate Nearest Neighbors
* [Product quantization](https://lear.inrialpes.fr/pubs/2011/JDS11/jegou_searching_with_quantization.pdf) can compress large vector representations for nearest neighbor search
* Common approach is to combine approximate and exact methods -- use approximate method to filter results, then compute sim scores exactly

### Combining vector search with traditional indexing
* Filtering: get recipes from vector search, then filter using entry in inverted index 
* Sorting: allow users to sort by results
	* tricky because there's no absolute similarity threshold that guarantees relevance; so need to manage precision-recall tradeoff
	* perhaps avoid user-specified sorting entirely OR replace with filtering (specify price filter rather than sorting by price)