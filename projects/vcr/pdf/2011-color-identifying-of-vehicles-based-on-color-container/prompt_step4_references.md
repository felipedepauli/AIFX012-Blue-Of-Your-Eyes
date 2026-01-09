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

Color identifying of vehicles based on color container 
and BP network 

Jing Fang 
The Institute of Intelligent Information Processing and Appli-
cation 
Soochow University 
Suzhou, China 
Zoe0824fang@sina.com 

Hengjun Yue1, Xiuzhi Li1, Jian Wu1,2, Zhiming Cui1,2 
1The Institute of Intelligent Information Processing and Ap-
plication 
Soochow University 
Suzhou, China 
2Jiangsu Yihe Traffic Engineering Co., Ltd. 
Suzhou, China 
szjianwu@163.com 
Abstract—On the basis of model building and extracting of 
moving vehicles, the paper propose a new method to iden-
tify the vehicle color based on color container and BP 
neural network. The method analyze the contribution of 
three channel of the HSI color space, extract the vehicle 
features using container, design a special neural network 
for the experiment. The experimental results show that the 
accuracy rate of the color identifying is high and the error 
rate is low using this method, which overcome the short-
comings of the conventional method. 
Keywords- Color, BP network, container. 
I.  Introduction 
For the past few years, with the rapid development of the 
national economy and the rapid increase of motor vehicles, 
China's increasingly serious urban transport problems, traffic 
congestion, traffic accidents occurred frequently. To establish 
effective intelligent transportation systems (ITS), for effective 
traffic monitoring, traffic manage and traffic control has be-
come a pressing problem [1]. In addition to license plates, 
vehicle type and other vehicle features, color is also an im-
portant feature. Therefore, the vehicle color recognition as an 
important vehicle identification aids were valued by the re-
searchers[2]. Automatic identification of the vehicle color 
management system can overcome the low efficiency of con-
ventional vehicle management system and greatly improve the 
impact of the automation of vehicle management system. 
Most of the current vehicle color recognition algorithms 
are based on chromatic aberration, where chromatic aberration 
is the Euclidean distance between two points in the color 
space. The size of the distance of two points determines the 
color differences. However, the current research about vehicle 
color is still in its infancy and there are many unresolved is-
sues. The paper is based on the retrieving and mining system 
of vehicle in our laboratory, which make use of the type and 
color features of the vehicle and do searching, tracking, ana-
lyzing, understanding of the vehicle appear in the traffic video. 
Part of the process about the color characteristics is as figure 
1. 


Figure 1. Flow chart of the color recognition 
II. CONTAINER FOR COLOR 
 colorspace
To process color image, we must first select a appropri-
ate color space[3] and it is critical for color recognition to 
choose a color space which is consistent with the human visual. 
In a variety of proposed color space, RGB color space is the 
most practical one. As the earliest and most simple color rep-
resentation, it uses the principle sum of the three primary col-
ors of red, green and blue, with the RGB values to say the 
color. But the RGB color space is not a uniform color space, 
the color difference in the color space is not consistent with the 
human visual similarity. That is to say, the RGB color space is 

___________________________________ 
978-1-61284-109-0/11/$26.00 ©2011 IEEE  



---

# Page 2

simple but is different from the human visual characteristics. 
When dealing with color features, HSI color space is 
closer to human visual characteristics and do meet the experi-
mental demands. HSI color space is composed of three com-
ponents of hue, saturation, intensity (or brightness). Where the 
intensity (I) say the degree of bright or dark and saturation (S) 
say whether the color is undertone or deep. The three compo-
nents in this color space is independent and is with linear scal-
ability, the perceived color difference is proportional to the 
Euclidean distance of the points in the color space 
Figure 2 (a) and 2(b) are the color space schemes of RGB 
and HSI. 



(a) RGB                         (b)HIS 

Figure 2. Color space 

The HSI color space has the feature that it wipes the rela-
tion between the brightness and the color while the definition 
of saturation is closely related to the way people define the 
color. The feature mentioned above make HSI color space the 
ideal one to process images and it is more suitable for us to 
recognize the color of the vehicles. We get the values of RGB 
and transform them to the HSI color space using the formula as 
follows: 



2
1 (
)
3
3
1
min( ,
, )
2
arccos
2 (
)
(
)(
)
I
R
G
B
S
R G B
R
G
B
R
G
B
H
R
G
R
B G
B








 

























