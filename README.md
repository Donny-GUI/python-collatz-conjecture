

# python-collatz-conjecture
Collectz Conjecture Grapher and Classes for use in Python



## About
The Collatz conjecture is one of the most famous unsolved problems in mathematics. The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1. It concerns sequences of integers in which each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence. 

![Screenshot from 2022-10-19 15-30-00](https://user-images.githubusercontent.com/108424001/196817417-37d09ad6-48c7-4b42-b205-7dddeadb9b16.png)
![Screenshot from 2022-10-19 15-33-12](https://user-images.githubusercontent.com/108424001/196817407-a4be91e7-a718-4f6a-9e10-545538a06391.png)

# Installation

### Linux and Macos

```bash
git clone https://github.com/Donny-GUI/python-collatz-conjecture.git
cd python-collatz-conjecture
pip3 install matplotlib
python3 collatz.py
```

### Windows

```bash
git clone https://github.com/Donny-GUI/python-collatz-conjecture.git
cd python-collatz-conjecture
pip install matplotlib
py collatz.py
```
### Usage
```python3
from collatz import CollatzGraph, Collatz
collatz_graph = CollatzGraph([13,12,456])
collatz_graph.line()
```
![Screenshot from 2022-10-19 15-31-11](https://user-images.githubusercontent.com/108424001/196817503-95a3334c-3327-4c2a-9aac-f5f3546a3b00.png)


## additional information

https://en.wikipedia.org/wiki/Collatz_conjecture

https://en.wikipedia.org/wiki/Lothar_Collatz

![220px-Lothar_Collatz](https://user-images.githubusercontent.com/108424001/196818564-c0b0b9a6-d939-4eb4-82cd-9a13bbf1d3c1.jpg)

