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



        # Paper (entrada)
        TEXTO DO PAPER:


---

# Page 1




Abstract 

Several recent investigations attempt to classify 
vehicles into a small number (5-7) of colors. A 
significant complication arises, however; a large 
proportion of vehicles (>50%) are various shades of 
gray: white, black, silver, gray, and variations such as 
gun metal and pearly white. Distinguishing such 
shades of gray in vehicle body color from lighting 
changes is an unsolved problem. Furthermore, 
previous studies have evaluated their performance on 
private 
datasets 
precluding 
a 
comparison 
of 
methodologies. In this paper, we release a public 
dataset with ground truth color classification for future 
evaluations and comparisons based on the publicly 
available i-LIDS data [9]. We describe a method to 
perform vehicle color classification into 7 frequently 
occurring colors including dark red, dark blue and 
light silver, using pose dependent vehicle detection,  
vehicle alignment, and vehicle body part masks. We 
introduce new features for tree-based vehicle color 
classification based on the reliability of color 
information and the relative color of various vehicle 
parts.  

1. Introduction 
As more digital video surveillance solutions are 
deployed, the need for accurate object characteristic 
measurements has become critical. Yet the ability for 
video analytics to extract useful attributes is limited. 
For example, although color is extremely useful and 
one of the first attributes to be used by people to 
describe vehicles, the ability to accurately characterize 
vehicle color has been extremely challenging.  
Although, there are many publications describing 
research in this area [1-8], commercial systems provide 
only a rudimentary ability to search for vehicles based 
on color and there are no industrial publications 
describing their accuracy. 
 There are many challenges to the problem of vehicle 
color classification.  First of all, the vehicle has to be 
found and segmented from the image. Second, the 
body of the car or a part of it such as the “hood”, needs 
to be segmented from the rest of the car. Thirdly, the 
pixels of the body of the car are used to determine the 
actual color of the car. Unfortunately, the color of these 
pixels may not actually represent the color of the 
vehicle due to lighting, reflections (specular and non-
specular) and shadows effects. Similarly, the time of 
day, the weather, and the settings of the camera such 
automatic white balance can all affect the observed 
color. Finally, as shown in Fig. 1, the colors of vehicle 
are not uniformly distributed. A majority of vehicles 
are either various shades of gray or very dark or very 
pale, such as dark navy or silver with a slight color 
cast.  


Figure 1. The color of some vehicles is very difficult to 
characterize. Top row: silver or white? Bottom row: black or 
navy? 

According to the 2011 DuPont Automotive Color 
Popularity Report [10] regarding the choice of colors 
in American cars, white is the top choice with 20% and 
silver and black are tied for second with 17% each. In 
addition, gray takes another 12%. Clearly an important 
task in vehicle color classification is to distinguish 
different shades of gray since more than half of all cars 
do not contain a hue. 




Tree-Based Vehicle Color Classification  
Using Spatial Features on Publicly Available Continuous Data 

Lisa M. Brown, Ankur Datta, Sharathchandra Pankanti 
IBM T.J. Watson Research Center 
Yorktown Heights, NY 10598 
lisabr@us.ibm.com 

2013 10th IEEE International Conference on Advanced Video and Signal Based Surveillance
978-1-4799-0703-8/13/$31.00 ©2013 IEEE
347


---

# Page 2



Method 
Colors 
Accuracy 
Pose 
Cameras 
Reso- 
lution 
Contin-
uous 
Samples 
#train/ 
#test 
samples 
Preprocess 
Segment 
Features 
Classifier 
Dule 
2010 
Black,  
Gray, 
White, 
Red, Blue, 
Green, 
Yellow 
83.5% 
Front 
N/S 
N/S 
No 
180/100 
train/test 
for each 
color 
No 
Given car, 
hood 
relative to 
license plate 
16 color 
space 
histograms 
K-NN, 
artificial 
NN, 
SVM 
Hsieh 
2012 
Black, 
Silver, 
White, 
Red,Blue, 
Green, 
Yellow 
94.02% 
Front 
1 
N/S  
No 
16648 
total 
Color 
correction 
[Reinhard] 
in train/test 
Fore ground 
detection & 
window 
removal 
28 polar 
bins from 
LAB, 6 
RGB  bins 
Multiple 
SVMs in 
tree 
structure 
Yang 
2011 
Black, 
Silver, 
White, 
Red,Blue, 
Green, 
Yellow 
89% 
Any 
view, 
front 
& rear 
shown 
N/S 
N/S 
No 
319 total 
Gauss filter 
Fore ground 
detection & 
& 
homogenous 
region 
detection 
Hue angle, 
saturation 
weighted 
hue sum, 
average 
intensity 
Empirical 
cut-offs 
Table 1. Comparison of recent methods in vehicle color classification [N/S = not specified] 


