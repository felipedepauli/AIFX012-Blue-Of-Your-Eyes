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

Traffic-Aware Multi-Camera Tracking of Vehicles Based on ReID
and Camera Link Model
Hung-Min Hsu
hmhsu@uw.edu
University of Washington
Seattle, Washington
Yizhou Wang
ywang26@uw.edu
University of Washington
Seattle, Washington
Jenq-Neng Hwang
hwang@uw.edu
University of Washington
Seattle, Washington
ABSTRACT
Multi-target multi-camera tracking (MTMCT), i.e., tracking multi-
ple targets across multiple cameras, is a crucial technique for smart
city applications. In this paper, we propose an effective and reliable
MTMCT framework for vehicles, which consists of a traffic-aware
single camera tracking (TSCT) algorithm, a trajectory-based cam-
era link model (CLM) for vehicle re-identification (ReID), and a
hierarchical clustering algorithm to obtain the cross camera vehicle
trajectories. First, the TSCT, which jointly considers vehicle appear-
ance, geometric features, and some common traffic scenarios, is
proposed to track the vehicles in each camera separately. Second,
the trajectory-based CLM is adopted to facilitate the relationship
between each pair of adjacently connected cameras and add spatio-
temporal constraints for the subsequent vehicle ReID with temporal
attention. Third, the hierarchical clustering algorithm is used to
merge the vehicle trajectories among all the cameras to obtain the
final MTMCT results. Our proposed MTMCT is evaluated on the
CityFlow dataset and achieves a new state-of-the-art performance
with IDF1 of 74.93%.
CCS CONCEPTS
• Computing methodologies →Tracking; Computer vision
tasks; Neural networks.
KEYWORDS
MTMCT, multi-camera tracking, traffic-aware single camera track-
ing, camera link model, vehicle ReID, hierarchical clustering
ACM Reference Format:
Hung-Min Hsu, Yizhou Wang, and Jenq-Neng Hwang. 2020. Traffic-Aware
Multi-Camera Tracking of Vehicles Based on ReID and Camera Link Model.
In Proceedings of the 28th ACM International Conference on Multimedia (MM
’20), October 12–16, 2020, Seattle, WA, USA. ACM, New York, NY, USA, 9 pages.
https://doi.org/10.1145/3394171.3413863
1
INTRODUCTION
Due to the exponential growth of the deployed surveillance cameras
with networking supports, the opportunity to take advantage of
the rich information from the multi-camera systems is immense.
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than ACM
must be honored. Abstracting with credit is permitted. To copy otherwise, or republish,
to post on servers or to redistribute to lists, requires prior specific permission and/or a
fee. Request permissions from permissions@acm.org.
MM ’20, October 12–16, 2020, Seattle, WA, USA
© 2020 Association for Computing Machinery.
ACM ISBN 978-1-4503-7988-5/20/10...$15.00
https://doi.org/10.1145/3394171.3413863
Among the techniques for multi-camera systems, multi-target multi-
camera tracking (MTMCT) is important for traffic flow optimization
and anomaly detection. Basically, MTMCT consists of two sub-tasks:
1) Single camera tracking (SCT): Detection and tracking of the
objects within each single camera; 2) Inter-camera tracking (ICT):
Associations of the object trajectories across different cameras.
Overall, MTMCT is aimed to obtain the trajectories of every object
in the scene through all the cameras in the system.
However, MTMCT is a very challenging task due to unreliable
object detection, heavy occlusion, low resolution, and varying light-
ing and viewing-perspective conditions. Recently, many proposed
works for MTMCT take into account target motion and human
pose. Among these works, most of them are person based MTMCT,
which only considers humans as the tracking targets. For vehicles,
this task becomes more challenging because: 1) vehicles may stop
for a long time at the traffic signs and continually be occluded
among each other, which makes occlusion even more severe; 2)
inter-class similarity for vehicles is higher because there may exist
many different identities with the similar appearance.
To solve these two aforementioned challenges, we propose a
novel MTMCT framework, which mainly consists of two inno-
vations, i.e., traffic-aware single camera tracking (TSCT) and the
trajectory-based camera link model (CLM).
First, TSCT is proposed to handle the long-term occlusions cre-
ated in the traffic scenarios. Usually, there will be a large number
of isolated and fragmented vehicle trajectories, created from a sin-
gle camera multi-target tracker, in the center of the frames where
vehicles do not enter or exit the camera’s field of view (FoV). For
example, when a vehicle stops in front of a red traffic light, it can be
partially or even fully occluded in the camera’s FoV for a long time.
We would like to call this kind of zone as a traffic-aware zone. Here,
we use the TrackletNet tracker (TNT) [36], which is a superior SCT
method in intelligent transportation system application [11, 37, 38],
as our single camera tracker. According to this condition, TSCT
is proposed to find out the traffic-aware zones, where this kind of
occlusion happens, by clustering the start and end nodes of all the
resulting trajectories from the TNT. Vehicle Re-ID in the single cam-
era is then implemented for these traffic-aware zones to connect
these disconnected trajectories created in the traffic scenarios.
Second, facing higher inter-class appearance similarity of dis-
tinct vehicles, trajectory-based CLM is further proposed to impose
spatio-temporal constraints and reduce solution search space for
the cross camera ReID. For two different vehicles with a very sim-
ilar appearance, it is nearly impossible to re-identify them using
a typical ReID method. However, taking advantage of the spatial
and temporal constraints between a pair of adjacently connected
cameras, we can easily filter out the vehicles that are not likely to
arXiv:2008.09785v2  [cs.CV]  30 Aug 2020


---

# Page 2

