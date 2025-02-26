import pandas as pd
import matplotlib.pyplot as plt

def kanal_grafigi_olustur(dosya_yolu):
    df = pd.read_excel(dosya_yolu)
    print("İlk 5 satır kanal adları:")
    print(df.iloc[0:5, 0])
    
    plt.figure(figsize=(25, 10))
    
    kanal_adlari = df.iloc[:, 0].tolist()
    
    print("\nToplam kanal sayısı:", len(kanal_adlari))
    print("Benzersiz kanal sayısı:", len(set(kanal_adlari)))
    
    gunluk_veriler = df.iloc[:, 3:368]
    gunler = list(range(1, 366))
    
    renkler = ['blue', 'red', 'green', 'orange', 'yellow', 'brown', 'pink', 'gray', 'olive', 'cyan']
    
    for i, kanal in enumerate(kanal_adlari):
        renk = renkler[i % len(renkler)]
        plt.plot(gunler, gunluk_veriler.iloc[i], 
                label=str(kanal).strip(), 
                color=renk,
                linewidth=1.5)
    
    plt.title('Yıllık Bitrate Değerleri', fontsize=16, pad=20)
    plt.xlabel('Günler (1-365)', fontsize=12, labelpad=10)
    plt.ylabel('Bitrate', fontsize=12, labelpad=10)
    
    plt.xticks(range(0, 366, 30), range(0, 366, 30), fontsize=10)
    plt.ylim(0, 10)
    plt.yticks(range(0, 11, 1))
    plt.xlim(1, 365)
    
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plt.legend(bbox_to_anchor=(1.02, 1), 
              loc='upper left', 
              fontsize=10,
              borderaxespad=0)
    
    plt.subplots_adjust(right=0.85)
    
    plt.show()

dosya_yolu = r''
kanal_grafigi_olustur(dosya_yolu)