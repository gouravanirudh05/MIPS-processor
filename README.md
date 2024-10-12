# MIPS Processor Design
## Project Overview
This project demonstrates a MIPS processor design by simulating three distinct C programs:

1. Binary Search
2. Selection Sort
3. Two Sum 
The MIPS processor is designed using the five stages of instruction execution:

* **Fetch**: Fetches the instruction from instruction memory.
* **Decode**: Decodes the instruction using the opcode and function fields.
* **Execute (EX)**: Executes the instruction using the ALU.
* **Memory Access (MEM)**: Accesses the data memory.
* **Write Back (WB)**: Writes back to the register file or data memory.
Each C program has a corresponding MIPS assembly implementation, which is run on a Python simulator (```Processor.py```), showcasing the contents of registers at each stage of execution. This project also utilizes the colorama package to highlight different phases of the cycle with distinct colors for better visibility.
## Programs
1. **Binary Search(Binary_Search.c)**
* Memory Locations:
  * ```n```:Size of the array
  * ```arr```:Sorted array
  * ```x```:Element to search for
  *  ```res```:Initialized to ```-1```, stores the index of the first occurrence of ```x```, or retains ```-1``` if not found.
*Operation: Performs a binary search for ```x``` in ```arr```. The result is stored in ```res```.
2. Selection Sort (Selection_Sort.c)
* Memory Locations:
  * ```n```: Size of the array.
  * ```arr```: Array to be sorted.
* Operation: Performs selection sort on the array ```arr```.
3. Two Sum (Two_Sum.c)
* Memory Locations:
  * ```n```: Size of the array.
  * ```arr```: Array of integers.
  * ```x```: Target sum.
  * ```res```: Initialized to ```0```. If two distinct elements in the array sum to ```x```, res is set to ```1```.
* Operation: Checks if there are two elements in the array whose sum equals ``x``.
## Assembly Programs
For each C program, there is a corresponding MIPS assembly implementation:
* bin_search.asm
* sel_sort.asm
* two_sum.asm
The assembly code is converted into binary using the MARS (MIPS Assembler and Runtime Simulator) tool.

## Setting Up the Project
### Prerequisites
1. Python: Ensure Python 3 is installed on your system.

2. MARS: Download and install the MARS 4.5 simulator from MARS website.

3. colorama: Install the ``colorama`` Python package to display colored output in the terminal.
```bash 
pip install colorama
```

## MARS Setup
1. Open the MIPS assembly code (```bin_search.asm```, ```sel_sort.asm```, ```two_sum.asm```) in MARS.
2. Assemble the code by clicking the "Assemble" button.
3. For each program, generate a binary dump:
* Select the ```.text``` memory segment and binary text format in the dump dialog box.
* Save the output to a file (e.g., ```bin_search_text.txt```, ```sel_sort_text.txt```, ```two_sum_text.txt```).
* Similarly, dump the data segment to a file (e.g., ```bin_search_data.txt```, ```sel_sort_data.txt```, ```two_sum_data.txt```).
4. Save the instruction and data memory files in the same directory as the ```Processor.py``` file.
## Running the Processor Simulation
Once you have set up the binary dumps of the assembly programs, you can run the MIPS processor simulation using the provided ```Processor.py``` file.
```bash
# Clone or download the project repository
git clone <repository_link>

# Navigate to the project directory
cd mips-processor-simulation

# Run the processor simulation
python3 Processor.py
```
## Processor Output
The processor simulates the five stages of the MIPS pipeline for each instruction and provides a detailed breakdown of register contents during the execution. The colorama package is used to highlight different parts of the pipeline:

* Red: Register values and Program Counter (PC).
* Yellow: Beginning or completion of a pipeline phase.
* Blue: Descriptions of what is happening at each instruction.
* Cyan: Control signals.

## Project Files
* C Programs:
  * Binary_Search.c
  * Selection_Sort.c
  * Two_Sum.c
* MIPS Assembly Programs:
  * bin_search.asm
  * sel_sort.asm
  * two_sum.asm
* Processor:
  * Processor.py: The Python script simulating the MIPS pipeline.
## Output Example
For detailed output, including the register states and control signals at each stage of execution, please refer to the attached processor output file: [Processor_output.pdf](Processor_output.pdf).
