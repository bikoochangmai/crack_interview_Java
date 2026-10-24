"""Reproduce the AI guide's toy arithmetic; no packages, network or model needed.

Run: python examples/ai/notes_worked_examples.py
These calculations demonstrate concepts, not a production tokenizer or model.
"""
from collections import Counter
import math

def softmax(values):
    peak=max(values)
    weights=[math.exp(x-peak) for x in values]
    total=sum(weights)
    return [x/total for x in weights]

def cosine(a,b):
    return sum(x*y for x,y in zip(a,b))/(math.sqrt(sum(x*x for x in a))*math.sqrt(sum(x*x for x in b)))

def toy_bpe():
    corpus={tuple(word):count for word,count in {'low':3,'lower':2,'new':1}.items()}
    merges=[]
    for _ in range(2):
        counts=Counter()
        for tokens,count in corpus.items():
            for pair in zip(tokens,tokens[1:]):counts[pair]+=count
        best=min(counts,key=lambda pair:(-counts[pair],pair))
        merges.append((best,counts[best]))
        updated={}
        for tokens,count in corpus.items():
            result=[];index=0
            while index<len(tokens):
                if tokens[index:index+2]==best:result.append(''.join(best));index+=2
                else:result.append(tokens[index]);index+=1
            key=tuple(result);updated[key]=updated.get(key,0)+count
        corpus=updated
    return merges,corpus

def main():
    merges,corpus=toy_bpe()
    assert merges==[(('l','o'),5),(('lo','w'),5)]
    assert corpus=={('low',):3,('low','e','r'):2,('n','e','w'):1}
    weights=softmax([1/math.sqrt(2),0])
    output=[weights[0]*10,weights[1]*20]
    assert math.isclose(sum(weights),1)
    assert math.isclose(output[0],6.697615493,abs_tol=1e-8)
    assert math.isclose(output[1],6.604769013,abs_tol=1e-8)
    assert softmax([1/math.sqrt(2),float('-inf')])==[1,0]
    assert math.isclose(cosine([1,0],[.8,.6]),.8)
    assert cosine([1,0],[0,1])==0
    pe=[math.sin(1),math.cos(1),math.sin(.01),math.cos(.01)]
    assert [round(x,6) for x in pe]==[.841471,.540302,.01,.99995]
    full=4096*4096;adapter=4096*8+4096*8
    assert (full,adapter)==(16777216,65536)
    assert math.isclose(100*adapter/full,.390625)
    assert 8192-(600+1200+4000+200+1500)==692
    gold={'A','B'};retrieved=['A','C','B'];hits=len(gold.intersection(retrieved))
    assert hits/len(retrieved)==2/3 and hits/len(gold)==1
    assert math.isclose(-math.log(.25),1.38629436112,abs_tol=1e-10)
    print('PASS: counted BPE merges, attention + causal mask, cosine, positions, LoRA parameter count, context budget, retrieval precision/recall and log loss.')

if __name__=='__main__':main()
