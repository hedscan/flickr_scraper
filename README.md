# Flickr Scraper - Fork Info :fork_and_knife:

This fork is maintained by Gethin Davies, and optimised for scraping of images for use as training data for generative adversarial networks.

## Changes :recycle:

- `--minsize`, `--originals` and `--out_dir` options added to `flickr_scraper.py`

- Pass FlickrAPI JSON as positional argument to `flickr_scraper.py`

## ReadMe

<img src="https://storage.googleapis.com/ultralytics/logo/logoname1000.png" width="160">

### Introduction

This directory contains Flickr image-scraping software developed by Ultralytics LLC, and **is freely available for redistribution under the GPL-3.0 license**. For more information please visit https://www.ultralytics.com.

### Requirements

Python 3.7.x or 3.8.x with all of the `pip install -U -r requirements.txt` packages including:

- `flickrapi`

### Install
```bash
$ git clone https://github.com/hedscan/flickr_scraper
$ cd flickr_scraper
$ pip install -U -r requirements.txt
```

### Use

1. Request a Flickr API key: <https://www.flickr.com/services/apps/create/apply>

2. Store your API key and secret in a JSON file:

```json
{
    "key": "456787687234hjksvb8427679",
    "secret": "dabadeedabadai"
}
```

3. Search for up to `n` images, optionally filtering by minimum image size with `--minsize`. If `-v` flag passed, URLs and corresponding image sizes (width, height) are printed to screen. Using `--download` images are downloaded and by default saved to `flickr_scraper/images`, however an alternative can be given using the `--out_dir` option. Note that image downloads may be subject to Flickr rate limits and other limitations. See https://www.flickr.com/services/developer/api/ for full information.

```bash
$ python3 flickr_scraper.py path/to/my_key.json --search 'honeybees on flowers' --n 10 --download --minsize 1024

01/10 https://live.staticflickr.com/8360/8437557091_c3b0a08e7d_o.jpg    (2415, 1610)
02/10 https://live.staticflickr.com/6149/6200906487_4623a60953_o.jpg    (3088, 2056)
03/10 https://live.staticflickr.com/6020/6012016425_c581da286e_o.jpg    (2420, 1617)
04/10 https://live.staticflickr.com/1750/28554413088_66a7356f87_o.jpg   (2966, 2591)
05/10 https://live.staticflickr.com/1441/23600354234_ac2ddb1554_k.jpg   (2048, 1365)
06/10 https://live.staticflickr.com/5337/9545156380_b5ac1bf6a7_o.jpg    (4912, 3264)
07/10 https://live.staticflickr.com/8159/7103042537_735b617109_k.jpg    (2048, 1365)
08/10 https://live.staticflickr.com/4017/4525284074_173a29272e_h.jpg    (1302, 1600)
09/10 https://live.staticflickr.com/962/28098876898_e355bb853e_o.jpg    (3031, 2660)
10/10 https://live.staticflickr.com/3868/14704899756_7d997770a7_k.jpg   (2048, 1362)
Done. (7.6s)
All images saved to /Users/glennjocher/PycharmProjects/flickr_scraper/images/honeybees_on_flowers/
```

<img src="https://user-images.githubusercontent.com/26833433/75074332-4792c600-54b0-11ea-8c98-22acf58ba8e7.jpg" width="">

### Cite

[![DOI](https://zenodo.org/badge/242235660.svg)](https://zenodo.org/badge/latestdoi/242235660)

### Contact

**Issues should be raised directly in the repository.** For additional questions or comments please email Glenn Jocher at glenn.jocher@ultralytics.com or visit us at <https://contact.ultralytics.com>.