Figure 1: The illustration of our MTMCT framework. First, the traffic-aware single camera tracking (TSCT) is utilized to obtain
SCT results for each camera. Second, CLMs with entry/exit zones and transition times are automatically generated. Third,
vehicle ReID with temporal attention is implemented on the solution space from the CLM. Finally, the hierarchical clustering
is involved for the final MTMCT results.
appear in a certain camera at a certain timestamp. We define these
constraints, including the vehicle entry/exit zones and the transi-
tion times, as the CLM. Using the CLM automatically generated
from the training data, cross camera vehicle ReID becomes much
more accurate and efficient.
Finally, a hierarchical clustering algorithm, based on the Eu-
clidean distance between the feature space of different trajectories,
is used to merge the trajectories among all the cameras to obtain
the final MTMCT results.
Overall, the framework of our proposed MTMCT is shown in
Fig. 1. First, we use the TNT [36] to obtain SCT results for each
camera. Based on the results from the TNT, our proposed TSCT
can generate the traffic-aware zones and perform vehicle ReID
within each camera to solve the occlusion problem. We then analyze
the vehicle trajectories in the training dataset and automatically
generate the CLM, i.e., the entry/exit zones and the transition times,
for each camera. After that, vehicle ReID with temporal attention
is implemented on the solution space from the CLM. Finally, the
hierarchical clustering is introduced for the final MTMCT results.
To summarize, we claim the following contributions:
• Propose a new MTMCT framework specifically designed for
vehicles.
• Utilize a novel TSCT strategy to improve vehicle SCT results,
considering common traffic scenarios.
• Create a trajectory-based CLM generation method that adds
spatio-temporal constraints and reduces the solution space
for cross camera vehicle ReID.
• Achieve a new state-of-the-art performance on the CityFlow
dataset.
The rest of the paper is organized as follows. In Section 2, we
provide an overview of the related works. Our proposed framework
for MTMCT of vehicles is introduced in Section 3. Section 4 presents
our experimental results of the proposed MTMCT framework on the
CityFlow dataset [34]. Finally, the conclusion is drawn in Section 5.
2
RELATED WORKS
Single camera multi-object tracking. Tracking-by-detection based
multi-object tracking approaches [2, 42] are the most popular schemes
for single camera tracking (SCT). Many approaches define SCT as a
graph optimization problem [3, 14, 29–31, 35, 39], i.e., each detected
object is represented as a vertex to form a graph with edges denot-
ing the affinity (similarity) between two detections in two image
frames, while in some works [3, 29, 35, 39], a vertex denotes a track-
let formed from some association rules, with the edges denoting the
affinity between two disconnected tracklets. The appearance fea-
ture plays a vital role in the tracking-by-detection framework. Many
different types of appearance features are applied to deal with SCT.
For example, CNN-based features have been widely used for ReID
tasks [25, 31, 43, 45], where metric learning is exploited to train
the CNN-based features [25]. Furthermore, appearance features
and temporal features can be combined [35, 43] to achieve better
performance. However, none of these methods can fully handle the
long occlusion caused by the different traffic scenarios.
Camera link model. A camera link model (CLM) consists of
camera link information and transition time distribution of a pair
of adjacently connected cameras, i.e., CLM takes spatio-temporal
constraints into consideration. In MTMCT, the CLM can be used as
effective constraints to reduce the search space of matching so as to


---

# Page 3

