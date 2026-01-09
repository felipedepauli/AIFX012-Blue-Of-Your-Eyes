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

Real-time Vehicle Color Identification for 
Surveillance Videos  

Chih-Yang Lin* 
Dept. of Computer Science & 
Information Engineering 
Asia University 
Taichung, Taiwan, R.O.C. 
e-mail: andrewlin@asia.edu.tw 
Cheng-Hao Yeh 
Department of Electrical 
Engineering 
National Sun Yat-sen University 
Kaohsiung, Taiwan, R.O.C. 
e-mail:showard308sec@gmail.com 
Chia-Hung Yeh 
Department of Electrical 
Engineering 
National Sun Yat-sen University 
Kaohsiung, Taiwan, R.O.C. 
e-mail: yeh@mail.ee.nsysu.edu.tw 


Abstract— Vehicles are one of the main detection targets of 
the traffic and security video surveillance system. In this paper, 
we propose an automatic vehicle color identification method for 
vehicle classification. The main idea of the proposed scheme is to 
divide a vehicle into a hierarchical coarse-to-fine structure to 
extract its wheels, windows, main body, and other auto parts. In 
the proposed method, the main body alone is used by a support 
vector machine (SVM) for classification. Experimental results 
show that the proposed scheme is efficient and effective and the 
proposed vehicle color identification is suitable for real-time 
surveillance applications. 
Keywords— vehicle color classification; tree structure; support 
vector machine 
I. INTRODUCTION  
Video surveillance is a technology that is widely used in 
our daily lives, especially for the monitoring of public security. 
In public security, traffic monitoring and vehicle detection are 
two important issues for the security administration. For 
example, the police may want to identify a specific vehicle in 
a surveillance footage to track suspicious criminals. In order to 
effectively monitor vehicles, an automatic vehicle color 
classification (VCC) system is required. 
For a vehicle color classification system, extracting 
features from a vehicle is the most critical task. In previous 
research, color histogram and HSV color space are common 
features used to VCC. In [1], the authors investigated how the 
dimensions of a histogram affect the similarity measurement 
between images. Chapelle et al. [2] showed that image 
classification can be implemented by SVM for high 
dimensional features. Sural et al. [3] analyzed the properties of 
hue, saturation, and intensity and proved that HSV (Hue-
Saturation-Value) color space outperforms the RGB color 
space.  
From these previous research results, we recognize that 
color histogram and HSV color space are two important 
features in the color classification research area. In this paper, 
we present a VCC approach with features extracted from the 
histogram of the HSV color space. The proposed scheme uses 
a recursive approach to partition a vehicle into a tree structure. 
Each node in the tree structure represents a part of the vehicle. 
Our goal is to select the main body of an auto called the 
representative image of the vehicle from the tree structure, 
which contains the dominant color of the vehicle.  Then, the 
features of the representative image are extracted from the 
HSV color space for the input of a SVM classifier. The 
classifier is used to distinguish four different colors: red, green, 
blue, and yellow. The rest of this paper is organized as follows.  
Related works of VCC is discussed in Section II. The propose 
algorithm is presented in Section III. Experimental results are 
presented in Section IV. Finally, conclusions are made in 
Section V. 
II. RELATED WORKS 
One of the challenges of conventional VCC methods is 
different shooting angles coming from different surveillance 
cameras. In [4], the detected vehicle is partitioned horizontally 
into three layers. Then, the authors set different conditions for 
different layers in order to remove the non-main body parts of 
the vehicle. However, the identification accuracy of the VCC 
of this method depends heavily on the shooting angle. In other 
words, this method fails in VCC when the shooting angle is 
not properly set. Therefore, this method is not applicable to a 
variety of situations. In [5], the authors extract the color 
histogram in HSI color space as the color feature of a vehicle 
without removing any non-main body parts. However, the 
noise greatly affects the accuracy of the VCC. In [6], authors 
constructed a special and-or graph (AOG) to represent vehicle 
objects, and detected vehicle objects using a bottom-up 
inference based on the AOG. The disadvantage of this method 
is that only front-view and rear-view of the vehicle can be 
used for detection, so their method cannot be widely used in 
various shooting angles and situations. 
In the following section, we examine the way to both 
effectively filter out the non-main body parts of the vehicle 
and design the VCC invariant to shooting angle. 
978-1-4799-3469-0/14/$31.00 ©2014 IEEE
59


