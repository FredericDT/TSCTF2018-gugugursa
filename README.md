# 不正常的RSA
## 一个缩进引发的血案;
(有了代码缩不缩进无所谓┑(￣Д ￣)┍)

解题思路:

审计.py知：

用户种类由合成字符串的最后一个逗号后面的admin/user决定

粗略得知输入的字符串会经过RSA加解密过程

已知 e = 7

d 为取得值，使 ed 与 1 模 (p-1)(q-1) 同余

N = p * q

密文 c 由此生成 

c = s ** e mod N

对于明文s有

s mod N = c ** (ed) mod N

则有

c mod N = s ** e mod N = c ** (ede) mod N

所以我们构造 s ** e 充当 c

在题中即为 s ** 7

得 FLAG

TSCTF{Very_Easy_RSA_Right?}