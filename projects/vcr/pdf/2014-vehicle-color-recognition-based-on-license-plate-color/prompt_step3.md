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

Vehicle Color Recognition Based on License Plate Color 
Yanmei Dong, Mingtao Pei, Xiameng Qin 
Beijing Lab of Intelligent Information Technology, School of Computer Science 
Beijing Institute of Technology 
Beijing, China 
dongyanmei@bit.edu.cn, peimt@bit.edu.cn, qxm0405@bit.edu.cn 


Abstract—As a significant feature of vehicle, the color feature 
plays an important role in the intelligent transportation systems. 
However, the color feature is easily affected by the variations of 
the lighting condition. In this paper, we present a new method for 
vehicle color recognition, which is based on license plate color. 
The color of license plate is recognized by the prior knowledge 
and the recognition result of the license plate, which is not 
sensitive to the variations of lighting condition. We select the 
vehicle ROI (region of interest) near the license plate, and 
convert the color space of the plate image and the vehicle ROI 
image from RGB to HSV. The vehicle color is identified by the 
relative location of the ROI color and the plate color in the 
spectrum. We verify the feasibility of our approach through a 
comparison experiment. Experiment results show that the color 
of license plate is helpful to recognize the vehicle color. 
Keywords-vehicle color recognition, license plate color, HSV, 
color space, spectrum 
I. 
 INTRODUCTION 
Vehicle information recognition has played an important 
part in ITS (Intelligent Transportation Systems). As a 
significant feature of vehicle, color has received people’s 
attention in recent years. And extracting vehicle color 
effectively has become a hot problem. Dule et al. [4] used 
the plate position parameters to determine two kinds of ROIs 
(smooth hood peace and semi front vehicle), and made 
feature selection over the determined ROIs. He used three 
classification methods (K-Nearest Neighbors, Artificial 
Neural Networks, and Support Vector Machines) to classify 
vehicles into seven colors: black, gray, white, red, green, 
blue, and yellow. Li et al. [5] used vector matching of 
template and a color normalization operator to preprocess the 
images, and applied relative error distance matching 
algorithm to classify the vehicles into seven colors in HSI 
color space. Li et al. [6] recognized car-body color based on 
color difference and color normalization. Hu et al. [7] 
removed the useless part of vehicle body, estimated the 
impact of sunlight on each pixel, and recognized the vehicle 
color based on specular-free image. Brown et al. [8] used 
spatial features to identify vehicle color with tree-based 
method, and tested it on publicly available continuous 
dataset. 
In this paper, we present a new method to recognize 
vehicle color based on license plate color. We extract the 
license plate region and vehicle ROI near the license plate 
from vehicle image, and convert the color of the two regions 
from RGB space into HSV space. Then, we use the relative 
location of the vehicle ROI color and the license plate color 
in the spectrum to recognize the vehicle color. The color of 
license plate can be inferred from the prior knowledge and 
the recognition result of the plate, which is not sensitive to 
the variations of lighting condition. Therefore, the color of 
license plate can be used to recognize the vehicle color. 
The remainder part of the paper is organized as follows: 
color spaces, especially RGB color space and HSV color 
space are discussed in Section 2. In Section 3, we explain the 
details of our method. The experiment results are shown in 
Section 4, and conclusions are presented in section 5. 
II. 
COLOR SPACE 
The purpose of a color space (also called color model or 
color system) is to facilitate the specification of colors in 
some standard, generally accepted way [2]. Color space can 
be divided into three categories. First, the color space based 
on HVS (Human Vision System), which consists of RGB, 
HSI and Munsell color space, etc. Second, the color space 
based on specific applications, including YUV (be used in 
the television system), CMY (K) (be used in the printer 
system) and YIQ color space. The last one is called CIE 
color space, such as CIE, XYZ, Lab and Luv color space, 
etc. 
A. RGB Color Space 
RGB color space is one of the color standards for the 
industry, and one of the most commonly used color spaces. It 
is an additive color space in which red, green, and blue lights 
are added together in various ways to reproduce a broad 
array of colors [12]. In this color space, all the colors can be 
expressed by three components, R, G and B, which mean red, 
green and blue, respectively. When all the components have 
full intensity, the color is white, and when all the intensity is 
zero, the color becomes black. Zero intensity in two 
components and full intensity in the third component give a 
primary color of the third component. For example, 
component blue and green have zero intensity, and red 
component have the full, then the color is red. The RGB 
color space is represented by a cube in geometric, as shown 
in Figure 1.  
The RGB color space is device-dependent. The 
relationships between the composition amounts of the three 
components are unintuitive, and the resulting colors are not 
specified as absolute.  
2014 10th International Conference on Computational Intelligence and Security
978-1-4799-7434-4/14 $31.00 © 2014 IEEE
DOI 10.1109/.62
264
2014 10th International Conference on Computational Intelligence and Security
978-1-4799-7434-4/14 $31.00 © 2014 IEEE
DOI 10.1109/CIS.2014.63
264
2014 Tenth International Conference on Computational Intelligence and Security
978-1-4799-7434-4/14 $31.00 © 2014 IEEE
DOI 10.1109/CIS.2014.63
264


