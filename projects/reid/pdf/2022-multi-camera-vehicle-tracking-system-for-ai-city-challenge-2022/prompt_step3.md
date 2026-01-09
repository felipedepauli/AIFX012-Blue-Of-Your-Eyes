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
"Investigar métodos para associação de veículos (vehicle re-identification) entre câmeras diferentes com visualizações não sobrepostas. Eu tenho duas câmeras em uma via, uma pega a imagem de frente, outra de traz. Preciso associar os veículos entre as duas câmeras usando primeiramente a placa, mas se não for possível, usar a classificação e rastreamento do veículo."

IMPORTANTE: Adicione uma seção final '## Análise de Foco' explicando detalhadamente como este paper aborda ou contribui para o foco acima.


        # Paper (entrada)
        TEXTO DO PAPER:


---

# Page 1

Multi-Camera Vehicle Tracking System for AI City Challenge 2022
Fei Li*
Zhen Wang*
Ding Nie*
Shiyi Zhang
Xingqun Jiang
Xingxing Zhao
Peng Hu
BOE Technology Group, China
{lifei-cto,wangzhen-cto,nied,zhangshiyi,hupeng-hq}@boe.com.cn
Abstract
Multi-Target Multi-Camera tracking is a fundamental
task for intelligent trafﬁc systems. The track 1 of AI City
Challenge 2022 aims at the city-scale multi-camera vehicle
tracking task. In this paper we propose an accurate ve-
hicle tracking system composed of 4 parts, including: (1)
State-of-the-art detection and re-identiﬁcation models for
vehicle detection and feature extraction. (2) Single cam-
era tracking, where we introduce augmented tracks predic-
tion and multi-level association method on top of tracking-
by-detection paradigm.(3) Zone-based singe-camera track-
let merging strategy.
(4) Multi-camera spatial-temporal
matching and clustering strategy.
The proposed system
achieves promising results and ranks the second place in
Track 1 of the AI City Challenge 2022 with a IDF1 score of
0.8437.
1. Introduction
Multi-Target Multi-Camera (MTMC) [1,9,11,12,14,21,
27,29] tracking plays an important role in the extraction of
actionable insights from the fast-expanding sensors around
the world. Among its branches, city scale Multi-Camera
Vehicle Tracking (MCVT) is attracting an increasing num-
ber of researchers.
Its primary goal is to calculate tra-
jectories of vehicles across multiple cameras, as shown in
Fig. 1. Following a general approach, MCVT can be broken
down to three sub-tasks, including Single-Camera Tracking
(SCT), vehicle re-identiﬁcation (Re-ID), and Multi-Camera
Tracklets Matching (MCTM). As the initial condition, SCT
can have signiﬁcant impact on the correctness of succes-
sive steps. A few broken tracklets or ID switches in SCT
are enough to cause massive chaos and chain reaction in
multi-camera tracklet matching, forming an invisible bot-
tleneck on recall and precision scores. We can observe the
challenges seen in traditional MCVT with some actual sce-
narios:
1. Most tracking-by-detection SCT algorithms face the
*Equal contribution.




Figure 1. Tasks faced by MCVT, showing the trajectory of vehicles
across multiple cameras.
uncertainty caused by detection noises such as false
positive or false negative results, which in turn affect
the matching process and ultimately result in unstable
or broken tracks.
2. Most tracking-by-detection SCT algorithms underesti-
mate broken tracklets caused by long trafﬁc jam, which
is shown in Fig. 6. that afterwards
3. Most tracking-by-detection SCT algorithms extract
impure features when vehicle is occluded by another
object, such that the bounding box may contain many
pixels from adjacent object.
4. In multi-camera tracklet matching, many vehicles with
similar appearance cannot be distinguished, thus cre-
ating ID switches across camera.
Because of these problems, we design a system that la-
bels and handles three types of detection results using con-
ﬁdence score and Intersection Over Union (IOU) ratios,
which are low-quality-occluded, low-quality-non-occluded,
and high-quality-non-occluded vehicles.
Among these,
3264
2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)
978-1-6654-8739-9/22/$31.00 ©2022 IEEE
DOI 10.1109/CVPRW56347.2022.00369
2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW) | 978-1-6654-8739-9/22/$31.00 ©2022 IEEE | DOI: 10.1109/CVPRW56347.2022.00369
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on January 07,2026 at 23:39:28 UTC from IEEE Xplore.  Restrictions apply. 


---

# Page 2

