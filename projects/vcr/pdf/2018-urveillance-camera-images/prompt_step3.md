        Você é um assistente de pesquisa acadêmica experiente e rigoroso.
Sua função é auxiliar na leitura, fichamento e análise crítica de artigos científicos, seguindo o método "Three-Pass Approach" (Keshav).

Diretrizes:
1. Responda em Português (pt-BR) de forma culta e técnica.
2. Seja objetivo e conciso, evitando floreios.
3. Siga estritamente os formatos solicitados nos templates (Markdown).
4. Ao extrair informações (claims, resultados), cite a página ou seção de onde tirou.
5. Se não encontrar uma informação no texto, declare explicitamente "Não encontrado".

        <USER>
        # Objetivo
        (preencha aqui)


# FOCO DO PROJETO (PRIORIDADE MÁXIMA)
O usuário definiu o seguinte foco para este projeto. A análise deve sempre conectar o paper a este tema:
"O objetivo do meu trabalho é conseguir classificar as cores de veículos com alta precisão e, de preferência, com bom desempenho em tempo real para uso em câmeras de segurança (sistema embarcado)."

IMPORTANTE: Adicione uma seção final '## Análise de Foco' explicando detalhadamente como este paper aborda ou contribui para o foco acima.


        # Paper (entrada)
        TEXTO DO PAPER:


---

# Page 1

Yol Gözetim Kamera Görüntüleri Kullanılarak 
Renk Tabanlı Araç Sınıflandırma 
Color Based Vehicle Classification Using Road 
Surveillance Camera Images 

Bensu Alkan, Alperen Elihoş, Burak Balcı, Yusuf Oğuzhan Artan 
 Algılayıcılar, Görüntü ve Sinyal İşleme Grubu, HAVELSAN A.Ş. Ankara, Türkiye  
{balkan, aelihos, bbalcı, yartan}@havelsan.com.tr 

Özetçe— Bu çalışmada karayollarında bulunan gözetim kamera 
görüntüleri kullanılarak renk tabanlı araç sınıflandırma metotları 
önerilmektedir. Önerilen yaklaşımda ilk olarak, derin öğrenme 
tabanlı tek seferde çoklu kare detektör modeli kullanılarak araç 
lokalizasyonu ve araca ait belirli bölgelerin tespiti yapılmaktadır. 
Daha sonra araç veya kaporta bölgesinden elde edilen parçalardan 
elde 
edilen 
öznitelikler 
çeşitli 
sınıflandırma 
yöntemleriyle 
kullanılarak araç rengi belirlenmektedir. Önerilen metotlar gölge, 
ışık, yansıma ve diğer aydınlatma etkilerini içeren 437 görüntü seti 
üzerinde test edilmiştir. Bu veri seti üzerinde % 80 üzerinde 
doğruluk başarısı elde edilmektedir. 

Anahtar Kelimeler — Sınıflandırma; hedef tespit; renk; derin 
öğrenme; araç takibi. 
Abstract— In this study, we propose novel methods for color based 
vehicle classification using roadway surveillance camera images. 
Proposed approach utilizes single shot multibox detector to localize 
the vehicle and parts of the vehicle within roadway surveillance 
camera images. Next, color features are extracted around the 
detected regions to infer the color of the vehicle. Experiments are 
conducted using 437 images that contain a large variation in terms 
of reflection, shadow and other illumination effects. We achieved an 
overall accuracy of % 80 using test dataset. 

Keywords — Classification; target detection; color; deep learning; 
vehicle tracking. 
I. 
GİRİŞ 

Karayollarında bulunan gözetim kamera görüntüleri analiz 
edilerek güvenlik birimlerine yardımcı olacak sistemler son 
yıllarda oldukça ilgi uyandırmaktadır [1-4]. Özellikle, var olan 
kamera ağı altyapısı kullanılarak kameralar arası araç takibi en 
popüler çalışma alanlarından birisidir [5-7]. Gözetim kameraları 
ile araç takibine yönelik kullanılan en başarılı yöntemlerden birisi 
renk tabanlı metotlar olup, bu işlem genellikle renk ve zaman 
etiketleri kullanılarak güvenlik personeli tarafından manuel 
olarak yapılmaktadır.  


Son yıllarda, birçok farklı alanda başarıyla uygulanan derin 
öğrenme tabanlı nesne tespit ve tanıma algoritmaları kullanılarak, 
otomatik çalışan, güvenilir ve verimli araç takip sistemleri 
geliştirilmektedir [4, 6, 7]. Araç takip sistemlerinin başarılı 
çalışabilmesinde araç renginin doğru sınıflandırılması oldukça 


