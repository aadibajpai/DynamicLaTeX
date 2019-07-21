"""
Made by Aadi Bajpai <me AT aadibajpai DOT me>, originally for personal use.
Don't use my résumé lol, but feel free to use the LaTeX template
You'll probably need to modify the variables for your own use
"""

import re
from urllib.parse import quote_plus

import requests

r = re.compile(r'\\py{([\w]+)}')


def dl_count(libraries):
    """
    to fetch download count of specified libraries.
    Currently works for python libraries.
    :param libraries: list of libraries
    :return: total download count of libraries
    """
    py_url = 'https://api.pepy.tech/api/projects/{lib}'
    cnt = 0
    for lib in libraries:
        req = requests.get(py_url.format(lib=lib))
        cnt += req.json()['total_downloads']
    return cnt


def update_resume(template_values):

    with open('resume.tex', 'r') as f:
        tex = r.sub(lambda x: str(format(template_values[x.group(1)], ',d')), f.read())

    # print(tex)
    ltx = requests.get(f'https://latexonline.cc/compile?text={quote_plus(tex)}&force=true')
    with open('aadi_resume.pdf', 'wb') as f:
        f.write(ltx.content)


if __name__ == '__main__':
    update_resume({'dlt': dl_count(['swaglyrics', 'SwSpotify'])})
