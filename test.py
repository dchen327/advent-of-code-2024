#%%
s = '''
mrh XOR bnc -> z32
y14 XOR x14 -> vvw
bjt XOR mmm -> z42
y41 AND x41 -> gwr
sbs AND vbj -> kpf
x01 XOR y01 -> rbr
jkf XOR kmf -> z21
x25 XOR y25 -> knp
y05 AND x05 -> jcj
qpn OR gmv -> krq
x19 AND y19 -> mfq
mrh AND bnc -> rvw
wrg XOR mjr -> z44
y10 XOR x10 -> gtn
y42 AND x42 -> dmw
wmj OR pft -> tkg
x13 AND y13 -> qkc
y05 XOR x05 -> tjs
pmk XOR vqg -> z36
tcg OR fbd -> z45
y33 AND x33 -> wmj
sqs OR thj -> sch
y16 AND x16 -> hbc
y09 XOR x09 -> svf
mjb OR bbc -> bhq
dvf XOR fdj -> z33
x34 AND y34 -> pbp
y44 XOR x44 -> mjr
x28 XOR y28 -> qdq
qkc OR crp -> mgc
vgn AND wfn -> khj
rwc OR svg -> dng
y33 XOR x33 -> dvf
y29 XOR x29 -> fqc
vqg AND pmk -> stq
rbr XOR rnv -> z01
x37 XOR y37 -> kbh
x35 AND y35 -> nsb
hqn XOR kbh -> z37
ftq XOR fqc -> z29
y21 XOR x21 -> jkf
y39 XOR x39 -> vvc
x16 XOR y16 -> gnc
x41 XOR y41 -> dgn
y12 XOR x12 -> nvv
dmw OR hgm -> cjb
crb OR bgw -> mrh
stq OR cfj -> hqn
qdh XOR bhq -> z13
svf XOR thf -> z09
skb OR qdj -> nbm
x24 AND y24 -> pwp
x07 XOR y07 -> gpb
qsj OR khj -> qvs
y30 XOR x30 -> rdj
x20 XOR y20 -> vtd
qmm XOR svb -> z26
y20 AND x20 -> tsn
pbp OR cpb -> ngc
cct AND pvb -> jnk
y06 AND x06 -> nfr
gnc AND nbm -> mfr
tkg XOR bpm -> z34
sbs XOR vbj -> vkq
srj OR rvr -> wfn
y04 XOR x04 -> brf
x21 AND y21 -> drv
mmk AND knp -> jss
x22 AND y22 -> rvr
y27 AND x27 -> srb
vvc AND hth -> qvm
mdm OR hqh -> hth
bjr AND cjb -> wgc
prm XOR jps -> z18
hpg AND ssv -> jvt
ngc XOR mqw -> z35
gbw XOR vjb -> z02
jbf OR ptp -> ghq
pwp OR cwc -> z24
hkh OR nst -> gnn
fkb XOR vrp -> z03
svb AND qmm -> jbf
y09 AND x09 -> thj
hdk AND gpb -> gmv
gnn AND brf -> wfw
knv OR nfr -> hdk
mgc XOR vvw -> z14
rbp OR qvm -> ssv
y34 XOR x34 -> bpm
qvs AND kmc -> cwc
hqp OR nbf -> gbw
svf AND thf -> sqs
y30 AND x30 -> svg
vgs OR gwr -> bjt
y28 AND x28 -> pvb
y17 AND x17 -> jcs
bsv OR vrn -> vrp
jpk OR rvw -> fdj
x11 AND y11 -> z11
vwh XOR dgn -> z41
y08 AND x08 -> wwb
wrg AND mjr -> tcg
hbc OR mfr -> mjp
knp XOR mmk -> z25
y44 AND x44 -> fbd
y15 XOR x15 -> mjc
x32 XOR y32 -> bnc
x04 AND y04 -> qvq
ssg XOR shm -> z22
ghq XOR fnc -> z27
x10 AND y10 -> jmb
y32 AND x32 -> jpk
y07 AND x07 -> qpn
ngc AND mqw -> hrj
x43 AND y43 -> cts
vmb AND mjc -> skb
sch XOR gtn -> z10
rnv AND rbr -> nbf
frv AND rdj -> rwc
tjs XOR ncd -> z05
qbd OR jcs -> jps
prm AND jps -> hrb
qdq OR jnk -> ftq
x29 AND y29 -> jft
y40 AND x40 -> pqh
gtn AND sch -> kbf
wmp XOR mft -> z19
tcj AND mjp -> qbd
dvf AND fdj -> pft
nkj OR drv -> shm
jcj OR kfn -> cpw
cpw XOR gqf -> z06
jss OR qwb -> svb
x02 XOR y02 -> vjb
cts OR wgc -> wrg
nmq OR jhd -> vmb
mks XOR nvv -> z12
jmb OR kbf -> sbs
vkm OR wwb -> thf
qhh OR jft -> frv
jpf OR cdf -> dkp
x36 XOR y36 -> vqg
nbm XOR gnc -> z16
gqf AND cpw -> knv
ghg OR mfq -> gnk
y38 AND x38 -> mdm
y23 XOR x23 -> vgn
pqh OR jvt -> vwh
vtd AND gnk -> hbb
x18 AND y18 -> sds
x02 AND y02 -> bsv
ssv XOR hpg -> z40
qvs XOR kmc -> mmk
y26 AND x26 -> ptp
qdh AND bhq -> crp
y12 AND x12 -> bbc
y23 AND x23 -> qsj
y37 AND x37 -> cdf
hth XOR vvc -> z39
pkp OR srb -> cct
fnc AND ghq -> pkp
x18 XOR y18 -> prm
y43 XOR x43 -> bjr
x26 XOR y26 -> qmm
kbh AND hqn -> jpf
x08 XOR y08 -> gjd
vwh AND dgn -> vgs
x27 XOR y27 -> fnc
gnn XOR brf -> z04
kpf OR vkq -> mks
frv XOR rdj -> z30
y25 AND x25 -> qwb
ftq AND fqc -> qhh
gjd AND krq -> vkm
x35 XOR y35 -> mqw
y06 XOR x06 -> gqf
x15 AND y15 -> qdj
tjs AND ncd -> kfn
nvv AND mks -> mjb
dng XOR pwd -> z31
mjc XOR vmb -> z15
hdk XOR gpb -> z07
y36 AND x36 -> cfj
y39 AND x39 -> rbp
y03 AND x03 -> nst
dng AND pwd -> crb
x03 XOR y03 -> fkb
mgc AND vvw -> nmq
x31 AND y31 -> bgw
y13 XOR x13 -> qdh
wfw OR qvq -> ncd
x22 XOR y22 -> ssg
x11 XOR y11 -> vbj
bjr XOR cjb -> z43
x17 XOR y17 -> tcj
pvb XOR cct -> z28
tsn OR hbb -> kmf
y38 XOR x38 -> vsb
x42 XOR y42 -> mmm
bjt AND mmm -> hgm
hrb OR sds -> mft
x24 XOR y24 -> kmc
vtd XOR gnk -> z20
y00 AND x00 -> rnv
wfn XOR vgn -> z23
vsb AND dkp -> z38
y00 XOR x00 -> z00
mjp XOR tcj -> z17
shm AND ssg -> srj
dkp XOR vsb -> hqh
vrp AND fkb -> hkh
gjd XOR krq -> z08
vjb AND gbw -> vrn
kmf AND jkf -> nkj
x14 AND y14 -> jhd
y31 XOR x31 -> pwd
x01 AND y01 -> hqp
y40 XOR x40 -> hpg
nsb OR hrj -> pmk
bpm AND tkg -> cpb
y19 XOR x19 -> wmp
wmp AND mft -> ghg
'''

