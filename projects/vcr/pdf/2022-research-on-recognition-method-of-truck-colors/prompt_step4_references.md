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

Research on Recognition Method of Truck Colors 
Based on Convolutional Neural Network Model 

Jian Cui1, Chuangang Kang1, Xiaogang Ma1, Rong Cao1, Xuehui Chen1, Hao Li2, Jing Zhang2, Chihang Zhao2, *, Teng Ma3, Xinliang Wang3 
1Shandong Hi-speed Company Limited, Jinan 250014, P. R. China 
2School of Transportation, Southeast University, Nanjing 210096, P. R. China 
3Shandong Hi-peed Xinwei Information Technology Company Limited, Jinan 250102, P. R. China 
2003cuijian2003@163.com, 8917119@163.com, maxg@sdecl.com.cn, redleaves_3@126.com, cxh1225@163.com, 1728715170@qq.com, 
461536205@qq.com, chihangzhao@seu.edu.cn, mateng79@163.com, lonelywell@163.com 
* Corresponding author: C. Zhao, Email: chihangzhao@seu.edu.cn 
Abstract—Truck color is one of the important information of 
vehicle ownership in intelligent transportation system. Aiming at 
the problem that truck color recognition is easy to be affected by 
complex scene and illumination changes, this paper studied the 
truck recognition method based on convolutional neural network, 
constructed the truck color image set, transformed truck vehicle 
image samples into RGB, HSV, and LAB color spaces. A truck 
color recognition method based on convolutional neural network 
model is proposed and experimental research is proposed. The 
experimental results show that the performance of the proposed 
convolutional neural network model based on LAB color space is 
better than that of proposed convolutional neural network model 
based on HSV color space, and achieved a verification accuracy at 
96.36%. 
Keywords—Intelligen Transportation System (ITS), Vehicle 
Ownership, Convolutional Neural Network (CNN), Truck Color, 
LAB Color Space 
I. 
INTRODUCTION 
Truck recognition is one of the key important methods of 
truck attribute recognition, which is widely used in the fields of 
vehicle recognition in expressway scene, non-stop charging, 
truck violation inspection and so on. Truck color information is 
one of the key information of vehicle besides truck license plate 
information. By truck color recognition, the weakness of vehicle 
recognition based on single vehicle attribute could be made up, 
which could play an important role in combating false license 
plate. However, because of the influence of factors such as long 
vehicle driving time, complex road scene and illuminations 
changes, it is difficult and challenging to realize accurate 
recognition of truck color through truck image. Therefore, how 
to realize the accurate recognition of truck color through truck 
image has become an urgent problem to be solved in the field of 
intelligent transportation system. In 2017, Xue et al. [1] adopted 
a vehicle image fusion processing method including histogram 
equalization 
method, 
local 
contrast 
enhancement 
and 
homomorphic filtering method to process the vehicle image and 
improve the accuracy of vehicle color recognition. In 2017, 
Aarathi et al. [2] proposed a method to solve the problem that 
vehicle images taken from roads or hill areas could not be 
effectively recognized because of haze, which mainly adopts the 
dark channel prior technique and CNN to remove the haze and 
learn feature respectively. In 2018, Kim et al. [3] proposed a 
vehicle color classification method based on representative color 
region extraction and convolutional neural (CNN), which 
randomly selects points from the probability map of 
representative color region produced by Harris corner detection 
method to generate an input image for CNN model training. In 
2018, Zhang et al. [4] proposed a vehicle color recognition 
method based on a lightweight CNN which contains three 
convolutional layers, a global pooling layer and a fully 
connection layer. Compared with traditional vehicle color 
recognition method, this method could reduce the dimension of 
feature vector and the memory occupation of the model, at the 
same time improve model accuracy slightly. In 2019, Sun et al. 
[5] integrated the trained vehicle brand recognition network and 
vehicle color recognition network based on the training mode of 
multi-task learning, and constructed a vehicle multi-attribute 
recognition model. In 2019, Zhang et al. [6] built a vehicle color 
recognition network model based on deep convolution neural 
network by adjusting structure and parameters of Deep-VGG-
16 model. In 2020, Fu et al. [7] put forward a multi-scale 
comprehensive feature fusion convolutional neural network 
(MCFF-CNN) based on residual learning to solve the problem 
of automatic vehicle color conditions, which first extracts the 
dark color features of vehicles through MCFF-CNN network, 
and then through support vector machine (SVM) classifier to 
obtain the final color recognition results. In 2021, Tariq et al. [8] 
proposed a vehicle detection and vehicle color classification 
method based on Faster R-CNN to solve the problem that the 
commonly used recognition methods rely heavily on hand-made 
features. In 2021, Awang et al. [9] studied at the impact of 
different schemes of color images on the performance of vehicle 
type recognition system, and compared the performance of 
vehicle feature extraction models under YCrCb and RGB color 
schemes. In 2021, Hu et al. [10] built a vehicle color database 
contains 24 vehicle colors and proposed a Smooth Modulated 
Neural Network with Multi-layer Feature Representation 
(SMNN-MFR) to solve the problem of long tail distribution in 
the dataset. 
At present, the research on truck color recognition is still 
considered as a part of the research of vehicle color recognition 
in a broad sense. However, due to the problems of low body 
cleanliness of truck, changeable road lighting and weather 
conditions caused by long-time driving, truck body color 
recognition is more difficult and challenging than other types of 
230
2022 IEEE 14th International Conference on Computer Research and Development
978-1-6654-2373-1/22/$31.00 ©2022 IEEE
2022 14th International Conference on Computer Research and Development (ICCRD) | 978-1-7281-7721-2/22/$31.00 ©2022 IEEE | DOI: 10.1109/ICCRD54409.2022.9730465
Authorized licensed use limited to: Tsinghua University. Downloaded on November 13,2022 at 16:17:37 UTC from IEEE Xplore.  Restrictions apply. 


