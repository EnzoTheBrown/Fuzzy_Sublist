# Fuzzy_Sublist 

## To Run
```bash
pip install graphviz
pip install Levenshtein
git clone https://github.com/EnzoTheBrown/Fuzzy_Sublist.git
cd Fuzzy_Sublist
python main.py
```


## Algorithm:

If we want to see if:
```python
sublist = ['manga', 'un', 'pimme']
```
is a fuzzy sublist of:
```python
l = ['je', 'mange', 'une', 'pomme']
```

with a threshold:
```python
threshold = 0.7
```

Firstable we need to see every possible combination of words we can have with the levenshtein algorithm:

Here, only one:

```python
candidates = [
    ('manga', 'mange'),
    ('un', 'une'),
    ('pimme', 'pomme')
]
```

From this we can build a directed graph representing every possible combination we can have:

here it's quite simple:
![simple_graph](https://github.com/EnzoTheBrown/Fuzzy_Sublist/blob/master/test-output/pomme_simple.gv-1.png?raw=true)

But for a more complex sublist such as:

```python
sublist = ['pomge', 'un', 'momge']
```
is a fuzzy sublist of:
```python
l = ['je', 'mange', 'une', 'pomme']
```

with a threshold:
```python
threshold = 0.4
```

The graph will be:

![complex_graph](https://github.com/EnzoTheBrown/Fuzzy_Sublist/blob/master/test-output/pomme_complex.gv-1.png?raw=true)

To see the importance of low complexity algorithm, here is an example of what can happend:

![which](https://github.com/EnzoTheBrown/Fuzzy_Sublist/blob/master/test-output/which.gv-1.png?raw=true)

There is 4*2*6*6 = 288 possible sublist and it groes exponentially


The good point of this representation is due to the fact that the more we reduce the threshold and the more the word in the sentence are similar, the harder it becomes to compute the algorithm. So with a graph algorithm we get rid of every combinatory problems such as complexity.
