# kelime_sayici.py

def kelime_say(metin, aranan_kelime):
    kelimeler = metin.lower().split()
    kelime_sayisi = kelimeler.count(aranan_kelime.lower())
    return kelime_sayisi

if __name__ == "__main__":
    metin = """
    Hava kirliliği, dünya genelinde büyük bir çevresel sorun olarak karşımıza çıkmaktadır. Hava kirliliği,
    atmosferdeki zararlı gazlar, kimyasallar, tozlar ve partiküllerin yüksek seviyelerde bulunması sonucu
    ortaya çıkar. Bu kirleticiler, sanayi tesisleri, araç emisyonları, enerji üretimi ve tarım gibi kaynaklardan
    atmosfere salınır. Hava kirliliği, ciddi sağlık sorunlarına yol açabilir ve doğal ekosistemlere zarar
    verebilir.
    Hava kirliliği, insan sağlığına bir dizi olumsuz etki yapar. Kirli hava solumak, solunum yolu
    hastalıklarının, kalp hastalıklarının, kanser riskinin artmasına ve genel yaşam kalitesinin
    düşmesine neden olabilir. Ayrıca, çocuklar, yaşlılar ve kronik sağlık sorunları olanlar, hava
    kirliliğinin etkilerine daha fazla maruz kalabilirler.
    Hava kirliliği aynı zamanda ekosistemlere zarar verir. Bitkiler, hayvanlar ve su kaynakları
    üzerinde olumsuz etkiler yaratabilir, biyolojik çeşitliliği azaltabilir ve tarım verimliliğini
    etkileyebilir.
    Bu sorunun çözümü için dünya genelinde çevresel düzenlemeler ve temiz enerji kaynaklarına
    geçiş gibi adımlar atılmaktadır. Ayrıca, bireysel olarak daha çevre dostu seçimler yaparak da
    hava kirliliğinin azaltılmasına katkı sağlayabiliriz. Hava kirliliği ile mücadele, hem insan
    sağlığını hem de gezegenimizin geleceğini korumak için önemlidir.
    """
    aranan_kelime = "hava"
    sayim = kelime_say(metin, aranan_kelime)
    print(f"'{aranan_kelime}' kelimesi metinde {sayim} defa geçmektedir.")
