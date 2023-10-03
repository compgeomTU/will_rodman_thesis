# Traversal Distance Python Library

### Command Line
To run the program, run a command line execution in the package with format:
```
python3.9 main.py samples/paris/arc_de_triomphe samples/paris/vehicle -p 5 -g1_ids 0 -g2_ids 0,1,2
```

```
python3.9 main.py samples/paris/arc_de_triomphe samples/paris/vehicle -p 4.3
```

```
python3.9 main.py samples/paris/arc_de_triomphe samples/paris/vehicle -b -p 5
```

```
python3.9 main.py samples/square/aside samples/square/bside -b
```
```
python3.9 main.py samples/square/aside samples/square/bside -p 10
```

**Flags:**
* `-l` type: *str* logs the computation of the Traversal Distance to .log files.
* `b` binary search
* `-p` plots graph 1 and graph 2.
* `g1_ids1`
* `g2_ids1`

### Sample Inputs
Sample graph and curve files can be copied and pasted into the command line.
1. samples/paris/arc_de_triomphe samples/paris/vehicle
2. samples/athens/groundtruth samples/athens/kevin
3. samples/chicago/groundtruth samples/chicago/james

### Authors
**Dr. Carola Wenk** 
Tulane University
cwenk@tulane.edu

**Erfan Hosseini** 
Tulane University
shosseinisereshgi@tulane.edu

**Will Rodman** 
Tulane University
wrodman@tulane.edu

**Rena Repenning** 
Morgan Stanley
renarepenning.com

**Emily Powers**
Tulane University
epowers3@tulane.edu

### Lisence
MIT License • Copyright (c) 2022 Computational Geometry @ Tulane