Figure 2. Distribution of vehicle colors in the U.S. 
Gray: white, silver, black, gray (20+ 17+17+12) =66% 

Furthermore,  the research conducted to date has 
been performed on in-house datasets making it difficult 
to evaluate and compare results across different 
approaches. In this paper, we introduce a publicly 
available dataset with ground truth annotation for 
vehicle color classification. We hope that the release of 
this dataset will encourage research in this task and 
provide a forum for comparison. We believe an 
important challenge for research in this area is an 
underestimation of the difficulty of the problem. 
Making a dataset available will provide useful training 
data for color classification systems and a verifiable 
benchmark for progress. 

2. Related Work 
Vehicle 
color 
classification 
methods 
can 
be 
categorized into four steps. The first step is based on 
image preprocessing and may include such processes 
as gamma correction, intensity normalization, color 
correction and noise filtering. The second step provides 
a segmentation of the vehicle or part of the vehicle for 
color analysis. This may be based on vehicle detection, 
license plate detection, and/or background subtraction. 
It also includes finding regions of the vehicle with a 
certain spatial relationship (i.e. to the license plate, or 
w.r.t. to the object segmentation) or specific properties 
such as color smoothness.  
 The third step is the selection of image features 
including the choice of color space (or color spaces). 
Typical 
features 
include 
histograms, 
statistical 
properties  such as the mean, majority,  co-occurrence 
or correlogram.  
The last step is a classification method (such as 
support vector machines, neural network, nearest 
neighbor etc.) and the associated similarity metric (or 
distance measure) such as Bhattacharya distance, L1, 
L2, color distance etc. 
 Table 1 compares three of the most recent 
methods including the reported accuracy, dataset 
attributes, and algorithm choices. Each of these works 
use in-house data, does not give the image resolution, 
and does not specify the number of cameras used. They 
each use 7 colors, but the data is not collected 
continuously and therefore does not represent the real-
world distribution. The resulting accuracies reported 
reflect this bias. The division between training and 
testing is also unclear. 
All the methods rely on either background 
subtraction or assume the vehicle window is given. 
This will not be sufficient in practice where cars may 
be too close together, and shadows and occlusions are 
prevalent. 
Yang et al. [7] claim to deal with any pose, but the 
method they describe relies on finding smooth regions. 
We believe this method will break down in many 
instances where both specular and non-specular 
reflections occur and body trim and shadows are 
common. 
Hsieh et al. [6] perform color correction on both 
training and testing data and have developed a 
promising approach using a tree-based classifier. Our 
method is based on a similar scheme in which we train 
separate classifiers for different distinctions in order to 
348


---

# Page 3



optimize performance. 
3. Public Vehicle Dataset 
To facilitate research in vehicle color classification, 
we have annotated the publicly available i-LIDS 
dataset (UK) [9]. This annotation can be downloaded 
from [14]. We use two high resolution (720x576) clips 
from scenario 3:  
2010-01-01-123030_720x576_PVTRN301b 
2010-01-01-123030_720x576_PVTRN301a 
The i-LIDS dataset includes many other clips of the 
same camera at different times of the day and under 
different weather conditions. It also includes clips from 
other cameras. This will be useful for extending the 
dataset as research in the area progresses.  
We believe an important value of this dataset is the 
availability of the original video. This will make it 
possible to test a broader set of research questions 
concerning vehicle classification. For example, it will 
be possible to evaluate different methods for vehicle 
extraction/segmentation and color correction.  It will 
also enable the use of multiple frames to improve color 
classification accuracy. Other vehicle attributes such as 
model or headlight type could also be explored.  
 Tables 2 and 3 show the statistics of the dataset 
