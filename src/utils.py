import re
import urllib.request

from constants import APIMANIA_URL


def is_url(url: str) -> bool:
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


def download_file(download_url: str, filename: str) -> None:
    response = urllib.request.urlopen(download_url)
    file = open(filename, 'wb')
    file.write(response.read())
    file.close()


def url_to_pdf(url: str) -> str:
    filename = "{}.pdf".format(get_filename_from_url(url))
    url = "{}/pdf?url={}".format(APIMANIA_URL, url)
    download_file(url, filename)
    return filename


def convert_web_to_img(url: str) -> str:
    filename = "{}.png".format(get_filename_from_url(url))
    url = "{}/screenshot?url={}".format(APIMANIA_URL, url)
    download_file(url, filename)
    return filename


def convert_text_to_img(text: str) -> str:
    url = "{}/txt2img?text={}".format(APIMANIA_URL, text.replace(' ', '%20'))
    download_file(url, "{}.png".format(text))
    return "{0}.png".format(text)


def get_filename_from_url(url: str) -> str:
    return url.split('://')[1].split('/')[0].replace('.', '-')
