# Make CPU

## ASM
```
python asm.py -o [output] path
```
--- 
## LD 
Load data at the address of RAM pointed to by RA to data in RB

```
LD RA, RB
```

## ST
Store data in RB to memory address pointed to by RA

```
ST RA, RB
```

## DATA
Load byte data into RB

```
DATA RB, BYTE
```


## JMPR
Jump to the address of RAM in RB

```
JMPR RB
```

## JMP
Jump directly to a specific RAM address

```
JMP ADDR
```

## JC, JA, JE, JZ
Jump when specific flag is on
(C = CARRY, A = A>B, E = A=B, Z = ZERO)

```
JC ADDR
```

## JCA, JCE, JCZ, JAE, JAZ, JEZ, JCAE, JCAZ, JCEZ, JAEZ, JCAEZ
Jump when specific flags are on
(C = CARRY, A = A>B, E = A=B, Z = ZERO)

```
JCAEZ ADDR
```

## CLF
Clear flag register to 0

```
CLF
```

## ADD
ADD operation on RA and RB and put the result in RB

```
ADD RA, RB
```

## SHL
Shift RA left to put in RB

```
SHL RA, RB
```

## SHR
Shift RA right to put in RB

```
SHR RA, RB
```

## NOT
NOT operation RA and put the result into RB

```
NOT RA, RB
```

## AND
AND operation on RA and RB and put the result in RB

```
AND RA, RB
```

## OR
OR operation on RA and RB and put the result in RB

```
OR RA, RB
```

## XOR
XOR operation on RA and RB and put the result in RB

```
XOR RA, RB
```

## CMP
Compare RA and RB and put the result in flag register

```
CMP RA, RB
```