---

# Page 2


Figure 1.  RGB color model 
B. HSV Color Space 
HSV color space, which also named the “hexcone 
model”, is proposed based on the visual characteristics of 
color [1] in 1978. This color space has been widely used in 
scientific research, such as object tracking [9], face detection 
[10], and object detection [11]. 
HSV color model divides color into H (hue), S 
(saturation) and V (value), which apperceives color change 
independently [3]. It is represented by an inverted cone in 
geometric, as shown in Figure 2. In the inverted cone, the 
gray colors comprise the center vertical axis, which ranges 
from black at value 0 to white at value 1, and the value of the 
top is 1 while the bottom is 0. The component hue is 
represented by the angular dimension, which starting from 
pure red at 
o
0 , across pure yellow at 60° , pure green 
at120° , pure blue at 240° , and then turning back to pure red 
at 360°. The radial dimension of the cone, ranging from 0, 
the center, to 1, the edge, was labeled as saturation.  
HSV color space is more intuitive and perceptually 
relevant than RGB color space [13]. And the components H, 
S, and V in the HSV color space are more separating than the 
components R, G, B in RGB color space. 
A color can be converted from RGB color space to HSV 
color space with the following expressions: 
max(R, G, B)
min(R, G, B)
max(R, G, B)
S


 − 


=


,                (1) 
0,
0
60
max(R, G, B)
R& G
B
2
(B R)
60
, max(R, G, B)
4
(R
B)
60
, max(R, G, B)
6
(G
B)
60
, max(R, G, B)
&
S
G
B
S
V
H
G
S
V
B
S
V
R
G
B
S
V

=
−
×



=
≥
×
+
−
=
×



=
×
+
−
×



=
×
+
−
×



=
<
×












䯸
,      (2) 
max(R, G, B)
V =


,                              (3) 
where R, G and B are respectively the normalized values of 
the RGB color space. The ranges of components H, S and V 
are [0, 360)

, (0,1]
  and [0,1]

, respectively. 

Figure 2.  HSV color model 
III. 
VEHICLE COLOR RECOGNITION 
Our color recognition method is based on the color of the 
license plate. We extract the license plate region and vehicle 
ROI near the license plate from vehicle image, and convert 
the color of the two regions from RGB space into HSV 
space. Then, the relative location of the vehicle ROI color 
and the license plate color in the spectrum are utilized to 
recognize the vehicle color. 
Generally, the vehicle colors are classified into six 
categories: white, red, yellow, gray, blue and green. 
However, since the white and gray are not chromatic colors, 
we only examine red, yellow, blue, and green in our 
experiments. 
A. License Plate Processing 
From the existing license plate recognition system, we 
can get the recognition results of the license plate, including 
the license plate location and the type of the license plate 
(blue plates with white letters, white plates with black letters, 
and yellow plates with black letters.). 
The color of license plate can be inferred by the 
recognition results. A military vehicle, e.g., the license plate 
must be white. And the plate color of a double deck non-
military vehicle must be yellow, while the single ones have 
ordinary plates (blue plates). The blue and yellow plates can 
be distinguished by whether the letters are lighter or darker 
than the background. In order to reduce the influence of 
ambient light, we get the plate color not only by color 
recognition, but also utilize other information of the plates 
(for example, the structure of the plate). Some sample plate 
images are shown in Figure 3. 


Figure 3.  Some sample plate images 
265
265
265


---

# Page 3


Figure 4.  Some sample vehicles including the license plate, and the 
rectangles with green color are the selected ROIs 

