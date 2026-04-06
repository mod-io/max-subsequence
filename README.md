# Max Subsequence (HVLCS)

## Student Information
| Name | UFID |
|------|------|
| Stephen | 63144483 |

## Repository Structure
max-subsequence/
├── src/
│   ├── subsequence.py       
│   └── graph.py         
├── data/
│   ├── example1.in          
│   └── example1.out         
├── tests/
│   └── subsequenceTests.py  
└── README.md

## Dependencies
Python 3.8+
matplotlib (only needed for  graph)

pip install matplotlib

## Assumptions
- All characters in A and B appear in the alphabet block
- All character values are nonnegative integers
- Input file is located at `data/example1.in`
- Code is run from the root of the repository

## How to Run

### Run the algorithm
python3 src/subsequence.py

### Save output to file
python3 src/subsequence.py > data/example1.out

### Run unit tests
python3 tests/subsequenceTests.py

## Example
Input file: data/example1.in

3
a 2
b 4
c 5
aacb
caab

Output file: data/example1.out

9
cb

To reproduce:
python3 src/subsequence.py > data/example1.out

## Benchmark

To generate the runtime graph run:
python3 src/graph.py

This will print a runtime table to the terminal and save the graph to:
data/runtime_chart.png

