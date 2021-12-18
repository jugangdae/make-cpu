
import click
from click.decorators import command
#from parse import compile

mnemonic = {
    'LD'  : 0x0,    # 0001 rarb
    'ST'  : 0x1,    # 0000 rarb
    'DATA': 0x2,    # 0010 00rb / int8
    'JMPR': 0x3,    # 0011 00rb
    'JMP' : 0x4,    # 0100 0000 / int8
    #'JZ'  : 0x5,    # 0101 caez / int8
    'JZ'  : 0x5,    # JUMP IF ANSWER IS ZERO	JZ Addr
    'JE'  : 0x5,    # JUMP IF A EQAULS B	JE Addr
    'JA'  : 0x5,    # JUMP IF A IS LARGER THAN B	JA Addr
    'JC'  : 0x5,    # JUMP IF CARRY IS ON	JC Addr
    'JCA' : 0x5,    # JUMP IF CARRY OR A LARGER	JCA Addr
    'JCE' : 0x5,    # JUMP IF CARRY OR A EQUAL B	JCE Addr
    'JCZ' : 0x5,    # JUMP IF CARRY OR ANSWER IS ZERO	JCZ Addr
    'JAE' : 0x5,    # JUMP IF A IS LARGER OR EQUAL TO B	JAE Addr
    'JAZ' : 0x5,    # JUMP IF A IS LARGER OR ANSWER IS ZERO	JAZ Addr
    'JEZ' : 0x5,    # JUMP IF A EQAULS B OR ANSWER IS ZERO	JEZ Addr
    'JCAE': 0x5,    # JUMP IF CARRY OR A LARGER OREQUAL TO B	JCAE Addr
    'JCAZ': 0x5,    # JUMP IF CARRY OR A LARGER OR ZERO	JCAZ Addr
    'JCEZ': 0x5,    # JUMP IF CARRY ORA EQUALS B OR ZERO	JCEZ Addr
    'JAEZ': 0x5,    # JUMP IF A LARGER OR EQUAL TO B OR ZERO	JAEZ Addr
    'JCAEZ':0x5,    # JUMP IF CARRY OR A LARGER OR EQUAL OR ZERO	JCAEZ Addr
    'CLF' : 0x6,    # 0110 0000
    'ADD' : 0x8,    # 1000 rarb
    'SHL' : 0x9,    # 1001 rarb
    'SHR' : 0xA,    # 1010 rarb
    'NOT' : 0xB,    # 1011 rarb
    'AND' : 0xC,    # 1100 rarb
    'OR'  : 0xD,    # 1101 rarb
    'XOR' : 0xE,    # 1110 rarb
    'CMP' : 0xF     # 1111 rarb
}

register = {
    'R0' : 0x00,
    'R1' : 0x01,
    'R2' : 0x02,
    'R3' : 0x03
}

flags = {
    'C' : 0x8, #caez
    'A' : 0x4,
    'E' : 0x2,
    'Z' : 0x1
}

