"""
PROJECT BY:
        IMT2023005-Gourav Anirudh
        IMT2023030-Sathish Adithiyaa S V
        IMT2023104-Subhash H
"""
from colorama import Fore  # We are using this to show the output in each phase in a different colour

"""                       ************THE CODE FOR PROCESS STARTS HERE********************                           """

data_memory = {}  # Used to store all the data
instruction_memory = {}  # Used to store all the instructions

PC = "00000000010000000000000000000000"  # 32 bits wide PC

register_file = {}  # Used to store all the register values

end_address = ""

program_no = 0


class Instruction:  
    def __init__(self):
        
        self.opcode = "0"*6
        self.rd = ""*5
        self.rs = ""*5
        self.rt = ""*5
        self.imm = ""*16
        self.funct = ""*6
        self.shamt = ""*5
        self.regDst = 0
        self.regWr = 0
        self.AluSrc = 0
        self.zero_flag = 0
        self.MemWr = 0
        self.MemRd = 0
        self.Mem2Reg = 0
        self.jump = 0
        self.branch = 0
        self.branch_ne = 0
        self.PCsrc = 0
        self.lui = 0
        self.alu_ctrl_lines = [0]*4
        self.rs_val = '0'*32
        self.rt_val = '0'*32


def conv_to_bin(num: int):
    """Converts a decimal number to a binary string of two's complement form"""
    bin_str = bin(abs(num))[2:].zfill(32)
    if num >= 0:
        return bin_str
    ans = ''.join('0' if i == '1' else '1' for i in bin_str)
    ans = bin(int(ans, 2) + 1)[2:]
    return ans


def conv_to_dec(register: str):
    """Converts a binary number to decimal"""
    num = int(register[1:], 2)
    return -2**31 + num if register[0] == '1' else num


def read_in_memory():
    """This reads in the Machine code and splits it into data and instruction memory accordingly"""
    global end_address
    with open('two_sum_data_machine_code.txt', 'r') as f:
        base_add = "00010000000000010000000000000000"
        for line in f:
            for num in range(0, 32, 8):
                data_memory[base_add] = line.strip()[num:num + 8]
                base_add = conv_to_bin(conv_to_dec(base_add) + 1)
    with open("two_sum_instructions_machine_code.txt", 'r') as f:
        base_add = "00000000010000000000000000000000"
        for line in f:
            for num in range(0, 32, 8):
                instruction_memory[base_add] = line.strip()[num:num + 8]
                base_add = conv_to_bin(conv_to_dec(base_add) + 1)
        end_address = base_add


def initialise_regs():
    """Initialising all registers to zero"""
    global register_file
    for i in range(32):  # Setting all the register values to 0
        register_file[i] = "0"*32


class ALU:
    def __init__(self):
        global inst
        self.ctrl_line = inst.alu_ctrl_lines

    def execute(self, operand1, operand2):
        """This is the ALU that is used to perform operations"""
        # print(Fore.LIGHTBLUE_EX + "ALU operation performed:")
        print(Fore.LIGHTBLUE_EX + "ALU operands: ")
        operand1 = conv_to_dec(operand1)
        print(Fore.RED + "Operand1=" + str(operand1))
        operand2 = conv_to_dec(operand2)
        print(Fore.RED + "Operand2=" + str(operand2))

        if self.ctrl_line == [0, 0, 0, 0]:  # AND
            print(Fore.LIGHTBLUE_EX + "ALU AND operation is  performed")
            return operand1 & operand2
        elif self.ctrl_line == [0, 0, 0, 1]:  # OR
            print(Fore.LIGHTBLUE_EX + "ALU OR  operation is  performed")
            return operand1 | operand2
        elif self.ctrl_line == [0, 0, 1, 0]:  # ADD
            print(Fore.LIGHTBLUE_EX + "ALU ADD operation is  performed")
            return operand1 + operand2
        elif self.ctrl_line == [0, 1, 1, 0]:  # SUBTRACT
            if operand1 - operand2 == 0:
                inst.zero_flag = 1
            print(Fore.LIGHTBLUE_EX + "ALU SUBTRACT operation is  performed")
            return operand1 - operand2
        elif self.ctrl_line == [0, 1, 1, 1]:  # SLT (Set less than)
            print(Fore.LIGHTBLUE_EX + "ALU SLT operation is  performed")
            return 1 if operand1 < operand2 else 0
        elif self.ctrl_line == [0, 1, 0, 0]:  # Shift left logical
            print(Fore.LIGHTBLUE_EX + "ALU SLL operation is  performed")
            return operand1 << operand2
        elif self.ctrl_line == [0, 1, 0, 1]:  # Shift right logical
            print(Fore.LIGHTBLUE_EX + "ALU SRL operation is  performed")
            return operand1 >> operand2
        elif self.ctrl_line == [1, 0, 0, 0]:  # Shift right arithmetic
            print(Fore.LIGHTBLUE_EX + "ALU SRA operation is  performed")
            if conv_to_dec(operand1) < 0:
                pass
            else:
                return operand1 >> operand2