Figure 5.  color location in the spectrum 
B. Vehicle ROI Processing 
In our method, instead of using the whole vehicle for 
color recognition, we use a region of interest on the vehicle. 
The ROI we selected is the region near the license plate. On 
one hand, the neighbor regions have similar lighting 
conditions.  On the other hand, the correspondences between 
the color information on license plate and the color of ROIs 
are constructed to improve the accuracy of the vehicle color 
recognition. 
We locate the position of the license plate by utilizing the 
license plate recognition system, and cut out the vehicle ROI 
near the vehicle license plate automatically. Then, we select 
the vehicle ROI from the right side or the left side of the 
plate. 
Before selecting the ROI, we convert the vehicle color 
image to grayscale image. Then select couples of rectangle 
regions from the left side and the right side of the plate, 
calculate the mean values and the variances of those regions. 
Finally, we select the area with the minimum variance as the 
vehicle ROI. Some sample vehicles including the license 
plate are shown in Figure 4, and the rectangles with green 
color are the selected ROIs. 
C. Recognition Process 
In HSV color space, the parameter H (Hue) represents 
the color information, and we can obtain the location of the 
color in the spectrum according to this value. Hence, we only 
use the parameter H to recognize the vehicle color. 
During the above two parts, License Plate Processing and 
Vehicle ROI Processing, we have converted the color of the 
final images from RGB space to HSV space. Thus, the 
parameters H of both the license plate and the vehicle ROI 
can be obtained directly. Simultaneously, we can compute 
the averages of the H values that defined as h plate  and h ROI . 
Then we utilize the relative location of h plate  and h ROI  in the 
spectrum to recognize the vehicle color. For example, in 
Figure 5, the H value of red color is about 0, and yellow 
color is about 60, so the location of yellow is at the right side 
of red, and green is located at the right side of yellow. 
Suppose h
h
ROI
plate
<
( h ROI  is at the left side of h plate ), if the 
plate color is yellow, then the ROI color must be red, for the 
reason that the h value ranges between 0 and 360. If the plate 
color is blue, then the vehicle color may be blue, green, 
yellow, or red, we can recognize the color by the difference 
between h plate  and h ROI . For instance, if the difference is 
less than 
o
60  ( 60
240
180
o
o
o
=
−
, we make an assumption 
that the color value of blue plate is 240o ), then the vehicle 
color is blue. If the difference ranges between 60o  and 
150o ( 240
90
o
o
−
), the vehicle color would be green. If the 
difference ranges between 150o  and 210o   ( 240
30
o
o
−
), the 
vehicle color would be yellow, otherwise, the vehicle color 
must be red. 
IV. 
EXPERIMENTAL RESULTS 
We implement a comparison experiment to verify the 
feasibility of our approach. That is, we compare the vehicle 
color recognition results with and without using the license 
plate color information. 
A. Data Set 
The vehicle images in our data set are collected in the 
real road at different time with different lighting condition. 
We divide all images into six classes: red, yellow, blue, 
green, white, and gray. We examine our method on four of 
them (red, yellow, blue and green), since white and gray are 
not chromatic color. Figure 6 shows some sample images in 
the data set. There are 306 images in our data set, and the 
size of every image is1600 1280
×
. 
B. Results 
In the experiment without using the license plate color 
information, we use the average of H value h ROI  to identify 
the vehicle color. At last, we have an accuracy rate of 0.73 
on the red vehicles, 0.93 on the yellow vehicles, 0.90 on the 
blue, and 0.40 on the green. The average accuracy rate on 
our data set is 0.69. 
We have better results by employing the license plate 
color information. As shown in TABLE I, the accuracy rate 
on the red vehicles is 0.73, the yellow is 0.93, the blue is 
0.97, and the green is 0.53. The average accuracy rate on the 
data set is 0.75. 
The experiment results show that the accuracy rates on 
red and yellow vehicle images have not been improved. The 
reason is that: we use the relative location of the ROI color 
and the plate color in the spectrum to recognize the vehicle 
color. However, most vehicles have ordinary plate (blue 
plate), and the color yellow and red are far away from blue in 
the spectrum while blue and green are closer. So the plate 
color is less helpful in the recognitions on red vehicles and 
yellow vehicles. 
266
266
266


---

# Page 4


