from bs4 import BeautifulSoup
import urllib.request
import re

def get_kernel_versions(includes, excludes, limit):
    # Use soup to get all the links on the page
    resp = urllib.request.urlopen("https://kernel.ubuntu.com/~kernel-ppa/mainline/")
    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'), features="html.parser")
    links = soup.find_all('a', href=True)
    for link in links[-limit:]:
        # Includes
        if re.match(includes, link['href']):
            # Excludes
            if not re.match(excludes, link['href']):
                print(link['href'])


def get_installed_kernels():
    

get_kernel_versions("^v.*", ".*-rc\d+\/", 100)