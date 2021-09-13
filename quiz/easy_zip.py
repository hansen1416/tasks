from heapq import heappop, heappush, heapify
from collections import defaultdict, Counter
from typing import List

from itertools import product



def get_encodings(s_to_freq):
    freq_s_heap = [(freq, s) for s,freq in s_to_freq.items()]
    heapify(freq_s_heap)
    s_to_parent_and_bit = {}
    while len(freq_s_heap) >=2:
        freqs = []
        words = []
        for i in range(26):
            if len(freq_s_heap) <=0:
                break
            f, w = heappop(freq_s_heap)
            freqs.append(f)
            words.append(w)
        parent =  "".join(words)
        heappush(freq_s_heap, (sum(freqs), parent))
        for i in range(len(freqs)):
            s_to_parent_and_bit[words[i]] = (parent, chr(i+97))
    s_to_code = {}
    for s in s_to_freq:
        code_bits = []
        w = s
        while w in s_to_parent_and_bit:
            w, bit = s_to_parent_and_bit[w]
            code_bits.append(bit)
        s_to_code[s] = ''.join(map(str, code_bits))    
    return s_to_code    


def solve( sample_text: str, text_to_encode: str # has only spaces apart from words too) -> str:
    ):
    sample = sample_text.split()
    s_to_freq = Counter(sample)
    words = [k for k,v in sorted(s_to_freq.items(), key = lambda item: -item[1])]
    chars = [chr(i+97)  for i in range(26)]
    encoding = {}
    i = 1
    j = 0
    while i <= 26 and j!= len(words):
        for enc in product(chars, repeat = i):
            enc = "".join(enc)
            # print(len(words), j, enc, len(encoding), len(words))
            encoding[words[j]] = enc
            j+=1
            if(len(encoding) == len(words)):
                break
        i+=1    
    result = [encoding.get(w, w)  for w in text_to_encode.split()]
    return " ".join(result)
    # print(" ".join(result))
    
# sample_text = 'the cat the bat the rat chases and'
# text_to_encode ='the cat chases the rat and the rat chases the bat and the bat chases the bat'
# print(solve(sample_text, text_to_encode))