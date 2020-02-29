#!/usr/bin/env python
# coding: utf-8

# In[6]:


_end='_end_'
def list2trie(list1):
    '''Creates a prefix tree given the list of words
    
    Parameters
    ----------
    list1:list
     list to be stored in prefix tree
     
    Returns
    -------
    True or False
    
    Examples
    --------
    >>>list1=['a','be','bee','been','bet','bat','boat']
    >>>list2trie(list1)
    >>>{'_end_': False,
       'a': {'_end_': True},
       'b': {'_end_': False,
       'e': {'_end_': True,
       'e': {'_end_': True, 'n': {'_end_': True}},
       't': {'_end_': True}},
       'a': {'_end_': False, 't': {'_end_': True}},
       'o': {'_end_': False, 'a': {'_end_': False, 't': {'_end_': True}}}}}
    
    '''
    root=dict()
    preword=[]
        
    for word in range(len(list1)):
        current_dict=root
        current_dict[_end]=False
        preword.append(list1[word])
        for character in list1[word]:
            current_dict=current_dict.setdefault(character,{})
            for i in range(len(list1[word])):
                if list1[word][:i] in preword or character==list1[word][-1]:
                    current_dict[_end]=True
                else:
                    current_dict[_end]=False
            
    return root
        
list1=['a','be','bee','been','bet','bat','boat']
list2trie(list1)


# In[7]:


def search(trie, word):
    '''Tells if a given word is in tje given prefix tree
    
    Parameters
    ----------
    trie: given prefix tree for list1
    word: string
          the word to be searched
    
    Returns
    -------
    True or False
    
    Examples
    --------
    >>>trie=list2trie(list1)
    >>>search(trie,'bao')
    >>>False
    
    >>>search(trie,'bee')
    >>>True

    
    '''
    current_dict = trie
    for letter in word:
        if letter not in current_dict:
            return False
        current_dict = current_dict[letter]
    return _end in current_dict
    

trie=list2trie(list1)
search(trie,'bee')


# In[ ]:


from hypothesis import given, settings
import hypothesis.strategies as st


@given(list1=st.lists(st.text),word=st.text)
@settings(max_example=10**4)
trie=list2trie(list1)
def test_search(list1,trie,word):
    '''Tells if a search function is right
    
    Parameters
    ----------
    list1: list
          list is randomly generated from hypothesis package
    word: string
          word is randomly generated from hypothesis package
    trie: given prefix tree for list1
    
    Returns
    -------
    True or False
    
    Examples
    --------
    >>>test_search(list1,trie,word)
    >>>True
    '''
    
    if word in list1:
        trie_word=True
    else:
        trie_word=False
    
    if search(trie,word)==trie_word:
        assert search(trie,word)==trie_word
    else:
        assert search(trie,word) is False

