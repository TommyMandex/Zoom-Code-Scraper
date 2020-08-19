import os
import requests

os.system('cls && title [Zoom Code Scraper]')
scraped = 0


def save(text):
    print(text)
    with open('Codes.txt', 'a', encoding='UTF-8', errors='replace') as f:
        f.write(f'{text}\n')


response = requests.get(
    'https://api.twitter.com/2/search/adaptive.json?include_profile_interstitial_type=1&include_blo'
    'cking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1'
    '&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&'
    'include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&i'
    'nclude_entities=true&include_user_entities=true&include_ext_media_color=true&include_ext_media'
    '_availability=true&send_error_codes=true&simple_quoted_tweet=true&q=zoom%20code&tweet_search_m'
    'ode=live&count=20&query_source=typed_query&pc=1&spelling_corrections=1&ext=mediaStats%2Chighli'
    'ghtedLabel', headers={
        'x-twitter-client-language': 'sv',
        'x-csrf-token': 'f6ef58dbf184bb29c103e991b96c367c',
        'x-guest-token': '1296027737430384642',
        'x-twitter-active-user': 'yes',
        'accept': '*/*',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7'
                         'ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Ge'
                      'cko) Chrome/84.0.4147.125 Safari/537.36',
        'cookie': 'personalization_id="v1_rWHKZ735+1UccKsJ11w0cQ=="; guest_id=v1%3A1595721308692096'
                  '22; _ga=GA1.2.1409403259.1595721311; eu_cn=1; tfw_exp=0; external_referer=8e8t2x'
                  'd8A2w%3D|0|4abf247TNXg4Rylyqt4v49u2LWyy1%2FaFyfd602NkflM%3D; _gid=GA1.2.19129875'
                  '46.1597783066; ct0=f6ef58dbf184bb29c103e991b96c367c; gt=1296027737430384642'
    }
)

try:
    for tweet in response.json()['globalObjects']['tweets'].values():
        content = tweet['full_text']
        if any(i in content for i in ['pass', 'code', 'raid', 'join']) and '@' not in content:
            save(
                '[POSSIBLE]\n'
                f'{content}\n'
                '----------------------------------'
            )
            scraped += 1

        try:
            url = tweet['entities']['urls'][0]['expanded_url']
        except Exception:
            continue
        if 'us04web.zoom.us' in url and '?pwd=' in url:
            save(
                '[URL]\n'
                f'{url}\n'
                '----------------------------------'
            )
            scraped += 1
        elif 'us04web.zoom.us' in url and '?pwd=' not in url:
            save(
                '[URL AND TEXT]\n'
                f'URL: {url}\n'
                f'TEXT: {content}\n'
                '----------------------------------'
            )
            scraped += 1
except KeyError:
    print('Outdated cookies.')

os.system(f'title [Zoom Code Scraper] - Scraped: {scraped} && pause >NUL')
