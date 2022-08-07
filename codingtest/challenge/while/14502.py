def solution(s):
    answer = 0
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = ''
    stack = list(s)
    while stack:
        pop = stack.pop(0)
        if pop.isdigit():
            result += str(pop)
            continue
        while not pop in word:
            pop += stack.pop(0)
        result += str(word.index(pop))
    return result
print(solution("one4seveneight"))