# Traversal Distance Python Library

### Command Line
To run the program, run a command line execution in the package with format:
```
python3.9 main.py sample_data/paris/arc_de_triomphe sample_data/paris/vehicle -p 5 -g1_ids 0 -g2_ids 0,1,2
```

```
python3.9 main.py sample_data/paris/arc_de_triomphe sample_data/paris/vehicle -p 4.3
```

```
python3.9 main.py sample_data/paris/arc_de_triomphe sample_data/paris/arc_de_triomphe -b 
```

```
python3.9 main.py sample_data/square/aside sample_data/square/bside -b
```
```
python3.9 main.py sample_data/square/aside sample_data/square/bside -p 10
```

**Flags:**
* `-l` type: *str* logs the computation of the Traversal Distance to .log files.
* `b` binary search
* `-p` plots graph 1 and graph 2.
* `g1_ids1`
* `g2_ids1`

### Sample Inputs
Sample graph and curve files can be copied and pasted into the command line.
1. sample_data/paris/arc_de_triomphe sample_data/paris/vehicle
2. sample_data/athens/groundtruth sample_data/athens/kevin
3. sample_data/chicago/groundtruth sample_data/chicago/james

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
