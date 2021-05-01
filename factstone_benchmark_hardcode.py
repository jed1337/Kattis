year_to_bit_cache = {
    1960: 3,
    1970: 5,
    1980: 8,
    1990: 12,
    2000: 20,
    2010: 34,
    2020: 57,
    2030: 98,
    2040: 170,
    2050: 300,
    2060: 536,
    2070: 966,
    2080: 1754,
    2090: 3210,
    2100: 5910,
    2110: 10944,
    2120: 20366,
    2130: 38064,
    2140: 71421,
    2150: 134480,
    2160: 254016
}

while True:
    year = int(input())
    if year == 0:
        break
    year = (year // 10) * 10
    print(year_to_bit_cache[year])
