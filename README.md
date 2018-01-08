# Fuzzy_Sublist

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
![simple_graph](https://github.com/EnzoTheBrown/Fuzzy_Sublist/blob/master/data/simple_graph.png?raw=true)

But for a more complex fublist such as:

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

![complex_graph](https://github.com/EnzoTheBrown/Fuzzy_Sublist/blob/master/test-output/which.gv.pdf?raw=true)


The good point of this representation is due to the fact that the more we reduce the threshold and the more the word in the sentence are similar, the harder it becomes to compute the algorithm. So with a graph algorithm we get rid of every combinatory problems such as complexity.
