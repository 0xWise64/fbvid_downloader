import requests
import bs4
import json
import argparse
import random


def download(k):
    r = requests.get(str(k), timeout=10)
    bs = bs4.BeautifulSoup(r.text, 'html.parser')
    scripts = bs.find_all('script')

    if r.status_code == 200:
        for s in scripts:
            if 'embedUrl' in s.text:
                script = s.text
                jsonObj = json.loads(script)
                video_url = str(jsonObj['video']['embedUrl'])
                r = requests.get(video_url, timeout=10)
                n = random.randint(100, 9999)
                open(f'{n}.mp4', 'wb+').write(r.content)
                print(f'The video has been successfully downloaded and saved in {n}.mp4')

    else:
        print('Invalid URL or the specified URL could not be reached!')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='An script to download videos from facebook.')
    parser.add_argument('-u', '--url', type=str, nargs='+', help='URL of an existed package')
    parser.add_argument('-l', '--list', type=argparse.FileType('r'), help='A file containing the videos URL (-l filename.txt)')
    args = parser.parse_args()

    if args.list is not None:
        vd_list = list(args.list)
        for pl in vd_list:
            k = pl.strip()
            download(k)
    elif args.list is None and args.url is not None:
        for i in args.url:
            k = i.strip()
            download(k)
    else:
        print("- You didn't pass any argument (help: python3 fbvid_downloader -h).")
