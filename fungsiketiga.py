from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def fungsiketiga(text):
 
  analyzer = SentimentIntensityAnalyzer()
  text_input = str(text)
  analisis = analyzer.polarity_scores(text_input) 
  
  if analisis['compound'] >= 0.05:
    hasil = "Teks ini bersifat Positif"
  elif analisis['compound'] <= -0.05:
    hasil = "Teks ini bersifat Negatif"
  else:
    hasil = "Teks ini bersifat Netral" 

  return hasil
