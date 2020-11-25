#! usr/bin/env python3
# Generated by Glenn Jocher (glenn.jocher@ultralytics.com) for https://github.com/ultralytics

import argparse
import os
import time
import json

from flickrapi import FlickrAPI

from utils.general import download_uri

# Get Flickr API key at https://www.flickr.com/services/apps/create/apply


# Size codes:


# decending size order
SIZES = ["url_o",   # o: Original (4520 x 3229)
         "url_k",   # k: Large 2048 (2048 x 1463)
         "url_h",   # h: Large 1600 (1600 x 1143)
         "url_l",   # l: Large 1024 (1024 x 732)
         "url_c",   # c: Medium 800 (800 x 572)
         "url_z",   # z: Medium 640 (640 x 457)
         "url_m",   # m: Medium 500 (500 x 357)
         "url_n",   # n: Small 320 (320 x 229)
         "url_s",   # s: Small 240 (240 x 171)
         "url_t",   # t: Thumbnail (100 x 71)
         "url_q",   # q: Square 150 (150 x 150)
         "url_sq",  # sq: Square 75 (75 x 75)
         ]


def get_largest_url(img):
    """ Get URL of Flickr image.
    Returns tuple of URL of largest available image, and associated size suffix
    """
    for size in SIZES:
        url = img.get(size)
        if url:
            return url, size.split('_')[1]


def get_size(img, suffix='o'):
    """ Get size of Flickr image. returns (w, h)"""
    w = img.get(f"width_{suffix}")
    h = img.get(f"height_{suffix}")
    return tuple(map(int, (w, h)))


def get_images(image_tag='honeybees on flowers', n_images=10):
    extras = ','.join(SIZES)
    flickr = FlickrAPI(API_KEY['key'], API_KEY['secret'])
    license = ()  # https://www.flickr.com/services/api/explore/?method=flickr.imgs.licenses.getInfo
    images = flickr.walk(text=image_tag,  # http://www.flickr.com/services/api/flickr.imgs.search.html
                         extras=extras,  # get urls for acceptable sizes
                         per_page=5,  # 1-500
                         license=license,
                         sort='relevance')
    return images


def get_urls(image_tag: str, n: int, minsize=0, verbose=False):
    """ Get list of `n` Flickr image URLs given a search term `image_tag` """
    images = get_images(image_tag)

    urls = []

    for img in images:
        if len(urls) < n:
            result = get_largest_url(img)
            if result:
                url, suffix = result
                size = get_size(img, suffix)
                if min(size) < minsize:
                    continue
                urls.append(url)
                if verbose:
                    fmt = f'0{len(str(n))}d'
                    print(f"{len(urls):{fmt}}/{n} {url}\t{size}")
            # If no url available for desired size try next img
        else:
            break
    return urls


def main(image_tag, n_images, out_dir, minsize, download=False, verbose=False):
    t = time.monotonic()

    # Get image urls
    urls = get_urls(image_tag, n_images, minsize, verbose=verbose)

    if download:
        os.makedirs(out_dir, exist_ok=True)
        for url in urls:
            download_uri(url, out_dir)

    print('Done. (%.1fs)' % (time.monotonic() - t)
          + ('\nAll images saved to %s' % out_dir if download else ''))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('key', type=argparse.FileType('r'), help='Flickr API key JSON file')
    parser.add_argument('--search', type=str, default='honeybees on flowers', help='flickr search term')
    parser.add_argument('--n', type=int, default=10, help='number of images')
    parser.add_argument('--download', action='store_true', help='download images')
    parser.add_argument('--out_dir', help="output directory", default=None)
    parser.add_argument('--originals', action='store_true', help="force original sizes only")
    parser.add_argument('--minsize', type=int, default=1024, help="minimum image dimension")
    parser.add_argument('-v', '--verbose', action='store_true', help="print fetched URIs")
    args = parser.parse_args()

    if not args.download and args.out_dir:
        raise UserWarning("out_dir allocated without specifying download." 
                          " To download images use `--download`")
    # default search directory: `./images/search_terms_used/`
    if not args.out_dir:
        args.out_dir = os.path.join(os.getcwd(), 'images', args.search.replace(' ', '_'))

    if args.originals:
        SIZES = 'url_o'

    # Parse API Key
    API_KEY = json.load(args.key)

    main(image_tag=args.search,  # search term
         n_images=args.n,  # max number of images
         minsize=args.minsize,
         out_dir=args.out_dir,
         download=args.download,
         verbose=args.verbose)