(1) 
According the transformational relation of the RGB and 
HSI, we can get the values of H,S,I from the values of R,G,B, 
where the values of R, G, B are the red, green, blue value of 
the pixels. 
B. Colorfeatureextractionbasedoncontainer
There are black, silver and white vehicles as well as the 
colorful vehicles in the traffic video and we divided the vehi-
cles as seven categories of black, white, silver, red, green, blue 
and yellow. Many experiments show that it results in low de-
tect results when we only consider the H component of HSI 
color space, especially for the white, silver and black vehicles. 
The values of the three channels we extract from each 
pixels of the vehicle are the microscopic characteristics of the 
vehicle and it is hard for us to process them because of its large 
amount of information. In this paper, we define seven contain-
ers as the macro values. We get seven values after classifying 
each pixel to the seven color categories and the seven values 
are related to the seven colors but are not linear. We induce the 
relationship of the values and colors using BP neural network. 
After lots of experiments about a variety of traffic 
video, we find in this article that when we use the HSI color 
space to process the vehicles object, the three values of the 
channels contribute to the color in the following specific rules.  
1) 
When the value of brightness is small enough, the pixel is 
black no matter how much the values of hue and saturation 
are. While it is white when the value of brightness is big 
enough. 
2) 
If it doesn’t meet the first case, we come to its value of 
saturation. If the saturation is smaller than some certain value, 
we can’t feel its colorful information no matter what the value 
of hue is. Then we can classify it to the black, silver or white 
category. 
3) 
In addition to the foregoing two categories, the pixel is 
colorful when the value of brightness is moderate and the 
value of saturation is large enough. Then we can determine 
the category of the pixel according to the value of hue. 
Follow the above rules, we can associate each pixel with 
one of the seven containers and finally get the value of the 
containers. The steps to get the container values are shown as 
figure3. 


Figure 3. Flow of container calculation 

In figure 3, given a pixel with the values of H, S and I, 
it is classified to black container if the value of I is bigger than 
I1
 while white smaller than I2. Then come to the value of S. If it 
is smaller than S1, we determine its category by the value of I. 
Lastly, we assumed it as some colorful container and classify it 
by the value of H. In the specific test, the thresholds of H, S 
and I are slightly different. 
To recognize the color of the vehicle, we consider not 



---

# Page 3

only the color information of vehicle body, which is talked 
above, but also the background. For example, there are lots of 
shadows in the video taken in a glare condition, and the color 
of the vehicle body will be affected in human eyes. In order to 
accurately identify the color of the vehicle, the overall bright-
ness information of the video should be taken into account. 
This paper considers the current frame backgrounds of the ve-
hicles. We extract the relevant value about the brightness of the 
background and study it in the BP neural network as one of the 
inputs. 
III.  BP NETWORK 
 IntroductionforBPnetwork 
Back propagation algorithm is also referred to as BP al-
gorithm[4,5], which successfully solved lots of learning issues 
about the connection weights of the neurons in hidden layer of 
the multi-layer network and finally promoted the development 
of the neural network. In 1899, Robert Hecht-Nielson proved 
that the BP network with only one hidden layer can approach 
any continuous function in a closed interval[6]. In another 
word, a 3-layer BP network can complete any N-dimension to 
M-dimension mapping. So we usually use the single hidden 
layer in BP network. 
The output of the network is on behalf of the system 
goal, so it is much easier for us to determine. There are two 
basic principles to select the inputs of the network. One is the 
feature should be easily detected or extracted; the other is they 
each other is irrelevant or has small correlation. Both the way 
to extract the inputs and the number of output are closely re-
lated to the problem to be solved, so the specific selection will 
be described below.  
How many hidden-layer nodes will be the most suitable 
for the current system is a complex problem and there are no 
specific theoretical guidance[7]. It is interrelated to the re-
quirements of the problems and the numbers of input and out-
put. If the number of hidden-layer nodes is too small, the net-
work will not be strong enough. While if the number is too big, 
the study will easily fall into local minimum and not the global 
optimum. Therefore, the principle to determine the number of 
the hidden-layer nodes is to meet the accuracy requirements as 
far as possible under the premise of taking a compact structure, 
that is to take as few hidden nodes as possible. 
The performance of the network is closely related with 
the training samples. There are two factors we should consider 
to design a good training set. The first is to determine the 
number of training samples. In general, the more training sam-
ples, the training results more accurately reflect its inherent 
laws. But there are often many constraints for collecting sam-
ples and it is difficult to improve the accuracy of the network 
when the number of sample is large enough. Thus, we refer to 
the rule that the samples are the 5 to 10 times of the weights of 
the network. The second is to select and organize the samples. 
The inherent law of the network is contained in the samples, 
which should be representative. The number of samples in 
each category should be roughly equal and the categories are 
all covered by the samples. 
 Thedesignofthenetwork
     The neural network structure is shown in figure 4. For 
this paper, it contains an input layer, an output layer and one 
hidden layer. 

Figure 4. The structure of BP neural network 

We divided the vehicles into seven categories of red, 
green, blue, yellow, black, white, silver. So the number of 
nodes in output layer is seven. When comes to the number of 
nodes in hidden layer, the paper conduct the number of the 
nodes through trial and error.  

s
n
m




                  (2) 

