import time

def header():
    print("="*25)
    print("Web Scraper - v1.0.2")

def option_command():
    print("="*25)
    print("1) Update Harga")
    print("2) Close Produk")
    print("3) Open Produk")
    print("="*25)

def option_url():
    print("="*25)
    print("1) Tele H2h")
    print("2) Tele Chandra")
    print("3) Tele Dana")
    print("="*25)

def footer():
    print("Done!")
    for a in ['See', 'You', 'Again']:
        print(a, end=' ')
        time.sleep(1)