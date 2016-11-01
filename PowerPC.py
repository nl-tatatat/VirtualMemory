# -*- coding: utf-8 -*-
# Python 2.7.X
from __future__ import print_function
from types import FunctionType
from array import array
memchanged= [False,[]]
#defitions    
breakpoints = {}
#class Memory(object):
#    def __init__(self,data,
#        self.data = data #sorry, I started playing a game and didn't finish this
#    def __
def getmemory(start,bits):
    keys = range(start,start + bits / 8)
    keys.reverse()
    return_mem = 0
    for key in range(0,len(keys)):
        try:
          return_mem += memory[keys[key]] << (key * 8)
        except IndexError: #out of defined memory
          pass
    return return_mem
def addtomemory(key,value,bits):
    NS['memchanged'][0] = True
    lmem = len(memory) - 1
    dif = key - (lmem)
    val_bytes = []
    for i in range(0,bits / 8):
        val_bytes.append(  (value >> ((8 * i))) & ((0x1 << 8) - 1)); val_bytes.reverse()
    if dif > 0:
        if 1: #enters a scope, deletes extra_mem at end of scope without calling del
            extra_mem = []
            for i in range(0,dif-1):
                extra_mem.append(0) #creates zeros
            memory.extend(extra_mem) #adds zeros after memory
        memory.extend(val_bytes) #adds value
    else: memory[key:key + (bits / 8)] = array('B',val_bytes)
        
            
        
        
        
        
memory = array('B',)
# 100 = less; 010 = greater; 001 = equal
inequality = lambda arg1, arg2: cmp( arg1, arg2 )+1 or 4
one_comp = lambda val: val ^ ((1 << val.bit_length()) - 1) #ones complement
class label:
    def __init__(self, address):
        self.address = address
def swap_twos_comp(data, size):
    return (~data & ((0x1 << size) - 1)) + 1 # apply twos complement

def py_to_unsigned(data, outputBits):
    if data < 0: # check for negitive and apply signage
        # make data positive, then swap positive to negitive twos complement
        data = swap_twos_comp(-data, outputBits)
    else:
        data &= (0x1 << outputBits) - 1 # truncate to bitsize
    return data