@click.command()
@click.option('-o', '--output', help='Set an output file.')
@click.argument('filepath')
def asm(filepath, output):
    cnt = 0
    code = []
    a = open(filepath, 'r')
    
    while True:
        '''
        #p = compile("{} {}, {}")
        p = compile("{} {}")
        line = a.readline()
        if not line: break
        cnt += 1
        
        line = line.strip()
        code = line.split('#')[0]
        
        if code:
            result = p.parse(code)
            print(cnt, result)
        '''

        

        line = a.readline()
        if not line: break
        cnt += 1

        line = line.strip()
        command = line.split('#')[0].strip()
        
        if command:
            result=[]
            mne = command.split(' ', maxsplit=1)[0]
            
            if mne == 'LD' or mne == 'ST' or mnemonic[mne] & mnemonic['ADD']:
                result.append(mne)
                if command.split(' ', maxsplit=1)[1].count(', '):
                    result.append(command.split(' ', maxsplit=1)[1].split(', ')[0])
                    result.append(command.split(' ', maxsplit=1)[1].split(', ')[1])
                    b = (mnemonic[result[0]]<<4) | register[result[1]]<<2 | register[result[2]]
                    code.append(b)
                    print(result, end=" : ")
                    print(hex(b))

            elif mne == 'DATA' :
                result.append(mne)
                if command.split(' ', maxsplit=1)[1].count(', '):
                    result.append(command.split(' ', maxsplit=1)[1].split(', ')[0])
                    result.append(command.split(' ', maxsplit=1)[1].split(', ')[1])
                    b = (mnemonic[result[0]]<<4) | register[result[1]]
                    d = int(result[2])
                    code.append(b)
                    code.append(d)
                    print(result, end=" : ")
                    print(hex(b), hex(d))

            elif mne == 'JMPR':
                result.append(mne)
                if command.split(' ', maxsplit=1)[1]:
                    result.append(command.split(' ', maxsplit=1)[1].split(', ')[0])
                    b = (mnemonic[result[0]]<<4) | register[result[1]]
                    code.append(b)
                    print(result, end=" : ")
                    print(hex(b))

            elif mne == 'JMP':
                result.append(mne)
                if not command.split(' ', maxsplit=1)[1].count(', '):
                    result.append(command.split(' ', maxsplit=1)[1].split(', ')[0])
                    b = (mnemonic[result[0]]<<4)
                    d = int(result[1])
                    code.append(b)
                    code.append(d)
                    print(result, end=" : ")
                    print(hex(b), hex(d))
            
            elif mnemonic[mne] == mnemonic['JZ']:
                res_flag=[]
                tmp_flag=0
                result.append(mne)

                if not command.split(' ', maxsplit=1)[1].count(', '):
                    result.append(command.split(' ', maxsplit=1)[1].split(', ')[0])

                    for i in mne[1:]:
                        res_flag.append(i)
                        tmp_flag |= flags[i]
                    b = (mnemonic[result[0]]<<4) | tmp_flag
                    d = int(result[1])
                    code.append(b)
                    code.append(d)
                    print(result, end=" : ")
                    print(hex(b), hex(d))

            elif mne == 'CLF':
                result.append(mne)
                if len(result) == 1:
                    b = (mnemonic[result[0]]<<4)
                    code.append(b)
                    print(result, end=" : ")
                    print(hex(b))
    print("")
    print('lines: ', cnt)
    print('code: ', code)

    a.close()

    o = open(output, 'wb')
    o.write(bytes(code))
    o.close()

if __name__ == '__main__':
    asm()
    
    
'''
JZ	    JUMP IF ANSWER IS ZERO	JZ Addr
JE	    JUMP IF A EQAULS B	JE Addr
JA	    JUMP IF A IS LARGER THAN B	JA Addr
JC	    JUMP IF CARRY IS ON	JC Addr
JCA	    JUMP IF CARRY OR A LARGER	JCA Addr
JCE	    JUMP IF CARRY OR A EQUAL B	JCE Addr
JCZ	    JUMP IF CARRY OR ANSWER IS ZERO	JCZ Addr
JAE	    JUMP IF A IS LARGER OR EQUAL TO B	JAE Addr
JAZ	    JUMP IF A IS LARGER OR ANSWER IS ZERO	JAZ Addr
JEZ	    JUMP IF A EQAULS B OR ANSWER IS ZERO	JEZ Addr
JCAE	JUMP IF CARRY OR A LARGER OREQUAL TO B	JCAE Addr
JCAZ	JUMP IF CARRY OR A LARGER OR ZERO	JCAZ Addr
JCEZ	JUMP IF CARRY ORA EQUALS B OR ZERO	JCEZ Addr
JAEZ	JUMP IF A LARGER OR EQUAL TO B OR ZERO	JAEZ Addr
JCAEZ	JUMP IF CARRY OR A LARGER OR EQUAL OR ZERO	JCAEZ Addr


LD R0, R1
ST R0, R1
DATA R1, 10
JMPR R0
JMP 32
JZ 1
JE 2
JA 3
JC 4
JCA 5
JCE 6
JCZ 7
JAZ 8
JEZ 9
JCAE 10
JCAZ 11
JCEZ 12
JAEZ 13
JCAEZ 14
CLF
ADD R0, R1
SHL R0, R1
SHR R0, R1
NOT R0, R1
AND R0, R1
OR R0, R1
XOR R0, R1
CMP R0, R1
'''
