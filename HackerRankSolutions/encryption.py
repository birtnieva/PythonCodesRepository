import math

str = input().strip()

st = str.replace(' ','')

s = len(st)

r = math.ceil(math.sqrt(s))

m = []
for c in range(0,s,r):
    m.append(st[c:c+r])

out = []
for i in range(0, len(m[0])):
    if s%r != 0 and i >= s%r:
        line = []
        for j in range(0,s%r):
            line.append(m[j][i])
        out.append(''.join(line))
    else:
        line = []
        for j in range(len(m)):
            line.append(m[j][i])
        out.append(''.join(line))

print(' '.join(out))


#in6: roqfqeylxuyxjfyqterizzkhgvngapvudnztsxeprfp
#out6: rlyzatp oxqkps quthvx fyegue qxrvdp ejinnr yfzgzf

#in11: jqlvizzusfkmuevvtcbnlcvmocjvfskqkyluxmqru
#out11: juvcfu qsvvsx lftmkm vkcoqq imbckr zunjyu zelvl

#in12: bgwdyygtmwhtwhusfedckrgybozfjaukgsngqvzftiypqukxypbkghjiwkphkjtsdizueaz
#out12: bwdfqujs ghcjvkid wtkazxwi dwrufykz yhgktppu yuygibhe gsbsykka tfonpgjz mezgqht