---

# Page 2

vehicle color recognition, Therefore, it is necessary to study a 
specific color recognition method of trucks according to the 
special characteristics of trucks. 
The content of this article is arranged as following: The first 
is introduction, which mainly introduces the research 
background of this article. The second part is related work, 
which mainly introduce the methods and theories of truck color 
image data set construction and truck color recognition. The 
third part is experimental results and analysis. And the fourth 
part is the conclusion. 
II. 
METHODOLOGY 
A. Color space theory 
1) RGB color space 
RGB color space is a color space based on trichromatic 
principle, which could express most colors in nature by 
adjusting the brightness of red (R), green (G) and blue (B) and 
superimposing them. The three primary colors are independent 
of each other. None of primary colors could be superimposed by 
the other two colors. As shown in Fig. 1, by trichromatic 
principle, the required color C could be configured through RGB 
color, which means by adding and mixing three primary colors. 

Fig. 1. RGB color space 
2) HSV color space 
HSV color space is a color representation method according 
to the intuitive characteristics of color, which map points in 
RGB color space into the cone model.  In HSV model, H means 
hue, which represents color category, with the value range 
between 0° and 360°. S means saturation, which indicates the 
degree to which the color is close to the spectral color, with the 
value range between 0% to 100%, the more the proportion of 
spectral color, the higher the degree to which the color is close 
to the spectral color, and the more saturated the color is. V means 
value, which stands for the brightness of the color with the value 
range between 0% to 100%. The vertex of the cone model is the 
darkness point, indicating the pure black, and the center point of 
the cone ground is the brightness point, indicating pure white. 
The HSV color space is shown in Fig. 2. 

Fig. 2. HSV color space 
3) LAB color space 
LAB color space is a color space based on the international 
standard for color measurement formulated by the International 
Commission on illumination (CIE) in 1931. In LAB color space, 
L represents brightness, A and B are used to describe color. In 
an image, each pixel has a corresponding LAB value. L stores 
the brightness information of the image, the value range of it is 
[0,100], indicating from pure black to pure white. Component A 
represents the change from green to gray to red, and the value 
range is [-128,127]. Component B represents the change from 
blue to gray to yellow, and its range value is [-128,127]. The 
LAB model separates lightness from color. There is no color 
component in channel L, but only color component in channel 
A and channel B. Therefore, modifying the output of channel A 
and channel B could accurately represent the color, and channel 
L is used for brightness adjustment. The HSV color space is 
shown in Fig. 3. 

