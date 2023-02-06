# DATA PREPARATION
adj = """ manis | tiap | jauh | ramah | keras | susah | lebih | cepat | mahir | punya | cukup | panas | demam |
 basah | saja | hanya | sendirian | tahu | suasana | tidak | sedih | kelihatan | rajin | putih | banyak |
 baru | besar | konsisten | luas | mahal | manis | nakal | pada | sakit | Senang | terakhir | tertinggi |
 sakit | khas | terpanjang | cinta | banyak | nasional | raya | baru | memesan | bakar | cantik | kaya | 
 Sombong | tinggi | baru | aktif | handal | nominal | besar"""

adv = """ sangat | paling | selalu | sering | jarang | setelah | kadang-kadang | sebelum | agak | sedang |
 sedikit | selama | sekadar | masih |  akan | dengan | jarang | kadang-kadang | oleh | sangat | sedang |
 selalu | sering | setelah | sudah | telah | sedang | sangat | paling | sedang | akan | sangat | baru"""

noun = """ tim | ternak | babi | guling | kue | mobil | gadis | kota | pekerjaan | rumah | baju | nasi |
 kecap | malam | warung | alat | sekolah | tempat | lagu | bola | motor | sore | kabar | saat | lampu |
 merah | taman | latihan | kawan-kawan | mainan | ibu | oleh-oleh | undangan | pasar | orang | bunga |
 sepak | bola | motor | kopi | saat | uang | siang | pesawat | tebu | latihan | air | obat | semangat |
 hari | drum | covid | pengalaman | acara | pejabat | negara | sebulan | gaji | minggu | ketua | osis |
 modal | boneka | skor | pertandingan | penentu | kemenangan | perbaikan | mengucapkan | perpisahan |
 pizza | mie | menghemat | pengeluaran | penonton | perlombaan | memeriahkan | sepak | bola | seminar |
 lomba | Adik | adik | adik-adik | air | air hujan | alat | Anak | Andi | anggota | anjing | atas | Ayah |
 Ayam | Ban | banteng | bibit | binatang | biru | buku | Burung | cantik | Dani | dapur | depan | desa |
 dinding | diskusi | dokter | DPR | dunia | gajah | gelas | gerobak | goreng | hakim | hewan | hutan |
 ibu | inspirasi | jam | jantan | jerapah | kakak | kakak | kakek | kayu | kebun | kecantikan | kecap |
 kehamilan | kemarin | kemarin | kepala | kepandaian | kertas | kewajiban | kucing | kue | lagu | makanan |
 malam | manusia | Meja | melata | Mobil | motor | narkoba | Nasi | nasi goreng | nasi goreng | Operasi |
 orang-orang | Padi | paman | pantai | pasar  | pecandu | pedagang | pelajar | pemburu | pemilihan | pencuri |
 peristirahatan | Persidangan | pesan | pokok | polisi | ponsel | rapat | restoran | Rotan | ruang | rumah |
 sampah | sapi | sate | Sayu | sayur-sayuran  | sebuah | secarik | sekolah | selama | semester | seorang |
 sepak bola | simbol | Singkong | sore | sumber  | tahun | Tani | tante | tebu | Televisi | teman |
 tempat | tidur | Tikus | timnas | tugas | tulis | tunangan | udang | Ular | usaha | usia | waktu | warung | pantai
 banyak | baru | besar | konsisten | luas | mahal | manis | nakal | pada | sakit | Senang | terakhir | tertinggi |
 programming | bola | ibu | sayur | dapur | makanan | pasar | kue | toko | ojek | online | sampah | lapangan |
 sayur | bayam | adik | obat | kakek | rumah | obat | apotek | sepeda | kota | bapak | tiket | liburan | negara |
 piala | dunia | paman | sungai | Universitas | provinsi | kota | pantai | danau | pulau | jurnal | planet |
 Yupiter | bukit | ibu | teluk | hijau | kuda | gunung | sungai | turis | lautan | teman | laut | lembah |
 selat | wilayah | barat | perahu | dayung | danau | hari | suci | Galungan | bulan | Januari | Senin |
 upacara | bendera | sumpah | pemuda | tanggal | Oktober | batik | nyepi | Maret | adik | guru | sekolah |
 Saraswati | pendidikan | Mei | perayaan | Natal | Desember | mobil | ayah | buku | air | hujan | sidang |
 skripsi | ruang | keluarga | makan | ikan | warung | kamar belajar | pagar | tanaman | Ibu | kilogram |
 gula | pasir | ekor | anjing | daging | sapi | penjual | ayam | puluh | potong | kambing | Idul Adha 
 Candi | abad | makanan | kotoran | air | putih | tubuh | kopi | Sepeda | perahu | kertas | Rumah | bukti |
 perjuangan | kerja | hati | Alat | kue | anggaran | pidato | pendengar | surat | air | penampilan | penonton |
 baju | tubuhmu |Ayah | nasi | Raja |wilayah | perlengkapan | orang | teman |laptop |pisang | gelas | minuman |
 buku | Nelayan | ikan | hutang | motor | masalah | solusi | organisasi | Perusahaan | sopir | manajer |
 Pemerintah | Ayah | atap | rumah | mobil | hukuman | rumus | ibu | baju | alumni | mahasiswa | program |
 pemandangan | alam | pesawat | bonsai | suami | istri | hotel | keputusan | hal | karyawan | kantor |
 Murid | Kelas | predikat | lagu | milik | berlian | beliau | langit | hadiah | adik | kucingnya |
 diskon | bibi | remaja | botol | plastik | permasalahan | paman | ketua | buah | mangga | tikus | kucing |
 hama | taman | kota | peraturan | lingkungan | pakaian | sepatu | roda | rendang | hutang | pengendali |
 piring | uang | tugas | teman - teman
"""

