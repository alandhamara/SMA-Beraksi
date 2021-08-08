def fungsipertama():
    import numpy as np
    import pandas as pd
    import functools
    import itertools

    lol = pd.read_csv('semangatkawan (1).csv', delimiter=';')
    lol.tail()

    X = lol.iloc[:,0].values
    y = lol.iloc[:,1].values

    X[20:]

    from sklearn.feature_extraction.text import TfidfVectorizer  
    tfidfvectorizer = TfidfVectorizer(max_features=100000, use_idf=True)
    tfidfvectorizer.fit(X[:30])
    X_train = tfidfvectorizer.transform(X[:30])
    X_test = tfidfvectorizer.transform(X[30:])
    y_train = y[:30]
    y_test = y[30:]

    X[1]
    text_coba = str(input("Masukan Teks          : "))
    coba = tfidfvectorizer.transform([text_coba]).todense()

    cobaa = coba.tolist()

    features = tfidfvectorizer.get_feature_names()

    aku = []
    kata = []

    for i in range(len(cobaa[0])):
        if cobaa[0][i] != 0.0:
            hahaha = cobaa[0][i]
            aku.append(hahaha)

    for i in range(len(cobaa[0])):
        if cobaa[0][i] != 0.0:
            haha = features[i]
            kata.append(haha)
    # Converting to list
    zipped = zip(aku, kata)
    zipped = list(zipped)
  
    # Printing zipped list
    # print("Initial zipped list - ", str(zipped))
  
    # Using sorted and lambda
    katapenting = sorted(zipped, key = lambda x: x[0],reverse=True)
      
    # printing result
    # print("final list - ", str(res))
    print("Kata Penting          : ")
    print(katapenting[:5])

def fungsikedua():
  import nltk
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
      print("Kata Typo             :", kata_inputan, ", seharusnya adalah", saran)
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
    print("Teks Akhir            : ", end ='')
    for i in pembenaran_kata:
        print(i, end = ' ')
  
  x = input("Masukkan Teks         : ")

  input_kata = [] #array untuk menyimpan input
  input_kata = word_tokenize(x) #menambah input ke dalam array

  prediction = prediksi(input_kata, predict) #variabel prediction untuk menampung hasil dari prediksi
  cetak(prediction, input_kata)
  
def fungsiketiga():
  from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
 
  analyzer = SentimentIntensityAnalyzer()
  text_input = str(input("Masukkan Teks         : "))
  analisis = analyzer.polarity_scores(text_input) 
  
  if analisis['compound'] >= 0.05:
    print("Hasil                 : Teks ini bersifat Positif")
  elif analisis['compound'] <= -0.05:
    print("Hasil                 : Teks ini bersifat Negatif")
  else:
    print("Hasil                 : Teks ini bersifat Netral")

print("FUNGSI PERTAMA: PENCARI 5 KATA PENTING")
print("======================================")
fungsipertama()
print("")
print("FUNGSI KEDUA: DETEKSI KATA TYPO & SARAN KATA")
print("============================================")
fungsikedua()
print("")
print("")
print("FUNGSI KETIGA: ANALISIS SENTIMEN TEKS")
print("=====================================")
fungsiketiga()