and the distribution of colors that were found in the 
dataset. Every vehicle that passed along the road on the 
bottom right hand side of the video was annotated. In 
addition to the color, we also specified if the vehicle 
was not a car or if it contained multiple colors. An 
example frame from the video is shown in Figure 3. 
Determining the number and specific distinct color 
categories was very challenging. In an effort to 
determine as many categories as possible, we had the 
user specify two levels of information. First, the user 
specified the color as one of 7 categories: black, white, 
silver, blue, green, yellow, and red. After specifying 
the color, the user then specified the color saturation 
and brightness by specifying one of 6 categories: light, 
medium, dark, pale light, pale medium, pale dark. The 
“pale” categories were needed to label vehicles which 
were difficult to categorize.  In practice there were two 
types of instances that required the “pale” category: 
cars which were either dark blue or black and cars 
which were light silver or white. If the user had 
difficulty deciding which category, these vehicles were 
labeled pale dark blue and pale light silver 
respectively. Examples are shown in Figure 1 and the 
distribution of pale samples for each color class is 
shown in Figure 4. 




Total 
#Frames 
Non-
Car 
Multi-
colored 
Visible 
Color 
Ambiguous 
color 
506 
89K 
18 
25 
378 
85 
Table 2. i-LIDS video ground truth distribution.  


Figure 3. Example frame from i-LIDS dataset [9]. Each 
vehicle that traverses the road on the right is annotated as it 
passes along the bottom right. Notice the difficulty in 
discerning the color of each vehicle.    

 To gain some insight into how challenging these 
examples were, we took 12 examples of pale dark blue 
and pale light silver and had 5 different users label 
them either dark blue or black for the pale dark blue 
examples and either light silver or white for the pale 
light silver examples. Figure 5 shows the histogram of 
label frequency for pale dark blue alongisde the 
histogram for pale light silver. In only 1/12 of these 
examples, users were able to agree upon the label for 
these vehicles. However, in another 5/12, users were 
unable to consistently label the vehicle. 


Table 3. Color Distribution of Ground Truth Data  


0
20
40
60
80
100
black white silver
red
blue green yellow
dark
medium
light
349


---

# Page 4




Figure 4. Histogram of vehicles with uncertain color 
categorization – i.e. between the specified color and either 
white, silver or black. 


Figure 5. Histogram of the number of users who agree on the 
color of a vehicle from the “pale dark blue” and “pale light 
silver” collection. There were 5 users. The histogram shows 
that for many of the examples in the collection the users were 
inconsistent about the color label they associated with the 
given vehicle sample. Inconsistent is 3/5 agree and all agree 
is 5/5 agree. For some examples (the middle bar) 4/5 agree. 

4. Method 
In order to deploy vehicle color classification for 
different cameras, for vehicles at different poses, we 
utilize pose-dependent vehicle detection developed by 
Behjat et al.[12]. Vehicle detection can be applied in 
many situations where standard foreground detection 
may fail – particularly in crowded scenarios, partial 
occlusions and fast lighting changes. This system uses 
12 different vehicle detectors to detect vehicles whose 
poses vary every 30 degrees. The method is very 
general and has been shown to be both fast and 
accurate.  Once detected, the pose is known and can be 
used to apply the proper vehicle body segmentation 
and pose-dependent color classifier. 
 For each vehicle that is detected, the pose is given 
within 30 degrees. We then apply the entropy 
minimization method of Huang [13] to refine the 
alignment between all vehicles of this pose. This 
method 
works 
particularly 
well 
for 
vehicles. 
Furthermore, the model for each pose can be built off-
line, and the alignment for a new detection can be 
efficiently applied at run-time. 
Alignment allows us to find relative body parts of 
cards such as the hood, the windshield, and the side of 
the car using various car body part masks. Examples of 
the alignment and car body part extraction are shown 
in Fig 6. 
 Our approach is a tree-bases classification similar in 
spirit to that used by Hsieh[6].  At each node of the 
tree, the system uses a sub-classifier with features 
optimal for the specific decision. The tree of sub-
classifiers, their specialized features, and its layout are 
shown in Fig. 7. 
 Once the body part is extracted, we measure each 
feature for every pixel in the given region. We first 
separate cars with color from cars without color. To do 
this, we measure the amount of color information in 
each body part using the color strength metric 
developed by Brown [11]. The color strength metric 
takes into account the reliability of the color 
information at each pixel based on the saturation and 
hue.  This has been shown to accurately predict the 
error in the hue measurement. We use three features 
based on the color strength (CS) metric: 

         ∑   






                 ∑



∑






For these measures, we use only pixels i  in the hood of 
the car. N is the number of pixels in the hood region. 
 If a car is classified as chromatic, it is then sub-
classified based on its hue. For this classifier the CS 
weighted Hue metric is used. If the car is achromatic, 
we then classify the vehicle as light or dark. For this 
classifier we use the normalized intensity. We 
normalize the intensity based on the road color. 
 For each color, we further sub-classify based on 