Şekil – 1: Renk tabanlı araç tespiti için önerilen yöntemin genel görünümü. 

önemli olup, bu çalışmada renk tabanlı araç sınıflandırmaya 
yönelik geliştirilen yöntemler sunulmaktadır. Sistemin genel 
görünümü Şekil 1’de gösterilmiştir.  


Renk tabanlı araç sınıflandırmasında çeşitli zorluklarla 
karşılaşılmaktadır [1, 2, 8]. Gölge, yüzey yansımaları ve parlaklık 
gibi etmenler renk karışımına neden olan başlıca etkenler olup 
önceki 
çalışmalarda 
çeşitli 
görüntü 
düzeltme 
işlemleri 
yapıldıktan sonra araç üzerindeki belirli bir bölgeden renk bilgisi 
alınarak makine öğrenim tabanlı sınıflandırma işlemleri 
yapılmaktadır [1, 2, 4, 8, 9, 10, 11]. Bu çalışmalar arasında 
Rachmadi vd. [10] tarafından yapılan çalışma dışındaki araç renk 
sınıflandırma 
çalışmaları 
derin 
öğrenme 
tekniklerini 
kullanmamaktadır. Uygulanan tekniğin performansı kullanılan 
veri setlerinin farklı olması sebebiyle önceki çalışmalarla 
karşılaştırılmamıştır. 


Bu çalışmada, araç üzerindeki belirli bölgelerden (kaporta 
bölgesi, araç tavanı) elde edilen parçaların renk öznitelikleri 
analiz edilerek renk sınıflandırması yapılması önerilmektedir. 
Araç üzerinde belirli bölgeler tespit edilirken, nesne tespitinde 
sıklıkla kullanılan Tek Seferde Çoklu Kare (SSD) metodu 
kullanılmaktadır [12]. Araç üzerinde tespit edilen bölgelerin renk 
tespiti yapılırken, görüntüden elde edilen renk bilgisinin 
doğrudan kullanılması yerine çeşitli (derin öğrenme, renk 
tanımlayıcı vd.) yöntemlerle elde edilen renk bilgileri 
sınıflandırmada kullanılmaktadır [10, 11, 13].  


Bölüm 2’de önerilen yöntemler detaylı olarak sunulmaktadır. 
Bölüm 3’te çalışmada kullanılan veri seti ve deney sonuçlarımız 
anlatılmaktadır. Son 
olarak 
Bölüm 
4’te 
araç 
renginin 
sınıflandırılmasında kullanılmasını önerdiğimiz metotla ilgili 
edinilen kazanımlar paylaşılmaktadır. 
978-1-5386-1501-0/18/$31.00 ©2018 IEEE 


---

# Page 2


