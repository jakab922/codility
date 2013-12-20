def solutionv2(A, B):
    a_max = max(A)
    A2 = []
    for i, a in enumerate(A):
        if i == 0:
            A2.append((a, len(A2)))
        elif A[i] != A2[-1]:
            A2.append((a, len(A2)))

    A2 = sroted(A2)
    la2 = len(A2)
    island_count = 1
    if len(A2) == 1:
        clevels = [(A2[0][0], 0)]
    else:
        clevels = []
        pval = -1
        for val, ind in A2:
            if ind == 0:
                if val > A2[1][0]:
                    island_count -= 1
            elif ind == la2 - 1:
                if val > A2[-2][0]:
                    island_count -= 1
            else:
                if val > A2[ind - 1][0] and val > A2[ind + 1][0]:
                    island_count -= 1
                elif val < A2[ind - 1][0] and val < A2[ind + 1][0]:
                    island_count += 1
            if pval != -1 and pval != val:
                clevels.append((pval, ))
                levels[val] = island_count
            pval = val
        levels[pval] =







def solution(A, B):
    a_max = max(A)
    la = len(A)
    lb = len(B)
    cache = [0 for _ in xrange(a_max + 1)]
    coll = {}
    for i, a in enumerate(A):
        if a in coll:
            coll[a].append(i)
        else:
            coll[a] = [i]
    curr = la
    cache[0] = la
    for i in xrange(1, a_max + 1):
        if i in coll:
            prev = -1
            ctype = -1
            for j in coll[i]:
                if prev != -1:
                    if prev
            curr -= coll[i]
        cache[i] = curr

    print "cache: %s" % cache
    print "coll: %s" % coll

    ret = [0 for _ in xrange(lb)]
    for b in B:
        if b > a_max:
            ret[i] = 0
        else:
            ret[i] = cache[b]

    return ret


if __name__ == "__main__":
    A = [2, 1, 3, 2, 3]
    B = [0, 1, 2, 3, 1]
    print "A: %s" % A
    print "B: %s" % B
    print solution(A, B)