---

# Page 2

III. THE PROPOSED VEHICLE COLOR CLASSIFICATION 
The proposed scheme is designed for different light  
conditions and shooting angles. Fig. 1 shows the flowchart of 
the proposed feature extraction for the SVM classifier. The 
first step of the feature extraction called “recursively 
singularize color algorithm” generates a representative image 
of the vehicle. A representative image contains only the main 
body of the vehicle and removes all its non-main body parts 
including wheels, windows, and shadows.  


Fig 2. SVM classifier construction. 
Then, the representative image generates a hue histogram for 
the input of the SVM. In the proposed scheme, four vehicle 
colors are identified by the SVM, which are red, green, blue, 
and yellow. The traditional SVM is a binary classifier. In 
order to extend the classifier to handle the four colors, any of 
the two colors generate a classifier. In this case, six classifiers 
altogether are generated for the VCC. Fig. 3 shows the SVM 
classifier construction for the VCC. 

A. 
Recursively singularized color algorithm 
A vehicle may contain several different colors, but the 
main body of the vehicle is what determines the representative 
color. The proposed strategy uses the color information of the 
detected vehicle image to decompose this image into several 
single color subimages. Since the proposed partition process is 
recursive, Image_In is defined as the input of the recursive 
function, and Image_H and Image_L are derived from 
Image_In. Initially, the detected vehicle image (Image_In) is 
transformed into the  HSV (Hue-Saturation-Value) color 
space. In the proposed scheme, only the hue channel is used. 
Then the mean value and the standard deviation of Image_In 
of the hue channel are represented as Mean_In and Std_In, 
respectively.  Equations (1) and (2) illustrate the calculates of 
these two parameters, where P(xi,yi) is the hue value of the i-th 
pixel in the image and N is the total pixel number of Image_In.  
1
( ,
)
_
N
i
i
i
P x y
Mean
In
N
=
= ¦
. 
(1) 
(
)
(
)
2
,
1
_
_
i
i
N
x y
i
P
Mean
in
Std
In
N
=
−
= ¦
. 
(2) 
The value of Mean_In is used to generate two subimages. 
If a pixel is greater than Mean_In, the pixel is classified into 
the Image_H category; otherwise, Image_L is generated for 
the pixels smaller than or equal to Mean_In. Similarly, 
Mean_H and Std_H representing the mean and thestandard 
deviation of the Image_H are obtained, and Mean_L and 
Std_L are generated for Image_L. The process is repeated until 
all the subimages become single color images. Therefore, a 
tree structure of a vehicle is generated. The single color 
criteria of an image are shown in (3) to (5). Equations (3) and 
(4) represent the color variations of the input image and (5) is 
used to measure the hue distribution of the input image. If (3) 

Fig 1. Feature extraction for the SVM classifier. 
978-1-4799-3469-0/14/$31.00 ©2014 IEEE
60


---

# Page 3

to (5) can be satisfied, the image is regarded as a single color 
image.  
For example, if one of the (3) to (5) cannot be satisfied by 
Image_In, it means that Image_In is not pure enough and 
Image_H or Image_L may be better representatives for the 
main body color of the vehicle. In this case, Image_H (or 
Image_L) is regarded as another new input image Image_In', 
and the new image is further partitioned into two parts 
Image_H' or Image_L' to evaluate (3) to (5) again.  

_
_
_
Std
In
Threshold
std
Std
H >

(3) 
_
_
_
Std
In
Threshold
std
Std
L >

(4) 
_
_
_
Mean
H
Mean
L
threshold
mean
−
<