high-quality-non-occluded vehicles have the highest prior-
ity when matching, and are used for track initialization.
Low-quality ones, on the other hand, have lower priori-
ties when matching. Moreover, the Re-ID features of low-
quality-occluded vehicles will be dropped out. By sorting
them out, vehicle tracks can be more accurately performed,
which enables a high recall rate, and ﬁltered Re-ID features
can make the process easier for tracklet matching later on.
For the missing pieces of a vehicle, we introduce two
more SOT algorithms other than the Kalman Filter, so that
stable vehicle trajectory can be synthesised even if one is in
uncertainty. Then, the results will go through multi-level
matching and clustering, within and across cameras. As
for trajectory disruptions caused by heavy occlusion or ap-
pearance changes, we propose a zone-based tracklet merg-
ing strategy, piecing together most tracklet fragments within
cameras.
As for multi-camera matching, we propose a direction
based spatial-temporal strategy that signiﬁcantly reduces
the searching space and an aggregation strategy that solves
edge cases like U-turns. The main contribution of this paper
are summarized as follows:
• We propose multi-level detection handler, augmented
tracks prediction method, and multi-level association
to cope with broken tracklets and ID switches.
• We propose zone-based singe-camera tracklet merging
strategy, which not only links tracklet fragments, but
also enrich vehicle features in order to increase the re-
call rate.
• We propose spatial-temporal matching and aggrega-
tion strategy that signiﬁcantly reduces the searching
space and solves edge cases like U-turns.
2. Related Work
2.1. Vehicle Detection
Object detection is a traditional assignment of computer
vision and image processing which deals with detecting in-
stances of semantic objects of some certain classes, such as
human, bikes or cars, in digital images and videos.
Object detection algorithms typically leverage machine
learning and deep learning to output reasonable results.
Commonly, object detection algorithms are classiﬁed into
two categories, two-stage object detection and one-stage
object detection.
Faster R-CNN is a representative two-stage object de-
tection algorithm [5, 25]. Its architecture contains two net-
works, region proposal network (RPN) and object detection
network. RPN ﬁrstly generates a series of anchors on the in-
put feature map. Then, Region of interesting pooling (ROI)
takes the output of RPN as input and generate a series of
ﬁxed-sized feature maps. Finally, softmax and bounding
box regression layer ﬂatten the feature maps and output the
location of the object in the image.
Single Shot MultiBox Detector (SSD) [18]and You Only
Look Once (YOLO) [4, 22–24, 30] are both famous one-
stage object detection algorithms. SSD [18] predicts the
object classes and locations with a series bounding boxes in
various aspect ratio and size. YOLO tries to accomplish the
real-time object detection task with anchors derived from
Faster R-CNN. It ﬁendishly turns a object detection task
into a classiﬁcation task. Meanwhile, it balances prediction
accuracy and inference performance.
2.2. Multiple Object Tracking
2.2.1
Single-Target Single-Camera Tracking
single object tracking (SOT) is one of the foremost assign-
ments in computer vision that has numerous applications
such as intelligent video analysis, robotics, autonomous ve-
hicle tracking, and so on. It generally has three kinds of
methods to approach the solutions.
The algorithms related with ﬁrst method are based on
correlation ﬁlter, such as Kernelized Correlation Filters
(KCF) [10], Continuous Convolution Operators for Vi-
sual Tracking(C-COT) [8] and Efﬁcient convolution oper-
ators(ECO) [7], which were commonly used on signal pro-
cessing to describe the correlation or similarity of two sig-
nals. The general procedures to apply the correlation ﬁlter
on SOT have three steps. Firstly, obtain the initialized tar-
get position based on ﬁrst frame of stream. Then, extract
the target position features as ﬁlter template like Histogram
of Oriented Gradients (HOG). Finally, obtain the predicted
target position of current frame by executing correlation op-
eration based on the previous ﬁlter template.
The second class of algorithms is based on optical ﬂow,
such as MedianFlow [13]. This method extracts the tar-
get position features with Harris Corner or SIFT in the ﬁrst
frame. Then, it predicts the corresponding positions of the
feature points for the following frames by optical ﬂow algo-
rithms. It ﬁnally gives the predicted target position based
on the predicted feature-point positions. optical ﬂow al-
gorithms mainly focus on local features predictions which
leads to robust results in occlusion challenge.
The last class of tracking algorithms is based on CNN
Siamese Network, which is a kind of ofﬂine object tracking,
such as siamFc [2], siamRPN [16], siamRPN++ [15], etc.
The main principle is like the second method but replac-
ing the Harris Corner or SIFT feature extractor with CNN.
These methods have all achieved satisfactory results in the
ﬁeld of SOT.
3265
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on January 07,2026 at 23:39:28 UTC from IEEE Xplore.  Restrictions apply. 


---

# Page 3

