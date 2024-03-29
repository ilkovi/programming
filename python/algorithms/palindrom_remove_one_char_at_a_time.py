# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

s = 'radkar'


def solution(s):
    for i in range(len(s)):
        t = s[:i] + s[i + 1:]
        print(f"#### {i} ---- {s[:i]} --- {s[i + 1:]} ----{t}")
        if t == t[::-1]: return True

    return s == s[::-1]


solution(s)