(5) 
However, during the partition process, some subimages 
may be too small. If the size of Image_In is much smaller than 
that of the original vehicle, the subimage will be removed. 
This part will be discussed in the next subsection. The 
complete algorithm of the proposed partition process is shown 
in the following.  
• Recursively singularized color algorithm  
• Input: A vehicle image.  
• Output: A tree structure of the vehicle. 
• Step 1: Calculate the mean (Mean_In) of the input 
image Image_In. 
• Step 2: Set Mean_In as the threshold value and divide 
the input image into two parts, “image_H” and 
“image_L”  
• Step 3: Calculate the mean and the standard deviation 
of image_H, Mean_H and Std_H, respectively, and 
Mean_L and Std_L for image_L.  
• Step 4: If one of the Eqs. (3) to (5) cannot be satisfied, 
image_H (or image_L) will be treated as another new 
input image Image_In'. Go to step 1. Otherwise, a 
hierarchical coarse-to-fine tree structure of the vehicle 
is generated.  
Fig. 3 shows the partition result of the detected vehicle. In 
this example, Fig. 3(h) is too smaller so it is removed. 
Figs. 3(f), 3(g), 3(i), 3(j), and 3(j) will not be involved in 
the further partition process since Figs. 3(c), 3(d), and 3(e) 
all satisfy (3) to (5). In the next subsection, we describe 
how one of the Figs. 3(c), 3(d), and 3(e) is selected as the 
representative color of the detected vehicle. 


Fig. 3. The generation of the tree structure. 

B. 
Selection of the representative image 
The representative image contains the major color of the 
vehicle. Since the main-body of the vehicle, the area that helps 
determine the color of the vehicle, is always larger than the 
noise area, the subimages in the tree structure can be removed 
if their size is too small. In order to filter out the small sub-
images, the minimal size of a subimage is set by (6). If the 
subimage size is smaller than the threshold, the subimage is 
removed. In (6), the qualified_subimagei means that the 
subimage has passed the criteria from (3) to (5) and could be 
the valid candidate for the vehicle’s representative image. 
Therefore, the threshold is set by selecting the maximal size of 
the valid candidate multiplied by 0.8. In our previous example, 
Fig. 3(h) is removed because its size is not larger than or equal 
to the threshold. 
0.8 max(
_
)
i
threshold
qualified
subimage
=
×

(6) 
After the noise subimages are removed, one of the 
remaining subimages will be selected as the main body of the 
978-1-4799-3469-0/14/$31.00 ©2014 IEEE
61


---

# Page 4

vehicle. According to our observation, the main body of the 
vehicle usually contains more prominent color information 
than the other parts. In other words, the colors of the non-main 
body parts of the vehicle are usually close to gray. Therefore, 
(7) is used to determine whether there exit a dominant color 
other than gray in the subimage. If a pixel’s color is not gray, 
the differences between its R, G, and B values should be large. 
Equation (7) shows the channel difference of a pixel.  
(
)
(
)
Channel difference
max
,
,
min
,
,
R G B
R G B
=
−

(7) 
In the above formula, the average channel difference of 
each of the sub-images is calculated. The sub-image that has 
the greatest channel difference will be selected as the 
representative image of the vehicle. 

C. 
Extracting features and building SVM classifier 
This subsection describes how the SVM classifier of four 
colors classification is built: red, green, blue, and yellow. 
First, for each color, randomly select N vehicle images as the 
training data. Then, the hue histogram of the representative 
image is used as the feature of each vehicle. The dimensions 
of the hue histogram is set to 360. In the training phase, any of 
the two colors will generate a classifier, so six classifiers will 
be generated altogether. In the testing phase, the test image 
will go through each classifier and the final result of the color 
identification will be decided by the six classifier. Since the 
sizes of representative images are varied, the normalization 
process in (8) of the histogram should be completed before 
training and testing. 
360
1
( )
_ ( )
( )
i
d i
Normalize
d i
d i
=
=
¦
, 
(8) 
where d(i) is the original value of i- th bin in the histogram. 
IV. EXPERIMENTAL RESULTS 
The following shows the experimental results of the 
proposed scheme. Fig 4. shows the results of the selected 
representative images of the four vehicle colors. Fig. 4(a) is 
the detected original vehicle images and Fig. 4(b) shows the 
representative images. The results show that the proposed 
method can successfully remove the non-main body parts of a 
vehicle properly. 
The number of images used for training and testing are 
listed in Table 1. In our method, only a small amount of data 
are used for training. 
Table 1. The numbers of images used in the training and testing phases 