improve the performance of MTMCT, as evidenced in some works
[11, 15, 34, 35]. For example, Lee et al. [15] use the CLM to estimate
bidirectional transition time distribution in an unsupervised scheme
for MTMCT. Tang et al. [34, 35] and Hsu et al. [11] also use the car
speed to generate the transition time distribution for each connected
pair of adjacently connected cameras. Therefore, the accuracy of
MTMCT can be significantly improved by CLM by reducing the
candidate set of matching. In this paper, we systematically generate
the CLMs to assist the ReID in the MTMCT tasks.
Appearance feature based vehicle ReID. Vehicle ReID has attracted
more research efforts in the past few years. VeRi-776 [17] and VeRi-
Wild [20] are the most widely used benchmarks, which provide not
only the high quality annotations but also the camera deployment
geometry. In ReID, there are two types of appearance feature ex-
traction methods. One is traditional handcrafted methods, such as
SURF [1] and ORB [26]. The other is CNN-based methods [41, 44],
which have been proven to achieve better performance than tradi-
tional handcrafted methods in the past years. Thus, recent meth-
ods [17, 19] focus on learning an embedding model that maps the
samples into an embedding space. Liu et al. [17] propose a mixed
difference network using a vehicle model and ID information to
construct more robust feature embedding. Liu et al. [19] propose
a “PROVID” ReID model by using visual feature, license plate and
spatio-temporal information for the vehicle ReID task. Shen et
al. [27] incorporate complex spatio-temporal information for ef-
fectively regularizing the ReID results by a two-stage framework.
Based on a multi-view inference scheme, Zhou et al. [46] generate
a global-view feature representation to improve the vehicle ReID.
Huang et al. [12] utilize car key points to train orientation-based
embedding for vehicle ReID. Tang et al. [33] propose a pose-aware
multi-task re-identification (PAMTRI) framework by explicitly rea-
soning about vehicle pose, shape, color, and types. In this work, we
propose a trajectory-based CLM to enhance the performance of
vehicle ReID.
3
PROPOSED METHOD
There are four steps in our proposed method, as illustrated in Fig. 1.
First, we apply TSCT after a single camera tracker TNT, as presented
in Section 3.1. Then, the camera links are established based on the
generated entry/exit zones, as illustrated in Section 3.2. Moreover,
we utilize a vehicle ReID method by combining the temporal atten-
tion and batch sampling for inter-camera tracking, as explained in
Section 3.3. Finally, we use the hierarchical clustering to merge the
tracklets into object trajectories, as described in Section 3.4.
3.1
Traffic-Aware Single Camera Tracking
(TSCT)
In our MTMCT framework, the first step is SCT, where we imple-
ment the TrackletNet Tracker (TNT) [36]. A TNT is a tracklet-based
graph clustering approach, where the vertices are generated based
on detection association via CNN-based appearance feature and
the intersection-over-union (IOU) in the two consecutive frames.
While, the edge weights are estimated by a TrackletNet, which is
a Siamese neural network trained to predict the likelihood of the
two tracklets belonging to the same object. After the tracklet-based
graph is constructed, graph clustering [35] is applied to merge the
tracklets of the same vehicle into one single trajectory.
After using TNT to generate the SCT results, we observe that
there are some vehicle ID switches due to some isolated trajectories,
which usually appear while vehicles are waiting for a traffic light.
Therefore, we propose TSCT to deal with this issue by generat-
ing the traffic-aware zones and performing single camera ReID to
reconnect the isolated trajectories caused by the traffic scenarios.
First of all, all the traffic-aware zones within each camera are
detected in an unsupervised manner based on the MeanShift cluster-
ing algorithm [4] applied on the collected entry/exit measurements.
The procedure of traffic-aware zone generation is as follows: 1)
use the first and the last positions of all the trajectories from the
SCT results as zone nodes; 2) cluster the zone nodes into different
groups by apply the MeanShift algorithm.
After the MeanShift, we define a rectangular zone for each group
to bound the inside nodes. We denote Ne,k as the number of entry
nodes and Nx,k as the number of exit nodes in the zone k. The
traffic-aware density Dta is defined by
Dta = 1 −|Ne,k −Nx,k |
Ne,k + Nx,k
,
(1)
where Dta needs to be above a threshold ρta, the zone will be
designated as a traffic-aware zone, as shown in Fig. 2(c).
After the traffic-aware zones are generated, the next step is to
reconnect the isolated trajectories in these zones. Here, we build a
queue for each zone to store the ordering and appearance features of
the vehicles that are interrupted in the traffic-aware zones. If there
is a bounding box of an isolated trajectory that suddenly appears
in the traffic-aware zone, we select a trajectory from the queue
to compute the appearance similarity. The appearance feature is
trained by single camera ReID, which is similar to the cross camera
ReID, as explained in Section 3.3.
3.2
Trajectory-based Camera Link Model
Our trajectory-based CLM can be divided into three steps: 1) en-
try/exit zones generation in each single camera; 2) vehicle trajectory
classification according to entry-exit zone pairs in each single cam-
era; 3) camera links and transition time estimation across different
cameras. These three steps are described below.
Entry/exit zones generation. With the available routes and the
detected entry/exit zones, we can estimate the relationship between
each two zones. For a trajectory-based CLM, the procedure of the
entry/exit zone generation is similar to the traffic-aware zone gen-
eration. The only difference is to calculate the entry and exit density
to determine whether the generated zone is an entry/exit zone or
not. The entry and exit densities are defined as De and Dx, where
De =
Ne,k
Ne,k + Nx,k
, Dx =
Nx,k
Ne,k + Nx,k
.
(2)
If the density of an entry or exit zone is higher than a threshold ρe
or ρx, this zone will be recognized as an entry or exit zone. There
may be multiple entry/exit zones within one camera’s FoV.
Vehicle trajectory classification by zone pairs. After the zones are
generated, all of the trajectories need to be classified according to
entry-exit zone pairs. In our model, an entry-exit zone pair is used


---

# Page 4

Figure 2: Traffic-aware zone generation. (a) Raw video from a surveillance camera. (b) Start/end points of all trajectories from
SCT (red: entry; blue: exit). (c) The clustering result for traffic-aware zone generation from Meanshift (red: stop for traffic light;
blue: truncated vehicles). (d) A queue for isolated trajectories is maintained to keep the ordering and appearance features for
following single camera ReID.
to uniquely describe a trajectory, which is called a zone pair trajec-
tory, as shown in Fig. 3(a). In this paper, we generate all possible
camera links by using the training data of MTMCT to systematically
generate the camera links instead of human labeling. In most cases,
the straight and the right-turn trajectories can be described using
different zone pairs being passed through. Sometimes the trajectory
may not pass through the corresponding zone pair perfectly due to
the viewing angle of the camera, i.e., also passes through the neigh-
boring zones associated with the adjacently connected zone pair.
In this case, measuring the distance (mismatch) between a tracked
vehicle and a zone-pair trajectory is necessary. The distance can be
calculated as
dist(P,V ) =
Õ
z ∈P∪V
|1(z ∈P) −αz |,
(3)
where P denotes the zone-pair trajectory and V is the actual zones
gone through by the tracked vehicle, αz represents the overlapping
ratio of the vehicle to zone z, i.e., the overlapping area divided by
the vehicle bounding box area. Furthermore, the order of the zones
in the zone pair and the tracked vehicle is also considered. Once
the order in the tracked vehicle conflicts with the zone pair, the
distance between a tracked vehicle and a zone-pair trajectory is set
to infinity. Finally, the closest zone-pair trajectory with minimum
distance is assigned by comparing the tracked vehicle with all the
possible zone-pair trajectories within the camera. An example of
distance calculation is shown in Fig. 3(b).
Camera link model construction. Given the locations of the cam-
eras, we can obtain the routing information provided by the training
data. The routing information contains all the links between every
two adjacently connected cameras. If there is one link that connects
two cameras without passing through another camera, we define
them as a camera link. In other words, if all the routes from the
training data between two cameras passed by at least one other
camera, this link should not exist in our camera link model.
The camera link and the corresponding transition time of each
camera pair can be defined as T = (Cs,Cd), where Cs = {Ps
i }m
i=1 is
the zone pair trajectories set in the source camera andCd = {Pd
j }n
j=1
is that set in the destination camera. Each camera pair can have
more than one transition time due to the bi-directional traffic. In
the camera pair with the overlapping view, T usually only contains
one single zone pair trajectory, while for the non-overlapping view
case, T can involve multiple zone pair trajectories. An example to
explain the concept of our camera link model is shown in Fig. 4(a).
Transition time estimation. To estimate the transition time of
each camera link T, we first define the transition zones zs and zd,
such that zs ∈Ps
i (∀Ps
i ∈Cs) and zd ∈Pd
j (∀Pd
j ∈Cd). Then, the
transition time can be applied as the temporal constraint for both
Cs and Cd. Given a camera link of a vehicle trajectory from Ps to
Pd, i.e., from source camera to destination camera, the transition
time is defined as
∆t = ts −td,
(4)
where ts and td represent the time of the tracks passing zs and zd,
respectively. We can then obtain a time window (∆tmin, ∆tmax) for
each camera link T so that only the tracked vehicle pairs whose
transition time are within the time window are considered as valid.
Thus, the search space of the ReID can be greatly reduced by using
the appropriate time window. Then, we can use the embedding
feature from the ReID model, trajectory-based camera link model,
and clustering algorithm to produce the global IDs for MTMCT.


