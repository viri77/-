# def ips_between(start, end):
#     suma = 0
#     k = start.split('.')
#     b = end.split('.')
#     for i in range(len(b)):
#         b[i] = int(b[i])
#     for _ in range(len(k)):
#         k[_] = int(k[_])
#     if b[3] > k[3]:
#         suma += b[3] - k[3]
#     elif b[3] < k[3]:
#         suma -= k[3] - b[3]
#
#     if b[2] > k[2]:
#         suma += 256 * (b[2] - k[2])
#     elif b[2] < k[2]:
#         suma -= 256 * (k[2] - b[2])
#         print(256 * (k[2] - b[2]))
#
#     if b[1] > k[1]:
#         suma += 256 ** 2 * (b[1] - k[1])
#     elif b[1] < k[1]:
#         suma -= 256 ** 2 * (k[1]) - b[1]
#
#     if b[0] > k[0]:
#         suma += 255 ** 3 * (b[1] - k[1])
#
#     return suma
#

#ips_between('154.137.154.181', '156.211.3.45')
print(2*(256**3 )+ 74*(256**2)- 151*256-136)
