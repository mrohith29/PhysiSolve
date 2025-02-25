class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.flag = False

def insert(word, root):
    curr = root
    for i in word:
        idx = ord(i)-ord('a')
        if curr.child[idx] is None:
            curr.child[idx] = TrieNode()
        curr = curr.child[idx]
    curr.flag = True

def partition(s, root, i, l, dp, min_parts):
    # Base case: if we've reached the end of string
    if i == l:
        return 1, 0  # One valid way, 0 additional partitions needed
    
    # If already computed
    if dp[i] != -1:
        return dp[i], min_parts[i]
    
    curr = root
    total_ways = 0
    min_partitions = float('inf')
    
    # Try all possible partitions starting from index i
    for j in range(i, l):
        idx = ord(s[j])-ord('a')
        if curr.child[idx] is None:
            break
        curr = curr.child[idx]
        if curr.flag:
            # Found a valid word, try remaining string
            ways, parts = partition(s, root, j+1, l, dp, min_parts)
            if ways > 0:  # If remaining string can be partitioned
                total_ways += ways
                min_partitions = min(min_partitions, parts + 1)
    
    dp[i] = total_ways
    min_parts[i] = min_partitions if total_ways > 0 else float('inf')
    return total_ways, min_parts[i]

def solve_test_case():
    n = int(input())
    strg = input()
    k = int(input())
    strgs = input().split()
    
    # Build Trie
    root = TrieNode()
    for s in strgs:
        insert(s, root)
    
    # Initialize DP arrays
    dp = [-1] * (n+1)
    min_parts = [-1] * (n+1)
    
    # Get total ways and minimum partitions
    ways, min_partitions = partition(strg, root, 0, n, dp, min_parts)
    
    print(ways, min_partitions)

# Process all test cases
for _ in range(int(input())):
    solve_test_case()