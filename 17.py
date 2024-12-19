import sys
sys.stdin = open('input2.txt', 'r')
from collections import defaultdict

# reg_a, reg_b, reg_c = int(input().split()[-1]), int(input().split()[-1]), int(input().split()[-1])
# regs = [reg_a, reg_b, reg_c]
# input()
# program = list(map(int, input().split()[-1].split(',')))
# print(program)

# ip = 0  # ins pointer
# output = []
# while True:
#     try:
#         op = program[ip]
#         if op == 0:
#             operand = program[ip+1]
#             if operand <= 3:
#                 regs[0] = regs[0] // (2 ** operand)
#             else:
#                 regs[0] = regs[0] // (2 ** (regs[operand - 4]))
#         elif op == 1:
#             operand = program[ip+1]
#             regs[1] ^= operand
#         elif op == 2:
#             operand = program[ip+1]
#             if operand <= 3:
#                 regs[1] = operand
#             else:
#                 regs[1] = regs[operand - 4] % 8
#         elif op == 3:
#             if regs[0] != 0:
#                 ip = program[ip+1]
#                 continue
#         elif op == 4:
#             regs[1] ^= regs[2]
#         elif op == 5:
#             operand = program[ip+1]
#             if operand <= 3:
#                 output.append(operand % 8)
#             else:
#                 output.append(regs[operand - 4] % 8)
#         elif op == 6:
#             operand = program[ip+1]
#             if operand <= 3:
#                 regs[1] = regs[0] // (2 ** operand)
#             else:
#                 regs[1] = regs[0] // (2 ** (regs[operand - 4]))
#         elif op == 7:
#             operand = program[ip+1]
#             if operand <= 3:
#                 regs[2] = regs[0] // (2 ** operand)
#             else:  
#                 regs[2] = regs[0] // (2 ** (regs[operand - 4]))
#         print(ip, op, regs)
#         ip += 2
#     except IndexError:
#         break

# print(','.join(map(str, output)))


# part 2
reg_a, reg_b, reg_c = int(input().split()[-1]), int(input().split()[-1]), int(input().split()[-1])
input()
program = list(map(int, input().split()[-1].split(',')))
print(program)

# last_3 = set()
# for reg_a in range(1, 3 * 10**7):
# # while True:
#     if reg_a % 1000000 == 0:
#         print(reg_a)
fixed_part =          '100000010101000101'
fixed_part = '110010101100100'
fixed_part = ''
suffixes = ['25055', '25057', '62544', '25052']
# convert suffixes to 3 bit binary (each digit goes to 3 bit binary)
new_suffixes = []
for suffix in suffixes:
    new = ''
    for d in suffix:
        new += bin(int(d))[2:].zfill(3)
    new_suffixes.append(new)
suffixes = new_suffixes
print(suffixes)


freqs = defaultdict(set)
last_5 = set()

for i in range(1000000):
    # if i % 100000 == 0:
    #     print(i)
    # prefix = format(i, '03b')
    prefix = bin(i)[2:]
    for suffix in suffixes:
        reg_a = int(prefix + suffix, 2)
        regs = [reg_a, reg_b, reg_c]
        ip = 0  # ins pointer
        output = []
        while True:
            try:
                op = program[ip]
                if op == 0:
                    operand = program[ip+1]
                    if operand <= 3:
                        regs[0] = regs[0] // (2 ** operand)
                    else:
                        regs[0] = regs[0] // (2 ** (regs[operand - 4]))
                elif op == 1:
                    operand = program[ip+1]
                    regs[1] ^= operand
                elif op == 2:
                    operand = program[ip+1]
                    if operand <= 3:
                        regs[1] = operand
                    else:
                        regs[1] = regs[operand - 4] % 8
                elif op == 3:
                    if regs[0] != 0:
                        ip = program[ip+1]
                        continue
                elif op == 4:
                    regs[1] ^= regs[2]
                elif op == 5:
                    operand = program[ip+1]
                    if operand <= 3:
                        output.append(operand % 8)
                    else:
                        output.append(regs[operand - 4] % 8)
                    # if output is not prefix of program
                    if output != program[:len(output)]:
                        n = 10
                        if output[:n] == program[:n]:
                            # cut off last 3 of bin(reg_a)
                            # x = bin(reg_a)[:-3]
                            x = bin(reg_a)
                            # if last part of x is 100000010101000101, remove that
                            if x[-len(fixed_part):] == fixed_part:
                                x = x[:-len(fixed_part)]
                            x = x[2:].zfill(45)
                            # print x in groups of 3 space sep
                            y = ' '.join([str(int(x[i:i+3], 2)) for i in range(0, len(x), 3)]) + ' | ' + x
                            print(y)
                            a = ''.join([str(int(x[i:i+3], 2)) for i in range(0, len(x), 3)])
                            last_5.add(a[-5:])
                            for i, z in enumerate([int(x[i:i+3], 2) for i in range(0, len(x), 3)]):
                                freqs[i].add(z)
                            # print('11:', output[6])
                            # print(bin(reg_a)[:-3], reg_a)
                            # last_3.add(bin(reg_a % 8))
                        break
                elif op == 6:
                    operand = program[ip+1]
                    if operand <= 3:
                        regs[1] = regs[0] // (2 ** operand)
                    else:
                        regs[1] = regs[0] // (2 ** (regs[operand - 4]))
                elif op == 7:
                    operand = program[ip+1]
                    if operand <= 3:
                        regs[2] = regs[0] // (2 ** operand)
                    else:  
                        regs[2] = regs[0] // (2 ** (regs[operand - 4]))
                
                # print(ip, regs, output)
                # print(bin(regs[0]), bin(regs[1]), bin(regs[2]))
                ip += 2

            except IndexError:
                break

        if output == program:
            print(reg_a)
            break
print(freqs)
print(last_5)