brightness, since this is a useful categorization given 
the  distribution of vehicle colors seen in practice. We 
use both the normalized intensity and the average color 
strength. 
 Finally, we classify light achromatic cars into light 
silver and white given the large number of cars found 
in these categorizations. This is a very challenging 
differentiation, and we found the most useful cues to 
be the variance in the intensity,  the difference between 
the hood and the side of the car, and the difference 
between the hood and the windshield.  
 We 
tested 
both 
k-nearest 
neighbor 
(NN) 
classification (k=3) and least squares (LS). These 
0
10
20
30
40
50
60
silver
red
blue
green
yellow
Pale Dark
Pale Medium
Pale Light
0
1
2
3
4
5
6
7
inconsistent
all agree
Navy/Black
Light Silver/White
350


---

# Page 5



methods were selected since we did not have sufficient 
training data for more complex machine learning. Also, 
since we built several sub-classifications and we use a 
small number of features, they were both practical and 
efficient. 


Figure 6. The flow chart of the method is shown in the 
center. Examples of pose-dependent detection are shown 
above and below on the left. Examples of these detections 
after alignment are shown in the center. Examples of the 
extracted vehicle body parts and the road are shown on the 
right. 

Figure 
7. 
Tree-based 
classifier 
for 
vehicle 
color 
classification into 7 categories and the associated features 
used at each decision point. 
5. Results of Vehicle Color Classification 
 The results of our system are shown in Table 4. 
Least squares classification was superior to nearest 
neighbor. The chart also shows the advantage of using 
the color strength metrics.  The methods were tested 
using cross validation since our dataset is small. The 
data was divided into 20 parts. The results are averaged 
over 20 tests, each using 19 parts for training and the 
remaining part for testing. 
 The total accuracy is based on the relative amount of 
data in each color category and is therefore realistic for 
real-time performance where this distribution is 
realized. Since our data was constructed from 
continuous sampling, we believe this is an important 
aspect of the system and should in practice be the 
metric used. For LS classification including the color 
strength metrics, we obtained 91% accuracy including 
differentiating cars that are red from dark red, blue 
from dark blue and white from light silver. These are 
each difficult categorizations with some noise in the 
ground truth data. We expect our accuracy is at least 
partially limited by the accuracy of the ground truth 
data. In some cases, the system performance is 
possibly improving upon the ground truth. 

Sub-Classifier 
NN - No CS LS - No CS NN 
LS 
Chromatic vs. Achromatic 
81% 
99% 
93% 
100% 
Hue (Red vs. Blue) 
80% 
99% 
58% 
99% 
Dark vs. Light Red 
70% 
77% 
90% 
93% 
Dark  vs. Light Blue 
68% 
73% 
75% 
82% 
Light vs. Dark 
99% 
99% 
100% 100% 
White vs. Light Silver 
86% 
86% 
76% 
83% 
Total Accuracy 
73% 
83% 
76% 
91% 
Table 4. Results of each sub-classifier using a Nearest 
Neighbor (NN) classifier and Least Squares (LS) classifier 
with and without color strength (CS) features. 
6. Conclusions 
    We have introduced a new public dataset for vehicle 
color classification. The dataset is based on publicly 
available high resolution video from the larger i-LIDS 
dataset. This will enable research in the area to use 
video information when needed, and to extend the 
dataset in many ways: more cameras, different times of 
day, variations in lighting, vehicle tracks, background 
subtraction information, etc. Most importantly, it will 
provide a benchmark for comparative work. 
 The annotation provided is based on continuous 
sampling. In this way, the data is more representative 
of the underlying color distribution. We have also 
provided a benchmark system for vehicle classification 
on this dataset. This classification uses the underlying 
distribution to categorize vehicles into the most useful 
classes in practice. We have found that the following 7 
categories were useful for this dataset: white, light 
silver, red, dark red, blue, dark blue, and black. 
Although green and yellow are typically used by 
investigators, we did not find sufficient data for these 
351


---

# Page 6



categories. We believe these categories are useful and 
easy to implement and will only improve the accuracy. 
 Previous work in this area has been focused on 
primary color distinctions (typically using color 
histograms) and some initial work on distinguishing 
gray from white or black cars. In this work, we 
developed vehicle color classification based on the a 
priori distribution of vehicle color using new spatial 
features comparing the intensity and color of the 
different parts of the car. We also show the advantage 
of using the color strength metric, a measure of color 
reliability. We are able to classify vehicles into new 
relevant color classes: dark red, dark blue and light 
silver. 
 In future work, we would like to extend the dataset 
