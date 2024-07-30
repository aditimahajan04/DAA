N = 3  # Number of men or women

# Function to check if woman 'w' prefers man 'm1' over man 'm'
def wpreferM1overM(prefer, w, m, m1):
    for i in range(N):
        if prefer[w][i] == m1:
            return True
        if prefer[w][i] == m:
            return False
    return False  # Just in case we reach here, though ideally, we shouldn't

def stableMatching(prefer):
    # Initialize all women and men as free
    wPartner = [-1 for _ in range(N)]
    mFree = [False for _ in range(N)]
    freeCount = N

    while freeCount > 0:
        # Find the first free man
        m = 0
        while m < N:
            if not mFree[m]:
                break
            m += 1

        # One by one go to all women according to m's preferences
        i = 0
        while i < N and not mFree[m]:
            # Index of the woman m prefers
            w = ord(prefer[m][i]) - ord('V')  # Convert woman 'V', 'W', 'X' to 0, 1, 2

            # If the woman is free, engage with her
            if wPartner[w] == -1:
                wPartner[w] = m
                mFree[m] = True
                freeCount -= 1
            else:
                # If the woman prefers the current man over her engaged man
                m1 = wPartner[w]
                if not wpreferM1overM(prefer[N:], w, m, m1):
                    wPartner[w] = m
                    mFree[m] = True
                    mFree[m1] = False

            i += 1

    print("Woman", "Man")
    for i in range(N):
        print(chr(i + ord('V')), "\t", chr(wPartner[i] + ord('A')))

# Men's and women's preferences
prefer = [
    ['V', 'W', 'X'], ['W', 'V', 'X'], ['V', 'W', 'X'],  # Men's preferences
    ['A', 'B', 'C'], ['B', 'C', 'A'], ['C', 'A', 'B']   # Women's preferences
]

stableMatching(prefer)