"""
def unsigned_to_py(data):

    bl = data.bit_length()

    if data & (0x1 << bl-1): # signed data
        data = -1*swap_twos_comp(data, bl) # convert out of twos complement

    return data
"""
def asm_to_hex(asm):
    #print (asm)
    asm = asm.replace(',',' ').split()
    bits = 0b00000000000000000000000000000000 #formatted in an easy way for me
    #print (asm)
    try:
        if asm[1][0] == "r": #removes register prefix
            asm[1] = asm[1][1:]
        elif "0x" in asm[1]:
            asm[1] = int(asm[1], 16)
        if asm[2][0] == "r":
            asm[2] = asm[2][1:]
        elif "0x" in asm[2]:
            asm[2] = int(asm[2], 16)
        if asm[3][0] == "r":
            asm[3] = asm[3][1:]
        elif "0x" in asm[3]:
            asm[3] = int(asm[3], 16)
    except:
        pass
    if asm[0] == "li":
        bits = bits | (0b00111000000000000000000000000000) # codeword for li
        bits = bits | ((int(asm[1])) << 21) # overflow from register
        bits = bits | ((int(asm[2]) & 0b1111111111111111)) 
        return (bits)
    elif asm[0] == "add":
        bits = bits | (0b1111100000000000000001000010100)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1)) << 11)
        bits = bits | ((int(asm[2]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1)) << 21)
        return (bits)
    elif asm[0] == "addc":
        bits = bits | (0b1111100000000000000000000010100)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1)) << 11)
        bits = bits | ((int(asm[2]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1)) << 21)
        return (bits)
    elif asm[1] == "andc":
        bits = bits | (0b1111100000000000000000000111000)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1)) << 11)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[2]) & ((0x1 << 8) - 1)) << 21)
        return (bits)
    elif asm[0] == "or":
        bits = bits | (0b1111100000000000000001101111000)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1)) << 11)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[2]) & ((0x1 << 8) - 1)) << 21)
        return (bits)
    elif asm[0] == "orc":
        bits = bits | (0b1111100000000000000001100111000)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1)) << 11)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[2]) & ((0x1 << 8) - 1)) << 21)
        return (bits)
    elif asm[0] == "mr":
        bits = bits | (0b1111100000000000000001101111000)
        bits = bits | ((int(asm[2]) & ((0x1 << 8) - 1)) << 21)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[2]) & ((0x1 << 8) - 1)) << 11)
        return (bits)
    elif asm[0] == "sub":
        bits = bits | (0b1111100000000000000000001010000)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1)) << 21)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[2]) & ((0x1 << 8) - 1)) << 11)
        return (bits)
    elif asm[0] == "b":
        bits = bits | (0b1001000000000000000000000000000)
        bits = bits | (int(asm[1]) & (((0x1 << 18) - 1) << 2))
        return (bits)
    elif asm[0] == "bl":
        bits = bits | (0b1001000000000000000000000000001)
        bits = bits | (int(asm[1]) & (((0x1 << 18) - 1) << 2))
        return (bits)

    elif asm[0] == "bne":
        bits = bits | (0b1000000100000100000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bne-":
        bits = bits | (0b1000000100000100000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bne+":
        bits = bits | (0b1000000101000100000000000001100)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bnel":
        bits = bits | (0b1000000100000100000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bnel-":
        bits = bits | (0b1000000100000100000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bnel+":
        bits = bits | (0b1000000101000100000000000001101)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "beq":
        bits = bits | (0b1000001100000100000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "beq-":
        bits = bits | (0b1000001100000100000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "beq+":
        bits = bits | (0b1000001101000100000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "beql":
        bits = bits | (0b1000001100000100000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "beql-":
        bits = bits | (0b1000001100000100000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "beql+":
        bits = bits | (0b1000001101000100000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bgt":
        bits = bits | (0b1000001100000010000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bgt-":
        bits = bits | (0b1000001100000010000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bgt+":
        bits = bits | (0b1000001101000010000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bgtl":
        bits = bits | (0b1000001100000010000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bgtl-":
        bits = bits | (0b1000001100000010000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bgtl+":
        bits = bits | (0b1000001101000010000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bge":
        bits = bits | (0b1000000100000000000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bge-":
        bits = bits | (0b1000000100000000000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bge+":
        bits = bits | (0b1000000101000000000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bgel":
        bits = bits | (0b1000000100000000000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bgel-":
        bits = bits | (0b1000000100000000000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bgel+":
        bits = bits | (0b1000000101000000000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "blt":
        bits = bits | (0b1000001100000000000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "blt-":
        bits = bits | (0b1000001100000000000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "blt+":
        bits = bits | (0b1000001101000000000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bltl":
        bits = bits | (0b1000001100000000000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bltl-":
        bits = bits | (0b1000001100000000000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bltl+":
        bits = bits | (0b1000001101000000000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "ble":
        bits = bits | (0b1000000100000010000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "ble-":
        bits = bits | (0b1000000100000010000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "ble+":
        bits = bits | (0b1000000101000010000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "blel":
        bits = bits | (0b1000000100000010000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "blel-":
        bits = bits | (0b1000000100000010000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "blel+":
        bits = bits | (0b1000000101000010000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111100))
        return (bits)
    elif asm[0] == "bne":
        bits = bits | (0b1000000100000100000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bne-":
        bits = bits | (0b1000000100000100000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bne+":
        bits = bits | (0b1000000101000100000000000001100)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bnel":
        bits = bits | (0b1000000100000100000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bnel-":
        bits = bits | (0b1000000100000100000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bnel+":
        bits = bits | (0b1000000101000100000000000001101)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "beq":
        bits = bits | (0b1000001100000100000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "beq-":
        bits = bits | (0b1000001100000100000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "beq+":
        bits = bits | (0b1000001101000100000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "beql":
        bits = bits | (0b1000001100000100000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "beql-":
        bits = bits | (0b1000001100000100000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "beql+":
        bits = bits | (0b1000001101000100000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bgt":
        bits = bits | (0b1000001100000010000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bgt-":
        bits = bits | (0b1000001100000010000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bgt+":
        bits = bits | (0b1000001101000010000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bgtl":
        bits = bits | (0b1000001100000010000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bgtl-":
        bits = bits | (0b1000001100000010000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bgtl+":
        bits = bits | (0b1000001101000010000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bge":
        bits = bits | (0b1000000100000000000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bge-":
        bits = bits | (0b1000000100000000000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bge+":
        bits = bits | (0b1000000101000000000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bgel":
        bits = bits | (0b1000000100000000000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bgel-":
        bits = bits | (0b1000000100000000000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bgel+":
        bits = bits | (0b1000000101000000000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "blt":
        bits = bits | (0b1000001100000000000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "blt-":
        bits = bits | (0b1000001100000000000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "blt+":
        bits = bits | (0b1000001101000000000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bltl":
        bits = bits | (0b1000001100000000000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bltl-":
        bits = bits | (0b1000001100000000000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "bltl+":
        bits = bits | (0b1000001101000000000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "ble":
        bits = bits | (0b1000000100000010000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "ble-":
        bits = bits | (0b1000000100000010000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "ble+":
        bits = bits | (0b1000000101000010000000000000000)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "blel":
        bits = bits | (0b1000000100000010000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "blel-":
        bits = bits | (0b1000000100000010000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "blel+":
        bits = bits | (0b1000000101000010000000000000001)
        bits = bits | ((int(asm[1]) & 0b111111111111111))
        return (bits)
    elif asm[0] == "eqv":
        bits = bits | (0b1111100000000000000001000111000)
        bits = bits | ((int(asm[2]) & ((0x1 << 8) - 1)) << 21)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1))  << 11)
        return (bits)
    elif asm[0] == "lwz":
        #print (bin(bits))
        bits = py_to_unsigned(bits | (0b10000000000000000000000000000000),32)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1)) << 21)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[2]) & ((0x1 << 15) - 1)))
        return (bits)
    elif asm[0] == "lbz":
        #print (bin(bits))
        bits = bits | py_to_unsigned((0b10001000000000000000000000000000),32)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1)) << 21)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[2]) & ((0x1 << 15) - 1)))
        return (bits)
    elif asm[0] == "nand":
        bits = bits | (0b1111100000000000000001110111000)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1)) << 11)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[2]) & ((0x1 << 8) - 1))  << 21)
        return (bits)
    elif asm[0] == "nor":
        bits = bits | (0b1111100000000000000000011111000)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1)) << 11)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[2]) & ((0x1 << 8) - 1)) << 21)
        return (bits)
    elif asm[0] == "stb":
        bits = bits | py_to_unsigned(0b10011000000000000000000000000000,32)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1)) << 21)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[2]) & ((0x1 << 15) - 1)))
        return (bits)
    elif asm[0] == "stw":
        bits = bits | py_to_unsigned(0b10010000000000000000000000000000,32)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1)) << 21)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[2]) & ((0x1 << 15) - 1)))
        return (bits)
    elif asm[0] == "sth":
        bits = bits | py_to_unsigned(0b10110000000000000000000000000000,32)
        bits = bits | ((int(asm[1]) & ((0x1 << 8) - 1)) << 21)
        bits = bits | ((int(asm[3]) & ((0x1 << 8) - 1))  << 16)
        bits = bits | ((int(asm[2]) & ((0x1 << 15) - 1)))
        return (bits)
def hex_to_asm(val):
    identifier = val >> 27 #'first' 5 bits
    if not (identifier ^ 0b10010):#branch       #10010 ^ 10010 = 0 == False
        if val & 0b1: #bl
            return ("bl " + str(hex(val )))
    #10010
    #check if branch
def branch_conditional(offset,bit,equal=False,link=False): # bit 3 means Not equal.
    crval = cast(getgl("CR").value,3, True) # 3 bits of conditional register
    if ( crval&0b1 and equal ) or ( crval&0b10 and bit==2 ) or ( crval&0b100 and bit==1 ) or ( (not crval&0b001) and bit==3 ):
        if link: LR.set(PC.value) # updates link register (bl)
        PC.set(PC.value + offset)
        
cast = lambda reg, bits=0, nonreg=False: reg&((1<<bits)-1) if nonreg else reg.value&((1<<reg.bits)-1)

class register(object):
    __slots__ = ['value','bits']
    __int__ = lambda this: int(this.value)
    def __init__(self,value,bits):
        self.value = value
        self.bits = bits
    def set(self,value,casts=False,bits=16):
        if value.__class__ == register: # value is a register
            raise TypeError('value is a register')
        self.value = value
        self.value = cast(self)
        #print (self.value)
        if casts:
            self.value = cast(self,bits)
#li = lambda rx, nx:rx.set(int(nx))

#some ideas on op codes before I forget
#All powerpc commands will be inputted as a string with enters seperating lines
#each line shall be an individual index in a list
#example line
# "li r1, 0x3
# mr r2, r1"
# ["li r1, 0x3", "mr r2, r1"]

#defines registers
#global r0; global r1; global r2; global r3; global r4; global r5; global r6; global r7; global r8; global r9; global r10; global r11; global r12; global r13; global r14; global r15; global r16; global r17; global r18; global r19; global r20; global r21; global r22; global r23; global r24; global r25; global r26; global r27; global r28; global r29; global r30; global r31;
#global f0; global f1; global f2; global f3; global f4; global f5; global f6; global f7; global f8; global f9; global f10; global f11; global f12; global f13; global f14; global f15; global f16; global f17; global f18; global f19; global f20; global f21; global f22; global f23; global f24; global f25; global f26; global f27; global f28; global f29; global f30; global f31;
#global PC; global LR; global CTR; global CR; global FPSCR; global MSR; global SRR0; global SRR1; global Exceptions; global IntMask; global IntCause; global DSISR; global DAR; global PTHashmask;
#global DBAT0; global DBAT1; global DBAT2; global DBAT3; global IBAT0; global IBAT1; global IBAT2; global IBAT3; global DBAT4; global DBAT5; global DBAT6; global DBAT7; global IBAT4; global IBAT5; global IBAT6; global IBAT7;
#global SR00; global SR01; global SR02; global SR03; global SR04; global SR05; global SR06; global SR07; global SR08; global SR09; global SR10; global SR11; global SR12; global SR13; global SR14; global SR15;

# get register from number
grn = lambda num: num.value if num.__class__==register else getgl("r%i"%num).value

NS = {} # Tcll - this is our restricted environment
for n in range(32):
    NS['r%i'%n] = NS['R%i'%n] = register(0,32) # r1 == R1
    NS['f%i'%n] = NS['F%i'%n] = register(0,128) # f1 == F1
NS.update(dict(
    CR = register(0,32), LR = register(0,32),
    PC = register(0,32), # current position in memory
    
    # TODO: these should not be in this namespace:
    inequality = inequality,
    branch_conditional = branch_conditional,
    grn = grn,
    
    # add a few basic builtins
    int = int,
    str = str,
    True = True, False = False,
    cast = cast,
    one_comp = one_comp,
    breakpoints = breakpoints,
    memory = memory,
    py_to_unsigned = py_to_unsigned,
    swap_twos_comp = swap_twos_comp,
    addtomemory = addtomemory,
    getmemory = getmemory,
    memchanged = memchanged,
))
PC = NS['PC'] # Tcll - needed for the execution address.
LR = NS['LR']

#registers = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29, r30, r31, f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f20, f21, f22, f23, f24, f25, f26, f27, f28, f29, f30, f31, CR, LR]
#print (bin(r0.value))
#opcodes["li"](r1, 5)
#print (r1.value)
#opcodes["li"](r2,5)
#print (r2.value)
#opcodes["add"](r0,r1,r2)
#print (r0.value)
#opcodes["sub"](r3,r1,5)
#print (r3.value)
#opcodes["li"](r4,0b1111000011110000111100001111000011101011001010110010010101001011)
#print (bin(r4.value))
#opcodes["srw"](r5,r4,3)
#print (bin(r5.value))
'''
print ("Address: " + str(hex(PC.value)))
opcodes["b"](0xC)
print ("Address: " + str(hex(PC.value)))
print (hex(LR.value))
opcodes["bl"](0x8)
print ("Address: " + str(hex(PC.value)))
print(hex(LR.value))
'''
#opcodelist
opcodes = { # ignore the error highlights for CR and LR, they're defined in NS where these functions are used.
    "li": lambda ax, bx: ax.set(bx & 0b1111111111111111, True, 16),
    "lis": lambda ax, bx: ax.set((bx & 0b1111111111111111)<< 16,False),
    "add": lambda ax, bx, cx:ax.set(grn(bx) + grn(cx)),
    #"addc": lambda ax, bx, cx:ax.set(grn(bx) + (grn(cx)),
    "sub": lambda ax, bx, cx:ax.set(grn(bx) - grn(cx)),
    "subf": lambda ax, bx, cx:ax.set(-(grn(bx)) + (grn(cx))),
    #"slw": lambda ax, bx, cx:ax.set((((grn(bx)) >> 32) << 32) + (cast((cast(((grn(bx)) << (grn(cx))),32,True)),32,True))), 
    #"srw": lambda ax, bx, cx:ax.set((((grn(bx)) >> 32) << 32) + (cast((cast(((grn(ax)) >> (grn(cx))),32,True)),32,True))), 
    "slw": lambda ax, bx, cx:ax.set((grn(bx)<< grn(cx),False)),
    "cmpwi": lambda ax, bx:CR.set(inequality((grn(ax)), (grn(bx)))),
    "blr": lambda: PC.set(LR.value + 4),
    "bl": lambda ax: [LR.set(PC.value), PC.set(PC.value + int(ax))],
    "b": lambda ax: PC.set(PC.value + int(ax)),
    "bne": lambda ax: branch_conditional(int(ax), 3),
    "bne-": lambda ax: branch_conditional(int(ax), 3),
    "bne+": lambda ax: branch_conditional(int(ax), 3),
    "bnel": lambda ax: branch_conditional(int(ax), 3, False, True),
    "bnel-": lambda ax: branch_conditional(int(ax), 3, False, True),
    "bnel+": lambda ax: branch_conditional(int(ax), 3, False, True),
    #"bnespaghetti": lambda ax: branch_conditional(int(ax), 3, False, False, spaghetti),
    "beq": lambda ax: branch_conditional(int(ax), 4, True),
    "beq+": lambda ax: branch_conditional(int(ax), 4, True),
    "beq-": lambda ax: branch_conditional(int(ax), 4, True),
    "beql": lambda ax: branch_conditional(int(ax), 4, True, True),
    "beql-": lambda ax: branch_conditional(int(ax), 4, True, True),
    "beql+": lambda ax: branch_conditional(int(ax), 4, True, True),
    "bgt": lambda ax: branch_conditional(int(ax),2),
    "bgt-": lambda ax: branch_conditional(int(ax),2),
    "bgt+": lambda ax: branch_conditional(int(ax),2),
    "bgtl": lambda ax: branch_conditional(int(ax),2,False, True),
    "bgtl+": lambda ax: branch_conditional(int(ax),2,False, True),
    "bgtl-": lambda ax: branch_conditional(int(ax),2,False, True),
    "blt": lambda ax: branch_conditional(int(ax),1),
    "blt-": lambda ax: branch_conditional(int(ax),1),
    "blt+": lambda ax: branch_conditional(int(ax),1),
    "bltl": lambda ax: branch_conditional(int(ax),1,False,True),
    "bltl-": lambda ax: branch_conditional(int(ax),1,False,True),
    "bltl+": lambda ax: branch_conditional(int(ax),1,False,True),
    "and": lambda ax, bx, cx: ax.set((grn(bx) & int(cx))),
    "andc": lambda ax, bx, cx: ax.set((grn(bx) & (one_comp(grn(cx))))),
    "nand": lambda ax, bx, cx: ax.set(one_comp(grn(bx) & (grn(cx)))),
    "or": lambda ax, bx, cx: ax.set((grn(bx) | (grn(cx)))),
    "nor": lambda ax, bx, cx: ax.set(one_comp(grn(bx) | grn(cx))),
    "xori": lambda ax, bx, cx: ax.set((grn(bx) ^ (grn(cx)))), #need to fix
    "xor": lambda ax, bx, cx: ax.set((grn(bx) ^ (grn(cx)))),
    "mr": lambda ax, bx: ax.set(grn(bx)),
    "eqv": lambda ax, bx, cx: ax.set(one_comp(grn(bx) ^ (grn(cx)))),
    "lbz": lambda ax, bx, cx: ax.set(cast(getmemory(grn(cx) + bx,8),8,True)), #2
    "lhz": lambda ax, bx, cx: ax.set(cast(getmemory(grn(cx) + bx,16),16,True)), #4
    "lwz": lambda ax, bx, cx: ax.set(cast(getmemory(grn(cx) + bx,32),32,True)),
    "stw": lambda ax, bx, cx: addtomemory(grn(cx) + bx,grn(ax),32),
    "sth": lambda ax, bx, cx: addtomemory(grn(cx) + bx,grn(ax),16),
    "stb": lambda ax, bx, cx: addtomemory(grn(cx) + bx,grn(ax),8),
    #"stw": lambda ax, bx, cx: set_memory(int(bx) + grn(cx) / 4,grn(ax),32),
    #"lbz": lambda ax, bx, cx: ax.set(int("0x" + ("".join(memory))[((bx + grn(cx)) ) : ((bx + grn(cx)) * 2) + 2],16),True,8),
    #"lhz": lambda ax, bx, cx: ax.set(int("0x" + ("".join(memory))[((bx + grn(cx)) ) : ((bx + grn(cx)) * 2) + 4],16),True,16),
    #"lwz": lambda ax, bx, cx: ax.set(int("0x" + ("".join(memory))[((bx + grn(cx)) * 2) : ((bx + grn(cx)) * 2) + 8],16)),
#    "xor.": lambda ax, bx, cx: [ax.set(int(bx) ^ int(cx)), None]

#cast((0b1000000000000000000000000000000000000000000000000000000000000000 + cast(((int(bx) << int(cx))), 32, True)), 32, True))
}
opcodes = { k: FunctionType(v.__code__,NS) for k,v in opcodes.items() } # restrict all functions to the NS

opcodes['xor.'] = opcodes['xor']

# speedy sorcery:
getop = opcodes.__getitem__
getgl = NS.__getitem__
hasgl = NS.__contains__

def execute(op,*args): # Tcll - do not use anything outside this function
    # comment switch:
    #''' # debug operation (uncomment this line for normal operation)
    print('(%s)@0x%08X: %s'%( _ln, _addr, line ))
    arguments = []; aapp = arguments.append
    _registers = {} # for debug
    for arg in args:
        if hasgl(arg): _r = _registers[arg] = getgl(arg); aapp(_r) # append value from register
        else: aapp(eval(arg)) # convert code to value and append

    getop( op )( *arguments ) # execute current line
    print('LR: %s'%( LR.value ))
    print('r#: %s'%[getgl('r%s'%r).value for r in range(32)])
    print('f#: %s'%[getgl('f%s'%f).value for f in range(32)])

    for k,v in _registers.items(): # display info
        print('    %s: %s'%(k,v.value))
    print()

    ''' # normal operation
    getop(op)(*(getgl(arg) if hasgl(arg) else eval(arg) for arg in args))
    #'''



#user section

def breakp():
    try: #py 2.X
        raw_input("Breakpoint reached. Press enter to continue... ")
    except: #py 3.X
        input("Breakpoint reached. Press enter to continue... ")


# our code to execute:
ASM = '''li r0,0
li r1,16
li r2, 50
li r3, 80
Li r4, 100
li r5, 25
BeQ 12
li r4, 24
lwz r6, -0xC(r1)
nor r6, r6, r4
stw r6,4(r0)'''


#global starting_address;
print_mem = True #debug
starting_address = 0x0 #arbitrary starting address
if starting_address != 0: PC.set(starting_address)

break_list = '''0x10'''
break_list = break_list.replace(" ","") #no spaces
breakpoint_strings = break_list.split('\n')
del break_list #not needed

#end of user section
#=======================
#preprocessing

#process breakpoints
for breakpoint in range(0,len(breakpoint_strings)):
    try:
        if (int(breakpoint_strings[breakpoint] , 16) % 4 == 0): #is disivible by four
          breakpoints[str(int(breakpoint_strings[breakpoint],16))] = False #adds breakpoint to dict
          #breakpoint syntax
          #name: breakpoint address
          #value: whether breakpoint has been met
        else:
          raise Exception("Number must be divisible by four for breakpoints. Line: " + str(breakpoint) + " . >> '" + str(breakpoint_strings[breakpoint]) + "'")
    except:
        raise Exception("Invalid number given as breakpoint. Line: " + str(breakpoint) + " . >> '" + str(breakpoint_strings[breakpoint]) + "'")
#end of breakpoints

lines = ASM.split('\n')

del ASM #not needed

_mod,_join = '%s %s'.__mod__, ''.join; _fmt = lambda op, *args: _mod((op,_join(args))).rstrip()
lines = map(lambda line: _fmt(*line.split()),lines) # remove unneeded spaces



#format cases of opcodes

for line in range(0,len(lines)):
    lines[line] = (lines[line].replace("("," ")).replace(")"," ")
    llen = len(lines[line])
    if not (":" in lines[line]): #isn't a label
        if not lines[line][0].lower() == "b": #isn't a branch
            lines[line] = lines[line].lower()
        else: #is a branch
            if ("blr" in lines[line]):
                lines[line] = "blr"
                continue
            #print (lines[line])
            lines[line] = lines[line][:lines[line].index(" ")].lower() + lines[line][lines[line].index(" "):]
labels = {}
#look for labels
for line in range(0,len(lines)):
    lines_deleted = 0
    if (line + lines_deleted) >= len(lines):
        break
    lines[line - lines_deleted] = lines[line - lines_deleted].split('#')[0] # split comments
    if ":" in  lines[line - lines_deleted]: #is a label
        if not (" " in lines[line - lines_deleted]):
            label_area = lines[line - lines_deleted][:len(lines[line - lines_deleted]) - 1]
            if label_area.isalnum() == True: #valid label
                if not label_area[0].isalpha(): #starts with a number
                    raise Exception("Labels can't start with numbers. Line: " + str(line) + " . >> '" + str(lines[line - lines_deleted]) + "''")
                #create_label
                #print (label_area)
                labels[label_area] = label(starting_address + (line * 4)) #adds label to labels
                #print (labels[label_area].address)
                del lines[line - lines_deleted]
            else:
                raise Exception("Labels can only contain letters and numbers. Line: " + str(line) + " . >> '" + str(lines[line - lines_deleted]) + "'")
        else:
            raise Exception("Labels can't have spaces in them. Line: " + str(line) + " . >> '" + str(lines[line - lines_deleted]) + "'")
    # load word syntax
    #else: #not a label
    #    if lines[line - lines_deleted][0] == "l": #is a load opcode
    #        pass
    #        #try:
    #            if not (("(" in lines[line - lines_deleted]) and  (")" in lines[line - lines_deleted])):
    #                raise Exception("Load opcode doesn't contain parentheses. Line: " + str(line) + " . >> '" + str(lines[line - lines_deleted]) + "'")
    #            line[line - lines_deleted] lines[line - lines_deleted].index("(")
    #            
    #        #except:
    #        #    raise Exception("Incorrect syntax for Load opcode. Line: " + str(line) + " . >> '" + str(lines[line - lines_deleted]) + "'")
"""
#while 1:
#    restart = False
#    to_delete = 0
#    for line in range(0,len(lines)):
#        llen = len(lines[line])
#        if not (" " in lines[line]): #no spaces
#            if lines[line][llen - 1] == ":": #is a label
#                label_area = lines[line][:llen - 1] #used twice
#                if label_area.isalnum() == True: #valid label
#                    #create label
#                    labels[label_area] = label(starting_address + (line * 4)) #adds label to labels
#                    restart = True
#                    to_delete = line
#                    break
#    if restart == False:
#        break
#    #print (to_delete)
#    del lines[to_delete]
"""
"""
ASM="" #had to remove

NS = {}

lines = ASM.split('\n')
setLine = lines.__setitem__
pop = lines.pop

insert = list.insert
index,find,strip,split = str.__getitem__, str.find, str.strip, str.split
mod,join = '%s %s'.__mod__,''.join
setGlobal = NS.__setitem__
#fmt = lambda op,*args: mod((op,join(args)))

def formatLine(op,*args):
    args = map( formatArgs, join(args).split(',') )
    return insert(args,0,op)
    
_numbers = '0123456789'
i = 0
for line in lines:
    if '#' in line: line = index(line,slice(find(line,'#'))) # remove comment
    line = strip(line) # strip whitespace
    
    if not line: continue # pop the empty line
    if ':' in line: # pop label and map the proposed address
        label = strip(index(line,slice(find(line,':'))))
        if (not label) or ' ' in label or label[0] in _numbers:
            raise SyntaxError('Invalid syntax.')
        setGlobal(label,i*4)
        continue

    setLine(i,formatLine(*line.split()))
    i+=1
lines = lines[:i]

for l in lines: print l
print labels
"""
#have to do the iteration twice to first get all labels

#remove labels from opcode
for line in range(0,len(lines)):
    #print ("line: " + lines[line])
    #llen = len(lines[line])
    if (not (":" in lines[line])): #isn't a label
        if lines[line][0] == "b": #is a branch
            if ("blr" in lines[line]): #branch link register
                    continue
            if not (" " in lines[line]): #no label
                continue
                #can insert code for checking if divisble by 4 here
            if lines[line][1] != "c": #normal branch
                #print (lines)
                #print (lines[line])
                b_label_index = lines[line].index(" ") #where the label is in the branch
                if not (lines[line][1 + b_label_index].isalpha()): #isn't a label
                    continue
                b_label = lines[line][b_label_index + 1:]
                #print (b_label)
                #print (labels[b_label].address)
                lines[line] = lines[line][0:b_label_index] + " " + str(hex(labels[b_label].address - (starting_address + (line * 4))))
                #print (lines[line])
            else: #has C
                if (lines[line][2].lower() == "c") or (lines[line][2:3] == "lr"): #no labels possible
                    continue
                else: #branch conditional
                    #r_line = lines[line][::-1]
                    commas = []
                    commas.append(lines[line].index(","));commas.append(1 + commas[0] + lines[line][commas[0] + 1:].index(","))
                    #print (commas)
                    b_label_index = commas[1] #where the label is in the branch
                    del commas
                    if not (lines[line][2 + b_label_index].isalpha()): #isn't a label
                        continue
                    b_label = lines[line][b_label_index + 2:]
                    lines[line] = lines[line][0:b_label_index] + " " + str(hex(labels[b_label].address - (starting_address + (line * 4))))
    #update branches with label addresses
#for line in range(0,len(lines)):
#  print (lines[line])

#replace register substitutes

  
#remove proprocessing variables
print ("hi")

del labels
#print (lines)
#execution

#memory
memory_list = []
for line in lines:
    #print (line)
    ath = asm_to_hex(line)
    memory_list[len(memory_list):len(memory_list) + 4] = [ath >> 24,(ath >> 16) & 0b11111111,(ath >> 8) & 0b11111111,ath & 0b11111111]
memory = array('B',memory_list)
#print (memory)

del memory_list

_ln = 0 # execution point (line number)
_addr2ln = {} # addr: ln
if print_mem == True: print(memory)
while True:
    start_pc = PC.value
    try: # faster than if
        line = lines[_ln].split('#')[0] # split comments
    except IndexError: break # looks like we've finished our execution
    if line: # '' evaluates to False
        _addr = PC.value
        _addr2ln[_addr] = _ln # map the address to the line number of the code to "jump" to
        execute( *line.replace(',',' ').split() )
        
    if start_pc == PC.value: # hasn't branched
        PC.value += 0x4
    try:
        pass
        if not (breakpoints[str(PC.value)]): #breakpoint not activated yet
            breakp() #breaks
    except: pass
    if NS['memchanged'][0]:
        if print_mem:
            print(memory)
    _ln = (PC.value - starting_address) / 4
