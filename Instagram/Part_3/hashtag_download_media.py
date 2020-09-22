import requests

count = 0
end_cursor = ''
while True:

    hashtag = input('Silakan masukkan hashtag:')
    url1 = 'https://www.instagram.com/explore/tags/{}/?__a=1'.format(hashtag)
    r1 = requests.get(url1).json()
    shortcodes = r1['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    for sc in shortcodes:
        shortcode = sc['node']['shortcode']
        url2 = 'https://www.instagram.com/p/{}/?__a=1'.format(shortcode)
        r2 = requests.get(url2).json()
        username = r2['graphql']['shortcode_media']['owner']['full_name']
        count = count + 1
        file_name_image = '{} {}.jpg'.format(count, username)
        file_name_video = '{} {}.mp4'.format(count, username)
        path_image = 'media_download/{}'.format(file_name_image)
        path_video = 'media_download/{}'.format(file_name_video)
        url_media_image = r2['graphql']['shortcode_media']['display_url']

        is_video = r2['graphql']['shortcode_media']['is_video']
        if is_video:
            url_media_video = r2['graphql']['shortcode_media']['video_url']
            r_url_media_video = requests.get(url_media_video).content
            open(path_video, 'wb').write(r_url_media_video)
        if not is_video:
            r_url_media_image = requests.get(url_media_image).content
            open(path_image, 'wb').write(r_url_media_image)
        print(count, shortcode)
    end_cursor = r1['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
    has_next_page = r1['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
    if not has_next_page:
        break
