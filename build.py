#-*-coding:utf8;-*-
import json
from datetime import datetime

# Informasi kredit tentang kode
credit = {
    "updated": datetime.now().strftime("%Y%m%d %H:%I:%S"),
    "author": "guangrei",
    "link": "https://github.com/guangrei"}

# Membaca konten dari file "calendar.json" dan menguraikannya menjadi bentuk dictionary Python
with open("calendar.json", "r") as f:
    js = json.loads(f.read())

# Menghapus kunci "info" dari dictionary "js"
del js["info"]
out = {}


def get_holiday(des, sum):
    """
    Fungsi untuk mendapatkan hari libur dari deskripsi dan ringkasan yang diberikan.

    Parameters:
        des (list): Daftar deskripsi yang berisi kata "libur" atau tidak.
        sum (list): Daftar ringkasan hari yang sesuai dengan deskripsi.

    Returns:
        str: Ringkasan hari libur jika ditemukan, jika tidak kembali None.
    """
    i = 0
    for cek in des:
        if "libur" in cek.lower():
            return sum[i]
        else:
            i = i + 1


# Iterasi melalui setiap kunci dan nilai dalam dictionary "js"
for k, v in js.items():
    if v["holiday"]:
        out[k] = {}
        # Mendapatkan ringkasan hari libur menggunakan fungsi get_holiday
        out[k]["summary"] = get_holiday(v["description"], v["summary"])

# Menambahkan informasi kredit ke dictionary "out"
out["info"] = credit

# Mengkonversi dictionary "out" menjadi format JSON dan menyimpannya di file "holidays.json"
s = json.dumps(out, sort_keys=True)
with open("holidays.json", "w") as f:
    f.write(s)
