# Week 2

### Content Annotation
- Rule-based content classification
	- Use regular expressions
	- Get brittle quickly

### Content classification
- Human annotation can help generate labels (e.g., mechanical turk) 
- I guess we have tags so maybe this isn't totally necessary? 

### How to use embeddings in search
- Supervised: need labeled training data
	- Content classification
	- Content annotation
- Unsupervised
	- Do not need labels
	- Synonym candidates
	- Content similarity
	- No ground truth to evaluate

### FastText
- Way of generating text embeddings
- Command line and python utilities 

### Synonyms
- Use nearest neighbors from embeddings
- Need a lot of data + training time

### Content annotation
- Finding tokens/phrases inside of content that corresponds to entities 
- Can do with rules or NER 
	- Typically done as part of a standard natural language pipeline 

### Integrating content understanding in search
- Can use to detect mistakes in existing categories 
	- We could use tags as our ground truth and expand tagging algorithmically 
- Annotate content to populate facets
- Synonyms: for increasing recall 
	- Can also do it with query understanding
	- In content, can augment the content index with synonyms 
	- Will introduce false positives (need to manage this) 
- Use embeddings for dense retrieval (week 4) 
	- Can fine-tune existing embedding model with domain-specific data