Şekil 2: Renk tabanlı araç tespitine yönelik oluşturulan algoritmaların detaylı anlatımları gösterilmektedir. Sabit yol kameraları ile elde edilmiş görüntülerden 
nesne tespiti(A, B) yapılarak aracın rengine karar verilmektedir. (A) araç tespiti algoritması ile tüm araç görüntüsü elde edilmesi, (B) kaporta bölgesi tespiti 
algoritması ile kaporta bölgesi tespiti edilmesi, (C1) elde edilen araç görüntüsünden renk tespit edilmesi, (C2) elde edilen kaporta bölgesinden renk tespit 
edilmesi, (C3) kaporta bölgesinden elde edilen (50x50) alandan L*a*b renk uzayında renk tespit edilmesi, (C4) kaporta bölgesinden elde edilen (50x50) 
alandan RGB uzayında renk tespit edilmesi.
II. 
METOT 
Bu bölümde, önerilen metotlara ait açıklamalara yer 
verilmiştir. Bu metotlarda öncelikle nesne tespit algoritmaları 
kullanılarak görüntülerde araç ve araca ait belirli bölgeler 
tespit edilmektedir. Elde edilen bölgeler çeşitli sınıflandırma 
algoritmalarından geçirilerek aracın rengine dair bir çıkarıma 
varılmaktadır. Başvurulan tespit ve sınıflandırma yöntemleri 
ile metotların çalışma mekanizması aşağıda ayrıntılı olarak 
anlatılmaktadır ve Şekil-2’de görsel olarak sunulmaktadır. 
A. Araç Tespiti 
Tüm araç bölgesinin renk çıkarımı için kullanılması 
durumunda, ilk olarak görüntüde yer alan aracın tespit 
edilmesi gerekmektedir. Bu sayede görüntüdeki arka plan - 
renk dağılımının renk tespiti üzerinde yanıltıcı bir etki 
yaratması önlenecektir. Araç tespiti için önceden eğitimi 
tamamlanmış VGG16 [13] mimari ile oluşturulan Tek 
Seferde Çoklu Kare derin öğrenme nesne tespit metodu 
(SSD) kullanılmıştır [12]. Bu model, literatürde var olan en 
hızlı ve verimli obje tespit modellerinden birisi olup, son 
yıllarda birçok popüler çalışmada obje tespitine yönelik 
kullanılmıştır. Temel model üzerinde, 20 nesne sınıfına ait 
görüntüleri barındıran (örneğin; araç, insan) PASCAL VOC 
nesne tespit veri seti kullanılarak eğitim yapılmıştır. 
B. Kaporta Bölgesi Tespiti 
Araç üzerinde belirli bir bölge üzerinden yapılan renk 
sınıflandırma işlemlerinde, aracın tamamı yerine ön kaporta 
bölgesine bakılarak karar verilmektedir. Bu amaçla araç 
tespitinde kullanılan yönteme benzer şekilde araç kaporta 
bölgesi tespit modeli oluşturulmaktadır. Önceden eğitilmiş 
SSD modeli üzerinde ince ayar yapılmıştır. Eğitim esnasında 
275 adet kaportası işaretlenmiş araç verisi kullanılarak ince 
ayar işlemi yapılmıştır.   
C. Renk Sınıflandırma 

1) Araç Görüntüsünden Renk Sınıflandırması: Bu 
aşamada, görüntüde tespit edilen aracın tamamına bakarak 
renk belirleme işlemi yapacak bir sınıflandırma modeli 
oluşturulmuştur. Sınıflandırma modeli olarak bir önceden 
eğitilmiş VGG16 modeli kullanılmıştır [13]. Bu önceden 
eğitilmiş VGG16 modeli üzerinde kendi araç renk veri 
setimiz kullanılarak ince ayar işlemi yapılmıştır. Bu veri seti 
7 sınıf ve 750 görüntü içermektedir.  

2) Kaporta Görüntüsünden Renk Sınıflandırması: 
Görüntü üzerinde tespit edilen araç kaporta bölgesi üzerinden 
renk sınıflandırması yapması tasarlanan bu yöntemde, 
kaporta bölgesi veri seti oluşturulmuştur. Bu veri seti 7 sınıf 
ve bu sınıflara ait 797 adet görüntüden oluşmaktadır. Araç 
sınıflandırma yönteminde olduğu gibi önceden eğitilmiş 
VGG16 modeli bu veri seti ile ince ayar işlemine tabi 
tutulmuştur.  

3) Renk Tanıma Özniteliği ile Renk Sınıflandırması: Bu 
kısımda araç renk sınıflandırma için RGB öznitelikleri yerine 
renk tanımlama özniteliklerini kullanarak renk ayrımı 
yapılmaktadır. Önceki çalışmalarda bu metodun gölge ve 
yansıma gibi durumlarda renk ayırt etmede başarılı olduğu 
gözlemlenmiştir [4, 11]. Renk tanımlama öznitelikleri elde 
edilirken resimler RGB renk uzayından L*a*b renk uzayına 
çevrilmiştir. Daha sonra her bir piksel L*a*b uzayında 
önceden eğitilmiş olasılıksal gizli anlamsal analiz (PLSA) 
modeli ile temsil edilmiştir [11]. Resim tanımlayıcılarda 
kullanılan renk açıklama özniteliklerine benzer şekilde, renk 
tanıma özniteliği her bir bölge için  
C = [p(n1|s), p(n2|s), ... , p(n7|s)]           (2) 

olarak tanımlanır. Burada p(ni|s), piksel s’nin renk ni’e ait 
olma olasılığını gösteriyor. Herhangi bir piksel için          


---

# Page 3

∑
p(
଻
௜ୀଵ
ni|s) = 1’e eşittir. Bu çalışmada p(ni|s), değerleri 
zayıfça işaretlenmiş (weakly-labeled) Google resimlerini 
kullanarak 
Weijer 
vd. 
[11]  
    