Where n is the number of nodes in the input layer, m  
output layer, s hidden layer, while a is an integer between 1 
and 10. After repeated trail of the same sample with different 
hidden layer nodes, we ultimately be sure that when the num-
ber of nodes in hidden layer is nine, the performance of the 
network is the best. 
The object to be processed in this experiment is the ve-
hicles in the traffic video. In order to prevent the large errors 
resulted by the different ways to get samples and test data, we 
extract all the samples from the traffic videos using the pro-
gram in this paper and the videos are under various conditions. 
IV.  EXPERIMENT AND DISCUSSION 
   Build the model using the Gaussian background model. 
Take two videos for example, as shown in figure 5, (a) and (c) 
are the source images of the video in cloudy day and sunny day, 
while (b) and (d) are the corresponding background images. 


(a) Source image in cloudy day      (b) Background image in cloudy day 



---

# Page 4


(c) Source image in sunny day       (d) Background image in sunny  day 
Figure 5. Source image and the corresponding background image 

The videos for our experiment are from the monitors of 
the highway and city roads from Suzhou. Extract all sorts of 
vehicle object in different colors and different shapes from the 
videos as the samples for the neural network and establish a 
large sample library as the training samples. 
Then we calculate the feature of container following the 
flow chart of containers and gain a large table of features com-
bined with the feature extract from the background. Train the 
neural network with the stable as input and get the final value 
of thresholds and weights of the network. Test the vehicle ob-
ject in the video using the network which is trained and display 
the results finally. Figure 6 shows the color identify results of 
the test in the video. 


Figure 6. The results of color identify. 

The trained neural network achieves good results in the 
test of identifying the color of the vehicles in the video. In this 
paper, we extract and select about 2000 samples from about 50 
video in different condition, each video is an average of 5 min-
utes. The test data are 20 videos which are similar to the train-
ing videos. Table 1 is the accuracy rate and error rate. 
TABLE I. 
THE ACCURACY RATE AND THE ERROR RATE 

Black
White
Sil-
ver 
Red 
Green
Blue
Yel-
low 
Accu-
racy 
rate 
83.4%
92.3%
88.9
% 
97.2
% 
98.1%
97.0
% 
97.3
% 
Error 
rate 
7.2% 
4.2% 
8.6% 
1.2
% 
2.4% 
0.5%
2.1%

As in the table 1, the accuracy rates of the colorful vehi-
cles are high while the error rates are very low. Because the 
black, white and silver vehicles usually affect by the lights and 
weather, the accuracy rate is lower than the colorful vehicles, 
while the error rate higher. But the results are better than other 
algorithms.  
V. CONCLUSION 
On the basis of analyzing the HSI color space, the paper 
proposed a method of the container to extract the features of 
the moving vehicles, design a special BP neural network to 
study the features. The test results are good when using the 
trained network to identify the vehicle color in the video. The 
next step is to identify the vehicle color at night or in rainy day, 
analyze and find the appropriate method. 
REFERENCES 
[1] Zhongke Shi, Li Cao. Detection and analysis of the traffic image. 
Beijing: Science Press, 2007:1-3(In Chinese). 
[2] Ming Chen. Models of neural network (M). Dalian, Dalian University of 
Technology Press, 1995:24(In Chinese). 
[3] Guohui Li. A color-based image retrieval method. Journal of Image and 
Graphics, 1999,4(3):248-255. 
[4] Juan Gao. The theory of Artificial Neural Network and the simulations. 
Beijing: China Machine Press, 2003:45-49(In Chinese). 
[5] D.E.Rumelhart. Learning representation by BP errors. Nature, 1986,7: 
149-154.  
[6] Nielsen R. Theory of the back-propagation neural network.. Proceeding 
of the International Joint Cenference on Neural Network, 1989:593-611. 
[7] Daqi Gao. Research of the Neural network structure with three layers 
prior to basic functions with a teacher. Chinese Journal of 
Computers.1998,21(1):26-2(In Chinese). 




        # Instruções de Metadados
        NÃO gere metadados no corpo da resposta.

        # Etapa atual
        Você está executando o **Passo 4: Extração de Referências**.

        **REGRAS ESTRITAS DE FORMATAÇÃO (PARA TODAS AS ETAPAS)**:
1. NÃO inclua textos introdutórios (ex: 'Você está executando...', 'Seguem os resultados...').
2. NÃO repita seções como '# Objetivo', '# Metadados', '# Referência do paper'.
3. Comece a resposta DIRETAMENTE com o conteúdo solicitado no template.
REGRAS ESPECÍFICAS DO PASSO 4 (REFERÊNCIAS):
- Liste as 5 referências mais importantes mencionadas no texto.
- Para cada uma, explique BREVEMENTE por que é importante no contexto do paper.
- Formato sugerido: '- [X] Autor et al. (Ano) - Título: Explicação...'
- NÃO inclua 'Análise de Foco' neste passo.

        PASSO EXTRA: Extração de Referências Prioritárias.
Analise a seção de Referências e as citações no texto para identificar as 5 obras fundamentais para entender este trabalho.
        </USER>
