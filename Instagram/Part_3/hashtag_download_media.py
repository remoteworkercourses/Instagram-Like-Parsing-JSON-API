import requests

count = 0
end_cursor = ''
while True:

    url1 = 'https://www.instagram.com/explore/tags/bangbewokchannel/?__a=1'
    r1 = requests.get(url1).json()
    shortcodes = r1['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    for sc in shortcodes:
        shortcode = sc['node']['shortcode']
        url2 = 'https://www.instagram.com/p/{}/?__a=1'.format(shortcode)
        r2 = requests.get(url2).json()
        username = r2['graphql']['shortcode_media']['owner']['full_name']
        count = count + 1
        print(count, username)

    end_cursor = r1['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
    has_next_page = r1['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
    if not has_next_page:
        break