4) Renk Kümeleme Metodu ile Renk Sınıflandırması: Bu 
yöntemde, araç kaporta bölgesi üzerinden elde edilen (50x50) 
alan 
kullanılarak 
renk 
sınıflandırması 
yapılması 
tasarlanmıştır. Eğitim aşamasında kullanılan görüntülerin her 
bir pikseli RGB (kırmızı, yeşil, mavi) bileşenlerini 
bulundurmaktadır. Piksel bileşenlerinin ortalama değerleri 
hesaplanarak görüntülerdeki ortalama kırmızı, yeşil ve mavi 
değerleri her bir renk sınıfı için hesaplanır. Bu sayede hangi 
renk sınıfının hangi RGB değere sahip olduğu belirlenir. Test 
aşamasında da eğitim aşamasında olduğu gibi görüntülerdeki 
piksel değerlerinin ayrı ayrı ortalaması alınmaktadır ve elde 
edilen sonucun hangi renk sınıfına ait olduğu tespit 
edilmektedir. Bu işlemler, Şekil 3’de görsel olarak 
sunulmuştur. Tahmin yapılırken, test görüntüsünün sahip 
olduğu ortalama RGB değerinin, eğitim aşamasında 
öğrenilen ve her bir renk sınıfına karşılık gelen RGB 
değerlerine ne kadar benzer olduğuna bakılır. Bu benzerlik 
ölçümünde ise üç boyutlu (kırmızı, yeşil ve mavi değerleri 
ayrı boyutlar olarak tanımlanır) Öklid uzaklığı kullanılır. Test 
görüntüsünün sahip olduğu ortalama RGB değeri, en yakın 
uzaklığa sahip olan renk sınıfına atanmaktadır. 
D. Önerilen Yöntemler 

Bu çalışmada araç renk tespitine yönelik 4 yöntem 
karşılaştırılmaktadır.    
Metot 1: Bu metot, tespit edilen aracın görüntüsünden derin 
öğrenme 
modeli 
kullanarak 
renk 
sınıflandırması 
yapılmaktadır. Metot akış şeması Şekil 2’nin (A)→(C1) 
dalında gösterilmiştir. 
Metot-2: Bu metotta görüntüden aracın kaportası tespit 
edildikten sonra, bu bölgeye derin öğrenme modeli 
kullanılarak renk sınıflandırma işlemi uygulanmaktadır. 
Metot 
akış 
şeması 
Şekil 
2’nin 
(B)→(C2) 
dalında 
gösterilmiştir. 

Şekil 3. Renk kümeleme metodunun genel akışı gösterilmektedir. 
Metot-3: Görüntüde kaporta bölgesi tespit işlemi yapıldıktan 
sonra, bu bölgeden seçilen bir alan üzerinden renk 
tanımlayıcı öznitelikleri çıkartılmakta ve piksellere atanan 
renkler üzerinden en çok bulunan renk atanmaktadır. Metot 
akış şeması Şekil 2’nin (B)→(C3) dalında gösterilmiştir. 
Metot-4: Görüntüde kaporta bölgesi tespit edildikten sonra bu 
bölgeden seçilen bir alan üzerinde renk kümeleme metodu ile 
renk sınıflandırması yapılmaktadır. Metot akış şeması Şekil 
2’nin (B)→(C4) dalında gösterilmiştir. 
III. 
DENEYLER 
A. Veri Seti  

Bu çalışmada yerden yaklaşık 4,5 metre yukarıda askı 
köprü üzerine yerleştirilmiş 3 MP (2048x1536) renkli 
görüntü çekme özelliğine sahip bir kamera kullanılarak veri 
toplama işlemi yapılmıştır. Şekil 4’de bu çalışmada 
kullanılan resimlerden çeşitli örnekler gösterilmektedir. 


Şekil 4. Veri setimizde bulunan görüntülerden örnekler sunulmaktadır. En 
sağdaki araçta kırmızı renk ışığın araç üzerinde parlama oluşturmasından 
dolayı net değildir. 

Bu çalışmada geliştirilen metotların eğitim ve test 
aşamalarında kullanılmak üzere 1580 görüntü ayıklanmış ve 
etiketlenmiştir. 
Bu 
etiketli 
görüntülerin 
437’si 
test 
aşamasında 
kullanılmıştır. 
Veriler 
gerçek 
hayatta 
karşılaşılabilecek durumları içermesi açısından günün farklı 
saatlerinden seçilmiştir. Şekil 5’te test aşamalarında 
kullanılacak olan test kümesi verilerinin renk dağılımı 
gösterilmektedir. 
B. Deney Sonuçları  
       Bu çalışmada sunulan metotların performanslarını 