num = """ banyak | sebuah | setiap | dua | ribuan | satu | dua | seluruh | tiga | tiap | tiga | setiap | 28 | 2 | dua | seperempat | lima | satu | dua | sepuluh | enam | beberapa | seluruh | banyak | semua | tiga | seluruh """

prep = """ dengan | di | ke | dari | daripada | untuk | dalam | para | kepada | agar | di | dari | pada | di | ke | dari | tentang | pada | di | sebagai | dari"""

pronoun = """ aku | dia | saya | itu | mereka | kami | kita | ini | disana | kelasnya | saya | itu | dia | disana | mereka | Aku | ini | saya | kami | aku | itu | ini | itu | begini | begitu | saya | dia | kami | anda | kalian | mereka | tersebut | Dia | Mereka | Kami | itu | Saya | ini | -nya | mu | aku"""

prop_noun = """ Dodi | Kelvin | Putra | Kino | Tania | Budi | Andi | Sintia | Maysa | Saputra | Munir | Nesi | Rina |
 Septian | Toni | Rian | Suma | Tina | Jerome | Gideon | Argentina | Putu | Hitomi | Tono | Starbucks | Makoto |
 Nagano | Mount | Midoriyama | Ani | Dinda | Joni | Dinar | Pak | Asia Tenggara | Adi | Kuta | Putra | Dodi |
 Yanto | Budi | Wayan | Tasya | Andi | Tono | Pandu | Joko | Wawan | Diah | Doni | Yudi | Agus | Farrel | Bento |
 Jakarta | Singapura | Tokyo | Nursini | Bali | Palembang | Bekasi | Indonesia | Qatar | Rina | Surabaya |
 Amerika Selatan | Yuda | Denpasar | Udayana | Bali | Bandung | Tabanan | Yoga | Jembrana | Pandawa | Raka |
 Tamblingan | Jawa | Bromo | Kiran | Aere | Asia | Flores | Jesika | Kuta | Serin | Grand | Canyon | Sunda | Bisma |
 Toba | Dono | Toni | Andini | Liam | Dinda | Pak Salim | Adi | Putri | Dina | Deva | Odi | Dani |Andi | Santosa |
 Kampus | Garut | Tono |Anto | Indonesia | Saputra | Krisna | Rinaldi | Munir | Monika | Rafly | Universitas Udayana | Pande | Krisna | Qiqi | Pak Hendri | Andi | Carlos | Ariana | Justin | Kurama | Naruto | TBO | Saputra | Anita"""

verb = """ suka | memukul | memasak | memakai | berbelanja | goreng | memikirkan | membeli | bangun | menyanyikan | membawa | tulis | tidur | merapikan | bertengkar | mencuci | bermain | bertukar | menerobos | melakukan | pemanasan | pergi | berfoto | olahraga | tersenyum | membukukan | membelikan | menagih | menyelesaikan | memiliki | minum | butuh | menghasilkan | berfungsi | menurunkan | belajar | membutuhkan | membuat | bernyanyi | menghibur | dihadiri | bisa | menjadi | ikut | melihat | makan | menyapu | memesan | menaiki | menghadiri | mewakili | adalah | bangun | berkuliah | berkumpul | berkunjung | berkunjung | berselancar | bertemu | bertengkar | digigit | dipimpin | ditembak | dituliskan | melakukan | melihat | memakan | memasak  | memasak  | memasang | membawa | membeli | membuang | membuka | memelihara | memesan | memikirkan | memukau | menarik | mencari | mengabaikan | mengalah | mengambil | mengerjakan | menghuni | mengobati | menjadi | menjual | menyantap | menyanyikan | menyayangi | menyebabkan | merupakan | terasa | terbuat | Tertangkap | tertusuk | belajar | bermain | memasak | membeli | memesan | membuang | lari | makan | merawat | meminum | dirawat | lahir | pergi | berlibur | bekerja | menyukai | lahir | menonton | datang | terdapat | dilahirkan | terletak | mengunjungi | berasal | memancing | berasal | membaca | berfoto | menaiki | tenggelam | berada | bercerita | berjemur | terdapat | dilaksanakan | diperingati | memperingati | adalah | terkena | melakukan | makan malam | membuat | membeli | menjual | memelihara | berhasil | sembelih | mengeroyok | membawa | membersihkan | minum | memberikan | menggunakan | membuat | pergi | digunakan | membahas | memukau | mengalami | makan | minum | menjadi | tetap | mengambil | mengangkat | memesan | Bersama | goreng | menarik | banjir | memperbaiki | mencari | berselancar | memasang | diantar | meminjam | tinggal | menaiki | membicarakan | ada | membaca | menangkap | membayar | menggadaikan | membuat | menemukan | membenahi | membutuhkan | mencari | mengekspor | memperbaiki | mengendarai | menjalani | menulis | membantu | membelikan | adalah | menjadi | mengode | menggambar | bersatu | mendarat | berkebun | menjemput | menyayangi | bermalam | menghormati | terpandai | mempermasalahkan | mengalungkan | menawarkan | menghadiahkan | memberi | menjual | bertemu | memberi | mengajak | menyanyikan | memasak | membeli | menjual | membuat | dipetik | ditangkap | menangkap | pergi | dijinakan | menabung | mencuci | mengerjakan | memancing
"""