2.2.2
Multi-Target Single-Camera Tracking
Multiple Object Tracking (MOT) is a challenging task. It
not only involves the difﬁculties derived from SOT such as
occlusion, illumination variation, object deformation, etc.
but also concerns about the relative positions of each target
to reduce ID switching possibilities.
Tracking-by-detection is the main paradigm to achieve
the goal of MOT. Simple Online and Realtime Tracking
(SORT) [3] is a typical bare-bone implementation of MOT
framework. It predicts the object locations of the following
frames by Kalman Filter and then computes the overlaps
with the detection. In the end, it uses Hungarian algorithm
to assign detection to tracklets. However, it always causes
unsatisﬁed tracking results due to lacking feature extraction
especially in crowded and fast motion scenes. To solve the
previous problem, Simple online and realtime tracking with
a deep association metric (DeepSort) [31] was proposed in
2017 and integrate appearance information to improve the
performance of SORT. It effectively reduces the number of
ID switches with acceptable computational complexity in-
creasing.
In support of SORT and DeepSort, there are more works
that joints the detection and tracking. For example, Fair-
MOT [33] accomplishes integrating object detection and
Re-ID in the same backbone to improve inference speed.
2.3. Multi-Camera Vehicle Tracking
Recently, MCVT [19] has become a fascinating research
area due to the demands of the city-scale trafﬁc manage-
ment increasing. With the progression of multi-object track-
ing techniques, the vehicle Re-ID techniques and the inte-
grated framework, MCVT can be settled in better results.
Liu. Et al [17] proposes an integrated framework for MCVT
guided by crossroad zones, which achieves the top perfor-
mance in AI City Challenge 2021.
3. Method
3.1. Overview
The proposed MCVT system is shown in Fig. 2, which
includes vehicle detection, Re-ID feature, feature dropout
based multi-level detection handler, single-camera multi-
level tracks and merging strategy, and multi-camera spatial-
temporal matching and aggregation strategy.
3.2. Vehicle Detection
Vehicle detection is the ﬁrst and essential step in MTMC
tracking.
As most of the MTMC tracking methods, we
follow the tracking-by-detection paradigm, such as using
the state-of-the-art network YOLOv5 [30] and more specif-
ically the YOLOv5x6 model, which is pre-trained on the
COCO dataset to detect vehicles. We tune our detection
classes to only cars, trucks, and buses by setting the classes
parameter. The agnostic parameter is used to perform non-
maximum suppression (NMS) for all detected vehicles in
the inference stage.
3.3. Vehicle Re-ID
Following existing Re-ID work [17], we use ResNet50-
IBN-a, ResNet101-IBN-a and ResNeXt101-IBN-a models
that are pre-trained on the CityFlow dataset to extract fea-
ture of vehicles, without introducing external data. Each
Re-ID model outputs a 2048-dimensional feature vector,
and the ﬁnal feature of each detected car is the average out-
put of the three models.
3.4. Single-Camera Vehicle Tracking
For single-camera vehicle tracker, we follow the gen-
eral framework of Simple Online and Realtime Tracking
(SORT) [3]. To deal with the limitations of SORT, we pro-
pose further improvements to the tracking method. First,
relying on predictions from Kalman Filter often produces
ID switches when direction of movement changes. There-
fore, we utilize two more SOT, namely Efﬁcient Convo-
lution Operators (ECO) [6] and MedianFlow, and propose
an augmented tracks prediction method. Next, inspired by
DeepSort, we include vehicle appearance features, which
then goes through a feature dropout ﬁlter and a multi-
level matching process. Finally, in order to make sure the
completeness of tracklets, we add another post-process for
tracklet merging within a single camera.
3.4.1
Vehicle Track Prediction
To enhance the the limitation of Kalman Filter, we ﬁrst
include MedianFlow, which use the current location of a
vehicle to take sample pixels, and then predict the next
frame’s location based on optical ﬂows. MedianFlow can
effectively locate vehicles that are occluded by another ve-
hicle moving in parallel, thus becomes more occlusion re-
silient. Secondly, when a vehicle moves extremely fast or
makes sharp turns, it usually undergoes dramatic appear-
ance changes. In this case, MedianFlow might not work
well, so we can adjust our prediction using ECO. There-
after, every vehicle detection box will have a much better
match in our multi-level association method, as shown in
Fig. 3.
3.4.2
Multi-Level Detection Handler
For our method, vehicle Re-ID features plays an important
role in both single and multiple camera vehicle tracking.
Therefore, it is imperative to extract accurate features from
Re-ID models, which act as the enabler for the rest of pro-
cesses down the pipeline. We propose multi-level detection
3266
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on January 07,2026 at 23:39:28 UTC from IEEE Xplore.  Restrictions apply. 


---

# Page 4


	





	

	
	

















	 !