---

# Page 5

Figure 3: Illustration of distance calculation between a ve-
hicle trajectory (black) and each entry-exit zone pair. There
are four zone pairs (A, B, C, D) with two entry and two exit
zones in current frame. The vehicle pass through the four
zones with certain IOU in the upper table in (b). The dis-
tances are calculated according to Eq. 3. As a result, this ve-
hicle trajectory is classified to zone pair A, which has the
smallest distance.
3.3
Cross Camera ReID
After TSCT, the SCT results for each camera are available as the
input data for MTMCT. Video-based ReID can achieve better perfor-
mance than image-based ReID since it can take advantage of tem-
poral continuity of a sequence of image frames instead of a single
image. Therefore, an MTMCT system usually uses trajectory-level
features for ReID. The feature extractor is based on the ResNet-50
[6], which is pre-trained on ImageNet, and the appearance feature
of a vehicle is a 2048-dim vector output by the fully connected layer.
Once the frame-level features are extracted, we use temporal
attention (TA) mechanism [5] to aggregate the frame-level features
into the clip-level features. After that, we use the average pooling to
generate trajectory-level features. In the TA modeling, there are two
convolutional networks, one is a spatial convolutional network with
2D convolutions and the other is a temporal convolutional network
with 1D convolution. Through training these two networks, an
attention vector vatt can be obtained to weight the frame-level
features ff rame, resulting in the clip-level features, where
fclip = vatt · ff rame.
(5)
In terms of network training, metric learning is adopted to en-
hance this vehicle ReID task. To train the model in a more efficient
way, we adopt the batch sample (BS) scheme [13] in the triplet
generation. Overall, in our final loss function, the BS triplet loss
Figure 4: Examples of camera link model and the order con-
straint. There are three cameras with overlapping FoV, the
blue/red bounding boxes represent the exit/entry zones, re-
spectively. According to (a), the location of the exit zone in
the Camera 6 is the same as the location of the entry zone of
Camera 8, which means the vehicle exits the Camera 6 will
immediately appear in the Camera 8. Similarly, Camera 7
connects to Camera 6 and Camera 8 links to Camera 7.
is combined with the cross-entropy loss to jointly exploit distance
metric learning and identity classification,
Ltotal = λ1LBStri + λ2LXent .
(6)
The objective of triplet loss is to minimize the feature distance
of the same identity and maximize the feature distance of different
identity pairs [8]. For the BS triplet loss, the objective is to calculate
triplet loss LBStri(θ; ξ) in a minibatch defined as
LBStri(θ; ξ) =
Õ
b
Õ
a∈B
ltriplet (a),
(7)
where
ltriplet (a) =

m +
Õ
p ∈P(a)
wpDap −
Õ
n∈N (a)
wnDan
+
.
(8)
Here, wp and wn are the weightings of positive and negative sam-
ples, m represents the margin, Dap and Dan are the distances be-
tween the anchor sample to the positive sample and negative sam-
ple, respectively.
Based on the BS strategy, the weightings of positive and negative
samples are defined as follows,
wp = P(wp == multinomialx ∈P(a){Dax }),
wn = P(wn == multinomialx ∈N (a){Dax }),
(9)
where xp and xn are positive and negative samples, respectively.


---

# Page 6

