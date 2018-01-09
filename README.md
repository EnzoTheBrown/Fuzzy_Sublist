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