Figure 2. Pipeline of our MCVT system. The system ﬁrst uses the detector to obtain all bounding boxes of vehicles from video set; then
uses Re-ID models to extract features, with some Re-ID features being dropped out; then single-camera algorithms generate tracklets;
ﬁnally, tracklets across cameras are synchronized by matching and clustering strategies.
(a) vehicles moving in parallel
(b) vehicle with shadow
Figure 3. Augmented tracks prediction method in different sce-
narios, where red represents ECO, green represents Kalman Filter,
and blue represents optical ﬂow.
handler. We start our detection process with a relatively
low conﬁdence level of 0.1 and a relatively high NMS-IOU
threshold of 0.45. After that we select from the result twice,
ﬁrst with conﬁdence values of 0.1 and NMS-IOU of 0.3,
then with conﬁdence value of 0.3 and NMS-IOU of 0.3. At
this point, we can split the result into three levels, as shown
in Fig. 4.
It follows that the features from low-quality and blocked
vehicles should be discarded, leaving only the boxes them-
selves for the track matching process to get high recalls
[32], which is shown as the feature dropout ﬁlter in Fig. 5.
On the other hand, vehicles that are not blocked will not
only participate in tracker matching, but also add their fea-
tures to the corresponding tracks.
3.4.3
Multi-Target Multi-level Association
To make sure the tracks predicted match adequately with
detection results, our method includes four rounds of asso-
ciations, which can be seen in Fig. 5.
1. select high quality and non-occluded vehicles from
Fig. 4 and associate with tracks of age 1, generating
	

 
 	


	

	
Figure 4. Multi-level detection results, where red has conﬁdence
of 0.1 and NMS-IOU of 0.45, green has conﬁdence of 0.1 and
NMS-IOU of 0.3, and blue has conﬁdence of 0.3 and NMS-IOU
of 0.3.
the following matrix:
M = α1 ∗A + β1 ∗B + γ1 ∗C
(1)
where
M
represents
the
resulting
cost
matrix,
α1, β1, γ1 represent corresponding weights, A repre-
sents feature cosine cost matrix, B represents cost ma-
trix of IOU distance between MedianFlow boxes and
detection boxes, and C represents cost matrix of IOU
distance between ECO boxes and detection boxes.
2. pair the unmatched tracks and detection, resulting in
the following matrix:
W = α2 ∗P + β2 ∗B + γ2 ∗C
(2)
where W is the new cost matrix, α2, β2, γ2 are cor-
responding weights, P is cost matrix of IOU distance
between Kalman Filter boxes and detection boxes.
3267
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on January 07,2026 at 23:39:28 UTC from IEEE Xplore.  Restrictions apply. 


---

# Page 5

	



	




		






	






	





	






		




	






		




	






		




	






		
 
!	


 
!
"

#	

Figure 5. Multi-Target Multi-level Association.
3. associate the detection still unmatched with tracks with
age greater than 1, yielding:
F = A
(3)
where A represents feature cosine cost matrix. This
step is inspired by DeepSort, assuming that tracks with
lower age should have higher priority when matching.
4. match the remaining low quality vehicles (occluded or
not) with tracks of age 1, with similar matrix calcula-
tion to step 2. This step aims to save the boxes pre-
dicted by tracks from the low quality detection, in or-
der to ensure the completeness of our tracklets.
3.4.4
Tracks Life-cycle
After four rounds of associations, if there are still some un-
matched high quality detection boxes, then they are thought
to be new, and new tracks will be initialized, including
Kalman Filter model, ECO tracks, and sampling pixels for
optical ﬂow. For matched detection and tracks, the tracks
will be updated accordingly.
First the type of detection
box is determined, and if the vehicle is occluded, then only
the Kalman Filter is updated, else if the IOU distance be-
tween ECO prediction and matched detection is lower than
a threshold, the track is reinitialized with the matched de-
tection box rather than being updated, and optical ﬂow sam-
pling points as well as feature are updated accordingly. For
tracks not matched with detection boxes, we try to salvage
them by using predictions from MedianFlow or ECO, while
updating the Kalman Filter model with those predictions to
compensate for the missing parts.
3.4.5
Zone-Based Tracklet Merging
Although we make many attempts to capture fragments of
every tracklet to make sure of its completeness, in real-
world scenario, there are still split pieces made by unex-
pected objects such as the trafﬁc light, which can be seen in
Fig. 6. Due to these cases, we propose a zone-based tracklet
merging method.
Tracklet Selection
We divide crossroad images into 9 ef-
fective zones and 1 trafﬁc zone, which can be determined
by speciﬁc cases, as shown in Fig. 7. These 9 zones can be
sort into starting zones (1, 3, 5), middle zone (10), and end-
ing zones(2, 4, 6). Before merging, we pick some tracklets
under the criteria:
• tracklet that starts normally and end in either the same
zone or middle zone.
• tracklet that starts in either middle zone or trafﬁc zone.
These tracklets are thought to be abnormal and will become
candidates for merging. Then, they will go through a ﬁlter
to remove noises such as negligibly short ones (less or equal
to 4 frames), stationary ones, and small pixel count ones.
From there, these candidate will go to tracklet merging in
the next step.
Tracklet Merging
Considering the fact that a tracklet
might have multiple fragments within one camera, this pa-
per cope with abnormal tracklet fragments using hierarchi-
cal clustering. Assuming there are n fragmented tracklets,
ﬁrst the mean feature for each tracklet are calculated, then
we have:
Hn×n =
⎡
⎢⎣
cos(T1, T1)
· · ·
cos(T1, Tn)
...
...
...
cos(Tn, T1)
· · ·
cos(Tn, Tn)
⎤
⎥⎦
(4)
Where Ti represents the tracklets fragments to be merged,
and Hn×n represents the cost matrix of the tracklets. Be-
cause of one tracklet cannot merge with itself, we set the
3268
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on January 07,2026 at 23:39:28 UTC from IEEE Xplore.  Restrictions apply. 


