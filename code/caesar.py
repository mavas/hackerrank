from string import ascii_lowercase, ascii_uppercase


def main(s, k):
    o = ''
    k = k % 26
    for c in s:
        if c in ascii_lowercase:
            i = ascii_lowercase.index(c)
            if (i+k) > 25:
                diff = abs((i+k) - 25) - 1
                o += ascii_lowercase[diff]
            else:
                o += ascii_lowercase[i+k]
        elif c in ascii_uppercase:
            i = ascii_uppercase.index(c)
            if (i+k) > 25:
                diff = abs((i+k) - 25) -1
                o += ascii_uppercase[diff]
            else:
                o += ascii_uppercase[i+k]
        else:
            o += c
    return o


if __name__ == '__main__':
    assert main('middle-Outz', 2) == 'okffng-Qwvb'
    assert main('Hello_World!', 4) == 'Lipps_Asvph!'
    assert main('www.abc.xy', 87) == 'fff.jkl.gh'
