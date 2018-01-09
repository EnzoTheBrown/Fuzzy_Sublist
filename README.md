# Fuzzy_Sublist 

## To Run
```bash
git clone https://github.com/EnzoTheBrown/Fuzzy_Sublist.git
cd Fuzzy_Sublist
python main.py
```


## Algorithm:

The main list is splited in every possible sublist the same size as the fuzzy sublist candidate:


```python
def get_all_sublists(list_, n):
    result = []
    for i in range(len(list_) - n + 1):
        result.append(list_[i:i+n])
    return result
```

Then we are checking if every element of a sublist got a ratio higher than the threshold:

```python
def is_list_fuzzy(l, ll, threshold):
    print('-'*50)
    for i_l in range(len(l)):
       print(l[i_l], ll[i_l], ratio(l[i_l], ll[i_l]))
       if ratio(l[i_l], ll[i_l]) < threshold:
           return False
    return True

```

And we apply this algortihm to every possible sublist of size n:

```python

def is_sublist_fuzzy(l, sublist, threshold):
    print('#'*50)
    if len(sublist) > len(l):
        return False
    if sublist == []:
        return True
    sublists = get_all_sublists(l, len(sublist))
    return reduce(or_, [is_list_fuzzy(sublist, i, threshold) for i in sublists], False)

```







## other technique: Graph representation

If we want to see if: ```python sublist = ['manga', 'un', 'pimme'] ``` is a fuzzy sublist of: ```python l = ['je', 'mange', 'une', 'pomme'] ```

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

and here:

![brutal](https://github.com/EnzoTheBrown/Fuzzy_Sublist/blob/master/test-output/brutal.gv-1.png?raw=true)



The good point of this representation is due to the fact that the more we reduce the threshold and the more the word in the sentence are similar, the harder it becomes to compute the algorithm. So with a graph algorithm we get rid of every combinatory problems such as complexity.