Figure 5: Illustration of hierarchical clustering. An example
is shown in (a) for the clustering steps. (b) shows the dendro-
gram of the example with the number of clusters at different
threshold levels.
The cross-entropy (Xent) loss in the training is defined as
LXent = −1
N
N
Õ
i=1
q(i) · log(prob(i)),
(10)
where prob(i) is the probability of the probe vehicle belongs to
vehicle i, q(i) is the ground truth vector of vehicle i, and N is the
number of vehicles in training data.
3.4
Hierarchical Clustering
We perform data association between a pair of single camera trajec-
tories corresponding to an adjacently connected exit/entry zone for
multi-camera trajectories utilizing correlation clustering in each
separate short time windows. The time window (∆tmin, ∆tmax) is
generated from CLM. In each window, there is a weighted graph
G = (V, E, W), where V represents the single camera trajectory
node set, the weight W of the edge E represents the corresponding
correlation between the nodes. Therefore, MTMCT can be referred
as a correlation clustering problem. Then the issue is to partition
the node set into subsets. The single camera trajectories of the same
identity should belong to the same subset. Edges in the same subsets
accumulate high positive correlations, while edges in the different
subsets accumulate high negative correlations. The problem can
thus be defined as the following Binary Integer Program (BIP),
X ∗= arg max
{xi,j }
Õ
(i,j)∈E
wi,jxi,j,
s.t. xi,j + xj,k ≤1 + xi,k, ∀i, j,k ∈V .
(11)
The set X is the set of all possible combinations of assignments to
the binary variables xi,j. We maximize the summation of wi,jxi,j,
which rewards edges that connect the same vehicle’s multi-camera
Algorithm 1: Hierarchical Clustering
Input
:Trajectories set Ξ = {ξn} from all cameras.
Output:Global ID for all trajectories within all cameras.
Initialize distance matrix M between each two trajectories
M ←∞;
for trajectory ξi from Ξ do
for trajectory ξj from Ξ do
Mi,j ←dist(f(ξi), f(ξj));
end
end
Flatten and sort the upper triangular part of M in ascending
order: F ←sort([Mi,j]i<j);
iter ←0, δ ←distance threshold;
while iter < # of iterations do
for mi,j from F do
if mi,j < δ and valid order constraint for ξi, ξj then
Assign the same global ID to ξi and ξj;
else
mi,j ←∞;
end
end
iter + +;
end
trajectories and penalizes edges that link to the different vehicles.
If the two multi-camera trajectories i, j are from the same vehicle,
then xi,j should be assigned 1. The constraints in Eq. 11 enforce
the transitivity in the solution.
To reduce the computational complexity, we use hierarchical
clustering in our method. Fig. 5 illustrates how to cluster the single
camera trajectories into cross camera trajectories. Since the search
space of ReID is reduced by the transition time constraint, the Rank-
1 accuracy will be close to 1. Therefore, we can greedily select the
smallest pair-wise distance to merge the tracked vehicles cross
cameras. Furthermore, the order between different tracked vehicles
can be used as a constraint to further reduce the search space of
the ReID. Due to the traffic scenarios or the road conditions, the
orders of vehicles should be almost the same. Take Fig. 4(b) as an
example, we will remove the pairs whose orders conflict with those
of previously matched pairs. The process will repeat until there is
no valid transition pair, or the minimum distance is larger than a
threshold.
4
EXPERIMENTS
4.1
Dataset and Evaluation
Our research aims to addressing multi-target multi-camera tracking
of vehicles from the video sequences. CityFlow [34] is the largest
and the most representative MTMCT dataset for practical scenarios,
which is proposed in CVPR 2019 by Nvidia. To the best of our
knowledge, it is the only existing city-scale traffic camera dataset.
CityFlow contains 3.25 hours of traffic videos collected from 40
cameras across 10 intersections, spanning about 2.5 km, in a mid-
sized U.S. city. Moreover, CityFlow covers a diverse set of road
traffic types, including intersections, stretches of roadways, and


---

# Page 7

highways. The length of the training videos is 58.43 minutes, while
testing videos are 136.60 minutes in length. There are five scenarios
in the CityFlow dataset, three of the scenarios are used for training,
and the remaining two are used for testing. In total, the dataset
contains 229,680 bounding boxes for 666 distinct annotated vehicle
identities. The resolution is at least 960p and the frame rate is 10
FPS. Moreover, the license plates are blocked out in advance due to
the privacy issues, i.e., the license plate information is not allowed
to be used in the MTMCT.
In terms of implementation details, we use the dataset of the AI
City Challenge 2018 [21] for training the TNT in the SCT. Since
there are over 3.3K vehicles in the AI City Challenge 2018 dataset,
which contains much richer information than the training set in
the benchmark dataset. For both feature extraction of single camera
ReID and cross camera ReID, we use ResNet-50 as the backbone
network, trained with the combination of BS Triplet loss and Xent
loss. In TNT, the dimension of the appearance feature is 512, the
time window size is 64, and the batch size is 32. The optimizer used
for training TrackletNet is Adam and the learning rate is from 10−3
to 10−5 for decreasing 10 times in every 2000 steps.
In terms of the single and cross camera ReID, the temporal at-
tention model is trained with tracklet features from ground truth
image ReID features. Same as UWIPL [11], we select the 4 as the clip
length for each tracklet. The learning rate is 3 × 10−4, the weight
decay is 5 × 10−4, the batch size is 32, and the network is totally
trained for 800 epochs. The similarity estimation of the ReID fea-
tures is calculated by the Euclidean distance. The input images are
resized to 224 × 224. We use ResNet-50 pre-trained on ImageNet as
the backbone for our model.
For MTMCT, we use IDF1, IDP, and IDR as evaluation metrics.
IDF1 [24] is used to rank the performance of each team in the
CityFlow dataset. It calculates the ratio of correctly identified de-
tections over the average number of ground truth and computed
detections. More specifically, false negative ID (IDFN), true nega-
tive ID (IDTN) and true positive ID (IDTP) counts are all used to
compute the identification precision (IDP), the identification recall
(IDR), and the corresponding F1 score IDF1.
IDP =
IDTP
IDTP + IDFP ,
IDR =
IDTP
IDTP + IDFN ,
IDF1 =
2IDTP
2IDTP + IDFP + IDFN .
(12)
The definition of IDFN, IDTN and IDTP are as following,
IDFN =
Õ
τ
Õ
t ∈Tτ
m(τ,γm(τ),t, ∆),
IDFP =
Õ
γ
Õ
t ∈Tγ
m(τm(γ),γ,t, ∆),
IDTP =
Õ
τ
len(τ) −IDFN =
Õ
γ
len(γ) −IDFP.
(13)
where τ is the ground truth trajectory, γm(τ) means the computed
trajectory that best matches τ; γ represents computed trajectory;
τm(γ) is ground truth trajectory that best matches γ; t is the frame
index; ∆means the IOU threshold that judges whether computed
bounding box matches the ground truth bounding box (here we set
Table 1: MTMCT results comparison on CityFlow dataset.
Methods
IDF1
MOANA+BA [34]
0.3950
DeepSORT+BS [34]
0.4140
TC+BA [34]
0.4630
ZeroOne [28]
0.5987
DeepCC [25]
0.5660
LAAM [10]
0.6300
ANU [9]
0.6519
TrafficBrain [7]
0.6653
DDashcam [16]
0.6865
UWIPL[11]
0.7059
Ours
0.7493
∆= 0.5); m(·) is a mismatch function which is equal to 1 if there is
a mismatch at t; otherwise, m(·) is 0.
4.2
MTMCT Results on CityFlow
In the CityFlow dataset, the spatio-temporal information is useful
in improving the performance [7, 11, 16]. Especially, the camera
links are applied to achieve the best performance [11]. Moreover,
some systems utilize data association graph for MTMCT [9] . Most
of the existing MTMCT methods are based on the tracking-by-
detection scheme and adapted for multi-camera views. However,
the proposed method also considers traffic scenarios as well as the
camera links to enhance the MTMCT performance.
The qualitative results are shown in Fig. 6, which shows that
our method is generalized well for different cameras and vehicles.
Table 1 compares our methods with the state-of-the-art approaches
on the CityFlow benchmark. Here, locality aware appearance met-
ric (LAAM) [10] is the state-of-the-art approach on DukeMTMC
dataset. LAAM improves the performance of DeepCC by training
the model based on both intra-camera and inter-camera metrics.
The ReID features in DeepCC are extracted by DenseNet-121 with
softmax and triplet loss. In terms of LAAM, they use ResNet-50
pre-trained on ImageNet. The tracklet length is set to 10 frames,
and the temporal window sizes for SCT and ICT are set to 500
frames and 2400 frames. According to the experimental results,
our proposed method outperforms all the state-of-the-art methods,
by incorporating the traffic-aware zones for isolated trajectories
ReID and also taking advantage of the generated camera link model.
Finally, we achieve IDF1 of 74.93% for MTMCT on CityFlow. More-
over, comparing to [11], our system can automatically generate
camera links instead of human labeling.
4.3
Ablation Studies
The ablation studies of MTMCT is showed in Table 2, including
the combinations of TNT, TSCT, TA, and CLM. The experimental
results show that each proposed component helps enhance the
robustness. First, we show all modules of the proposed method are
necessary. When replacing TSCT with the TNT, IDF1 based on the
TA feature drops by 4.3% on MTMCT. A similar but greater accuracy
drop can be observed when the TA is replaced by the average
pooling. The drop is consistent when using the same tracklet based


