N = int(input("Enter the number of men and women: "))

# Function to check if woman 'w' prefers man 'm1' over man 'm'
def wpreferM1overM(prefer, w, m, m1):
    women_pref = prefer[N:]  # Slice to get women's preferences
    for i in range(N):
        if women_pref[w][i] == m1:
            return True
        if women_pref[w][i] == m:
            return False
    return False  # Ideally, we shouldn't reach here

# Function to perform stable matching using the Gale-Shapley algorithm
def stableMatching(prefer):
    wPartner = [-1 for _ in range(N)]  # Women are initially not engaged to anyone
    mFree = [False for _ in range(N)]  # All men are initially free
    freeCount = N  # Number of free men

    # While there are free men
    while freeCount > 0:
        m = 0
        while m < N:
            if not mFree[m]:  # If the man is free
                break
            m += 1

        i = 0
        while i < N and not mFree[m]:
            w = prefer[m][i]

            # If the woman is free, engage her with the man
            if wPartner[w] == -1:
                wPartner[w] = m  # Engage woman 'w' with man 'm'
                mFree[m] = True  # Mark man 'm' as not free
                freeCount -= 1   # Decrease the count of free men

            else:
                m1 = wPartner[w]  # Current partner of woman 'w'
                if not wpreferM1overM(prefer, w, m, m1):
                    wPartner[w] = m  # Engage her with man 'm'
                    mFree[m] = True  # Mark man 'm' as not free
                    mFree[m1] = False  # Mark her previous partner 'm1' as free

            i += 1  # Check the next woman in man's preference list

    # Print the final pairings
    print("Woman", "Man")
    for i in range(N):
        print(chr(i + ord('V')), "\t", chr(wPartner[i] + ord('A')))

# Read men's preferences
print("Enter men's preferences:")
prefer = []
for i in range(N):
    preferences = input(f"Enter preferences for man {chr(i + ord('A'))} (space-separated): ").split()
    prefer.append([ord(p) - ord('V') for p in preferences])

# Read women's preferences
print("Enter women's preferences:")
for i in range(N):
    preferences = list(map(int, input(f"Enter preferences for woman {chr(i + ord('V'))} (space-separated, 0-indexed): ").split()))
    prefer.append(preferences)

# Run the stable matching algorithm
stableMatching(prefer)

#Time Complexity:O(N^2)
#Space Complexity:O(N^2)