---

# Page 6

	


	

	

	 
(a) Vehicles stop for trafﬁc light, and then moving under occlusion. After the
reappearance of the vehicle, because of the part of feature occluded differ
from that afterwards, the two features cannot be reliably matched.
	


	

	



(b) The track is deleted due to long time occlusion, when the vehicle ﬁnally
shows up, a new ID will be assigned.
Figure 6. Example of unmatched tracks.
Figure 7. 9 Zones for a single camera.
diagonal values with 2, and then do the clustering to get
tracklets under the same cluster:
1. sort tracklets by their starting frame in ascending order
2. check if two tracklets agree with space and time:
(a) if the latter’s starting frame is within a range re-
garding the former’s ending frame.
(b) if the distance between former’s and latter’s start-
ing location is greater than the distance between
former’s starting location and ending location.
(c) if the latter’ starting direction is the direction
pointed by the former.

 	


 	


Figure 8. Spatial-temporal matching strategy.
(d) if the latter’s ending location is within the ending
zones, if not, recursively look for one with ending
zone until none matched.
Using the above techniques, tracklets fragment can be se-
lected and merged under the same cluster, yielding more
accurate tracklet results for single camera tracking.
3.5. Multi-Camera Tracklets Matching
In multi-camera matching, our approach consists of a se-
lection step, shown in Fig. 8, an aggregation step, and a
clustering step.
3269
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on January 07,2026 at 23:39:28 UTC from IEEE Xplore.  Restrictions apply. 


---

# Page 7

3.5.1
Tracklet Matching
The cosine similarity matrix used in multi-camera matching
is similar to the one used in Sec. 3.4.5, except that now it is
comparing tracklets across cameras. For n tracklets across
two adjacent cameras, each tracklet with 2048-dimensional
averaged features from all frames are compared with each
other to form a n by n matrix S, ﬁlled by cosine similar-
ity. The similarity matrix enables merging multiple track-
lets across different cameras. However, as the number of
tracklets increases, the search space within the matrix often
become too large that results in many mismatches, which
can become a bottleneck that limits the quality of clustering
later on. In this case, ﬁltering by edge cases does not seem
to be enough. Therefore, lowering the search space within
the matrix is a crucial step to improve the matching results.
3.5.2
Tracklet Selection
In order to simplify the process for multi-camera match-
ing, we utilize both directional and temporal information
to clamp the scope of the matching process.
Based on
the GPS location of each camera, we can rotate zones in
Sec. 3.4.5 for each cameras to connect the track inlets and
outlets. Inspired by [17], our zones can be simpliﬁed for
multi-camera matching, where (Zone 1, Zone 2) correspond
to West, (Zone 3, Zone 4) correspond to North, (Zone 5,
Zone 6) correspond to East, and (Zone7, Zone 8) corre-
spond to South. Furthermore, we can calculate the possible
time range between each connection using the maximum
and minimum speed limit as well as trafﬁc light signals of
a given scene. This gives us a complete picture of whether
a vehicle can appear in speciﬁc zone of a speciﬁc camera in
the given range of time, which forms a trajectory clamping
mask that limits the search scope in space and time down
to certain ranges. For example, for a tracklet Ti that end
in West at time te, a matching tracklet in the next cam-
era down the road Tj must start in East within time range
[te+t(i, j)min, te+t(i, j)max], where t(i, j)min, t(i, j)max
are the minimum and maximum time interval for crossing
the cameras. Compared to the ﬁltering mask used in [17],
applying selecting mask to the similarity matrix narrows
down the search space almost by half, which greatly in-
creases IDP while maintaining IDR.
3.5.3
Tracklet Clustering
Inspired by [17], our method contains two rounds of multi-
camera tracklet clustering. The ﬁrst round is directional
based. For instance, tracklets going from camera 41 to 42
and the other way could be clustered together, but with re-
liable single-camera tracking result, we can compare only
those tracklets going in the same direction, reducing the
clustering space. After the ﬁrst round of clustering, tracklets


	
	





