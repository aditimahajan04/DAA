N = 3  # Number of men and women

# Function to check if woman 'w' prefers man 'm1' over man 'm'
def wpreferM1overM(prefer, w, m, m1):
    # 'prefer' array is split: first N rows for men, next N rows for women
    women_pref = prefer[N:]  # Slice to get women's preferences
    for i in range(N):
        # If 'm1' comes before 'm' in the list, she prefers 'm1' over 'm'
        if women_pref[w][i] == m1:
            return True
        # If 'm' comes before 'm1', she prefers 'm' over 'm1'
        if women_pref[w][i] == m:
            return False
    return False  # Ideally, we shouldn't reach here

# Function to perform stable matching using the Gale-Shapley algorithm
def stableMatching(prefer):
    # Initialize all women and men as free
    wPartner = [-1 for _ in range(N)]  # Women are initially not engaged to anyone
    mFree = [False for _ in range(N)]  # All men are initially free
    freeCount = N  # Number of free men

    # While there are free men
    while freeCount > 0:
        # Find the first free man
        m = 0
        while m < N:
            if not mFree[m]:  # If the man is free
                break
            m += 1

        # Iterate over all women according to this man's preferences
        i = 0
        while i < N and not mFree[m]:
            # Convert woman identifier ('V', 'W', 'X') to index (0, 1, 2)
            w = ord(prefer[m][i]) - ord('V')

            # If the woman is free, engage her with the man
            if wPartner[w] == -1:
                wPartner[w] = m  # Engage woman 'w' with man 'm'
                mFree[m] = True  # Mark man 'm' as not free
                freeCount -= 1   # Decrease the count of free men

            else:
                # If the woman is already engaged, check her preference
                m1 = wPartner[w]  # Current partner of woman 'w'
                # If she prefers the current man 'm' over her current partner 'm1'
                if not wpreferM1overM(prefer, w, m, m1):
                    wPartner[w] = m  # Engage her with man 'm'
                    mFree[m] = True  # Mark man 'm' as not free
                    mFree[m1] = False  # Mark her previous partner 'm1' as free

            i += 1  # Check the next woman in man's preference list

    # Print the final pairings
    print("Woman", "Man")
    for i in range(N):
        print(chr(i + ord('V')), "\t", chr(wPartner[i] + ord('A')))

# Men's and women's preferences
prefer = [
    ['V', 'W', 'X'], ['W', 'V', 'X'], ['V', 'W', 'X'],  # Men's preferences (A, B, C)
    [0, 1, 2], [1, 2, 0], [2, 0, 1]   # Women's preferences (V, W, X)
]
stableMatching(prefer)

#Time Complexity:O(N^2)
#Space Complexity:O(N^2)



