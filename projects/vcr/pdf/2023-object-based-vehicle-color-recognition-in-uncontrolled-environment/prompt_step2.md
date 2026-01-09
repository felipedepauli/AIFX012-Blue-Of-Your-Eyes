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

.
.
Latest updates: hps://dl.acm.org/doi/10.1145/3589572.3589585
.
.
RESEARCH-ARTICLE
Object-Based Vehicle Color Recognition in Uncontrolled Environment
PANUMATE CHETPRAYOON
.
THEERAT SAKDEJAYONT
.
MONCHAI LERTSUTTHIWONG
.
.
.
PDF Download
3589572.3589585.pdf
30 December 2025
Total Citations: 2
Total Downloads: 75
.
.
Published: 10 March 2023
.
.
Citation in BibTeX format
.
.
ICMVA 2023: 2023 The 6th International
Conference on Machine Vision and
Applications
March 10 - 12, 2023
Singapore, Singapore
.
.
ICMVA '23: Proceedings of the 2023 6th International Conference on Machine Vision and Applications (March 2023)
hps://doi.org/10.1145/3589572.3589585
ISBN: 9781450399531
.


---

# Page 2

Object-Based Vehicle Color Recognition in Uncontrolled
Environment
Panumate Chetprayoon, Theerat Sakdejayont, Monchai Lertsutthiwong
Kasikorn Labs Co., Ltd
Nonthaburi, Thailand
panumate.c@kbtg.tech,theerat.s@kbtg.tech,monchai.le@kbtg.tech
Figure 1: Challenge of vehicle color recognition in real-world situations. First row: examples of an uncontrolled environment.
Second row: examples of related vehicle colors. Third row: examples of multi-color cars
ABSTRACT
The demand for vehicle recognition significantly increases with
impact on many businesses in recent decades. This paper focuses
on a vehicle color attribute. A novel method for vehicle color recog-
nition is introduced to overcome three challenges of vehicle color
recognition. The first challenge is an uncontrolled environment
such as shadow, brightness, and reflection. Second, similar color
is hard to be taken into account. Third, few research works dedi-
cate to multi-color vehicle recognition. Previous works can provide
only color information of the whole vehicle, but not at vehicle part
level. In this study, a new approach for recognizing the colors of
vehicles at the part level is introduced. It utilizes object detection
techniques to identify the colors based on the different objects (e.g.
parts of a vehicle in this research). In addition, a novel generic post-
processing is proposed to improve robustness in the uncontrolled
environment and support not only single-color but also multi-color
vehicles. Experimental results show that it can effectively identify
the color under the three challenges addressed above with 99 %
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
ICMVA 2023, March 10–12, 2023, Singapore, Singapore
© 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-1-4503-9953-1/23/03...$15.00
https://doi.org/10.1145/3589572.3589585
accuracy for single-color vehicle and outperforms the other seven
baseline models, and 76 % accuracy for multi-color vehicle.
CCS CONCEPTS
• Computing methodologies →Object detection.
KEYWORDS
image classification, object detection, vehicle color recognition
ACM Reference Format:
Panumate Chetprayoon, Theerat Sakdejayont, Monchai Lertsutthiwong.
2023. Object-Based Vehicle Color Recognition in Uncontrolled Environment.
In 2023 The 6th International Conference on Machine Vision and Applications
(ICMVA) (ICMVA 2023), March 10–12, 2023, Singapore, Singapore. ACM, New
York, NY, USA, 7 pages. https://doi.org/10.1145/3589572.3589585
1
INTRODUCTION
Vehicle cameras, traffic surveillance camera systems, and mobile
cameras have been widely used in recent years, providing ample
data and information that can be used to enhance intelligent vehicle
technology. The growing availability of images and recordings from
these sources has been used and applied in various applications
such as driving safety [4], autonomous driving [7], InsurTech [2],
and used car valuation [21] etc.
Many applications make use of vehicle attributes, i.e., MAKE
(Vehicle brand), MODEL (Model name), YEAR (Year that it was
produced), TYPE (sedan, hatchback, pick-up, etc.), and COLOR.
Among these attributes, vehicle color is considered to be the easiest
attribute to be recognized. However, as stated in several research
88


---

# Page 3