def remove_duplicat(arr): # Untuk menghilangkan duplicat lexicon
    fiks = []
    for i in arr:
        if i not in fiks:
            fiks.append(i)
    return fiks

adj = adj.split("|")
adv = adv.split("|")
noun = noun.split("|")
num = num.split("|")
prep = prep.split("|")
pronoun = pronoun.split("|")
prop_noun = prop_noun.split("|")
verb = verb.split("|")
print (adj)

def to_list(arr,lex):
    for i in range(len(arr)):
        x = arr[i].replace("\n","")
        a = x.replace(" ","")
        lex.append(a.lower())
    return lex

adj2,adv2,noun2,num2,prep2,pronoun2,prop_noun2,verb2 = [],[],[],[],[],[],[],[]

adj2 = remove_duplicat(to_list(adj,adj2))
adv2 = remove_duplicat(to_list(adv,adv2))
noun2 = remove_duplicat(to_list(noun,noun2))
num2 = remove_duplicat(to_list(num,num2))
prep2 = remove_duplicat(to_list(prep,prep2))
pronoun2 = remove_duplicat(to_list(pronoun,pronoun2))
prop_noun2 = remove_duplicat(to_list(prop_noun,prop_noun2))
verb2 = remove_duplicat(to_list(verb,verb2))



# write adj
with open(r'C:/Users/hp/OneDrive/Documents/Belajar Pemrograman/JAVA PBO/TBO/FP TBO/Real TBO Deva/word/adj.txt', 'w') as fp:
    for item in adj2:
        fp.write("%s\n" % item)
    print('Done')

# write adv
with open(r'C:/Users/hp/OneDrive/Documents/Belajar Pemrograman/JAVA PBO/TBO/FP TBO/Real TBO Deva/word/adv.txt', 'w') as fp:
    for item in adv2:
        fp.write("%s\n" % item)
    print('Done')

# write noun
with open(r'C:/Users/hp/OneDrive/Documents/Belajar Pemrograman/JAVA PBO/TBO/FP TBO/Real TBO Deva/word/noun.txt', 'w') as fp:
    for item in noun2:
        fp.write("%s\n" % item)
    print('Done')

# write num
with open(r'C:/Users/hp/OneDrive/Documents/Belajar Pemrograman/JAVA PBO/TBO/FP TBO/Real TBO Deva/word/num.txt', 'w') as fp:
    for item in num2:
        fp.write("%s\n" % item)
    print('Done')

# write prep
with open(r'C:/Users/hp/OneDrive/Documents/Belajar Pemrograman/JAVA PBO/TBO/FP TBO/Real TBO Deva/word/prep.txt', 'w') as fp:
    for item in prep2:
        fp.write("%s\n" % item)
    print('Done')

# write pronoun
with open(r'C:/Users/hp/OneDrive/Documents/Belajar Pemrograman/JAVA PBO/TBO/FP TBO/Real TBO Deva/word/pronoun.txt', 'w') as fp:
    for item in pronoun2:
        fp.write("%s\n" % item)
    print('Done')

# write prop_noun
with open(r'C:/Users/hp/OneDrive/Documents/Belajar Pemrograman/JAVA PBO/TBO/FP TBO/Real TBO Deva/word/prop_noun.txt', 'w') as fp:
    for item in prop_noun2:
        fp.write("%s\n" % item)
    print('Done')

# write verb
with open(r'C:/Users/hp/OneDrive/Documents/Belajar Pemrograman/JAVA PBO/TBO/FP TBO/Real TBO Deva/word/verb.txt', 'w') as fp:
    for item in verb2:
        fp.write("%s\n" % item)
    print('Done')