# %%
carries = {'gbw': '1', 'vrp': '2', 'gnn': '3', 'ncd': '4', 'cpw': '5', 'hdk': '6', 'krq': '7', 'thf': '8', 'sch': '9', 'mks': '11', 'bhq': '12', 'mgc': '13', 'vmb': '14', 'nbm': '15', 'mjp': '16', 'jps': '17', 'mft': '18', 'gnk': '19', 'kmf': '20', 'shm': '21', 'wfn': '22', 'svb': '25', 'ghq': '26', 'cct': '27', 'ftq': '28', 'frv': '29', 'dng': '30', 'mrh': '31', 'fdj': '32', 'tkg': '33', 'ngc': '34', 'pmk': '35', 'hqn': '36', 'dkp': '37', 'hth': '38', 'ssv': '39', 'vwh': '40', 'bjt': '41', 'cjb': '42', 'wrg': '43'}
for k, v in carries.items():
    s = s.replace(k, f'c{v.zfill(2)}')
# %%
# print(s)
# which nums from 1 to 44 are not in carries values
print(set(range(1, 45)) - set(int(x) for x in carries.values()))
# %%
with open('edited.txt', 'r') as f:
    s = f.read()

for line in s.splitlines():
    if not line:
        continue
    if 'OR' in line.split() and 'c' not in line[-3:]:
        print(line)
# %%