ICMVA 2023, March 10–12, 2023, Singapore, Singapore
Panumate Chetprayoon, Theerat Sakdejayont, Monchai Lertsutthiwong
papers [1], [3], vehicle color recognition is not as straightforward
as it seems and poses several key challenges.
(1) Uncontrolled Environments. Colors can be easily affected
by different lighting conditions, perspective, and even parts
of the vehicle being occluded. This can cause the color to
appear differently in different images or recordings, making
it difficult for the algorithms to accurately recognize the
color.
(2) Related Colors. Two colors that appear similar in terms of
hue or color family can be difficult to differentiate, such as
black and grey, blue and cyan, orange and red, and pink and
purple. This can lead to incorrect recognition of the vehicle
color.
(3) Multi-colored Vehicles. Vehicles can be comprised of multi-
ple colors, with each section or part potentially painted differ-
ently. With the best of our knowledge, existing research has
limited capability to identify the colors of individual parts,
instead only providing information on the overall color of
the vehicle.
In addition, a set of standard vehicle colors defined in the vehicle
registration handbook may be different from one country to another.
There is no standard model to capture such a variety yet. In Thailand,
twelve colors are registered and some vehicles have more than one
color, i.e., taxi vehicle usually has two colors as shown in the third
row of Figure 1.
On a different note, object detection is a technique in computer
vision that aims to identify and locate objects within an image using
a bounding box. On the other hand, image segmentation divides
an image into multiple segments, each of which corresponds to
a different object or region, and representing each segment with
a polygon. Compared to image segmentation, object detection is
generally faster and requires less computational resources. It is
suitable for tasks where a rough estimation of the object location
using a bounding box is sufficient.
In this paper, a novel vehicle color recognition method is pro-
posed to tackle such deceptively simple challenges addressed above.
The method utilizes an idea of object detection and then propose
object-based (e.g., vehicle part) vehicle color recognition. The pro-
posed method consists of two tasks, 1) vehicle part and color detec-
tion task and 2) the post-processing task. A multi-color vehicle can
be covered in this model.
The main contributions of this paper are as follows:
(1) An idea of object-based (e.g., vehicle part) vehicle color recog-
nition and a generic post-processing formula are introduced.
The model overcomes three challenges of vehicle color recog-
nition as stated above.
(2) Business issues in Thai vehicle color recognition have been
resolved. It can identify a Thai vehicle color standard includ-
ing a special case like Thai multi-color taxis. The model can
differentiate the vehicle color in a part or a section level. For
example, this is a red-yellow car. The upper-half section is
yellow and the lower-half section is red.
This paper is organized as follows: Section 2 provides some
related knowledge for a vehicle color recognition. In Section 3,
our proposed method consists of vehicle part and color detection
task and the post-processing task are explained for both single-
color and multi-color cases. Next, Section 4 gives an explanation
of implementation details and its results for VCoR-TH dataset and
Taxi-TH test dataset. Finally, key concluding remarks and future
directions are presented in Section 5.
2
RELATED WORK
Recent literature review on vehicle color recognition methods can
be divided into two types: a traditional computer vision-based
method and a deep learning-based method. These two methods and
object detection technique, which will be utilized in our proposed
solution, are exclusively reviewed in this section.
[1] evaluated vehicle color recognition which turns into an area
segmentation problem. Vehicle color is generally represented with
the hood color. Therefore, they proposed a vehicle color classifi-
cation method using the HSV color system with Support Vector
Machine (SVM). [9] analyzed the effect of sunlight. Its reflection
transforms the color of vehicle window to white and significantly
leads to unexpected results in vehicle color classification. To reduce
this effect, a window-removing task is proposed and applied. [6]
examined two regions of interest named smooth car hood and semi-
front vehicle, and three classification methods consists of K-Nearest
Neighbors (K-NN), Artificial Neural Networks (ANN), and support
vector machine (SVM) for classifying the vehicle color.
Technically, Convolutional Neural Network (CNN) is designed
to learn classification method based on shape information. How-
ever, [14] proved that CNN can also learn classification based on
color distribution. [13] analyzed the use of CNNs for vehicle color
recognition and concluded the importance of alerts on amber and
silver colors.
With the state-of-the-art object detection models, one can enrich
vehicle color recognition with higher performance. For example,
[22] proposed a one-step method for vehicle color recognition us-
ing an object detection, named YOLO9000 [15]. [20] introduced
the solution by enhancing an object detection with Region-based
Convolutional Neural Network (R-CNN), named Faster R-CNN [16].
Their solutions effectively detected the whole car with its color.
However, there is some room of improvement in that of other
works. For example, existing object detection model detects the
whole car while our technique uses object detection to detect vehicle
parts and efficiently post-process them to classify the vehicle color.
In addition, we notice that the region proposal is very important
for vehicle color recognition. Without this, the model may use
improper vehicle parts for recognizing vehicle color, e.g., car grille,
headlights, taillights, tires, windows, windshield, etc. Finally, this
can lead the result with wrong recognition on vehicle colors. Our
novel solution leverages the object detection and overcomes three
challenges addressed earlier with correct vehicle color recognition.
3
METHOD
The proposed method consists of two tasks, vehicle part and color
detection task and the post-processing task. See Figure 2.
3.1
Vehicle part and color detection task
Given an input image 𝑥𝑖where 𝑖is the index of an image, vehicle
part detection 𝜃is defined as 𝜃(𝑥𝑖). Let 𝐽denote the total number of
89


