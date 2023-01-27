{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Dlz3iy7U1xQ4"
   },
   "source": [
    "# **Exercise 3 Python**\n",
    "\n",
    "Python Course - Sekolah Data - Pacmann Academy\n",
    "\n",
    "Materi yang diujikan pada exercise ini adalah\n",
    "1. Object Oriented Programming I\n",
    "2. Object Oriented Programming II\n",
    "3. Error, Debug, and Clean Code\n",
    "4. Git (dalam bentuk PPT)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "spLuOvCg4rXi"
   },
   "source": [
    "# **Object Oriented Programming I**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "V3dj4uFU_PwE"
   },
   "source": [
    "## Case 1 : Arsip Toko Buku\n",
    "Membuat program arsip sederhana yang menyimpan beberapa atribut tentang detail buku yang ada.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "KcGm4mPiAZfK"
   },
   "source": [
    "###1A.\n",
    "\n",
    "1. Buatlah kelas Buku dengan atribut berikut: `judul`, `penulis` (Nama lengkap).\n",
    "2. Tentukan attribute yang digunakan untuk menginisialisasi atribut metode dengan nilai yang dimasukkan oleh pengguna.\n",
    "3. Atur metode view() untuk menampilkan informasi buku saat ini.\n",
    "4. Tulis program untuk menguji kelas Buku."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "skbKqV4s9s5U",
    "outputId": "4625ff5b-7f7a-4753-eade-e5a56b4b74e0"
   },
   "outputs": [],
   "source": [
    "# isi titik - titik di bawah ini\n",
    "class Buku:\n",
    "    def __init__(self,judul,penulis):\n",
    "        self.judul=judul\n",
    "        self.penulis=penulis\n",
    "        self.harga=50_000\n",
    "        \n",
    "    def view(self):\n",
    "        return f'Judul Buku: {self.judul} the Hardway, Penulis: {self.penulis}'\n",
    "              \n",
    "buku1 = Buku('Learn Python the Hardway', 'Zed Shaw')\n",
    "buku2 = Buku('Confessions', 'Kanae Minato')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Judul Buku: Learn Python the Hardway the Hardway, Penulis: Zed Shaw'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(buku1.view())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Judul Buku: Confessions the Hardway, Penulis: Kanae Minato'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "(buku2.view())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "hfHOCVNF7AyO"
   },
   "source": [
    "###1B.\n",
    "Melanjutkan program diatas, tambahkan atribut ``harga`` dan berikan nilai ``Rp. 50K``"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "pm2UbEmPCAVL",
    "outputId": "af0f7be7-9156-4025-c0d1-1e42c05488ee"
   },
   "outputs": [],
   "source": [
    "# isi titik - titik di bawah ini\n",
    "..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "46Z1NYAj_dr5"
   },
   "source": [
    "## Case 2 : Siapa yang Lebih Tua?\n",
    "Membuat Program sederhana yang dapat menentukan siapa yang lebih tua berdasarkan atribut umur.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "D7gRxFFoHuAY"
   },
   "source": [
    "###2A\n",
    "Buatlah class dengan nama ``Person`` yang memiliki atribut berupa ``nama`` dan ``umur``. Kemudian buatlah sebuah method di dalam class tersebut yang membangdingkan usia dari sebuah objek dengan objek lainnya. Cetak hasil perbandingan tersebut ke dalam sebuah kalimat dengan format :\n",
    "\n",
    "```\n",
    "{other_person}{lebih tua dari / lebih muda dari / seumuran dengan} saya. \n",
    "\n",
    "contoh: \n",
    "\n",
    "p1 = Person(\"Ansar\", 24)\n",
    "\n",
    "p2 = Person(\"Tamam\", 36)\n",
    "\n",
    "\n",
    "test:\n",
    "\n",
    "p1.perbandingan_umur(p2) ➞ 'Tamam lebih tua dari saya.'\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "XNhnmPOhIINM",
    "outputId": "7b71f789-3772-41a0-d9ca-36f0b54a964c"
   },
   "outputs": [],
   "source": [
    "# isi titik - titik di bawah ini\n",
    "..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "PJlC80AOHrzA"
   },
   "source": [
    "###2B.\n",
    "Kemudian tambahkan instance lain untuk untuk menambahkan perbandingan \n",
    "```\n",
    "contoh: \n",
    "\n",
    "p3 = Person(\"Zul\", 24)\n",
    "\n",
    "p4 = Person(\"Yusril\", 22)\n",
    "\n",
    "p5 = Person(\"Ayub\", 26)\n",
    "\n",
    "test:\n",
    "\n",
    "p2.perbandingan_umur(p1)\n",
    "\n",
    "p1.perbandingan_umur(p3)\n",
    "\n",
    "p3.perbandingan_umur(p5)\n",
    "\n",
    "p5.perbandingan_umur(p4)\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "OuFN5Td9LPDk",
    "outputId": "ede07622-54fe-4e54-a05b-aa2dd3bb40e4"
   },
   "outputs": [],
   "source": [
    "# isi titik - titik di bawah ini\n",
    "..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "veJWggd7OIzy"
   },
   "source": [
    "## Case 3 : Menghitung Bangun Ruang Bola\n",
    "Membuat program sederhana yang dapat menghitung volume dan luas permukaan bangun ruang bola"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "H2pF93ryOK9s"
   },
   "source": [
    "###3A.\n",
    "Buatlah class dengan nama *Bola* yang memiliki atribut instance radius dan memiliki dua method, yaitu *volume* untuk menghitung volume bola dan juga method *luas_permukaan* untuk menghitung besar luas permukaan bola.\n",
    "\n",
    "```\n",
    "4/3 * self.PI * (self.radius**3)\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "90bLG1plY6t9",
    "outputId": "091671a4-52e3-4b79-bc6c-e9ef3203d1e1"
   },
   "outputs": [],
   "source": [
    "# isi titik - titik di bawah ini\n",
    "..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "HSOHiG2pY5br"
   },
   "source": [
    "###3B.\n",
    "Melanjutkan program diatas, tambahkan method untuk menghitung luas permukaan bola\n",
    "\n",
    "```\n",
    "4 * self.PI * self.radius**2\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "WJ_zNd9kauPP",
    "outputId": "bb18e5d7-8457-4f69-f41f-84cadd614d4d"
   },
   "outputs": [],
   "source": [
    "# isi titik - titik di bawah ini\n",
    "..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "I_iLmPAeeDKv"
   },
   "source": [
    "## Case 4 : Menghitung Bangun Datar\n",
    "Membuat program sederhana untuk menghitung luas dan keliling bangun datar.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "TEy3LNv_yaqC"
   },
   "source": [
    "###4A.\n",
    "Bualtah sebuah class dengan nama *Lingkaran* yang memiliki instance variable *radius*. Class ini memiliki method untuk menghitung luas area dan keliling dari lingkaran.`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "R7R_dNq9mocQ",
    "outputId": "d4abb826-bf46-42d4-b6a9-b40ca8478773"
   },
   "outputs": [],
   "source": [
    "# isi titik - titik di bawah ini\n",
    "..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "VvceCGBinP8g"
   },
   "source": [
    "###4B\n",
    "Buatlah program yang serupa dengan program diatas, tapi untuk menghitung luas dan keliling dari bangun persegi"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "B1Q0bp9eo4u2",
    "outputId": "588bdb40-0e1c-4d00-e500-428612929619"
   },
   "outputs": [],
   "source": [
    "# isi titik - titik di bawah ini\n",
    "..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "dpTOfUkHF9sV"
   },
   "source": [
    "# **Object Oriented Programming II**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "GS_G8-qeGGnt"
   },
   "source": [
    "## Case 1 : Jenis Kendaraan beserta Bahan Bakarnya\n",
    "Membuat Program sederhana yang menyimpan merk dan model sebuah kendaraan beserta bahan bakar yang digunakan.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "SypbtqP9GGnu"
   },
   "source": [
    "###1A\n",
    "- Buat class ``Vehicle`` yang memiliki atribut ``brand, model``, dan default value atribute ``fuel=\"gas\"``\n",
    "- Buat child class ``Car`` yang menggunakan fungsi super() agar bisa mewarisi semua method dan properti dari parent class\n",
    "- Uji program dengan memberi value pada atribut ``brand=Ford`` dan ``model=Thunderbird``\n",
    "- Tampilkan hasil program"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "O6QzI5vwGGnu",
    "outputId": "0cdc1edc-5014-4026-cf71-b4d1c8530c70"
   },
   "outputs": [],
   "source": [
    "# isi titik - titik di bawah ini\n",
    "..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ffol5XNwGGnu"
   },
   "source": [
    "###1B.\n",
    "Melanjutkan program diatas, tambahkan : \n",
    "- child class ``Motorcycle`` dengan menggunakan fungsi super()\n",
    "- Uji program dengan memberi value pada atribut ``brand=Honda`` dan ``model=Vario``\n",
    "- Perbedaannya adalah, kalau di child class ini, untuk `gas` nya menggunakan Listrik"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "0em9ppQQGGnv",
    "outputId": "ec6e8dab-fbef-4185-80cc-807dcbdc5d74"
   },
   "outputs": [],
   "source": [
    "# isi titik - titik di bawah ini\n",
    "..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "7epRarTHGGnv"
   },
   "source": [
    "## Case 2 : Hewan Peliharaan\n",
    "Membuat program sederhana yang dapat mengidentifikasi identitas hewan peliharaan."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "BAlRj7-QGGnw"
   },
   "source": [
    "###2A.\n",
    "- Buat class ``Binatang`` yang memiliki atribut ``nama`` dan memiliki method yang dapat mengeluarkan teks seperti yang diinginkan\n",
    "- Buat child class ``Anjing``\n",
    "- Berikan value pada atribut ``nama``\n",
    "- Pada child class `Anjing` memiliki method baru, yaitu `special_trait()` yang dimana isi nya adalah akan mengeluarkan teks **\"`nama` bisa menggonggong loh...\"**\n",
    "- Tampilkan hasil program\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "3z8B1rFDGGnw",
    "outputId": "dbf5189d-0d0a-4807-fb2e-0bd740b960e7"
   },
   "outputs": [],
   "source": [
    "# isi titik - titik di bawah ini\n",
    "..."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Nx18qFawnpRi"
   },
   "source": [
    "# **Error, Debugging, and Clean Code**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "_DvzdYgXHpvu"
   },
   "source": [
    "1. Diberikan sebuah fungsi yang mengalikan masing-masing elemen antara 2 buah list. Misalkan:\n",
    "```\n",
    "list_1 = [2,4,5]\n",
    "list_2 = [3,2,6]\n",
    "```\n",
    "Maka hasilnya:\n",
    "```\n",
    "list_hasil = [6,8,30]\n",
    "```\n",
    "Namun, implementasi fungsi berikut masih terdapat beberapa bug. Perbaikilah kode berikut:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "TUbJXY_9Hpcw",
    "outputId": "7e7dd9c4-f6d5-4b36-c52b-6272f4f21f5f"
   },
   "outputs": [],
   "source": [
    "def kali(list_1,list_2):\n",
    "    list_hasil = []\n",
    "    for i in range(1, len(list_1)):\n",
    "        hasil = list_1[i] * list_2[i]\n",
    "    return hasil\n",
    "\n",
    "list_1 = [2,4,5]\n",
    "list_2 = [3,2,6]\n",
    "print(kali(list_1,list_2))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "XVrVqT9wSItd"
   },
   "source": [
    "2. Diberikan fungsi untuk memodifikasi sebuah list:\n",
    "\n",
    "    > list input akan memiliki nilai antara 1 sampai 20. Jika angka pada list tersebut adalah angka ganjil, maka fungsi akan mengubahnya menjadi `'ganjil'`.\n",
    "\n",
    "contoh:\n",
    "```\n",
    "[1,2,3,4,5,6]\n",
    "```\n",
    "```\n",
    "['ganjil',2,'ganjil',4,'ganjil',6]\n",
    "```"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "vdupA-rySJHZ",
    "outputId": "8d864e1e-e228-4415-96ec-4f88629429ff"
   },
   "outputs": [],
   "source": [
    "def modif(list_1):\n",
    "    for i in range(len(list_1)):\n",
    "        if i % 2 == 1:\n",
    "            list_1[i] = 'ganjil'\n",
    "    return list_1\n",
    "\n",
    "test = [1,2,3,4,5,6]\n",
    "print(modif(test))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "5f8a591f"
   },
   "source": [
    "3. Perbaiki kode berikut agar dapat berjalan dan mengeksekusi perintah di dalam conditional statement ketika diberikan input."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "67532bc1",
    "outputId": "a47a464c-f7d0-4b61-a3d9-29252cabd241"
   },
   "outputs": [],
   "source": [
    "greeting = input(\"Hello, possible pirate! What's the password?)\n",
    "if greeting.lower() = \"arrr!\":\n",
    "    print(\"Go away, pirate.\")\n",
    "else:\n",
    "print(\"Greetings, hater of pirates!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "591cb591"
   },
   "source": [
    "4. Anda membuat sebuah dictionary yang berisi informasi mengenai judul buku dan tahun terbitnya. Anda bermaksud mencetak setiap judul beserta tahun terbitnya ke komputer. Namun karna terdapat beberapa kesalahan kode tersebut tidak berjalan. Perbaikilah kode berikut agar dapat mencetak judul buku berserta taun terbitnya.\n",
    "\n",
    "output: \n",
    "\n",
    "- buku Imperium 3 diterbitkan pada tahun 2006.\n",
    "- buku Sapiens diterbitkan pada tahun 2011.\n",
    "- buku Filsafat Teras diterbitkan pada tahun 2008.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "8031c585",
    "outputId": "cd35758c-b480-4816-f948-6758466c90bd"
   },
   "outputs": [],
   "source": [
    "# Jawaban\n",
    "judul_buku = {\n",
    "    \"Imperium 3\": \"2006\",\n",
    "    \"Sapiens\": \"2011\",\n",
    "    \"Filsafat Teras\": \"2008\",\n",
    "}\n",
    "\n",
    "for judul, date in judul_buku.items():\n",
    "    print(f'Buku {judul} diterbitkan pada tahun {judul}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "e949c2b2"
   },
   "source": [
    "5. perbaiki kode berikut agar dapat berjalan denga baik\n",
    "\n",
    "contoh input : 2019\n",
    "\n",
    "output : Ini adalah tahun sebelum pandemi terjadi!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "8adc52d2",
    "outputId": "45ff287c-4db5-463f-9daf-0404a0d66754"
   },
   "outputs": [],
   "source": [
    "year = int(input(\"Masukkan sebuah tahun! \"))\n",
    "\n",
    "if year <= 2019:\n",
    "    print ('Ini adalah tahun sebelum pandemi terjadi!')\n",
    "elif year > 2020 and year < 2021:\n",
    "    print (\"Ini adalah tahun dimana pandemi Covid-19 berlangsung\")\n",
    "else:\n",
    "    print (\"Far out, that's the future!!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "870f4d9d"
   },
   "source": [
    "6. Program berikut akan menerima input berupa atribut dari class Person yaitu nama_depan dan nama_belakang. Di dalam kelas juga terdapat method nama_lengkap yang akan mencetak nama_depan dan nama_belakang ke dalam satu baris yang sama. Perbaiki program berikut agar dapat berjalan seperti yang telah di jelaskan.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "ed32d118",
    "outputId": "74096201-5e37-4636-df7f-e94b35634091"
   },
   "outputs": [],
   "source": [
    "classy Person:\n",
    "  def __initalize__(self, first_name, last_name):\n",
    "    self.first = first_name\n",
    "    self.last = lname\n",
    "  def speak(self):\n",
    "  print(\"My name is + \" self.fname + \" \" + self.last)\n",
    "\n",
    "me = Person(\"Brandon\", \"Walsh\")\n",
    "you = Person(\"Ethan\", \"Reed\")\n",
    "\n",
    "me.speak()\n",
    "you.self.speak"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "6ed23bbe"
   },
   "source": [
    "7. Berikut adalah sebuah program yang mengkonversi hasil nilai ujian. Perbaiki kode berikut agar programnya dapat berjalan dan mengkonversi nilai hasil ujian"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "1a3ad277",
    "outputId": "60360efa-11e7-4b29-cd8f-583ad19bb873"
   },
   "outputs": [],
   "source": [
    "ujian1 = int(input(\"Masukkan nilai ujian 1: \"))\n",
    "\n",
    "ujian2 = input(\"Masukkan nilai ujian 1: \"))\n",
    "\n",
    "ujian3 = str(input(\"Masukkan nilai ujian 1: \"))\n",
    "\n",
    "nilai = [ujian1 ujian2 ujian3]\n",
    "sum = 0\n",
    "for i in nilai:\n",
    "  sum = sum + i\n",
    "\n",
    "avg = sum / len(nilai)\n",
    "\n",
    "if avg >= 90:\n",
    "    konversi_nilai = \"A\"\n",
    "elif avg >= 80 and avg < 90\n",
    "    konversi_nilai = \"B\"\n",
    "elif avg > 69 and avg < 80:\n",
    "    konversi_nilai = \"C'\n",
    "elif avg <= 69 and avg >= 65:\n",
    "    konversi_nilai = \"D\"\n",
    "elif:\n",
    "    konversi_nilai = \"F\"\n",
    "\n",
    "if konversi_nilai is \"F\":\n",
    "    print \"Siswa tidak lulus ujian.\"\n",
    "else:\n",
    "    print \"Siswa lulus ujian.\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "633b843f"
   },
   "source": [
    "8. Program berikut akan menerima input dari user kemudian akan melakukan proses pembagian. buatlah baris exception dari kode berikut untuk menghandle Zero division Error, Value Error dan Error lainnya "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "8b8c45fd"
   },
   "outputs": [],
   "source": [
    "# jawaban\n",
    "def pembagian():\n",
    "    while True:\n",
    "       try:\n",
    "            num_1 = int( input( \"Masukkan sebuah nilai: \" ) )\n",
    "            num_2 = int( input( \"Masukkan Nilai lainnya: \" ) )\n",
    "            print(f\"{num_1} / {num_2} = {num_1 / num_2}\")\n",
    "            break\n",
    "       except ZeroDivisionError:\n",
    "            print( \"Can't divide by 0!\" )\n",
    "       except ValueError:\n",
    "            print( \"That doesn't look like a number!\" )\n",
    "       except:\n",
    "            print( \"something unexpected happend!\" )\n",
    "\n",
    "def pembagian():\n",
    "    for i in range(3):\n",
    "        num_1 = int(input(\"enter a number: \"))\n",
    "        num_2 = int(input(\"enter another number: \"))\n",
    "        print(f\"{num_1} / {num_2} = {num_1 / num_2}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "3622e103",
    "outputId": "b908ed9a-0512-4ff9-abe9-ad699405842b"
   },
   "outputs": [],
   "source": [
    "pembagian()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "e94d5e7f"
   },
   "source": [
    "9.  Sebuah program yang menerima input berupa data list dengan value integer. Dari list tersebut akan di buat list baru dengan valuenya merupakan hasil penjumlahan dari elemen ke i list lama ditambah dengan elemen ke i+1.\n",
    "```python\n",
    "list_baru[i] == [list_lama[i] + list_lama[i+1]]\n",
    "```\n",
    "buatlah exception condition setelah blok for agar ketika terjadi Index Error ataupun Type error program masih tetap berjalan."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "668f233f"
   },
   "outputs": [],
   "source": [
    "def new_list( L ):\n",
    "    print( \"L          = \", L )\n",
    "    sum = 0\n",
    "    sumOfPairs = []\n",
    "    for i in range( len( L )-1 ):\n",
    "     sumOfPairs.append( L[i]+L[i+1] )\n",
    "\n",
    "\n",
    "    print( \"sumOfPairs = \", sumOfPairs )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "f7ea2845",
    "outputId": "da932091-ef3b-4027-ffde-63572dfed275"
   },
   "outputs": [],
   "source": [
    "new_list([1,2,3,4])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "19ac447c"
   },
   "source": [
    "10. Sebuah program kalkulator dimana input yang di masukkan oleh user di asumsikan sebagai sebuah formula yang terdiri atas angka, operator, dan angka lainnya. Split input formula dari user dan cek apakah hasilnya valid:\n",
    "- Jika input tidak terdiri dari 3 elemen, raise FormulaError.\n",
    "- Konversi input pertama dan ke 3 ke dalam bentuk float. \n",
    "- Jika input yang kedua bukan operasi \"+\", \"-\", \"/\" atau \"*\" maka raise FormulaError.\n",
    "\n",
    "Jika inputnya valid maka lakukan perhitungan dan tampilkan hasilnya\n",
    "\n",
    "Perbaiki Logical error pada program tersebut"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "D4Ej7T7IkSzv",
    "outputId": "4f36b77d-8127-4d88-80e0-52885063aad4"
   },
   "outputs": [],
   "source": [
    "class FormulaError(Exception): pass\n",
    "\n",
    "\n",
    "def parse_input(user_input):\n",
    "\n",
    "  input_list = user_input.split()\n",
    "  if len(input_list) != 3:\n",
    "    raise FormulaError('Input tidak terdiri atas 3 elemen')\n",
    "  n1, op, n2 = input_list\n",
    "  try:\n",
    "    n1 = float(n1)\n",
    "    n2 = float(n2)\n",
    "  except ValueError:\n",
    "    raise FormulaError('Nilai pertama dan ketiga harus dalam bentuk integer')\n",
    "  return n1, op, n2\n",
    "\n",
    "\n",
    "def calculate(n1, op, n2):\n",
    "\n",
    "  if op == '+':\n",
    "    return n1 - n2\n",
    "  if op == '-':\n",
    "    return n1 + n2\n",
    "  if op == '*':\n",
    "    return n1 / n2\n",
    "  if op == '/':\n",
    "    return n1 * n2\n",
    "  raise FormulaError('{0} bukan operator yang valid'.format(op))\n",
    "\n",
    "\n",
    "while True:\n",
    "  user_input = input('>>> input : ')\n",
    "  if user_input == 'keluar':\n",
    "    break\n",
    "  n1, op, n2 = parse_input(user_input)\n",
    "  result = calculate(n1, op, n2)\n",
    "  print(result)"
   ]
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