Fig. 3. LAB color space 
B. Truck color recognition method based on convolutional 
neural network 
Convolutional neural network is composed of convolutional 
layer, activation function, pooling layer full connection layer, 
dropout layer and so on. The main function of convolutional 
layer is to extract the local features of the input image and 
enhance the features of the input image. Each convolutional 
layer contains multiple feature planes, each feature plane 
represents a feature graph, and the number of convolutional 
cores determines the number of feature graphs. Activation 
231
Authorized licensed use limited to: Tsinghua University. Downloaded on November 13,2022 at 16:17:37 UTC from IEEE Xplore.  Restrictions apply. 


---

# Page 3

function changes the linear hidden layer into a nonlinear 
function. The activation function gives the convolutional 
network the ability to classify nonlinear functions, meanwhile, 
it affects the convergence of the network model. Therefore, the 
selection of activation function has a great impact on the 
accuracy and speed of convolutional neural network. Because 
there would be a large number of redundant convolution values 
after the convolution operation. The feature of pooling layer is 
to reduce the redundant values, minimize the number of model 
parameters and further expand the receptive field while retaining 
the image information to the greatest extent. Through the 
convolutional layer, activation function layer and pooling layer, 
the convolutional neural network could effectively extract the 
features of the input information, that is, the data input data is 
mapped to the high-dimensional hidden feature space. The 
function of full connection layer is to map the distributed feature 
information of the high-dimensional hidden layer feature space 
to the sample space and act as a classifier. Dropout means that 
in the process of neural network training, some hidden layer 
nodes are temporarily discarded according to a certain 
probability and their weights are stopped. The discarded nodes 
could be temporarily identified as not part of the network 
structure, and these nodes would not be updated when updating 
the weights. 
In this article, the structure of truck color recognition 
network based on convolutional neural network is composed of 
1 output layer, 3 convolutional layers, 3 maxpooling layers, 2 
full connection layers and 1 dropout layer. The input image of 
the whole convolutional neural network is three-channel image 
with the size of 64×128. The first convolutional layer adopts 32 
convolutional kernels with a size of 3×3, chooses ReLU as the 
activation function, and connects with a pooling layer with a size 
of 2×2. The second convolutional layer also adopts 32 
convolutional kernels with a size of 3×3, chooses ReLU as the 
activation function, and connects with a pooling layer with a size 
of 2×2. The third convolutional layer adopts 64 convolutional 
kernels with a size of 3×3, chooses ReLU as the activation 
function, and connects with a pooling layer with a size of 2×2. 
The extracted high-dimensional feature firstly connects with a 
full connection layer with 64 neural nodes, passes through the 
ReLU activation function, uses dropout with a dropout rate of 
0.5, and finally connects with a full connection layer with 6 
neural nodes, and then us Softmax to calculate the probability of 
truck color classification. 
III. 
EXPERIMENTS 
The experiment in this article is based on the SEU Truck 
Color Image Dataset (STCID), 60% of 1492 images in this 
dataset are used as training image, 20% of them are used as 
verification image and the remaining 20% images are used as 
test image. There are 6 types of truck color in this dataset, which 
are red, blue, white, yellow, green and black. The image set is 
transformed into HSV color space and LAB color space 
respectively, to obtain the image samples in three color spaces, 
and the three kinds of samples are input into the constructed 
convolutional neural network for training. In order to reduce the 
influence of redundant information brought by the air inlet hood 
with different color of the front face of the truck, the local area 
image of the front face of the truck is directly segmented to 
extract the left and right color block areas that do not include the 
air inlet hood, and then the color block areas are input into 
convolutional neural network to train. In the process of model 
training, the cross entropy loss function is selected as the loss 
function, and RMSprop and Adam are used as the optimizer for 
comparative experiments. The experimental results of CNN-
RGB, CNN-HSV and CNN-LAB using different optimizers are 
shown in Table Ⅰ. According to Table Ⅰ, the difference of 
optimizers has little impact on the model accuracy, which 
belongs to the normal error range. Therefore, it could be 
concluded that the selection of optimizer has little impact on the 
accuracy of convolutional neural network model. 
TABLE I.  
COMPARISON OF MODEL ACCURACY OF DIFFERENT 
OPTIMIZERS 