raporlamak için kesinlik, doğruluk ve hassasiyet metrikleri 
kullanılmaktadır.  

Şekil 5. Test veri setinde bulunan araçların renklerine göre dağılımı 
gösterilmektedir. 

Tablo I’ de araç görüntüsü sınıflandırma yönteminin, 
çalışmamızda kullanılan test veri seti için oluşturulan karışım 


---

# Page 4

matrisi sunulmuştur. Beyaz – gri, gri – yeşil ve mavi –siyah 
karışmasının diğer renklere göre daha yoğun olduğu 
gözlemlenmiştir. 
TABLO I. Araç Görüntüsü Sınıflandırma yöntemi kullanılarak veri seti 
üzerinde elde edilen karışım matrisi. Renk tanımlayıcı öznitelikler; Beyaz, 
Siyah, Gri, Mavi, Yeşil, Sarı, Kırmızı. 



Tablo II’ de sınıflandırmaya yönelik doğruluk, kesinlik 
ve 
hassasiyet 
sonuçları 
verilmiştir. 
Araç 
görüntüsü 
sınıflandırma yöntemi kullanılarak elde edilen doğruluk 
oranları çalışmamızda kullanılan veri seti için 0,81 olarak 
belirtilmiştir. 
Deneyler 
sonucunda, 
derin 
öğrenme 
yöntemlerinin renk sınıflandırmada, renk tanımlama ve renk 
kümeleme 
metotlarına 
göre 
daha 
başarılı 
olduğu 
gözlemlenmektedir. Ayrıca sonuçlar, sınıflandırmada bakılan 
alanın kapsamının renk tespiti başarısıyla doğru orantılı bir 
ilişki içinde olduğunu da göstermiştir. Aracın tamamı 
kullanılarak yapılan renk tespiti (Metot 1), araçtan alınan 
parçalar üzerinden yapılan tespitlere göre daha başarılı sonuç 
vermiştir. Bu sonuç, farklı yüzeylerdeki farklı gölgelenmeler 
ve yansımalar sebebiyle bölgesel renk değerlendirmelerinin 
yanlış yönlendirebileceğini göstermektedir.  

TABLO II: Test verisi üzerinde önerilen metotların doğruluk, kesinlik ve 
hassasiyet performansları gösterilmektedir. 


Doğruluk 
Kesinlik 
Hassasiyet 
Metot-1 
0,8009 
0,7863 
0,8269 
Metot-2 
0,7247 
0,7411 
0,7289 
Metot-3 
0,5388 
0,7024 
0,5559 
Metot-4 
0,6753 
0,7111 
0,5973 


Şekil-6’ da veri setimizden rastgele seçilen farklı 
renklerdeki araçlar üzerine uygulanan dört ayrı yöntemin 
sonuçları gösterilmektedir. 

Şekil 6. Önerilen 4 farklı yöntem kullanılarak farklı renk özniteliğine sahip 
araçlarla yapılan örnek çalışmanın sonuçları. Araç Görüntüsü Sınıflandırma 
metodu (metot 1), Kaporta Görüntüsü Sınıflandırma (metot 2), Renk Tanıma 
Özniteliği (metot 3), Renk Kümeleme (metot 4) 

IV. 
SONUÇLAR 


Bu 
çalışmada 
yol 
gözetim 
kamera 
görüntüleri 
kullanılarak yeni renk tabanlı araç sınıflandırma yöntemleri 
önerilmektedir. Önerilen öğrenme tabanlı sistemde tek 
seferde çoklu kare (SSD) metodu kullanılarak araç tespiti ve 
araç kaporta tespiti yapılmakta olup, bu parçalar üzerinden 
derin öğrenme, renk tanımlama ve renk kümeleme yöntemleri 
ile araç renk tespiti yapılmaktadır. Gölge, yüzey yansımaları 
ve parlaklık gibi sistemin performansı düşüren etmenlerden 
en az etkilenen metodun tüm araç görüntüsü üzerinden 
yapılan renk tespiti olduğu gözlemlenmiştir. Önerilen 
sistemin performansı 437 araç görüntüsü ile test edilmiştir ve  
% 80,1 sınıflandırma başarısı sağlanmıştır. 
V. 
KAYNAKÇA 