to more cameras, times of day, and different poses. We 
also intend to use a multi-shot approach in which more 
than one frame is used to improve accuracy. 
References 
[1]   Wu, Y-T., Kao, J-H, and Shih, M-Y,  “A Vehicle Color 
Classification Method for Video Surveillance System 
Concerning Model-Based Background Subtraction,” 
Advances in Multimedia Information Processing, 
Lecture Notes in CS Vol. 6297, 2010, pp369-380. 
[2]   Li, X. et al., “Vehicle Color Recognition Using Vector 
Matching 
Template,” 
2010 
Third 
International 
Symposium on Electronic Commerce and Security, 
p189-193. 
[3]   Fang, J.  et al., “Color Identifying of Vehicles Based on 
Color Container and BP Network,” Int’l Conf. on 
Business Management and Electronic Information 2011, 
Vol. 3, pp. 226-229. 
[4]   Xu, Z., Cao, J. “Vehicle Color Extraction Based on First 
Sight Window,” The 1st Int’l Conf. on Information 
Science and Engineering (ICISE2009). 
[5]  Kim, K-J., Park, S-M, and Choi, Y-J., “Deciding the 
Number of Color Histogram Bins for Vehicle Color 
Recognition,” 
2008 
IEEE 
Asia-Pacific 
Services 
Computing Conference. 
[6] Hsieh, J-W,  et al., “Vehicle Color Classification under 
Different 
Lighting 
Conditions 
through 
Color 
Correction,” 2012 Int’l Sym. on Circuits and Systems. 
[7] Yang, M., Han, G. and Li, X., “Vehicle Color 
Recognition using Monocular Camera,” 2011 IEEE Int’l 
Conf on Wireless Comm. And Signal Processing. 
[8] Dule, E., Gokman, M, Sabur Beratoglu, M., “A 
Convenient Feature Vector Construction for Vehicle 
Color Recognition,” Proc. of the 11th WSEAS Int’l 
Conf. on Neural Networks, NN 2010. 
[9] 
i-LIDS 
dataset 
from 
the 
UK 
Home 
Office, 
http://www.homeoffice.gov.uk/publications/science/cast
/ilids-dataset-application 
[10] Dupont Automotive Color Popularity Study 2011, 
http://pc.dupont.com/dpc/en/US/html/visitor/b/dr/s/color
/oem_popularity.html 
[11]  Brown, L., Datta, A., and Pankanti, “Exploiting Color 
Strength to Improve Color Correction,” International 
Symposium in Multimedia, Irvine California 2012. 
[12]  Siddiquie, B., et al. “Unsupervised Model Selection for 
View-Invariant 
Object 
Detection 
in 
Surveillance 
Environments,”  Int’l Conf. Pattern Recognition (ICPR) 
Tsukuba, Japan 2012. 
[13]  Huang, G., Jain, V, and Learned-Miller, E., 
“Unsupervised joint alignment of complex images,” 
Int’l Conf. on Computer Vision (ICCV) 2007. 
[14]http://researcher.watson.ibm.com/researcher/v
iew_project.php?id=4528 


















352


        # Instruções de Metadados
        NÃO gere metadados no corpo da resposta.

        # Etapa atual
        Você está executando o **Passo 5: Ideias e Trabalhos Futuros**.

        **REGRAS ESTRITAS DE FORMATAÇÃO (PARA TODAS AS ETAPAS)**:
1. NÃO inclua textos introdutórios (ex: 'Você está executando...', 'Seguem os resultados...').
2. NÃO repita seções como '# Objetivo', '# Metadados', '# Referência do paper'.
3. Comece a resposta DIRETAMENTE com o conteúdo solicitado no template.
REGRAS ESPECÍFICAS DO PASSO 5 (TRABALHOS FUTUROS):
- Liste TODAS as ideias de trabalhos futuros propostas pelos autores.
- Adicione uma seção '## Minhas Sugestões (Criativas)': Proponha 2 novas ideias baseadas no potencial do trabalho.
- Seja criativo e visionário nestas 2 sugestões.
- NÃO inclua 'Análise de Foco' neste passo.

        PASSO EXTRA: Ideias e Trabalhos Futuros.
Identifique o que os autores disseram que fariam a seguir, e então use sua criatividade para propor novos caminhos de pesquisa.
        </USER>
