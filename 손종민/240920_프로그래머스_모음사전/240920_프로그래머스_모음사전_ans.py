CHARS = 'AEIOU'

def dfs(states, words):
    if len(states) == 5:
        return
    
    for c in CHARS:
        states.append(c)
        words.append(''.join(states))
        
        dfs(states, words)
        
        states.pop()

def solution(word):
    states, words = [], []
    dfs(states, words)
    
    return words.index(word) + 1