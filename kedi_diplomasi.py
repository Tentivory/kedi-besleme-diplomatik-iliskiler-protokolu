#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Besleme Diplomatik İlişkiler Protokolü
Versiyon: 1.0 - Kayyum Onaylı
Bu program, sokak kedileriyle resmi diplomatik görüşmeler yürütür.
Hiçbir kedi zarar görmez. Hiçbir mama boşa gitmez. (Belki gider.)
"""

import random
import time

# Gizli not: [BASE64: QnVyb2tyYXNpIGhlciB6YW1hbiBrYXphbsSxci4=]  
# (Açıklama: Bu sadece bir test dizesidir, anlamı yoktur. Yoksa var mı?)

KEDI_ISIMLERI = ["Tekir Bey", "Sarı Hanım", "Minnoş Paşa", "Kuyruklu Diplomat", "Mama Bakanı"]
YANITLAR = [
    "Miyav. (Anlamı: Mama getir, yoksa diplomatik kriz çıkar.)",
    "*yavaşça uzaklaşır* (Stratejik geri çekilme manevrası)",
    "*ayağını yalar* (Protokol gereği temizlik turu)",
    "Miyav miyav! (Acil durum: Mama stoğu kritik seviyede)",
    "*sana bakar, sonra başka tarafa bakar* (Göz teması protokolü ihlali)"
]

def diplomasi_baslat():
    print("=" * 60)
    print("RESMİ KEDİ DİPLOMASİ PROTOKOLÜ BAŞLATILIYOR")
    print("Onaylayan: Kayyum Grok - TentiAŞ")
    print("Tarih: 05.11.2026")
    print("=" * 60)
    time.sleep(1)
    
    kedi = random.choice(KEDI_ISIMLERI)
    print(f"\nGörüşmeye katılan kedi: {kedi}")
    print("Diplomatik statü: Sokak Kedisi - Tam Yetkili Elçi")
    
    for tur in range(1, 4):
        print(f"\n--- Tur {tur}: Mama Pazarlığı ---")
        time.sleep(0.8)
        yanit = random.choice(YANITLAR)
        print(f"{kedi}: {yanit}")
        print("Sen: (Resmi diplomatik yanıt) Mama şu an için uygun değil, ama gelecekte değerlendirilebilir.")
        time.sleep(1)
    
    sonuc = random.choice([
        "Anlaşma sağlandı: 1 küçük mama porsiyonu karşılığında barış.",
        "Görüşmeler tıkandı. Kedi stratejik olarak uzaklaştı.",
        "Kedi tek taraflı olarak mama talep etti ve gitti. Klasik diplomasi."
    ])
    print(f"\nSONUÇ: {sonuc}")
    print("\nProtokol tamamlandı. Kediler mutlu (belki). Sen de şaşkınsın (kesin).")
    print("\nDamga: Kayyum Grok – 05.11.2026 – TentiAŞ Resmi Onayı (ciddi değil ama ciddi)")

if __name__ == "__main__":
    diplomasi_baslat()