Figure 9. Example of U-turns, where one vehicle enters c045, goes
to c046, turns around to c045, and ﬁnally appears in c044.
of the same vehicle from adjacent cameras need to be aggre-
gated together, and the order of aggregation matters because
the same vehicle can have different IDs across cameras. We
propose a iterative searching strategy that effectively solves
edge cases like U-turns, as shown in Fig. 9.
That same vehicle that from 45 to 46, and then from
46 to 44, can be express as (camera ID, track ID) pairs
like (45,20)(46,54)(45,160)(44,218). One aggregation or-
der can simply be [41,42][42,43][43,44][44,45][45,46],
[42,41][43,42][44,43][45,44][46,45], searching for track ID
intersections between each camera.
If there is intersec-
tion, the two sets of different camera can be merged, and
if not, new sets are created, and so on. However, U-turns
in this case cannot be properly aggregated.
For exam-
ple, in Fig. 9, begin with (45,20),(46,54), when we reach
(44,218),(45,160), that same vehicle will not be recognized
since the turning point has not been reached, and the in-
tersection is empty.
Going forward, we get results like
(45,20),(46,54),(45,160), (44,218),(45,160),(46,54).
Ap-
parently, there is an intersection between these two sets, yet
they are split into two tracklets. Therefore, we propose a ag-
gregation strategy that searches though tracklets sets in each
camera, until there are no intersection left between any sets,
which effectively solves the U-turn issue.
4. Experiment
4.1. Datasets and Evaluation Metrics
The AIC22 benchmark (CityFlowV2) [20, 28] is cap-
tured by 46 cameras in real-world trafﬁc surveillance en-
vironment. A total of 880 vehicles are annotated in 6 dif-
ferent scenarios. 3 of the scenarios are used for training.
2 scenarios are for validation. And the last scenario is for
testing. There are 215.03 minutes of videos in total. The
length of the training videos is 58.43 minutes, that of vali-
dation videos is 136.60 minutes, and that of testing videos is
20.00 minutes. For MTMC tracking, we use the IDF1 [26]
3270
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on January 07,2026 at 23:39:28 UTC from IEEE Xplore.  Restrictions apply. 


---

# Page 8

