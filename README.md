# MIPS-processor
This is the python code which mimics the MIPS processor
 
EG 212 Computer Architecture- MIPS Processor Design

Project Description:
We have chosen three C programs.
1. Binary search
This program has memory locations n(the size of the array) , arr(the sorted array) and x(the element to search) which are hardcoded into the memory. These values can be changed for different test cases. The memory location res has –1. The program searches for the element x(through binary search technique) in the array and stores the index of the first occurence of the element. If the element is not found the original value of –1 is retained.
2. Selection sort
This program has memory locations n(the size of the array) and arr(the array). These values  can be changed for different test cases. The program performs selection sort on the given array. 
3. Two sum (For demonstration)
This program has memory locations n(the size of the array) , arr(the sorted array) and x(the sum) which are hardcoded into the memory. These values can be changed for different test cases. The memory location res has 0. The program stores 1 in res if there are arr[i] and arr[j] in the array such that arr[i] + arr[j] = x else the original value of 0 is retained.




Files Submitted:
C programs:
1. Binary_Search.c
2. Selection_Sort.c
3. Two_Sum.c

Assembly programs:
1. bin_search.asm
2. Sel_sort.asm
3. Two_sum.asm

Processor :
1.Processor.py
Steps to run the code:
1. Open the mips assembly code in MARS 4.5
2. Click on   icon to assemble the program
3. Then click   icon -> select .text in memory segment drop down box and binary text in the dump format drop down box and save. This saves the instructions in binary to a text file.
4. Repeat the same for data to save data in binary to a text file.
5. Save all the files in the same directory as processor imports ouput of the MARS assembler.
6. On the terminal enter ‘Python3 pip install colorama ‘ if not  installed  		
7. Run the command python3 processor.py
8. Output of the processor file is shown  with each  instruction’s associated register contents printed and in what stage it is present in.
The C code for Two sum:
 
The Assembly code for Two sum:
 

The Mars outputs for Two sum:
Instruction Memory:
 

Data Memory :
 
Processor Output:
We have implemented the five stages of the processor namely:
•	fetch()-In this stage the instruction is fetched from the instruction memory
•	decode()- In this stage   the instruction is decoded based on opcode and function field 
•	EX()-In this stage execution of  the instruction is done using the alu
•	MEM()-In this stage the data memory is accessed
•	WB()-In this stage the register file or the data memory is written back to.
We have used the package colorama to indicate different phased of the the cycle with distinct colors. The table below explains the use of these colours

COLOR	USE
RED	Register values and PC
YELLOW	Beginning or completion of a phase
BLUE	Description of what is happening in each instruction
CYAN	Control signals

Output of processor is in  the following  link below:-
Processor_output.pdf
PROJECT BY

GOURAV ANIRUDH BJ	IMT2023005
SATHISH ADITHIYAA SV	IMT2023030
SUBHASH H	IMT2023104