def ALU_CTRL():
    """Used to set te control lines of the alu control unit"""
    global inst
    function_field = inst.funct
    op = inst.opcode
    if (function_field == "100000" or op == "001001" or op == "100011"
            or op == "001000" or op == "101011" or function_field == "100001"):  # ADD, ADDIU, LW, ADDI, SW, ADDU
        inst.alu_ctrl_lines = [0, 0, 1, 0]
    elif function_field == "100010" or op == "000101" or op == "000100":  # SUB, BNE, BEQ
        inst.alu_ctrl_lines = [0, 1, 1, 0]
    elif function_field == "101010":  # SLT
        inst.alu_ctrl_lines = [0, 1, 1, 1]
    elif function_field == "000010":  # SRL
        inst.alu_ctrl_lines = [0, 1, 0, 1]
    elif function_field == "000000":  # SLL
        inst.alu_ctrl_lines = [0, 1, 0, 0]
    elif function_field == "100101" or op == "001101":  # OR, ORI
        inst.alu_ctrl_lines = [0, 0, 0, 1]
    elif function_field == "100100":  # AND
        inst.alu_ctrl_lines = [0, 0, 0, 0]
    elif function_field == "000011":  # SRA
        inst.alu_ctrl_lines = [1, 0, 0, 0]
    print(Fore.CYAN + "ALU_ctrl lines:", end=" ")
    print(*inst.alu_ctrl_lines)


def sign_extend(imm: str):
    """Used to make the immediate value to 32 bits"""
    if conv_to_dec(imm) >= 0:
        return imm.zfill(32)
    else:
        return imm.ljust(32, '1')


def EX():
    global inst, PC
    ALU_CTRL()
    alu = ALU()  # object of ALU class to execute alu operations
    if inst.jump:
        print(Fore.LIGHTBLUE_EX + "Jump instruction executed")
        PC = inst.imm
        return None
    elif inst.lui:
        print(Fore.LIGHTBLUE_EX + "LUI instruction executed")
        temp = inst.imm + '0'*16
        return temp
    inst.rs_val = register_file[int(inst.rs, 2)]
    if inst.AluSrc:
        inst.rt_val = sign_extend(inst.imm)
        print(Fore.CYAN + "Sign extended value:" + inst.rt_val)
    else:
        inst.rt_val = register_file[int(inst.rt, 2)]
    if inst.shamt != '00000' and inst.opcode == '000000':
        inst.rt_val = inst.shamt
        inst.rs_val = register_file[int(inst.rt, 2)]
    temp = conv_to_bin(alu.execute(inst.rs_val, inst.rt_val))
    if (inst.branch and inst.zero_flag) or (inst.branch_ne and not inst.zero_flag):
        PC = conv_to_bin(conv_to_dec(PC) + 4*conv_to_dec(sign_extend(inst.imm)))
    return temp


def MEM(address: str, data: str):
    """This helps to access the data memory"""
    global data_memory, inst
    ans = ''
    if inst.MemRd:
        print(Fore.RED + "MemRd=" + str(inst.MemRd))
        print(Fore.LIGHTBLUE_EX + "Data Memory is being Read")
        for cnt in range(4):
            ans += data_memory[conv_to_bin(conv_to_dec(address) + cnt)]
        print(Fore.LIGHTBLUE_EX + "Value read from the memory=" + str(conv_to_dec(ans)))
    elif inst.MemWr:
        print(Fore.RED + "MemWr=" + str(inst.MemWr))
        print(Fore.LIGHTBLUE_EX + "Data Memory is being Written")
        data = register_file[int(inst.rt, 2)]
        for cnt in range(4):
            data_memory[conv_to_bin(conv_to_dec(address) + cnt)] = data[8*cnt: 8*(cnt + 1)]
        # print(Fore.LIGHTBLUE_EX + "Value written to memory" + str(conv_to_dec(data[8*cnt: 8*(cnt + 1)])))
        return
    print(Fore.RED + "Mem2Reg=" + str(inst.Mem2Reg))
    if inst.Mem2Reg:
        print(Fore.LIGHTBLUE_EX + "Value from Memory is passed to write port of register file")
        return ans
    else:
        print(Fore.LIGHTBLUE_EX + "Value from ALU is passed to write port of register file")
        return address


