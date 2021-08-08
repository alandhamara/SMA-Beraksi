def fungsikedua():
  import nltk
  nltk.download('punkt')
  from nltk.metrics.distance import edit_distance #mengukur kesamaan suatu string dengan string lain atau dua buah teks
  import pandas as pd
  from nltk.tokenize import word_tokenize
  from openpyxl import load_workbook
  
  dataset = load_workbook(filename="kataa.xlsx") #memuat file xlsx
  sheet_range = dataset['stopwordbahasa']
  df = pd.DataFrame(sheet_range.values)
  df.columns = ['Kata_dasar']
  predict = []
  predict = df['Kata_dasar'].values.tolist() #mengambil isi pada kolom kata_benar dan merubah value ke bentuk list

  def cari(kata_inputan, predict): #fungsi untuk melakukan proses pencarian hasil prediksi minimum
    list_ed_value = {} #pencarian min edit distance dengan setiap kata prediksi
    for word in predict:
        list_ed_value[word] = edit_distance(kata_inputan, word) #menghitung distance setiap dua kata
        saran = min(list_ed_value, key=list_ed_value.get) #menghitung hasil prediksi minimum dan mengambil kata yang paling dekat
    if(kata_inputan != saran):
      print("Kata Typo         :", kata_inputan, ", seharusnya adalah", saran)
    return saran #mengembalikan nilai

  def prediksi(kata_inputan, predict): #fungsi untuk melakukan cek panjang kalimat
    kata_fix = []
    if len(kata_inputan) > 1:
        for i in kata_inputan:
            kata_fix.append(cari(i, predict))
    else:
      kata_fix.append(cari(kata_inputan[0], predict))
    return kata_fix
  
  def cetak(pembenaran_kata, kata_asli): #fungsi untuk melakukan cetak hasil
    print("Teks Akhir        : ", end ='')
    for i in pembenaran_kata:
        print(i, end = ' ')
  
  x = input("Masukkan Teks     : ")

  input_kata = [] #array untuk menyimpan input
  input_kata = word_tokenize(x) #menambah input ke dalam array

  prediction = prediksi(input_kata, predict) #variabel prediction untuk menampung hasil dari prediksi
  cetak(prediction, input_kata)
  
fungsikedua()