Red 
Green 
Blue 
Yellow
Training 
data 
8 
8 
8 
8 
Testing 
data 
200 
200 
200 
200 

Table 2 lists the accuracy of the classification of the four 
vehicle colors. The "Original" in the table suggests that the 
detected vehicle is the input of the SVM directly without the 
proposed partition process. The results show that the proposed 
scheme improves classification accuracy, especially for the 
colors blue and green. In average, the accuracy is improved 
from 68% to 85.75%. 

Table 2. Accuracy of classification 
Red
Green 
Blue 
Yellow
Original
73%
55.5% 
57% 
86.5%
Proposed
85%
77.5% 
84% 
96.5%

V. CONCLUSIONS 
In this paper, we propose a VCC method for vehicle color 
classification. The image of the detected vehicle is first 
divided into several sub-images through the proposed 
recursive partition process. Then the selection of the 
representative image is used to choose the best representative 
image from the subimages. Finally, the extracted feature, the 
hue histogram, is used to establish the SVM classifier. The 
built SVM classifier is responsible for the classification of the 
four colors (red, green, blue and yellow). Experimental results 
show that the average accuracy of the proposed method 
reaches 85.75% and prove that the proposed method is 
feasible for vehicle color classification. 

ACKNOWLEDGMENT 
This work was supported by National Science Council, 
Taiwan, under Grants NSC 102-2221-E-468-017. 

REFERENCES 
[1] 
S. M. Lee, J. H. Xin, S. Westland, “Evaluation of image similarity by 
histogram intersection,” Color Research and Application, Vol. 30, No. 
4, pp. 265-274, 2005. 
[2] 
O. Chapelle, P. Haffner, V. N. Vapnik, “Support vector machines for 
histogram-based image classification,” IEEE Transactions on Neural 
Networks, Vol. 10, No. 5, pp.1055-1064, 2004. 
[3] 
Sural, G. Qian, S. Pramanik, “Segmentation and histogram generation 
using the HSV color space for image retrieval,” Proc. of IEEE 
International Conference on Image Processing, Vol.2, pp.589-592, 
2002. 
[4] 
Wu, Yi-Ta, Jau-Hong Kao and Ming-Yu Shih, "A vehicle color 
classification method for video surveillance system concerning model-
based background subtraction," Proc. of of the 11th Pacific Rim 
Conference on Advances in Multimedia Information Processing, pp. 
369-380, 2010. 
[5] 
Kim, Ku-Jin, Sun-Mi Park and Yoo-Joo Choi, "Deciding the number 
of color histogram bins for vehicle color recognition," Proc. of Asia-
Pacific Services Computing Conference,  pp. 134-138, 2008. 
[6]      Ye Li, Bo Li, Bin Tian, Qingming Yao, "Vehicle detection based on the 
AND–OR graph for congested traffic conditions," IEEE Transactions 
on Intelligent Transportation Systems, Vol. 14, No. 5, pp.984-993, 
2013 
978-1-4799-3469-0/14/$31.00 ©2014 IEEE
62


---

# Page 5





























Fig 4(a). Detected original vehicle images. 
978-1-4799-3469-0/14/$31.00 ©2014 IEEE
63


---

# Page 6





























Fig 4(b). Representative images. 

978-1-4799-3469-0/14/$31.00 ©2014 IEEE
64


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
