"""
https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem

Thankfully, this was mostly simple 'checks' of conditions, and thankfully no
use of something like the modulo operator.
"""


def timeConversion(s):
    code = s[-2]
    hours = s[0:2]
    minutes = s[3:5]
    seconds = s[6:8]

    if code == 'A':
        if hours == '12':
            hours = '00'
    elif code == 'P':
        if hours != '12':
            hours = str(int(hours) + 12)

    return ':'.join([hours, minutes, seconds])


if __name__ == '__main__':
    assert timeConversion('12:01:00PM') == '12:01:00'
    assert timeConversion('12:01:00AM') == '00:01:00'
    assert timeConversion('12:45:54PM') == '12:45:54'
