"""
Made by Aadi Bajpai <me AT aadibajpai DOT me>, originally for personal use.
Don't use my résumé lol, but feel free to use the LaTeX template
You'll probably need to modify the variables for your own use
"""

import requests
from urllib.parse import quote_plus

libs = ['swaglyrics', 'SwSpotify']


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
        r = requests.get(py_url.format(lib=lib))
        cnt += r.json()['total_downloads']
    return cnt


def update_resume(python_libs=libs):

    dl = dl_count(python_libs)  # get download count of libraries

    with open('resume.tex', 'r') as f:
        tex = f.read() % {"dl": format(dl, ',d')}

    # print(tex)
    ltx = requests.get(f'https://latexonline.cc/compile?text={quote_plus(tex)}&force=true')
    with open('aadi_resume.pdf', 'wb') as f:
        f.write(ltx.content)


if __name__ == '__main__':
    update_resume()
