#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""
import sys


def print_stats(total_size, status_codes):
    """
    Prints the accumulated statistics.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # Sondan başlayaraq məlumatları götürürük (Format sabitdirsə)
            try:
                # Fayl ölçüsü həmişə sonuncu elementdir
                total_size += int(parts[-1])
                # Status kodu sondan ikinci elementdir
                status_code = parts[-2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except (IndexError, ValueError):
                # Sətir formatı səhvdirsə, onu keçirik
                pass

            # Hər 10 sətirdən bir çap et
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        # Əgər stdin normal şəkildə bitsə (məsələn, fayl sonu), statistikaları çap et
        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # CTRL + C basıldıqda statistikaları çap et və çıx
        print_stats(total_size, status_codes)
        raise
