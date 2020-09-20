import json
import requests
import time
import csv

url = 'https://www.instagram.com/graphql/query'

url_postingan = input('Silakan masukkan url postingan:')
kursor_terakhir = ''
hitung = 0
penghitung_file = 0
jumlah_per_file = 50

while 1:
    variabel = {
        "shortcode": url_postingan,
        "first": jumlah_per_file,
        'after': kursor_terakhir
    }

    parameter = {
        'query_hash': 'bc3296d1ce80a24b1b6e40b1e72903f5',
        'variables': json.dumps(variabel)
    }
    r = requests.get(url, params=parameter).json()
    try:
        komentator_komentator = r['data']['shortcode_media']['edge_media_to_parent_comment']['edges']
    except:
        print('Tunggu 20 detik')
        time.sleep(30)
        continue

    #    for komentator in komentator_komentator:
    #        nama_komentator = komentator['node']['owner']['username']
    #        komentar = komentator['node']['text']
    #        print(nama_komentator, '=', komentar)
    for komentator in komentator_komentator:
        if hitung % jumlah_per_file == 0 and penghitung_file != 'Azriel':
            penghitung_file = penghitung_file + 1
            pengekstrak_csv = csv.writer(
                open('hasil_komen/{} {}.csv'.format(url_postingan, penghitung_file), 'w', newline=''))
            judul_csv = ['Nama Komentator', 'komentar']
            pengekstrak_csv.writerow(judul_csv)

        nama_komentator = komentator['node']['owner']['username']
        komentar = komentator['node']['text']
        hitung = hitung + 1

        print(hitung, nama_komentator, komentar)
        pengekstrak_csv = csv.writer(
            open('hasil_komen/{} {}.csv'.format(url_postingan, penghitung_file), 'a', newline='', encoding='utf-8'))
        data = [nama_komentator, komentar]
        pengekstrak_csv.writerow(data)

    kursor_terakhir = r['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['end_cursor']
    halaman_terakhir = r['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['has_next_page']

    if not halaman_terakhir:
        break
    time.sleep(2)
