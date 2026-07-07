# =========================================
# ONION DISEASE KNOWLEDGE BASE
# =========================================
# SOURCE REFERENCES
# =========================================
# Knowledge base ini disusun berdasarkan:
#
# 1. Journal of Plant Pathology
# 2. Plant Disease Journal
# 3. Journal of Agricultural Science
# 4. Jurnal Hortikultura Indonesia
# 5. Crop Protection Journal
# 6. Frontiers in Plant Science
# 7. International Journal of Pest Management
# 8. Balai Penelitian Tanaman Sayuran
# 9. Kementerian Pertanian Republik Indonesia
# 10. Journal of Plant Protection Research
# 11. Agricultural Extension Service References
# 12. Journal of Plant Diseases and Protection
#
# Tujuan:
# Memberikan penjelasan AI yang mudah dipahami
# petani bawang merah Indonesia.
# =========================================


DISEASE_INFO = {

    # =====================================
    # ALTERNARIA
    # =====================================

    "Alternaria_D": {

        "display_name":
        "Penyakit Alternaria (Alternaria Disease)",

        "scientific_name":
        "Alternaria porri",

        "cause":
        "Penyakit ini disebabkan oleh jamur Alternaria porri yang berkembang pada kondisi lembap, curah hujan tinggi, dan sirkulasi udara buruk.",

        "symptoms":
        "Gejala awal berupa bercak kecil putih atau coklat muda yang kemudian berubah menjadi bercak ungu kehitaman memanjang pada daun bawang.",

        "impact":
        "Infeksi berat dapat menyebabkan daun mengering, menghambat pertumbuhan tanaman, dan menurunkan hasil panen hingga lebih dari 50 persen.",

        "prevention":
        "Gunakan bibit sehat, hindari kelembapan berlebih, lakukan rotasi tanaman, dan jaga jarak tanam agar sirkulasi udara tetap baik.",

        "solution":
        "Lakukan pemangkasan daun yang terinfeksi dan gunakan fungisida secara berkala sesuai dosis anjuran.",

        "pesticide":
        "Dithane M-45, Antracol 70 WP, Score 250 EC",

        "active_ingredient":
        "Mancozeb, Propineb, Difenoconazole",

        "usage":
        "Semprotkan fungisida setiap 5 sampai 7 hari sekali pada pagi atau sore hari sesuai petunjuk kemasan.",

        "risk":
        "Sedang - Tinggi",

        "notes":
        "Penyakit berkembang sangat cepat pada musim hujan dan kelembapan tinggi."

    },



    # =====================================
    # CATERPILLAR
    # =====================================

    "Caterpillar-P": {

        "display_name":
        "Hama Ulat Daun (Caterpillar Pest)",

        "scientific_name":
        "Spodoptera exigua",

        "cause":
        "Disebabkan oleh serangan ulat grayak yang memakan jaringan daun bawang merah.",

        "symptoms":
        "Daun berlubang, sobek, dan terlihat bekas gigitan terutama pada malam hari.",

        "impact":
        "Serangan berat dapat menghambat proses fotosintesis dan menyebabkan gagal panen.",

        "prevention":
        "Lakukan monitoring rutin, bersihkan gulma di sekitar lahan, dan gunakan perangkap hama.",

        "solution":
        "Gunakan insektisida sesuai dosis dan lakukan pengendalian hama secara terpadu.",

        "pesticide":
        "Prevathon, Curacron 500 EC, Decis 25 EC",

        "active_ingredient":
        "Klorantraniliprol, Profenofos, Deltamethrin",

        "usage":
        "Semprotkan pada daun yang terserang setiap 5 hari sekali jika populasi ulat meningkat.",

        "risk":
        "Tinggi",

        "notes":
        "Hama lebih aktif menyerang pada malam hari."

    },



    # =====================================
    # FUSARIUM
    # =====================================

    "Fusarium-D": {

        "display_name":
        "Layu Fusarium (Fusarium Wilt)",

        "scientific_name":
        "Fusarium oxysporum",

        "cause":
        "Disebabkan oleh jamur Fusarium oxysporum yang menyerang akar dan pembuluh tanaman.",

        "symptoms":
        "Daun menguning, tanaman layu, akar membusuk, dan pertumbuhan tanaman melambat.",

        "impact":
        "Penyakit dapat menyebabkan kematian tanaman secara bertahap dan kerugian besar pada hasil panen.",

        "prevention":
        "Gunakan media tanam steril dan hindari genangan air di area budidaya.",

        "solution":
        "Cabut tanaman yang terinfeksi dan gunakan fungisida sistemik.",

        "pesticide":
        "Nativo 75 WG, Benlate, Topsin M",

        "active_ingredient":
        "Trifloxystrobin, Benomyl, Thiophanate-methyl",

        "usage":
        "Semprotkan atau siram pada area akar sesuai dosis yang tertera pada kemasan.",

        "risk":
        "Tinggi",

        "notes":
        "Jamur dapat bertahan lama di dalam tanah."

    },



    # =====================================
    # HEALTHY
    # =====================================

    "Healthy leaves": {

        "display_name":
        "Tanaman Sehat (Healthy Leaves)",

        "scientific_name":
        "Healthy Condition",

        "cause":
        "Tanaman berada dalam kondisi sehat dan tidak menunjukkan gejala penyakit maupun serangan hama.",

        "symptoms":
        "Daun hijau segar, tegak, tidak terdapat bercak, dan pertumbuhan normal.",

        "impact":
        "Tanaman memiliki potensi pertumbuhan dan hasil panen optimal.",

        "prevention":
        "Lanjutkan perawatan rutin dan lakukan monitoring berkala untuk mencegah penyakit.",

        "solution":
        "Pertahankan pola pemupukan dan penyiraman yang seimbang.",

        "pesticide":
        "Tidak diperlukan",

        "active_ingredient":
        "-",

        "usage":
        "Lakukan pemantauan rutin terhadap kondisi daun dan lingkungan.",

        "risk":
        "Rendah",

        "notes":
        "Kondisi tanaman sangat baik."

    },



    # =====================================
    # IRIS YELLOW VIRUS
    # =====================================

    "Iris yellow virus_augment": {

        "display_name":
        "Virus Kuning Iris (Iris Yellow Virus)",

        "scientific_name":
        "Iris Yellow Spot Virus (IYSV)",

        "cause":
        "Disebabkan oleh infeksi virus yang ditularkan oleh serangga thrips pada tanaman bawang.",

        "symptoms":
        "Daun menguning, muncul bercak pucat memanjang, dan pertumbuhan tanaman melemah.",

        "impact":
        "Menurunkan kualitas dan kuantitas hasil panen bawang merah.",

        "prevention":
        "Gunakan bibit bebas virus dan lakukan pengendalian serangga pembawa virus.",

        "solution":
        "Cabut tanaman yang terinfeksi dan kendalikan populasi thrips secara rutin.",

        "pesticide":
        "Abacel, Confidor, Curacron",

        "active_ingredient":
        "Abamectin, Imidacloprid, Profenofos",

        "usage":
        "Semprotkan insektisida untuk mengendalikan thrips setiap 5 hari sekali.",

        "risk":
        "Sedang - Tinggi",

        "notes":
        "Virus tidak dapat disembuhkan tetapi penyebarannya dapat dicegah."

    },



    # =====================================
    # PURPLE BLOTCH
    # =====================================

    "Purple blotch": {

        "display_name":
        "Bercak Ungu (Purple Blotch)",

        "scientific_name":
        "Alternaria porri",

        "cause":
        "Disebabkan oleh infeksi jamur Alternaria porri pada daun bawang merah.",

        "symptoms":
        "Muncul bercak ungu memanjang dengan tepi kekuningan pada daun bawang.",

        "impact":
        "Mengurangi kemampuan fotosintesis dan menurunkan hasil panen secara signifikan.",

        "prevention":
        "Hindari kelembapan tinggi, lakukan sanitasi lahan, dan gunakan bibit sehat.",

        "solution":
        "Gunakan fungisida kontak dan sistemik secara bergantian untuk mencegah resistensi jamur.",

        "pesticide":
        "Dithane M-45, Cabrio Top, Amistar Top",

        "active_ingredient":
        "Mancozeb, Pyraclostrobin, Azoxystrobin",

        "usage":
        "Semprotkan fungisida setiap 5 sampai 7 hari sesuai tingkat serangan penyakit.",

        "risk":
        "Sedang",

        "notes":
        "Penyakit lebih cepat berkembang pada musim hujan."

    },



    # =====================================
    # VIROSIS
    # =====================================

    "Virosis-D": {

        "display_name":
        "Penyakit Virosis (Virosis Disease)",

        "scientific_name":
        "Onion Virus Complex",

        "cause":
        "Disebabkan oleh infeksi virus yang menyebar melalui serangga pembawa virus.",

        "symptoms":
        "Daun keriting, warna pucat, dan pertumbuhan tanaman tidak normal.",

        "impact":
        "Produksi bawang merah dapat menurun drastis jika tidak segera ditangani.",

        "prevention":
        "Gunakan bibit sehat dan kendalikan serangga pembawa virus.",

        "solution":
        "Cabut tanaman yang sakit dan semprot insektisida untuk mengendalikan vektor virus.",

        "pesticide":
        "Confidor, Pegasus, Marshal",

        "active_ingredient":
        "Imidacloprid, Diafenthiuron, Carbofuran",

        "usage":
        "Gunakan sesuai dosis pada label untuk pengendalian serangga pembawa virus.",

        "risk":
        "Tinggi",

        "notes":
        "Virus dapat menyebar sangat cepat pada lahan yang tidak terkontrol."

    },



    # =====================================
    # STEMPHYLIUM
    # =====================================

    "Stemphylium Leaf Blight": {

        "display_name":
        "Busuk Daun Stemphylium (Stemphylium Leaf Blight)",

        "scientific_name":
        "Stemphylium vesicarium",

        "cause":
        "Disebabkan oleh jamur Stemphylium vesicarium.",

        "symptoms":
        "Daun mengalami bercak coklat kekuningan dan mengering dari ujung daun.",

        "impact":
        "Menurunkan kualitas daun dan hasil produksi bawang merah.",

        "prevention":
        "Jaga sanitasi lahan dan hindari kelembapan berlebih pada area budidaya.",

        "solution":
        "Gunakan fungisida preventif dan kuratif secara berkala.",

        "pesticide":
        "Antracol, Nativo, Score",

        "active_ingredient":
        "Propineb, Trifloxystrobin, Difenoconazole",

        "usage":
        "Semprotkan fungisida setiap 7 hari sekali pada area terserang.",

        "risk":
        "Sedang",

        "notes":
        "Penyakit mudah berkembang pada suhu hangat dan lembap."

    }

}

