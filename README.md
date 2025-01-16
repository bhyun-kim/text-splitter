# text-splitter

A Python library for splitting text into smaller chunks (by words).  

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/bhyun-kim/text-splitter.git
```

## Usage 

```python
from text_splitter import split_text_by_words

text = "This is a sentence. This is another sentence! And yet another one?"
chunks = split_text_by_words(text, max_words=5)
print(chunks)
```