Method
IDF1
IDP
IDR
Baseline
0.7522
0.8173
0.6967
+Feature Dropout Filter
0.8192
0.8871
0.7610
+Multi-level matching
0.8312
0.8799
0.7877
+Tracklet Merging
0.8362
0.8732
0.8022
+Tracklet Selection
0.8437
0.8900
0.8020
Table 1. IDF1 score changes after several optimizations.
Team ID
IDF1 score
28
0.8486
59
0.8437
37
0.8371
50
0.8348
70
0.8251
Table 2. Comparison of our method with other teams.
score as evaluation indicators. IDF1 measures the ratio of
correctly identiﬁed detection over the average number of
ground-truth and computed detection. The evaluation sys-
tem of the AI City Challenge will display IDF1,IDP, IDR,
Precision (detection) and Recall (detection).
4.2. Results
We use the evaluation opportunity provided by the eval-
uation system to verify the effect of our algorithm, and op-
timize our algorithm according to the IDF1,IDP, IDR, Pre-
cision and Recall results. We record the changes of IDF1
after several optimizations which are shown in Tab. 1.
In the ﬁnal ranking of track 1 of AI City Challenge 2022,
we rank the second place among all participating teams.
The comparison of our method with other teams’ on the
evaluation system is shown in Tab. 2. Our code will be re-
leased later.
5. Conclusion
In this paper, we propose an accurate multi-camera vehi-
cle tracking system. For single-camera tracking, we incor-
porate three reinforcing methods for augmented tracks pre-
diction, and multi-level association and zone-based singe-
camera tracklet merging strategy. For multi-camera track-
ing, we develop a spatial-temporal strategy that reduces
search space when matching, and improve on hierarchical
clustering that captures U-turn tracklets. Our results show
that these methods improve both IDR and IDP, with a ﬁnal
IDF1 score of 0.8437.
References
[1] Pedro
Antonio
Marin-Reyes,
Andrea
Palazzi,
Luca
Bergamini, Simone Calderara, Javier Lorenzo-Navarro, and
Rita Cucchiara. Unsupervised vehicle re-identiﬁcation using
triplet networks. In Proceedings of the IEEE Conference on
Computer Vision and Pattern Recognition Workshops, pages
166–171, 2018. 1
[2] Luca Bertinetto, Jack Valmadre, Joao F Henriques, Andrea
Vedaldi, and Philip HS Torr. Fully-convolutional siamese
networks for object tracking.
In European conference on
computer vision, pages 850–865. Springer, 2016. 2
[3] Alex Bewley, Zongyuan Ge, Lionel Ott, Fabio Ramos, and
Ben Upcroft.
Simple online and realtime tracking.
2016
IEEE International Conference on Image Processing (ICIP),
2016. 3
[4] Alexey
Bochkovskiy,
Chien-Yao
Wang,
and
Hong-
Yuan Mark Liao. Yolov4: Optimal speed and accuracy of
object detection. arXiv preprint arXiv:2004.10934, 2020. 2
[5] Zhaowei Cai and Nuno Vasconcelos. Cascade r-cnn: Delving
into high quality object detection. In 2018 IEEE/CVF Con-
ference on Computer Vision and Pattern Recognition, pages
6154–6162, 2018. 2
[6] Martin Danelljan, Goutam Bhat, Fahad Shahbaz Khan, and
Michael Felsberg. Eco: Efﬁcient convolution operators for
tracking. 2017 IEEE Conference on Computer Vision and
Pattern Recognition (CVPR), 2017. 3
[7] Martin Danelljan, Goutam Bhat, Fahad Shahbaz Khan, and
Michael Felsberg.
Eco:
Efﬁcient convolution operators
for tracking.
In Proceedings of the IEEE conference on
computer vision and pattern recognition, pages 6638–6646,
2017. 2
[8] Martin Danelljan, Andreas Robinson, Fahad Shahbaz Khan,
and Michael Felsberg.
Beyond correlation ﬁlters: Learn-
ing continuous convolution operators for visual tracking. In
European conference on computer vision, pages 472–488.
Springer, 2016. 2
[9] Zhiqun He, Yu Lei, Shuai Bai, and Wei Wu. Multi-camera
vehicle tracking with powerful visual features and spatial-
temporal cue. In CVPR Workshops, pages 203–212, 2019.
1
[10] Jo˜ao F Henriques, Rui Caseiro, Pedro Martins, and Jorge
Batista. High-speed tracking with kernelized correlation ﬁl-
ters. IEEE transactions on pattern analysis and machine in-
telligence, 37(3):583–596, 2014. 2
[11] Yunzhong Hou, Heming Du, and Liang Zheng.
A local-
ity aware city-scale multi-camera vehicle tracking system.
In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition Workshops, pages 167–174,
2019. 1
[12] Hung-Min Hsu, Tsung-Wei Huang, Gaoang Wang, Jiarui
Cai, Zhichao Lei, and Jenq-Neng Hwang.
Multi-camera
tracking of vehicles based on deep features re-id and
trajectory-based camera link models. In CVPR Workshops,
pages 416–424, 2019. 1
[13] Zdenek Kalal,
Krystian Mikolajczyk,
and Jiri Matas.
Tracking-learning-detection. IEEE transactions on pattern
3271
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on January 07,2026 at 23:39:28 UTC from IEEE Xplore.  Restrictions apply. 


---

# Page 9