optimizer=RMSprop 
optimizer=Adam 

Train-
Accuracy 
Valid-
Accuracy 
Train-
Accuracy 
Valid-
Accuracy 
CNN-RGB 
0.9648 
0.9595 
0.9708 
0.9538 
CNN-HSV 
0.9536 
0.9438 
0.9615 
0.9437 
CNN-LAB 
0.9769 
0.9651 
0.9808 
0.9634 


(a) Bar Plot of Recognization 

(b) Box Plot of Recognization 
Fig. 4.  Comparison of accuracy of three models 
232
Authorized licensed use limited to: Tsinghua University. Downloaded on November 13,2022 at 16:17:37 UTC from IEEE Xplore.  Restrictions apply. 


---

# Page 4

The experimental results of truck color recognition method 
based on convolution neural network, which based on CNN-
RGB, CNN-HSV and CNN-LAB color spaces respectively, 
with RMSprop optimizer are shown in Fig. 4. According to the 
histogram in Fig 4 (a), the accuracy of the convolutional neural 
network based on LAB color space is 96.34%, which is slightly 
higher than those of the convolutional neural network models 
based on two other color spaces. The convolutional neural 
model based on RGB color space has an accuracy of 95.38%, 
which performs second best. The convolutional neural model 
based on HSV color space performs the worst with an accuracy 
of 94.37%. Fig. 4 (b) is the box diagram of three models, 
according to Fig. 4 (b), the average accuracy of the 
convolutional neural network model based on LAB color space 
is higher than that based on RGB color space, and the accuracy 
distribution span is smaller than that based on RGB color space, 
which means that the convolutional neural network model based 
on LAB color space not only has better performance, but also 
has better robustness and stability. The confusion matrix of truck 
color recognition experiment results based on convolutional 
neural network model is shown in Table Ⅱ. According to the 
confusion matrix, the correct classification rate of red and 
yellow is higher, followed by blue. The probably reason causing 
the higher correct classification rates of these two colors is may 
be these two kinds of colors have richer characteristics 
compared with other colors. 
TABLE II.  
CONFUSION MATRIX OF TRUCK COLOR RECOGNITION 
EXPERIMENT RESULTS 
Class 
Red 
Blue 
White 
Yellow 
Green 
Black 
Red 
99.06% 
0.31% 
0 
0.63% 
0 
0 
Blue 
0 
96.88% 
1.04% 
0 
2.08% 
0 
White 
2.07% 
0 
93.10% 
4.83% 
0 
0 
Yellow 
0 
0 
0 
100% 
0 
0 
Green 
0 
12.5% 
0 
0 
87.5% 
0 
Black 
0 
14.29% 
0 
0 
0 
85.71% 
IV. 
CONCLUSIONS 
In this paper, RGB color space, HSV color space and LAB 
color space are compared and analyzed, and the image samples 
of trucks are transformed into RGB, HSV and LAB color space 
respectively; A convolutional neural network model for truck 
color recognition is constructed, and the effects from RMSprop 
optimizer, Adam optimizer on the accuracy of the model are 
compared and analyzed. The experimental results based on the 
SEU Truck Color Image Dataset show that the selection of 
optimizer has little impact on the accuracy of the model. There 
are differences in the accuracy of truck color recognition models 
in different color spaces. The truck color recognition model 
based on convolutional neural network in LAB color space has 
better accuracy, and its accuracy reaches 96.34%. Meanwhile, 
colors of trucks also have an impact on the color classification 
accuracy. The best classification effect could be achieved for red 
and yellow Trucks. 
ACKNOWLEDGMENT 
The authors would like to thank Key Science and 
Technology Projects of Transportation Industry of Ministry of 
Communications (Grant No. 2020-MS5-134), Transportation 
Science and Technology Plan Project of Shandong Province 
(Grant No. 2020B36) and Science and Technology Project of 
Shandong High Speed Group Co., Ltd (Grant No. (2020) SDHS-
GSGF-09). Their assistances are gratefully acknowledged. 
REFERENCES 
[1] Xue, X., Ding, J. and Shi, Y, “Research and application of illumination 
processing method in vehicle color recognition” 2017 3rd IEEE 
International Conference on Computer and Communications (ICCC), 
Computer and Communications (ICCC), 2017 3rd IEEE International 
Conference on, pp. 1662–1666, 2017. 
[2] Aarathi, K. S., and Anish Abraham, “Vehicle Color Recognition Using 
Deep Learning for Hazy Images.” 2017 International Conference on 
Inventive Communication and Computational Technologies (ICICCT), 
Inventive Communication and Computational Technologies (ICICCT), 
2017 International Conference On, 335–39,2017. 
[3] Kwang-Ju Kim, Pyong-Kun Kim, Kil-Taek Lim, Yun-Su Chung, Yoon-
Jeong Song, Soo In Lee, and Doo-Hyun Choi, “Vehicle Color 
Recognition 
via 
Representative 
Color 
Region 
Extraction and 
Convolutional Neural Network.” 2018 Tenth International Conference on 
Ubiquitous and Future Networks (ICUFN), Ubiquitous and Future 
Networks (ICUFN), 2018 Tenth International Conference On. 89–
94,2018. 
[4] Zhang, Qiang, Li Zhuo, Jiafeng Li, Jing Zhang, Hui Zhang, and 
Xiaoguang Li. “Vehicle Color Recognition Using Multiple-Layer Feature 
Representations of Lightweight Convolutional Neural Network.” Signal 
Processing 147 (June): 146–53.2018. 
[5] Sun, J., Jia, C. and Shi, Z, “Vehicle Attribute Recognition Algorithm 
Based on Multi-task Learning”, 2019 IEEE International Conference on 
Smart Internet of Things (SmartIoT), Smart Internet of Things (SmartIoT), 
2019 IEEE International Conference on, pp. 135–141, 2019. 
[6] Zhang, M et al, “Vehicle Color Recognition Using Deep Convolutional 
Neural Networks”, AICS 2019: Proceedings of the 2019 International 
Conference on Artificial Intelligence and Computer Science. Pages 236–
238, 2019. 
[7] Fu, H. et al., “MCFF-CNN: Multiscale comprehensive feature fusion 
convolutional neural network for vehicle color recognition based on 
residual learning”, Neurocomputing, 395, pp. 178–187, 2020 
[8] Tariq, M. Z. Khan and M. U. Ghani Khan, "Real Time Vehicle Detection 
and Colour Recognition using tuned Features of Faster-RCNN," 2021 1st 
International Conference on Artificial Intelligence and Data Analytics 
(CAIDA), 2021, pp. 262-267, 2021. 
[9] S. Awang and N. M. Aizuddin Nik Azmi, "Performance Evaluation 
between RGB and YCrCb in TC-SF-CNNLS for Vehicle Type 
Recognition System," 2021 IEEE 8th International Conference on 
Industrial Engineering and Applications (ICIEA), pp. 550-555, 2021. 
[10] Ming-Di, Hu, Bai Long, Li Ying, Zhao Si-Rui, and Chen En-Hong. 
“Vehicle 24-Color Long Tail Recognition Based on Smooth Modulation 
Neural Network with Multi-Layer Feature Representation.”, 2021. 

233
Authorized licensed use limited to: Tsinghua University. Downloaded on November 13,2022 at 16:17:37 UTC from IEEE Xplore.  Restrictions apply. 


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