---

# Page 8

Figure 6: Qualitative results of our MTMCT results on CityFlow dataset.
Table 2: The MTMCT performance for different combina-
tions of the proposed method.
TNT
TSCT
TA
CLM
IDF1
IDP
IDR
✓
0.1583
0.4418
0.0959
✓
✓
0.5237
0.6816
0.4221
✓
✓
0.5776
0.5918
0.5779
✓
✓
✓
0.7059
0.6912
0.7211
✓
✓
✓
✓
0.7493
0.8071
0.6918
ReID features. These results show that both the TSCT and TA are
necessary components in our system. Second, from the ablation
studies, the removal of the CLM causes a greater accuracy drop. The
reason is the transition time constraint between cameras improves
data association in tracking, so the global matching in ReID is
much better in ICT. In the vehicle ReID, high inter-class similarity
leads to small appearance variance of the targets. Consequently,
after applying the CLM, the MTMCT performance can be largely
improved. Then, we show that the TA and CLM are both important,
IDF1 can be improved from 15.83% to over 50% by using TA or CLM.
Therefore, CLM can improve MTMCT by the general ReID model.
In Table 3, we show the performance of SCT, which favorably
compares with the state-of-the-art methods for SCT [32, 35, 40].
DeepSORT [40] is an online method incorporating Kalman-filter-
based tracking and the Hungarian algorithm. TC [35] is an offline
method using tracklet clustering which is the winner of the AI City
Challenge at CVPR 2018 [21]. MOANA [32] is a state-of-the-art ap-
proach on the MOTChallenge 2015 3D benchmark. There are three
sets of available detection results, i.e., SSD512 [18], YOLOv3 [22]
and Faster R-CNN [23], which are provided by the CityFlow dataset.
According to [34], SSD512 [18] performs the best and is used by us
Table 3: SCT results on CityFlow.
Methods
IDF1
MOTA
MOTP
Recall
MT
DeepSORT [40]
79.5%
68.9%
65.5%
69.2%
756
TC [35]
79.7%
70.3%
65.6%
70.4%
895
MOANA [32]
72.8%
67.0%
65.9%
68.0%
980
Ours
88.4%
79.3%
75.2%
85.1%
1726
for comparison. The metrics of SCT include IDF1, Multiple Object
Tracking Accuracy (MOTA), Multiple Object Tracking Precision
(MOTP), Recall and the mostly tracked targets (MT). According to
the experimental results, the proposed TSCT method achieves the
best performance.
5
CONCLUSION
In this paper, we propose a novel approach for multi-target multi-
camera tracking (MTMCT) of vehicles, which includes traffic-aware
single camera tracking (TSCT), trajectory-based camera link model
(CLM), and vehicle re-identification (ReID). Finally, hierarchical
clustering is utilized to merge the vehicle trajectories from differ-
ent cameras and generates the MTMCT results. From our experi-
ments, the proposed method is shown to be effective and robust. It
also achieves a new state-of-the-art performance on the CityFlow
dataset.
ACKNOWLEDGEMENT
This work was partially supported by Electronics and Telecommu-
nications Research Institute (ETRI) grant funded by the Korean
government. [20ZD1100, Development of ICT Convergence Tech-
nology for Daegu-GyeongBuk Regional Industry]


---

# Page 9