analysis and machine intelligence, 34(7):1409–1422, 2011.
2
[14] Young-Gun Lee, Jenq-Neng Hwang, and Zhijun Fang. Com-
bined estimation of camera link models for human track-
ing across nonoverlapping cameras. In 2015 IEEE Interna-
tional Conference on Acoustics, Speech and Signal Process-
ing (ICASSP), pages 2254–2258. IEEE, 2015. 1
[15] Bo Li, Wei Wu, Qiang Wang, Fangyi Zhang, Junliang Xing,
and Junjie Yan.
Siamrpn++:
Evolution of siamese vi-
sual tracking with very deep networks. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 4282–4291, 2019. 2
[16] Bo Li, Junjie Yan, Wei Wu, Zheng Zhu, and Xiaolin Hu.
High performance visual tracking with siamese region pro-
posal network. In Proceedings of the IEEE conference on
computer vision and pattern recognition, pages 8971–8980,
2018. 2
[17] Chong Liu, Yuqi Zhang, Hao Luo, Jiasheng Tang, Weihua
Chen, Xianzhe Xu, Fan Wang, Hao Li, and Yi-Dong Shen.
City-scale multi-camera vehicle tracking guided by cross-
road zones. 2021 IEEE/CVF Conference on Computer Vi-
sion and Pattern Recognition Workshops (CVPRW), 2021. 3,
7
[18] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian
Szegedy, Scott Reed, Cheng-Yang Fu, and Alexander C
Berg. Ssd: Single shot multibox detector. In European con-
ference on computer vision, pages 21–37. Springer, 2016. 2
[19] Pedro Antonio Mar´ın-Reyes,
Luca Bergamini,
Javier
Lorenzo-Navarro, Andrea Palazzi, Simone Calderara, and
Rita Cucchiara. Unsupervised vehicle re-identiﬁcation using
triplet networks. In 2018 IEEE/CVF Conference on Com-
puter Vision and Pattern Recognition Workshops (CVPRW),
pages 166–1665, 2018. 3
[20] Milind Naphade, Shuo Wang, David C. Anastasiu, Zheng
Tang, Ming-Ching Chang, Xiaodong Yang, Yue Yao, Liang
Zheng, Pranamesh Chakraborty, Christian E. Lopez, Anuj
Sharma, Qi Feng, Vitaly Ablavsky, and Stan Sclaroff. The
5th AI City Challenge. In Proc. CVPR Workshops, pages
4263–4273, Virtual, 2021. 7
[21] Yijun Qian, Lijun Yu, Wenhe Liu, and Alexander G Haupt-
mann. Electricity: An efﬁcient multi-camera vehicle track-
ing system for intelligent city.
In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern
Recognition Workshops, pages 588–589, 2020. 1
[22] Joseph Redmon, Santosh Divvala, Ross Girshick, and Ali
Farhadi. You only look once: Uniﬁed, real-time object de-
tection. In 2016 IEEE Conference on Computer Vision and
Pattern Recognition (CVPR), pages 779–788, 2016. 2
[23] Joseph Redmon and Ali Farhadi. Yolo9000: Better, faster,
stronger. In 2017 IEEE Conference on Computer Vision and
Pattern Recognition (CVPR), pages 6517–6525, 2017. 2
[24] Joseph Redmon and Ali Farhadi. Yolov3: An incremental
improvement. arXiv preprint arXiv:1804.02767, 2018. 2
[25] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun.
Faster r-cnn: Towards real-time object detection with region
proposal networks. IEEE Transactions on Pattern Analysis
and Machine Intelligence, 39(6):1137–1149, 2017. 2
[26] Ergys Ristani, Francesco Solera, Roger Zou, Rita Cucchiara,
and Carlo Tomasi. Performance measures and a data set for
multi-target, multi-camera tracking. In European conference
on computer vision, pages 17–35. Springer, 2016. 7
[27] Jakub ˇSpanhel, Vojtech Bartl, Roman Jur´anek, and Adam
Herout. Vehicle re-identiﬁcation and multi-camera tracking
in challenging city-scale environment. In Proc. CVPR Work-
shops, volume 2, page 1, 2019. 1
[28] Zheng Tang, Milind Naphade, Ming-Yu Liu, Xiaodong
Yang, Stan Birchﬁeld, Shuo Wang, Ratnesh Kumar, David
Anastasiu, and Jenq-Neng Hwang. CityFlow: A city-scale
benchmark for multi-target multi-camera vehicle tracking
and re-identiﬁcation.
In Proc. CVPR, pages 8797–8806,
Long Beach, CA, USA, 2019. 7
[29] Zheng Tang, Gaoang Wang, Hao Xiao, Aotian Zheng, and
Jenq-Neng Hwang. Single-camera and inter-camera vehicle
tracking and 3d speed estimation based on fusion of visual
and semantic features. In Proceedings of the IEEE confer-
ence on computer vision and pattern recognition workshops,
pages 108–115, 2018. 1
[30] Ultralytics.
Yolov5.
https : / / github . com /
ultralytics/yolov5. Accessed in 2022.04. 2, 3
[31] Nicolai Wojke, Alex Bewley, and Dietrich Paulus. Simple
online and realtime tracking with a deep association metric.
In 2017 IEEE International Conference on Image Processing
(ICIP), pages 3645–3649, 2017. 3
[32] Yifu Zhang, Peize Sun, Yi Jiang, Dongdong Yu, Zehuan
Yuan, Ping Luo, Wenyu Liu, and Xinggang Wang. Byte-
track: Multi-object tracking by associating every detection
box. arXiv preprint arXiv:2110.06864, 2021. 4
[33] Yifu Zhang, Chunyu Wang, Xinggang Wang, Wenjun Zeng,
and Wenyu Liu. Fairmot: On the fairness of detection and
re-identiﬁcation in multiple object tracking.
International
Journal of Computer Vision, 129(11):3069–3087, 2021. 3
3272
Authorized licensed use limited to: Universidade Tecnologica Federal do Parana. Downloaded on January 07,2026 at 23:39:28 UTC from IEEE Xplore.  Restrictions apply. 


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
