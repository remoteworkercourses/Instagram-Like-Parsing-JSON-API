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

# pengekstrak_csv = csv.writer(open('hasil_like/{} {}.csv'.format(url_postingan, penghitung_file), 'w', newline=''))
# judul_csv = ['Nama Pengguna', 'Nama Panjang', 'Foto Profil']
# pengekstrak_csv.writerow(judul_csv)

while 1:
    variabel = {
        "shortcode": url_postingan,
        "first": jumlah_per_file,
        'after': kursor_terakhir
    }

    parameter = {
        'query_hash': 'd5d763b1e2acf209d62d22d184488e57',
        'variables': json.dumps(variabel)
    }

    r = requests.get(url, params=parameter).json()

    try:
        para_pengguna = r['data']['shortcode_media']['edge_liked_by']['edges']
    except:
        print('Tunggu 20 detik')
        time.sleep(30)
        continue

    for pengguna in para_pengguna:

        if hitung % jumlah_per_file == 0 and penghitung_file != 'Azriel':
            penghitung_file = penghitung_file + 1
            pengekstrak_csv = csv.writer(
                open('hasil_like/{} {}.csv'.format(url_postingan, penghitung_file), 'w', newline=''))
            judul_csv = ['Nama Pengguna', 'Nama Panjang', 'Foto Profil']
            pengekstrak_csv.writerow(judul_csv)

        nama_pengguna = pengguna['node']['username']
        nama_panjang = pengguna['node']['full_name']
        foto_profil = pengguna['node']['profile_pic_url']
        hitung = hitung + 1

        print(hitung, nama_pengguna, nama_panjang, foto_profil)
        pengekstrak_csv = csv.writer(
            open('hasil_like/{} {}.csv'.format(url_postingan, penghitung_file), 'a', newline='', encoding='utf-8'))
        data = [nama_pengguna, nama_panjang, foto_profil]
        pengekstrak_csv.writerow(data)

    kursor_terakhir = r['data']['shortcode_media']['edge_liked_by']['page_info']['end_cursor']
    halaman_terakhir = r['data']['shortcode_media']['edge_liked_by']['page_info']['has_next_page']

    if not halaman_terakhir:
        break
    time.sleep(2)
