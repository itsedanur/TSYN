import pandas as pd
from sklearn.cluster import KMeans #Kümelemek için
import numpy as np


def tansiyon_coz(tansiyon_str):
    try:
        sistolik,diyastolik = tansiyon_str.split('/')
        return int(sistolik), int(diyastolik)
    except Exception as hata:
        return np.nan , np.nan

def ana():
    #excel verilerini al
    veri = pd.read_excel('tansiyon.xlsx')

    veri[['sabah_sistolik','sabah_diyastolik']] = veri['Sabah Tansiyon'].apply(lambda x: pd.Series(tansiyon_coz(x)))
    veri[['aksam_sistolik','aksam_diyastolik']] = veri['Akşam Tansiyon'].apply(lambda x: pd.Series(tansiyon_coz(x)))

    ozellikler = veri[['sabah_sistolik','sabah_diyastolik', 'aksam_sistolik','aksam_diyastolik']].dropna()

    kmeans = KMeans(n_clusters=2, random_state=42)
    kumeler = kmeans.fit_predict(ozellikler)
    ozellikler['cluster'] = kumeler


    kume_ortalamalari = ozellikler.groupby('cluster').mean()[['sabah_sistolik','aksam_sistolik']]
    riskli_kume = kume_ortalamalari.mean(axis=1).idxmax()

    ozellikler['risk'] = ozellikler['cluster'].apply(lambda x: 'Risk' if x == riskli_kume else 'Normal')

    #veriyi orjinal veriye göm
    veri = veri.join(ozellikler['risk'])

    risk_sayisi = veri['risk'].value_counts().get('Risk',0)
    toplam = veri['risk'].count()
    genel_risk = 'Yüksek Tansiyon / Kalp Riski' if  risk_sayisi/toplam >= 0.5 else 'Normal Tansiyon'

    print('Günlük Risk Durumları')
    print(veri[['Tarih', 'risk']])
    print("\nGenel Değerlendirme:", genel_risk)

if __name__ == '__main__':
    ana()
    