import random


# -- | Emulation of Haskell fst (Lisp car)
def fst(l):
    return l[0]

# -- | Emulation of Haskell fst (Lisp cdr)
def snd(l):
    return l[1]

# -- | Pop one element from a specific list position
def pop(i,l):
	#print i,l
	if len(l) > 0:
		e = l.pop(i) 
	    	return (e,l)
	else:
        	return ([],[])

# -- | Generate random number within interval a-b
def myrandom(a,b,s):
	random.seed(s)
	if a == 0 and b == 0:
		return 0
	else:
		return random.randrange(a,b)


# -- | Shuffle a list
def shuffle(l):
	return shufflep(myrandom(0,(len(l)-1),0),l,[])

# -- | Shuffle' auxiliary
def shufflep(r,l1,l2):
	llen= len(l1)
	#print l1
	t = pop(r,l1)
	if llen == 0:
		return l2
	else:
		l2 += [fst(t)]
		return shufflep(myrandom(0,llen-1,r),snd(t),l2)

def main():
	v = [i for i in range(1,100) ]
	print "List shuffle!"
	print shuffle(v)

if __name__ == "__main__":
	main()