def WB(data: str):
    """Used to writeback to the register file"""
    global inst
    if inst.regWr:
        print(Fore.LIGHTBLUE_EX + "RegWr=1")
        print(Fore.LIGHTBLUE_EX + "Register file is being written back")
        if inst.regDst:
            register_file[int(inst.rd, 2)] = data
            print(Fore.LIGHTBLUE_EX + "Writing back to  the register number:" + str(int(inst.rd, 2)))
        else:
            register_file[int(inst.rt, 2)] = data
            print(Fore.LIGHTBLUE_EX + "Writing back to register number :" + str(int(inst.rt, 2)))
        print(Fore.LIGHTBLUE_EX + "Value written back to register= " + str(conv_to_dec(data)))


def fetch():
    """This fetches the instruction from the instruction memory"""
    global PC, end_address, program_no
    curr_instr = ''
    if PC == end_address:
        print(Fore.BLUE+"Total clock cycles=",clock_cycle)
        print()
        print(Fore.YELLOW+"RESULT is")
        match program_no:
            case 0:
                print(bool(int(data_memory['00010000000000010000000000100111'], 2)))
            case 1:
                print("Sorted array")
                n = conv_to_dec(data_memory[conv_to_bin(conv_to_dec("00010000000000010000000000000000")+3)])
                pc="00010000000000010000000000000100"
                for i in range(n):
                    sorted_element=conv_to_dec(data_memory[pc]+data_memory[conv_to_bin(conv_to_dec(pc)+1)]+data_memory[conv_to_bin(conv_to_dec(pc)+2)]+data_memory[conv_to_bin(conv_to_dec(pc)+3)])
                    print(sorted_element,end=" ")
                    pc=conv_to_bin(conv_to_dec(pc)+4)

            case 2:
                print(f"Found {int(data_memory['00010000000000010000000000100111'], 2)}")
        exit(0)
    print()
    print("CLOCK CYCLE=", clock_cycle)
    print()
    print(Fore.YELLOW + "Entering fetch stage:")
    for cnt in range(4):
        curr_instr += instruction_memory[conv_to_bin(conv_to_dec(PC) + cnt)]
    print(Fore.RED + "Instruction fetched = " + curr_instr)
    PC = conv_to_bin(conv_to_dec(PC) + 4)
    print(Fore.LIGHTBLUE_EX + "PC updated to ")
    print(Fore.RED + "PC = " + PC)
    print(Fore.YELLOW + "Fetch stage completed")
    print()
    return curr_instr