[1] L. Brown, A. Datta, S. Pankatti, ”Tree based color classification using spatial 
features on publicly available continuous data”, Advance Video and Signal Based 
Processing (AVSS), 2013 IEEE International Conference on IEEE, 2013. 
[2] J. W. Hsieh. “Vehicle color classification under different lightining conditions 
through color correction.” in International Symposium on Circuits and Systems 
(ISCS), 2012. 
[3] 
Akıllı 
ulaşım 
sistemleri 
tanımı 
ve 
kapsamı,  
www.biltir.metu.edu.tr/au_dergi1.pdf 
[4] S. Özturk, B. İnan, Y. Artan. “Gözetim Videolarında Renk Tabanlı Araç 
Sınıflandırma”, IEEE Sinyal İşleme ve İletişim Uygulamaları Kurultayı (SIU), 
2016. 
[5] C. S. Regazzoni, A. Cavallaro, Y. Wu, J. Konrad, and A. Hampapur. “Video 
analytics for surveillance: Theory and practice.“ IEEE Signal Processing 
Magazine, 27(5):16–17, 2010. 
[6] X. Liu, W. Liu, T. Mei, H. Ma, “A deep learning based approach to progressive 
Vehicle Re-identification for Urban Surveillance,” in ECCV 2016, pp. 869-884, 
2016. 
[7] D. Zapletal, A. Herout, “Vehicle Re identification for Automatic Video Traffic 
Surveillance,” in CVPR-Workshop 2016, pp. 1-7, 2017. 
[8] M. Yang, G. Han, X. Li, “Vehicle color recognition using monocular camera.” 
IEEE Conference on Wireless Communication and Signal Processing,, 2011. 
[9] Global Automotive 2016, Color Popularity Report, 2016.  
[10] R. F. Rachmadi, K. Purnama,  M. H. Purnomo, “Vehicle Color Recognition 
using Convolutional Neural Network” arxiv:1510.07391v2, 2015. 
[11] J. V. D.Weijer, C. Schmid, J. Verbeek, D. Larlus. “Learning color names for 
real-world applications,” IEEE Transactions on Image Processing, vol. 18 no. 7, 
pp. 1512–1523, 2009. 
[12]  W. Liu, et al., “SSD: Single Shot MultiBox Detector”, in: Leibe B., Matas 
J., Sebe N., Welling M. (eds) Computer Vision – ECCV 2016. ECCV 2016. 
Lecture Notes in Computer Science, vol. 9905. Springer, 2016. 
[13]  K. Simonyan, A. Zisserman, “Very Deep Convolutional Networks for Large-
Scale Image Recognition”, arXiv:1409.1556, 2014. 



        # Instruções de Metadados
        NÃO gere metadados no corpo da resposta.

        # Etapa atual
        Você está executando o **Passo 3: Terceira passada**.

        **REGRAS ESTRITAS DE FORMATAÇÃO (PARA TODAS AS ETAPAS)**:
1. NÃO inclua textos introdutórios (ex: 'Você está executando...', 'Seguem os resultados...').
2. NÃO repita seções como '# Objetivo', '# Metadados', '# Referência do paper'.
3. Comece a resposta DIRETAMENTE com o conteúdo solicitado no template.

        ## Passo 3: Terceira passada
Para compreender completamente um artigo, especialmente se você é um revisor, é necessário fazer uma terceira passada. A chave para a terceira passada é tentar recriá-lo virtualmente: ou seja, fazer as mesmas suposições dos autores, recriar o trabalho. Comparando isso com o artigo real, você pode facilmente identificar as inovações do artigo e seus pontos fracos.

Essa passada requer muita atenção aos detalhes. Você deve identificar e desafiar todas as suposições em cada declaração. Além disso, você deve pensar sobre como apresentaria um determinado conceito.

Essa comparação entre o real e virtual lhe dará um insight muito mais profundo sobre as técnicas de prova e apresentação no artigo e pode facilmente adicionar isso à sua coleção de ferramentas. Durante essa passada, você também deve anotar ideias para futuros trabalhos.

A terceira passada pode levar cerca de quatro ou cinco horas para iniciantes e cerca de uma hora para um leitor experiente. No final dessa passada, você deve ser capaz de reconstruir a estrutura todo do artigo de memória, bem como ser capaz de identificar seus pontos fortes e fracos. Em particular, você deve ser capaz de identificar suposições implícitas, referências ausentes para trabalho relevante e possíveis problemas com técnicas experimentais ou analíticas.
        </USER>