REFERENCES
[1] Herbert Bay, Tinne Tuytelaars, and Luc Van Gool. 2006. Surf: Speeded up robust
features. In European conference on computer vision. Springer, 404–417.
[2] Jiarui Cai, Yizhou Wang, Haotian Zhang, Hung-Min Hsu, Chengqian Ma, and
Jenq-Neng Hwang. 2020. IA-MOT: Instance-Aware Multi-Object Tracking with
Motion Consistency. BMTT Challenge Workshop, IEEE Conference on Computer
Vision and Pattern Recognition (2020).
[3] Wongun Choi. 2015. Near-online multi-target tracking with aggregated local
flow descriptor. In Proceedings of the IEEE international conference on computer
vision. 3029–3037.
[4] Dorin Comaniciu and Peter Meer. 2002. Mean shift: A robust approach toward fea-
ture space analysis. IEEE Transactions on pattern analysis and machine intelligence
24, 5 (2002), 603–619.
[5] Jiyang Gao and Ram Nevatia. 2018. Revisiting Temporal Modeling for Video-
based Person ReID. arXiv preprint arXiv:1805.02104 (2018).
[6] Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian Sun. 2016. Deep residual
learning for image recognition. In Proceedings of the IEEE conference on computer
vision and pattern recognition. 770–778.
[7] Zhiqun He, Yu Lei, Shuai Bai, and Wei Wu. 2019. Multi-Camera vehicle tracking
with powerful visual features and spatial-temporal cue. In Proc. CVPR Workshops.
203–212.
[8] Alexander Hermans, Lucas Beyer, and Bastian Leibe. 2017. In defense of the
triplet loss for person re-identification. arXiv preprint arXiv:1703.07737 (2017).
[9] Yunzhong Hou, Heming Du, and Liang Zheng. 2019. A Locality Aware City-Scale
Multi-Camera Vehicle Tracking System. In Proceedings of the IEEE Conference on
Computer Vision and Pattern Recognition Workshops. 167–174.
[10] Yunzhong Hou, Liang Zheng, Zhongdao Wang, and Shengjin Wang. 2019. Local-
ity Aware Appearance Metric for Multi-Target Multi-Camera Tracking. arXiv
preprint arXiv:1911.12037 (2019).
[11] Hung-Min Hsu, Tsung-Wei Huang, Gaoang Wang, Jiarui Cai, Zhichao Lei, and
Jenq-Neng Hwang. 2019. Multi-Camera Tracking of Vehicles based on Deep
Features Re-ID and Trajectory-Based Camera Link Models. In AI City Challenge
Workshop, IEEE/CVF Computer Vision and Pattern Recognition (CVPR) Conference,
Long Beach, California.
[12] Tsung-Wei Huang, Jiarui Cai, Hao Yang, Hung-Min Hsu, and Jenq-Neng Hwang.
2019. Multi-View Vehicle Re-Identification using Temporal Attention Model and
Metadata Re-ranking. In AI City Challenge Workshop, IEEE/CVF Computer Vision
and Pattern Recognition (CVPR) Conference, Long Beach, California.
[13] Ratnesh Kuma, Edwin Weill, Farzin Aghdasi, and Parthasarathy Sriram. 2019.
Vehicle re-identification: an efficient baseline using triplet embedding. In 2019
International Joint Conference on Neural Networks (IJCNN). IEEE, 1–9.
[14] Ratnesh Kumar, Guillaume Charpiat, and Monique Thonnat. 2014. Multiple
object tracking by efficient graph partitioning. In Asian Conference on Computer
Vision. Springer, 445–460.
[15] Young-Gun Lee, Jenq-Neng Hwang, and Zhijun Fang. 2015. Combined estimation
of camera link models for human tracking across nonoverlapping cameras. In
2015 IEEE International Conference on Acoustics, Speech and Signal Processing
(ICASSP). IEEE, 2254–2258.
[16] Peilun Li, Guozhen Li, Zhangxi Yan, Youzeng Li, Meiqi Lu, Pengfei Xu, Yang Gu,
Bing Bai, Yifei Zhang, and DiDi Chuxing. 2019. Spatio-temporal consistency and
hierarchical matching for multi-target multi-camera vehicle tracking. In Proc.
CVPR Workshops. 222–230.
[17] Hongye Liu, Yonghong Tian, Yaowei Yang, Lu Pang, and Tiejun Huang. 2016.
Deep relative distance learning: Tell the difference between similar vehicles. In
Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition.
2167–2175.
[18] Wei Liu, Dragomir Anguelov, Dumitru Erhan, Christian Szegedy, Scott Reed,
Cheng-Yang Fu, and Alexander C Berg. 2016. Ssd: Single shot multibox detector.
In European conference on computer vision. Springer, 21–37.
[19] Xinchen Liu, Wu Liu, Tao Mei, and Huadong Ma. 2016. A deep learning-based ap-
proach to progressive vehicle re-identification for urban surveillance. In European
Conference on Computer Vision. Springer, 869–884.
[20] Yihang Lou, Yan Bai, Jun Liu, Shiqi Wang, and Lingyu Duan. 2019. Veri-wild:
A large dataset and a new method for vehicle re-identification in the wild. In
Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition.
3235–3243.
[21] Milind Naphade, Ming-Ching Chang, Anuj Sharma, David C Anastasiu, Vamsi
Jagarlamudi, Pranamesh Chakraborty, Tingting Huang, Shuo Wang, Ming-Yu
Liu, Rama Chellappa, et al. 2018. The 2018 nvidia ai city challenge. In Proceedings
of the IEEE Conference on Computer Vision and Pattern Recognition Workshops.
53–60.
[22] Joseph Redmon and Ali Farhadi. 2018. Yolov3: An incremental improvement.
arXiv preprint arXiv:1804.02767 (2018).
[23] Shaoqing Ren, Kaiming He, Ross Girshick, and Jian Sun. 2015. Faster r-cnn:
Towards real-time object detection with region proposal networks. In Advances
in neural information processing systems. 91–99.
[24] Ergys Ristani, Francesco Solera, Roger Zou, Rita Cucchiara, and Carlo Tomasi.
2016. Performance measures and a data set for multi-target, multi-camera track-
ing. In European Conference on Computer Vision. Springer, 17–35.
[25] Ergys Ristani and Carlo Tomasi. 2018. Features for Multi-Target Multi-Camera
Tracking and Re-Identification. arXiv preprint arXiv:1803.10859 (2018).
[26] Ethan Rublee, Vincent Rabaud, Kurt Konolige, and Gary R Bradski. 2011. ORB:
An efficient alternative to SIFT or SURF.. In ICCV, Vol. 11. Citeseer, 2.
[27] Yantao Shen, Tong Xiao, Hongsheng Li, Shuai Yi, and Xiaogang Wang. 2017.
Learning deep neural networks for vehicle re-id with visual-spatio-temporal path
proposals. In Proceedings of the IEEE International Conference on Computer Vision.
1900–1909.
[28] Xiao Tan, Zhigang Wang, Minyue Jiang, Xipeng Yang, Jian Wang, Yuan Gao,
Xiangbo Su, Xiaoqing Ye, Yuchen Yuan, Dongliang He, et al. 2019. Multi-camera
vehicle tracking and re-identification based on visual and spatial-temporal fea-
tures. In Proceedings of the IEEE Conference on Computer Vision and Pattern
Recognition Workshops. 275–284.
[29] Siyu Tang, Bjoern Andres, Miykhaylo Andriluka, and Bernt Schiele. 2015. Sub-
graph decomposition for multi-target tracking. In Proceedings of the IEEE Confer-
ence on Computer Vision and Pattern Recognition. 5033–5041.
[30] Siyu Tang, Bjoern Andres, Mykhaylo Andriluka, and Bernt Schiele. 2016. Multi-
person tracking by multicut and deep matching. In European Conference on
Computer Vision. Springer, 100–111.
[31] Siyu Tang, Mykhaylo Andriluka, Bjoern Andres, and Bernt Schiele. 2017. Multiple
people tracking by lifted multicut and person reidentification. In Proceedings of
the IEEE Conference on Computer Vision and Pattern Recognition. 3539–3548.
[32] Zheng Tang and Jenq-Neng Hwang. 2019. MOANA: An online learned adaptive
appearance model for robust multiple object tracking in 3D. IEEE Access 7 (2019),
31934–31945.
[33] Zheng Tang, Milind Naphade, Stan Birchfield, Jonathan Tremblay, William Hodge,
Ratnesh Kumar, Shuo Wang, and Xiaodong Yang. 2019. PAMTRI: Pose-Aware
Multi-Task Learning for Vehicle Re-Identification Using Highly Randomized
Synthetic Data. In Proceedings of the IEEE International Conference on Computer
Vision. 211–220.
[34] Zheng Tang, Milind Naphade, Ming-Yu Liu, Xiaodong Yang, Stan Birchfield,
Shuo Wang, Ratnesh Kumar, David Anastasiu, and Jenq-Neng Hwang. 2019.
Cityflow: A city-scale benchmark for multi-target multi-camera vehicle tracking
and re-identification. In Proceedings of the IEEE Conference on Computer Vision
and Pattern Recognition. 8797–8806.
[35] Zheng Tang, Gaoang Wang, Hao Xiao, Aotian Zheng, and Jenq-Neng Hwang.
2018. Single-camera and inter-camera vehicle tracking and 3D speed estima-
tion based on fusion of visual and semantic features. In Proceedings of the IEEE
Conference on Computer Vision and Pattern Recognition Workshops. 108–115.
[36] Gaoang Wang, Yizhou Wang, Haotian Zhang, Renshu Gu, and Jenq-Neng Hwang.
2019. Exploit the connectivity: Multi-object tracking with trackletnet. In Proceed-
ings of the 27th ACM International Conference on Multimedia. 482–490.
[37] Gaoang Wang, Xinyu Yuan, Aotian Zheng, Hung-Min Hsu, and Jenq-Neng
Hwang. 2019. Anomaly Candidate Identification and Starting Time Estimation
of Vehicles from Traffic Videos.. In CVPR Workshops. 382–390.
[38] Yizhou Wang, Yen-Ting Huang, and Jenq-Neng Hwang. 2019. Monocular Vi-
sual Object 3D Localization in Road Scenes. In Proceedings of the 27th ACM
International Conference on Multimedia. 917–925.
[39] Longyin Wen, Wenbo Li, Junjie Yan, Zhen Lei, Dong Yi, and Stan Z Li. 2014.
Multiple target tracking based on undirected hierarchical relation hypergraph.
In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition.
1282–1289.
[40] Nicolai Wojke, Alex Bewley, and Dietrich Paulus. 2017. Simple online and realtime
tracking with a deep association metric. In 2017 IEEE international conference on
image processing (ICIP). IEEE, 3645–3649.
[41] Xiang Wu, Ran He, Zhenan Sun, and Tieniu Tan. 2018. A light cnn for deep face
representation with noisy labels. IEEE Transactions on Information Forensics and
Security 13, 11 (2018), 2884–2896.
[42] Haotian Zhang, Yizhou Wang, Jiarui Cai, Hung-Min Hsu, Haorui Ji, and Jenq-
Neng Hwang. 2020. LIFTS: Lidar and Monocular Image Fusion for Multi-Object
Tracking and Segmentation. BMTT Challenge Workshop, IEEE Conference on
Computer Vision and Pattern Recognition (2020).
[43] Zhimeng Zhang, Jianan Wu, Xuan Zhang, and Chi Zhang. 2017. Multi-target,
multi-camera tracking by hierarchical clustering: Recent progress on dukemtmc
project. arXiv preprint arXiv:1712.09531 (2017).
[44] Wenzhi Zhao and Shihong Du. 2016. Spectral–spatial feature extraction for
hyperspectral image classification: A dimension reduction and deep learning
approach. IEEE Transactions on Geoscience and Remote Sensing 54, 8 (2016),
4544–4554.
[45] Zhun Zhong, Liang Zheng, Donglin Cao, and Shaozi Li. 2017. Re-ranking person
re-identification with k-reciprocal encoding. In Proceedings of the IEEE Conference
on Computer Vision and Pattern Recognition. 1318–1327.
[46] Yi Zhou and Ling Shao. 2018. Aware attentive multi-view inference for vehicle
re-identification. In Proceedings of the IEEE Conference on Computer Vision and
Pattern Recognition. 6489–6498.


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