def decode(curr_instr: str):
    """This decodes the instruction based on the opcode"""
    global inst
    inst.opcode = curr_instr[0:6]
    print(Fore.RED + "Opcode=" + inst.opcode)
    if inst.opcode == "000000":  # Decoding R format instructions
        inst.rs = curr_instr[6:11]
        inst.rt = curr_instr[11:16]
        inst.rd = curr_instr[16:21]
        inst.shamt = curr_instr[21:26]
        inst.funct = curr_instr[26:32]
        inst.rs_val = register_file[int(inst.rs, 2)]
        inst.rt_val = register_file[int(inst.rt, 2)]
        inst.regDst = 1
        inst.regWr = 1
        print(Fore.LIGHTBLUE_EX + "Instruction is decoded as R format")
        print(Fore.RED + "RS=" + inst.rs)
        print(Fore.RED + "RT=" + inst.rt)
        print(Fore.RED + "RD=" + inst.rd)
        print(Fore.RED + "Function field=" + inst.funct)
        print(Fore.RED + "Shift amount=" + inst.shamt)

    elif inst.opcode == "100011":  # Decoding LW instruction
        inst.rs = curr_instr[6:11]
        inst.rt = curr_instr[11:16]
        inst.imm = curr_instr[16:32]
        inst.AluSrc = 1
        inst.MemRd = 1
        inst.Mem2Reg = 1
        inst.regWr = 1
        print(Fore.LIGHTBLUE_EX + "Instruction is decoded as LW ")
        print(Fore.RED + "RS=" + inst.rs)
        print(Fore.RED + "RT=" + inst.rt)
        print(Fore.RED + "Immediate value=" + str(conv_to_dec(inst.imm)))

    elif inst.opcode == "001111":  # Decoding LUI instruction
        inst.rs = curr_instr[6:11]
        inst.rt = curr_instr[11:16]
        inst.imm = curr_instr[16:32]
        inst.regWr = 1
        inst.lui = 1
        inst.AluSrc = 1
        print(Fore.LIGHTBLUE_EX + "Instruction is decoded as lui")
        print(Fore.RED + "RS=" + inst.rs)
        print(Fore.RED + "RT=" + inst.rt)
        print(Fore.RED + "Immediate value=" + str(conv_to_dec(inst.imm)))

    elif inst.opcode == "101011":  # Decoding SW instruction
        inst.rs = curr_instr[6:11]
        inst.rt = curr_instr[11:16]
        inst.imm = curr_instr[16:32]
        inst.AluSrc = 1
        inst.MemWr = 1
        print(Fore.LIGHTBLUE_EX + "Instruction is decoded as sw")
        print(Fore.RED + "RS=" + inst.rs)
        print(Fore.RED + "RT=" + inst.rt)
        print(Fore.RED + "Immediate value=" + str(conv_to_dec(inst.imm)))

    elif inst.opcode == "001101":  # Decoding ori Instruction
        inst.rs = curr_instr[6:11]
        inst.rt = curr_instr[11:16]
        inst.imm = curr_instr[16:32]
        inst.AluSrc = 1
        inst.regWr = 1
        print(Fore.LIGHTBLUE_EX + "Instruction is decoded as ori")
        print(Fore.RED + "RS=" + inst.rs)
        print(Fore.RED + "RT=" + inst.rt)
        print(Fore.RED + "Immediate value=" + str(conv_to_dec(inst.imm)))

    elif inst.opcode == "001001" or inst.opcode == "001000":  # Decoding addiu  instruction or addi instruction
        inst.rs = curr_instr[6:11]
        inst.rt = curr_instr[11:16]
        inst.imm = curr_instr[16:32]
        inst.AluSrc = 1
        inst.regWr = 1
        print(Fore.LIGHTBLUE_EX + "Instruction is decoded as add type instruction(addi or addiu)")
        print(Fore.RED + "RS=" + inst.rs)
        print(Fore.RED + "RT=" + inst.rt)
        print(Fore.RED + "Immediate value=" + str(conv_to_dec(inst.imm)))

    elif inst.opcode == "000010":  # Decoding jump instruction
        inst.imm = "0000" + curr_instr[6:32] + "00"
        inst.jump = 1
        print(Fore.LIGHTBLUE_EX + "Instruction is decoded as jump")
        print(Fore.RED + "Jump target address=" + str(conv_to_dec(inst.imm)))

    elif inst.opcode == "000100":  # Decoding BEQ instruction
        inst.rs = curr_instr[6:11]
        inst.rt = curr_instr[11:16]
        inst.imm = curr_instr[16:32]
        inst.branch = 1
        print(Fore.LIGHTBLUE_EX + "Instruction is decoded as BEQ")
        print(Fore.RED + "RS=" + inst.rs)
        print(Fore.RED + "RT=" + inst.rt)
        print(Fore.RED + "Immediate value=" + str(conv_to_dec(inst.imm)))

    elif inst.opcode == "000101":  # Decoding BNE instruction
        inst.rs = curr_instr[6:11]
        inst.rt = curr_instr[11:16]
        inst.imm = curr_instr[16:32]
        inst.branch_ne = 1
        print(Fore.LIGHTBLUE_EX + "Instruction is decoded as BNE")
        print(Fore.RED + "RS=" + inst.rs)
        print(Fore.RED + "RT=" + inst.rt)
        print(Fore.RED + "Immediate value=" + str(conv_to_dec(inst.imm)))
    print()
    print(Fore.YELLOW + "Setting all control Signals ")
    print(Fore.CYAN + "Alusrc:" + str(inst.AluSrc))
    print(Fore.CYAN + "Zero_flag:" + str(inst.zero_flag))
    print(Fore.CYAN + "MemWr:" + str(inst.MemWr))
    print(Fore.CYAN + "MemRd:" + str(inst.MemRd))
    print(Fore.CYAN + "Mem2Reg:" + str(inst.Mem2Reg))
    print(Fore.CYAN + "jump:" + str(inst.jump))
    print(Fore.CYAN + "branch:" + str(inst.branch))
    print(Fore.CYAN + "branch_ne:" + str(inst.branch_ne))
    print(Fore.CYAN + "PCsrc" + str(inst.PCsrc))
    print(Fore.CYAN + "lui:" + str(inst.lui))
    print(Fore.YELLOW + "Decode stage completed")
    print()


def driver():
    """This is the driver code """
    global inst, clock_cycle
    read_in_memory()
    initialise_regs()
    print(Fore.YELLOW + "START:")
    while True:
        clock_cycle += 1
        print()
        inst = Instruction()  # Instruction class object having all the parameters for an instruction
        curr_instr = fetch()
        print(Fore.YELLOW + "Entering Decode stage")
        decode(curr_instr)
        print(Fore.YELLOW + "Entering Execute stage")
        temp = EX()
        print(Fore.YELLOW + "Execute stage completed")
        print()
        print(Fore.YELLOW + "Entering Memory access stage")
        data = MEM(temp, inst.rt_val)
        print(Fore.YELLOW + "Memory access stage completed")
        print()
        print(Fore.YELLOW + "Entering writeback stage")
        WB(data)
        print(Fore.YELLOW + "Writeback stage completed")
        print()



clock_cycle = 0
inst = Instruction()
driver()

"""                             **********THE PROCESSOR CODE ENDS HERE***************                               """
