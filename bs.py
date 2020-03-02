import unittest
import re
from bs4 import BeautifulSoup


def get_img_cnt(body):
    imgs = body.find_all('img')
    cnt = 0
    for i in imgs:
        if i.get('width') and int(i.get('width')) >= 200:
            cnt+=1
    return cnt

def get_headers_cnt(body):
    headers = body.find_all(re.compile('^h[1-6]$'))
    cnt = 0
    for header in headers:
        children = header.find_all(recursive=False)
        if children:
            children_cont = [x.getText() for x in children if x.getText()]
            try:
                first_letter = children_cont[0][0]
                if first_letter in 'ETC':
                    cnt += 1
            except IndexError:
                pass
        else:
            try:
                first_letter = header.getText()[0]
                if first_letter in 'ETC':
                    cnt += 1
            except IndexError:
                pass
    return cnt

def get_max_links_len(body):
    cnt = 0
    all_links = body.find_all('a')
    for link in all_links:
        current_count = 1
        siblings = link.find_next_siblings()
        for sibling in siblings:
            if sibling.name == 'a':
                current_count += 1
                cnt = max(current_count, cnt)
            else:
                current_count = 0
    return cnt

def get_list_num(body):
    cnt = 0
    all_lists = body.find_all(['ul', 'ol'])
    for tag in all_lists:
        if not tag.find_parents(['ul', 'ol']):
            cnt += 1
    return cnt


def parse(path_to_file):
    with open(path_to_file, encoding="utf-8") as data:
        soup = BeautifulSoup(data, "lxml")
    body = soup.find(id="bodyContent")

    imgs = get_img_cnt(body)
    headers = get_headers_cnt(body)
    linkslen = get_max_links_len(body)
    lists = get_list_num(body)
    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()
