# Facebook Video Downloader (Outdated)

**NOTE: As of a Facebook update that occurred within two weeks after the publication of this tool, it is no longer functioning correctly. I'm currently not maintaining this tool, so please be aware that the code provided here is outdated and not working.**

# Setup and Usage

- Setup:

```
git clone https://github.com/0xWise64/fbvid_downloader && cd fbvid_downloader/ && pip install -r requirements.txt
```

- Usage:

```
python3 fbvid_downloader.py -u https://www.facebook.com/groups/145845244080791/posts/303579131640734/
```

*Download multiple videos by passing more than one video URL:*

```
python3 fbvid_downloader.py -u https://www.facebook.com/groups/145845244080791/posts/303579131640734/ https://www.facebook.com/100074017523741/videos/1082925655809010/
```

![Screenshot 2021-12-03 123241](https://user-images.githubusercontent.com/54465159/144588134-57dcab7d-58e3-4360-b53d-c19d9d60c406.png)

*Download a list of videos:*

```
python3 fbvid_downloader.py -l fileofurls.txt
```