Figure 6.  some sample images in our vehicle images data set, and the size 
of every image is 1600 1280
×

TABLE I.  
EXPERIMENT RESULTS 
Vehicle color 
Without plate 
Using plate 
red 
0.73 
0.73 
yellow 
0.93 
0.93 
blue 
0.90 
0.97 
green 
0.40 
0.53 
all 
0.69 
0.75 

All in all, the results show that our new method of 
vehicle color recognition based on license plate color is 
effective. 
V. 
CONCLUSION 
In this paper, we propose a new method for vehicle color 
recognition based on license plate color. We identify the 
vehicle color by the relative location of vehicle color and 
plate color in HSV color space. The experiment results show 
that our method of vehicle color recognition based on license 
plate color is effective and robust.  
REFERENCES 
[1] 
A.R.Smith, “Color gamut transform pairs”, ACM Siggraph Computer 
Graphics, vol. 12, no. 3, pp. 12-19, August , 1978. 
[2] 
B. Ahirwal, M. Khadtare, and R. Mehta, “FPGA based system for 
color space transformation RGB to YIQ and YCbCr”, Proceedings of 
IEEE International Conference on Intelligent and Advanced Systems, 
pp. 1345-1349, 2007. doi: 10.1109/ICIAS.2007.4658603. 
[3] 
Y. Lu., Y. Liu, Y. Guo, L. Kong, X. Chang, and X. Shan, “Features 
of human skin in HSV color space and new recognition parameter”, 
Optoelectronics Letters, vol. 3, no. 4, pp. 312-314, 2007, doi: 
10.1007/s11801-007-6175-3. 
[4] 
E. Dule, M. Gökmen, and M. S. Beratoglu, “A convenient feature 
vector construction for vehicle color recognition”, Proceedings of the 
11th WSEAS International Conference on NEURAL NETWORKS 
(NN'10), G. Enescu University, Iasi, Romania, pp. 250-255, June, 
2010. 
[5] 
X. Li, G. Zhang, J. Fang, J. Wu, and Z. Cui, “Vehicle color 
recognition using vector matching of template”, Third International 
Symposium of IEEE on Electronic Commerce and Security (ISECS), 
pp.189-193, July, 2010. doi: 10.1109/ISECS.2010.50. 
[6] 
G. Li, Z. Liu, Z. You, and Y. Zhuang, “Car-body color recognition 
algorithm based on color difference and color normalization”, 
Computer Applications, vol. 24, no. 9, pp.47-49, 2004. 
[7] 
W. Hu, J. Yang, L. Bai, and L. Yao, “A new approach for vehicle 
color recognition based on specular-free image”, Sixth International 
Conference on Machine Vision (ICMV 13). International Society for 
Optics and Photonics, pp. 90671Q-90671Q, December, 2013. doi: 
10.1117/12.2051976. 
[8] 
L. M. Brown, A. Datta, and S. Pankanti, “Tree-based vehicle color 
classification using spatial features on publicly available continuous 
data”, 10th IEEE International Conference on Advanced Video and 
Signal Based Surveillance (AVSS), pp. 347-352, August, 2013. doi: 
10.1109/AVSS.2013.6636664. 
[9] 
J. G. Allen, R. Y. D. Xu, and J. S. Jin, “Object tracking using 
camshift algorithm and multiple quantized feature spaces”, 
Proceedings of the Pan-Sydney area workshop on Visual information 
processing. Australian Computer Society, Inc., pp. 3-7, June, 2004. 
[10] O. Ikeda, “Segmentation of faces in video footage using HSV color 
for face detection and image retrieval”, Proceedings of IEEE 
International Conference on Image Processing, vol. 3, pp. III-913-6,  
Sep. 2003, doi: 10.1109/ICIP.2003.1247394. 
[11] R. Cucchiara, C. Grana, M. Piccardi, A. Prati, and S. Sirotti, 
“Improving shadow suppression in moving object detection with 
HSV color information”, Proceedings of IEEE International 
Conference on Intelligent Transportation Systems, pp. 334-339, 
August, 2001, doi: 10.1109/ITSC.2001.948679. 
[12] Wikipedia, “RGB color model”, http://en.wikipedia.org/wiki/RGB 
color_model . 
[13] Wikipedia, “HSL and HSV”, http://en.wikipedia.org/wiki/HSL_and 
HSV#Motivation.   

267
267
267


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