---

# Page 4

Object-Based Vehicle Color Recognition in Uncontrolled Environment
ICMVA 2023, March 10–12, 2023, Singapore, Singapore
Figure 2: Pipeline of our proposed object-based vehicle color recognition
vehicle parts detected in an image 𝑥𝑖. 𝑗denote the index of vehicle
part where 𝑗∈{1, 2, ..., 𝐽}.
Then, 𝜃(𝑥𝑖) contains a vehicle part name 𝑝𝑖𝑗, a part color name
𝑞𝑖𝑗, a confidence score of the detection 𝑠𝑖𝑗, and a coordinate po-
sitions which can be transformed into an area 𝑎𝑖𝑗. See Equation
(1).
𝜃(𝑥𝑖) = [(𝑝𝑖1,𝑞𝑖1,𝑠𝑖1,𝑎𝑖1), (𝑝𝑖2,𝑞𝑖2,𝑠𝑖2,𝑎𝑖2), ..., (𝑝𝑖𝐽,𝑞𝑖𝐽,𝑠𝑖𝐽,𝑎𝑖𝐽)]
(1)
3.2
Post-processing task
The result from vehicle part and color detection task is applied as an
input for post-processing task. The output from the post-processing
task is the final result of predicted color 𝑦. Let 𝐶denote a set of
possible colors. That means the detected color of a vehicle part 𝑞
and the predicted color 𝑦must be the element of superset 𝐶. For
example, 𝐶= {𝑏𝑙𝑎𝑐𝑘,𝑏𝑙𝑢𝑒,𝑏𝑟𝑜𝑤𝑛,𝑐𝑦𝑎𝑛,𝑔𝑟𝑒𝑒𝑛,𝑔𝑟𝑒𝑦,
𝑜𝑟𝑎𝑛𝑔𝑒, 𝑝𝑖𝑛𝑘, 𝑝𝑢𝑟𝑝𝑙𝑒,𝑟𝑒𝑑,𝑤ℎ𝑖𝑡𝑒,𝑦𝑒𝑙𝑙𝑜𝑤}. 𝑐,𝑞∈𝐶.
Our optimization problem is to determine the element 𝑐in su-
perset 𝐶maximizing the objective function 𝑓. The optimal element
𝑐is defined as an optimal element 𝑦𝑖as described in Equation (2).
𝑦𝑖= argmax
𝑐∈C
𝑓(𝜃(𝑥𝑖))
(2)
Let 𝑝∗denote the appropriate weight of each vehicle part for
possible detected vehicle parts 𝑃. Let 𝑐∗denote the appropriate
weight of each vehicle part for all possible colors in 𝐶. One of the
simple and reasonable 𝑓can be calculated by summation of the dot
product of 𝑝∗
𝑖𝑗𝑐∗
𝑖𝑗𝑠𝑖𝑗and 𝑎𝑖𝑗where 𝑝∗, 𝑠, and 𝑎are normalized as
shown in Equation (3). This is because we want to find the main
color of the vehicle. Therefore, the area should be multiplied by
the confidence score of the predicted bounding box. For 𝑝∗, we
can adjust based on the dataset. For 𝑐∗
𝑖𝑗, it will be 1 if 𝑐𝑖𝑗= 𝑞𝑖𝑗,
otherwise it will be 0.
𝑦= argmax
𝑐∈C
∑︁
𝑗∈J
(𝑝∗
𝑖𝑗· 𝑐∗
𝑖𝑗· 𝑠𝑖𝑗· 𝑎𝑖𝑗)
𝑐∗
𝑖𝑗=
(
1
if 𝑐𝑖𝑗= 𝑞𝑖𝑗
0
otherwise
(3)
Next, we focus on solving the multiple-color challenge. First,
we create a list of the vehicle parts for each section. For example,
Thai taxi in Figure 1 has two sections. The upper half and lower
half are yellow and green, respectively. We can define the list of
vehicle parts in each section. That means the upper section consists
of the vehicle hood, tailgate, and roof. On the other hand, the lower
section consists of the bumper, door, and fender.
Let 𝑘denote the index of the section. 𝑦𝑖𝑘is the color of image 𝑖
of section 𝑘. 𝑃𝑘is the list of vehicle parts considered in section 𝑘.
We can define the color of each section as shown in Equation (4).
𝑦𝑘= argmax
𝑐∈C
∑︁
𝑗∈J
(𝑝∗
𝑖𝑗· 𝑐∗
𝑖𝑗· 𝑠𝑖𝑗· 𝑎𝑖𝑗)
𝑐∗
𝑖𝑗=
(
1
if 𝑐𝑖𝑗= 𝑞𝑖𝑗
0
otherwise 𝑝∗
𝑖𝑗=
(
1
if 𝑝𝑖𝑗∈𝑃𝑘
0
otherwise
(4)
4
EXPERIMENTS
First, this section describes the detail of model implementations,
i.e, the usage of the object detection model and some parameter
settings. Next, the experiment for the single-color vehicle with
VCoR-TH dataset is discussed. Lastly, we expand the experiment to
the multi-color vehicle with Taxi-TH test dataset.
4.1
Implementations
The detected vehicle part is analyzed in details. We use 5 vehicle
parts in this experiment: bumper (both front and rear bumpers
are in the same class), doors (every door is in the same class),
fender (front, rear, left, and right fenders are in the same class),
hood (front hood and tailgate are in the same class), and roof. That
means 𝑃= {𝑏𝑢𝑚𝑝𝑒𝑟,𝑑𝑜𝑜𝑟, 𝑓𝑒𝑛𝑑𝑒𝑟,ℎ𝑜𝑜𝑑,𝑟𝑜𝑜𝑓}. The objective func-
tion explained in Equation (3) is then applied to achieve the optimal
90


---

# Page 5

ICMVA 2023, March 10–12, 2023, Singapore, Singapore
Panumate Chetprayoon, Theerat Sakdejayont, Monchai Lertsutthiwong
solution. The parameters for single-color and multi-color vehicle
scenarios are set and defined as follows:
• For single-color vehicle, 𝑝∗is set to 1.
• For multi-color vehicle, according to Taxi-TH test set shown
in Figure 5, 𝑘is set 2, 𝑃𝑢𝑝𝑝𝑒𝑟= {ℎ𝑜𝑜𝑑,𝑟𝑜𝑜𝑓}, and 𝑃𝑙𝑜𝑤𝑒𝑟=
{𝑏𝑢𝑚𝑝𝑒𝑟,𝑑𝑜𝑜𝑟, 𝑓𝑒𝑛𝑑𝑒𝑟}.
In multi-color vehicle, door and fender consist of two colors, i.e.,
yellow and green. This is technically ambiguous and hard to be
recognized. Therefore, we assume 𝑝∗
𝑑𝑜𝑜𝑟= 0 and 𝑝∗
𝑓𝑒𝑛𝑑𝑒𝑟= 0 to
simplify our experience to achieve practical results.
Due to the performance and ease of use, we exploit one of the
state-of-the-art object detection models, named YOLOv5 [10]. We
use YOLOv5m which is trained by COCO [11] with a provided
pre-trained model.
We label each part with its corresponding color as a class in object
detection. For example, black bumper, black door, black fender, black
hood, and black roof are labeled as 0, 0, 2, 3 ,4, respectively. If next
color is blue, therefore, blue bumper, blue door, blue fender, blue
hood, and blue roof, are labeled as 5, 6, 7, 8, and 9, respectively.
4.2
Single-color vehicle with VCoR-TH
4.2.1
Data preparation. The Vehicle Color Recognition (VCoR)
dataset [12] is the most diverse and large-scale dataset with 10K im-
ages and 15 color classes, including beige, black, blue, brown, gold,
green, grey, orange, pink, purple, red, silver, tan, white, and yellow.
However, as the focus of this paper is on Thai vehicle color recog-
nition, a new dataset, VCoR-TH, has been proposed and created
by filtering and selecting the original VCoR dataset to be compre-
hensive and better suit the specific requirements and challenges of
color recognition in Thailand.
According to Thai vehicle registration book, VCoR-TH consists
of 12 colors: black, blue, brown, cyan, green, grey, orange, pink,
purple, red, white, and yellow. We set our𝐶as described in Section 3.
Key setup for generating certain color set is listed as follows:
• Cyan: Select some light blue images from original VCoR blue
images.
• Blue: Select some dark blue images from original VCoR blue
images.
• Grey: Combine grey images from the original VCoR dataset
with some silver images that looks grey from the same
dataset.
Furthermore, images with less than 50KB file size are removed.
For each color, there are 30 and 20 images for a test set and a
validation set, respectively. The remaining is used as a training
set. Moreover, our solution leverages the idea of object detection.
Therefore, we also label the vehicle parts. The number shown in
Table 1 is the number of bounding boxed for each vehicle part in a
training set.
In some colors, vehicle part may have the number of bounding
boxes more than the number of images. There are two key points to
be taken into account on this. First, there is more than one vehicle
part in one image, e.g., two doors, two fenders, etc. Second, a cyan
car may possibly have a black roof as shown in the third row of
Figure 1. The training dataset is fully described in Table 1.
Table 1: VCoR-TH Dataset
image
bumper
door
fender
hood
roof
black
136
141
218
240
139
274
blue
139
132
235
260
132
86
brown
119
99
199
220
110
65
cyan
54
54
83
98
52
29
green
173
152
227
318
157
85
grey
93
76
175
177
83
54
orange
63
51
96
120
56
20
pink
97
77
132
167
91
38
purple
169
153
215
297
143
75
red
194
186
309
372
186
116
white
117
114
222
221
116
88
yellow
136
130
186
249
126
55
sum
1490
1365
2297
2739
1391
985
4.2.2
Experimental results. A set of seven baseline models consists
of traditional computer vision methods such as KNN, SVM, deci-
sion tree, RandomForest, and a deep learning with a CNN such as
Resnet50 [8] and MobileNetV2 [17], and fine-grained image classi-
fication EfficientnetB3 [19], is used and experimented as an image
classification task. Pre-trained deep learning weight is trained and
computed by Imagenet [5].
Table 2: Comparison between our proposed algorithm and
baseline methods
accuracy
DecisionTree
0.381
KNN
0.394
RandomForest
0.642
SVM
0.681
Resnet50
0.911
MobileNetV2
0.897
EfficientnetB3
0.928
Ours
0.986
According to Table 4, our proposed solution significantly out-
performs other baseline models. The confusion matrix of Efficient-
netB3, which is the best in the baseline model, and ours are shown
in Table 3 and Table 4.
4.2.3
Discussion. The proposed solution has false recognition with
only 5 images from total of 360 testing images. The main reason
is vehicle part detection cannot recognize the target vehicle parts.
This is because detection model is trained by limited dataset of 1490
images for 60 classes (12 colors and 5 vehicle parts per color) which
is insufficient to achieve concrete results. However, detecting only
a few vehicle parts may lead to wrong detected color as a result
in wrong answer. On the other hand, few vehicle parts can be
efficiently detected with the correct color. Not only the proposed
model, but also the baseline model EfficientnetB3 fails to recognize
the vehicle color of those five images. Moreover, EfficientnetB3
cannot correctly detect color in certain conditions of related colors
such as grey-white, grey-black, cyan-blue, and pink-purple. To
91


---

# Page 6

Object-Based Vehicle Color Recognition in Uncontrolled Environment
ICMVA 2023, March 10–12, 2023, Singapore, Singapore
Table 3: Confusion maxtrix of EfficientnetB3
label\pred
black
blue
brown
cyan
green
grey
orange
pink
purple
red
white
yellow
black
28
1
0
0
0
1
0
0
0
0
0
0
blue
0
27
0
2
0
0
0
0
1
0
0
0
brown
0
0
28
0
0
2
0
0
0
0
0
0
cyan
0
3
0
26
0
1
0
0
0
0
0
0
green
0
0
0
1
29
0
0
0
0
0
0
0
grey
3
0
1
0
0
24
0
0
0
0
2
0
orange
0
0
2
0
0
0
27
0
0
0
0
1
pink
0
0
0
0
0
1
0
26
2
0
1
0
purple
0
0
0
0
0
0
0
0
30
0
0
0
red
0
0
0
0
0
0
0
0
0
30
0
0
white
0
0
0
0
0
0
0
0
0
0
30
0
yellow
0
0
0
0
1
0
0
0
0
0
0
29
Table 4: Confusion matrix of proposed solution
label\pred
black
blue
brown
cyan
green
grey
orange
pink
purple
red
white
yellow
black
30
0
0
0
0
0
0
0
0
0
0
0
blue
0
30
0
0
0
0
0
0
0
0
0
0
brown
0
0
30
0
0
0
0
0
0
0
0
0
cyan
0
0
0
30
0
0
0
0
0
0
0
0
green
0
0
0
0
30
0
0
0
0
0
0
0
grey
0
0
0
0
0
29
0
0
0
0
1
0
orange
0
0
2
0
0
0
28
0
0
0
0
0
pink
0
0
0
0
0
0
0
28
1
1
0
0
purple
0
0
0
0
0
0
0
0
30
0
0
0
red
0
0
0
0
0
0
0
0
0
30
0
0
white
0
0
0
0
0
0
0
0
0
0
30
0
yellow
0
0
0
0
0
0
0
0
0
0
0
30
analyze in details, Grad-CAM [18], the popular visualization tool
of deep neural network using gradient-based localization, is used
for further investigation.
Figure 3 shows that EfficientnetB3 provides an incorrect answer.
For example, it is an orange car but EfficientnetB3 returns the result
with a yellow car. It is because EfficientnetB3 mainly focuses the
middle position of the image such as left headlight more than the
other parts. See the visualization resulting using Grad-Cam in Fig-
ure 3b. This investigation corresponds with what [1] explains such
that the vehicle color recognition can turn into area segmentation
problem. YOLOV5, shown in Figure 3c, detects each part as an or-
ange color (class numbers 25-29 based on vehicle parts). Thus, final
answer from proposed solution is indeed orange color. Figure 4
shows more samples of incorrect recognition from EfficientnetB3
while our solution detects it correctly.
4.3
Multi-color vehicle with Taxi-TH
4.3.1
Data preparation. Thai taxi usually consists of two colors,
e.g., yellow-green, yellow-red, blue-red, pink-white, etc. Yellow-
green taxi is the only type of taxis that are owned by individuals.
Other colors are run by taxi companies, taxi co-ops, and their al-
liances. In this experiment, we collect 100 images of a yellow-green
Thai taxi, named Taxi-TH test set as shown in Figure 5.
4.3.2
Experimental results. We use the model trained in section 4.2
without further fine-tuning process. The result from our proposed
solution with Taxi-TH test set is shown in Table 5. The table denotes
the number of true positive predictions. 100 images are used in the
experiment. 81 images and 95 images are correctly detected with
upper-half and lower-half sections, respectively. Overall, 76 out
of 100 images are mutually correct for both upper and lower-half
sections.
Table 5: Taxi-TH dataset and its results with proposed solu-
tion
Number of images
Total images
100
Upper section
81
Lower section
95
All
76
92


---

# Page 7

ICMVA 2023, March 10–12, 2023, Singapore, Singapore
Panumate Chetprayoon, Theerat Sakdejayont, Monchai Lertsutthiwong
(a) Original input image
(b) Visualization of EfficientnetB3 using
Grad-Cam
(c) YOLOV5 vehicle part detection result
Figure 3: Error analysis by comparing our method with the baseline method
Figure 4: Samples of incorrect images with baseline method EfficientnetB3
Figure 5: Samples of Taxi-TH test set
4.3.3
Discussion. With detailed analysis on experimental results,
the upper-half section has higher wrong detection than the lower-
half section. Main root cause is insufficient training dataset on
yellow vehicle parts. Only 136 images are applied for 5 classes of
object detection tasks as mentioned in Table 1. Moreover, we have
only 55 bounding boxes of yellow roofs and 126 bounding boxes
93


---

# Page 8

Object-Based Vehicle Color Recognition in Uncontrolled Environment
ICMVA 2023, March 10–12, 2023, Singapore, Singapore
of yellow hood. The roof is hard to see compared to other vehicle
parts. The roof area is typically small if the image is taken from
the perspective of side view, not from the top view. Although a
hood can be easily detected, it is also easy to be influenced with an
impact on predictions by the light as stated in previous works. See
Figure 1 for more results.
5
CONCLUSIONS
In this paper, the modern vehicle color recognition model is pro-
posed. The model efficiently works under difficult circumstances,
i.e., uncontrolled environment, related vehicle color, and multi-
color vehicle. The object detection technique has been exploited in
identifying vehicle parts with its corresponding color. Additional
generic post-processing formula for vehicle color recognition is also
proposed. Our proposed method significantly outperforms conven-
tional models with 99% accuracy for single-color vehicle. Moreover,
we expand our experiment to multi-color vehicle with 76% accuracy.
According to our analysis, the conventional image classification
model may use the improper vehicle parts such as headlights, tires,
windows, etc. In contrast, our model utilizes various proper vehicle
parts so it can surpass the challenges stated above.
Future work involves furthering the proposed object-based vehi-
cle color recognition by exploring additional datasets for training
and addressing novel implementations from others in the field of
computer vision. Additionally, we aim to extend the object-based
method to include the detection and recognition of colors in other
objects, beyond just vehicle parts. This could broaden the scope of
the object-based method and demonstrate its versatility for use in
a wider range of applications and scenarios.
REFERENCES
[1] Nakhoon Baek, Sun-Mi Park, Ku-Jin Kim, and Seong-Bae Park. 2007. Vehicle
color classification based on the support vector machine method. In International
conference on intelligent computing. Springer, 1133–1139.
[2] Jaime Cepeda Villamayor. 2017. Car Features Recognition for Insurance Applica-
tions using Machine Learning. (2017).
[3] Pan Chen, Xiang Bai, and Wenyu Liu. 2014. Vehicle color recognition on urban
road by feature context. IEEE Transactions on Intelligent Transportation Systems
15, 5 (2014), 2340–2346.
[4] Tzu-Chih Chien, Chieh-Chuan Lin, and Chih-Peng Fan. 2020. Deep learning
based driver smoking behavior detection for driving safety. Journal of Image and
Graphics 8, 1 (2020), 15–20.
[5] Jia Deng, Wei Dong, Richard Socher, Li-Jia Li, Kai Li, and Li Fei-Fei. 2009. Imagenet:
A large-scale hierarchical image database. In 2009 IEEE conference on computer
vision and pattern recognition. Ieee, 248–255.
[6] Erida Dule, Muhittin Gökmen, and M Sabur Beratoğlu. 2010. A convenient
feature vector construction for vehicle color recognition. In Proceedings of the 11th
WSEAS international conference on nural networks and 11th WSEAS international
conference on evolutionary computing and 11th WSEAS international conference
on Fuzzy systems. 250–255.
[7] Ryo Hasegawa, Yutaro Iwamoto, and Yen-Wei Chen. 2020. Robust Japanese road
sign detection and recognition in complex scenes using convolutional neural
networks. Journal of Image and Graphics 8, 3 (2020), 59–66.
[8] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2016. Deep residual
learning for image recognition. In Proceedings of the IEEE conference on computer
vision and pattern recognition. 770–778.
[9] Jun-Wei Hsieh, Li-Chih Chen, Sin-Yu Chen, Duan-Yu Chen, Salah Alghyaline,
and Hui-Fen Chiang. 2014. Vehicle color classification under different lighting
conditions through color correction. IEEE sensors journal 15, 2 (2014), 971–983.
[10] Glenn Jocher, Alex Stoken, Jirka Borovec, NanoCode012, ChristopherSTAN,
Liu Changyu, Laughing, tkianai, Adam Hogan, lorenzomammana, yxNONG,
AlexWang1900, Laurentiu Diaconu, Marc, wanghaoyang0106, ml5ah, Doug, Fran-
cisco Ingham, Frederik, Guilhen, Hatovix, Jake Poznanski, Jiacong Fang, Lijun
Yu, changyu98, Mingyu Wang, Naman Gupta, Osama Akhtar, PetrDvoracek,
and Prashant Rai. 2020. ultralytics/yolov5: v3.1 - Bug Fixes and Performance
Improvements. https://doi.org/10.5281/zenodo.4154370
[11] Tsung-Yi Lin, Michael Maire, Serge Belongie, James Hays, Pietro Perona, Deva
Ramanan, Piotr Dollár, and C Lawrence Zitnick. 2014. Microsoft coco: Common
objects in context. In European conference on computer vision. Springer, 740–755.
[12] Karen Panetta, Landry Kezebou, Victor Oludare, James Intriligator, and Sos
Agaian. 2021. Artificial Intelligence for Text-Based Vehicle Search, Recognition,
and Continuous Localization in Traffic Videos. AI 2, 4 (2021), 684–704. https:
//doi.org/10.3390/ai2040041
[13] Uma K Kesava Pillai and Damian Valles. 2021. An initial deep CNN design
approach for identification of vehicle color and type for amber and silver alerts. In
2021 IEEE 11th Annual Computing and Communication Workshop and Conference
(CCWC). IEEE, 0903–0908.
[14] Reza Fuad Rachmadi and I Purnama. 2015. Vehicle color recognition using
convolutional neural network. arXiv preprint arXiv:1510.07391 (2015).
[15] Joseph Redmon and Ali Farhadi. 2017. YOLO9000: better, faster, stronger. In
Proceedings of the IEEE conference on computer vision and pattern recognition.
7263–7271.
[16] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun. 2015. Faster r-cnn:
Towards real-time object detection with region proposal networks. Advances in
neural information processing systems 28 (2015).
[17] Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov, and Liang-
Chieh Chen. 2018. Mobilenetv2: Inverted residuals and linear bottlenecks. In
Proceedings of the IEEE conference on computer vision and pattern recognition.
4510–4520.
[18] Ramprasaath R Selvaraju, Michael Cogswell, Abhishek Das, Ramakrishna Vedan-
tam, Devi Parikh, and Dhruv Batra. 2017. Grad-cam: Visual explanations from
deep networks via gradient-based localization. In Proceedings of the IEEE interna-
tional conference on computer vision. 618–626.
[19] Mingxing Tan and Quoc Le. 2019. Efficientnet: Rethinking model scaling for
convolutional neural networks. In International conference on machine learning.
PMLR, 6105–6114.
[20] Abdullah Tariq, Muhammad Zeeshan Khan, and Muhammad Usman Ghani Khan.
2021. Real Time Vehicle Detection and Colour Recognition using tuned Features
of Faster-RCNN. In 2021 1st International Conference on Artificial Intelligence and
Data Analytics (CAIDA). IEEE, 262–267.
[21] Michail Tsagris and Stefanos Fafalios. 2022. Advanced Car Price Modelling and
Prediction. In Advances in Econometrics, Operational Research, Data Science and
Actuarial Studies. Springer, 479–494.
[22] Xifang Wu, Songlin Sun, Na Chen, Meixia Fu, and Xiaoying Hou. 2018. Real-
time vehicle color recognition based on yolo9000. In International Conference in
Communications, Signal Processing, and Systems. Springer, 82–89.
94


        # Instruções de Metadados
        NÃO gere metadados no corpo da resposta.

        # Etapa atual
        Você está executando o **Passo 2: Segunda passada**.

        **REGRAS ESTRITAS DE FORMATAÇÃO (PARA TODAS AS ETAPAS)**:
1. NÃO inclua textos introdutórios (ex: 'Você está executando...', 'Seguem os resultados...').
2. NÃO repita seções como '# Objetivo', '# Metadados', '# Referência do paper'.
3. Comece a resposta DIRETAMENTE com o conteúdo solicitado no template.
REGRAS ESPECÍFICAS DO PASSO 2:
- Nos 'Pontos-chave': NÃO use citações de página/seção.
- REMOVA TOTALMENTE a seção de 'Análise das figuras/tabelas'.
- OBRIGATÓRIO: Adicione '## Análise de Foco' no final.

        ## Passo 2: Segunda passada
Na segunda passada, leia o artigo com mais atenção, mas ignore detalhes como provas. Ajuda a escrever os pontos-chave ou a fazer comentários nas margens enquanto você lê.
1. Olhe cuidadosamente nas figuras, diagramas e outras ilustrações no artigo. Dê atenção especial aos gráficos.
   São as espinhas dos dedos? São as legendas corretas? São os resultados apresentados com erros de medida, de forma que as conclusões sejam estatisticamente significativas? Erros comuns como esses separam trabalho rápido e mal feito do verdadeiramente excelente.
2. Lembre-se de marcar as referências relevantes para leitura posterior (essas são ótimas para aprender mais sobre o contexto do artigo).

A segunda passada deve levar até uma hora. No final dessa passada, você deve ser capaz de compreender o conteúdo do artigo. Você deve ser capaz de resumir a principal proposta do artigo, com evidências suportadas, para alguém. Esse é o nível de detalhe apropriado para artigos nos quais você está interessado, mas não está na sua área de especialidade.

Às vezes, até o final da segunda passada, você não entenderá o artigo. Isso pode ser porque o assunto é novo para você, com termos e acrônimos desconhecidos. Ou os autores podem usar uma prova ou uma técnica experimental que você não entende, de sorte, o conteúdo principal do artigo é incompreensível. O artigo pode ser mal escrito com afirmações não substanciadas e muitas referências futuras. Ou pode ser que seja tarde de noite e você está cansado.

Você pode agora escolher deixar o artigo de lado, retornar ao artigo posteriormente, ou persistir e prosseguir para a terceira passada.
        </USER>
