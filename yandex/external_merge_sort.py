import os
from random import shuffle, choice
from heapq import heappush, heappop
from collections import deque


def generate_urls(filename1, filename2):
    with open(filename1, 'x') as file1, open(filename2, 'x') as file2:
        urls = list(f"http://www.domain.com/{n:05}" for n in range(100000))
        urls1 = urls[:75000]
        urls2 = urls[25000:]
        
        shuffle(urls1)
        shuffle(urls2)

        file1.write('\n'.join(urls1))
        file2.write('\n'.join(urls2))


def generate_tmp_filename(length=16):
    chars = [chr(n) for n in range(97, 123)]
    return ''.join([choice(chars) for _ in range(length)])


def merge(in_filename1, in_filename2, out_filename):
    with open(in_filename1) as in_file1, open(in_filename2) as in_file2, open(out_filename, 'x') as out_file:

        url1 = in_file1.readline().rstrip()
        url2 = in_file2.readline().rstrip()
        
        while url1 and url2:
            if url1 < url2:
                out_file.write(url1 + '\n')
                url1 = in_file1.readline().rstrip()
            else:
                out_file.write(url2 + '\n')
                url2 = in_file2.readline().rstrip()

        while url1:
            out_file.write(url1 + '\n')
            url1 = in_file1.readline().rstrip()

        while url2:
            out_file.write(url2 + '\n')
            url2 = in_file2.readline().rstrip()


def merge_sort(in_filename, out_filename, max_buf_size=65536):
    chunk_files = deque()
    buf = []
    buf_size = 0

    with open(in_filename) as in_file, open(out_filename, 'x') as out_file:
        while True:
            url = in_file.readline().rstrip()
            if not url:
                break

            heappush(buf, url)
            buf_size += len(url)

            if buf_size > max_buf_size:
                tmp_filename = generate_tmp_filename()
                with open(tmp_filename, 'x') as tmp_file:
                    while buf:
                        tmp_file.write(heappop(buf) + '\n')
                    buf_size = 0

                chunk_files.append(tmp_filename)
        
        if buf:
            tmp_filename = generate_tmp_filename()
            with open(tmp_filename, 'x') as tmp_file:
                while buf:
                    tmp_file.write(heappop(buf) + '\n')
                buf_size = 0

            chunk_files.append(tmp_filename)

        while len(chunk_files) > 1:
            tmp_filename = generate_tmp_filename()
            filename1 = chunk_files.pop()
            filename2 = chunk_files.pop()

            merge(filename1, filename2, tmp_filename)
            chunk_files.appendleft(tmp_filename)

            os.remove(filename1)
            os.remove(filename2)

        with open(chunk_files[0]) as in_file:
            out_file.writelines(in_file)

        os.remove(chunk_files[0])


def file_diff(in_filename1, in_filename2, out_filename):
    with open(in_filename1) as in_file1, open(in_filename2) as in_file2, open(out_filename, 'w') as out_file:
        url1 = in_file1.readline().rstrip()
        url2 = in_file2.readline().rstrip()
        
        while url1 and url2:
            if url1 == url2:
                url1 = in_file1.readline().rstrip()
            elif url1 < url2:
                out_file.write(url1 + '\n')
                url1 = in_file1.readline().rstrip()                
            else:
                url2 = in_file2.readline().rstrip()

        while url1:
            out_file.write(url1 + '\n')
            url1 = in_file1.readline().rstrip()


def urls_diff(in_filename1, in_filename2, out_filename, max_buf_size=65536):
    tmp_filename1 = generate_tmp_filename()
    tmp_filename2 = generate_tmp_filename()

    merge_sort(in_filename1, tmp_filename1, max_buf_size)
    merge_sort(in_filename2, tmp_filename2, max_buf_size)

    file_diff(tmp_filename1, tmp_filename2, out_filename)

    os.remove(tmp_filename1)
    os.remove(tmp_filename2)


generate_urls('urls-1.txt', 'urls-2.txt')

urls_diff('urls-1.txt', 'urls-2.txt', 'urls-diff.txt')
