#binärMinusRechnen.txt
# 202205051355 antonius ehlen

# Rechnen: 10 - 15 = 10 + (-15)

# dez: 10 ist bin: 0000 1010
# dez: 15 ist bin: 0000 1111

# komplement zur 15_
#     binär:     : 0000 1111
#     inventiert : 1111 0000
#     + 1 zum Invert Wert:
#                : 1111 0001
# jetzt 10+ Komplement + 1 (15) rechnen:
#                : 0000 1010
#                + 1111 0001
#                  1111 1011  ist bei Vorzeichen losem Byte: 251
#         aber bei Vorzeichenbehaftetem Byte
#                     Wissen dazu: Plusbereich wäre : 0 - 127
#                                  Minusbereich wäre: -1 - 128