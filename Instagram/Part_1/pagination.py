import json
import requests
import time

url = 'https://www.instagram.com/graphql/query'

url_postingan = input('Silakan masukkan url postingan:')

kursor_terakhir = ''

hitung = 0

while 1:
    variabel = {
        "shortcode": url_postingan,
        "first": 50,
        'after': kursor_terakhir
    }

    parameter = {
        'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
        'variables': json.dumps(variabel)
    }

    r = requests.get(url, params=parameter).json()

    para_pengguna = r['data']['shortcode_media']['edge_liked_by']['edges']

    for pengguna in para_pengguna:
        nama_pengguna = pengguna['node']['username']
        nama_panjang = pengguna['node']['full_name']
        foto_profil = pengguna['node']['profile_pic_url']
        #    print(nama_pengguna)
        #    print(nama_panjang)
        hitung = hitung + 1
        print(hitung, nama_pengguna, '=', nama_panjang)

    kursor_terakhir = r['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    halaman_terakhir = r['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']
    if halaman_terakhir == False:
        break
    time.sleep(2)