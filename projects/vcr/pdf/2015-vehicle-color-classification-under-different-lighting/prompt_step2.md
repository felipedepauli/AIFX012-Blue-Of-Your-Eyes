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

IEEE SENSORS JOURNAL, VOL. 15, NO. 2, FEBRUARY 2015
971
Vehicle Color Classiﬁcation Under Different
Lighting Conditions Through Color Correction
Jun-Wei Hsieh, Member, IEEE, Li-Chih Chen, Sin-Yu Chen, Duan-Yu Chen,
Salah Alghyaline, and Hui-Fen Chiang
Abstract—This paper presents a novel vehicle color classiﬁca-
tion technique for classifying vehicles into seven categories under
different lighting conditions via color correction. First, to reduce
lighting effects, a mapping function is built to minimize the color
distortions between frames. In addition to color distortions, the
effect of specular highlights can also make the window of a vehicle
appear white and degrade the accuracy of vehicle classiﬁcation.
To reduce this effect, a window-removal task is performed to
make vehicle pixels with the same color more concentrated on the
analyzed vehicle. Thus, a vehicle can be more accurately classiﬁed
into its corresponding category even when it is shone by strong
sunlight. One major problem in vehicle color classiﬁcation is that
there are many shade colors; for example, white versus silver and
black versus navy. Traditional methods lack the ability to classify
vehicles with shade colors because a wrong classiﬁer is designed
by putting vehicles with the same label together even though
their chromatic attributes are different. To treat this problem,
a novel tree-based classiﬁer is designed for classifying vehicles
into chromatic/nonchromatic classes with their nonchromatic
strengths and then into detailed color classes with their color
features. The separation can signiﬁcantly improve the accuracy
of vehicle color classiﬁcation even that vehicles are with various
shade colors and captured under different lighting conditions.
Index Terms—Vehicle color classiﬁcation, color correction,
SVM, vehicle window removal.
I. INTRODUCTION
V
IDEO
surveillance
in
public
spaces
has
attracted
immense attention in recent years because of its promis-
ing capabilities for crime prevention and security. For
example, in the VSAM (Video Surveillance And Monitoring)
project [1], a wide range of advanced surveillance techniques
were developed for real-time moving object detection, track-
ing, and counting, recognition of generic object classes, human
activity recognition, and so on. To overcome the limited
Manuscript received April 11, 2914; revised July 24, 2014; accepted August
26, 2014. Date of publication September 16, 2014; date of current version
November 26, 2014. This work was supported in part by the National Science
Council of Taiwan under Grant NSC-97-2221-E-155-060 and in part by the
Ministry of Economic Affairs under Contract 98-EC-17-A-02-s1-032 and
MOEA-102-E0616. The associate editor coordinating the review of this paper
and approving it for publication was Prof. Alexander Fish.
J.-W.
Hsieh,
S.
Alghyaline,
and
H.-F.
Chiang
are
with
the
Department
of
Computer
Science
and
Engineering,
National
Taiwan
Ocean
University,
Keelung
202,
Taiwan
(e-mail:
shieh@ntou.edu.tw;
salahshaman2007@gmail.com; chelly.chiang@gmail.com).
L.-C. Chen is with the Department of Electrical Engineering, Lee-Ming
Institute of Technology, Taipei 243, Taiwan (e-mail: lcchen@mail.lit.edu.tw).
S.-Y. Chen and D.-Y. Chen are with the Department of Electrical Engineer-
ing, Yuan Ze University, Zhongli 320, Taiwan (e-mail: polor1010@gmail.com;
dychen@saturn.yzu.edu.tw).
Color versions of one or more of the ﬁgures in this paper are available
online at http://ieeexplore.ieee.org.
Digital Object Identiﬁer 10.1109/JSEN.2014.2358079
ﬁeld of view of a camera,many cameras should be used for
monitoring a wide-area scene. However, because of differences
in lighting and camera distortions, the visual properties of
an object will differ signiﬁcantly for different cameras. Thus,
tracking and identifying a target moving across cameras is
very challenging [2]. It is especially important for police to
be able to conﬁdently track a vehicle or search escape cars
across different cameras.
To treat the problem, different space-time cues are used
to build feature correspondences and then obtain different
spatial relations between cameras for object tracking. For
example in [3], Chen et al. proposed a batch learning
algorithm for determining the topology of camera networks;
then, they
extracted
the appearance relationships using
brightness transfer functions to track targets among multiple
disjoint cameras. In [4], Pﬂugfelder and Micusik mapped
the tracking problem to a tree structure and then used a
branch-and-bound scheme to associate the trajectories of an
object and track its positions across cameras. In addition,
Lian, Lai, and Zheng [5] proposed an online correspondence
updating method for building spatial relations and then
tracking pedestrians across non-overlapping cameras. In [6],
Lian et al. integrated color intensity (CI) and a distance-based
local binary pattern (DLBP) to construct a novel CI_DLBP
descriptor for matching and tracking pedestrians across
disjoint camera views. In real-world applications, although
the color of an object changes across different cameras, if
a proper color transform can be found for correcting this
visual distortion, the color can be a very useful cue for object
identiﬁcation. In addition, when a crime or accident happens,
color is often the only feature to be remembered by the
witness and provided for the policemen to search escape cars.
Maintaining color constancy between cameras is another
important technique for solving the problem of match-
ing objects using their colors among different cameras.
Finlayson, Drew, and Funt [9] proposed a sensor transforma-
tion called spectral sharpening for constructing a set of
sensor-sensitive functions to maintain color constancy between
cameras. Buchsbaum [10] proposed a “Gray-World” model
for obtaining some invariant surface color descriptors by
using a scene-averaging technique. Weijer and Gevers [11]
modiﬁed this model and then proposed an edge-based
model, called “Gray-Edge”, for measuring the color con-
stancy between objects. Gehler et al. [12] used a Bayesian
approach to improve the Gray-World algorithm such that
the true reﬂectance of visible surfaces in an image can be
1530-437X © 2014 IEEE. Personal use is permitted, but republication/redistribution requires IEEE permission.
See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.


---

# Page 2

972
IEEE SENSORS JOURNAL, VOL. 15, NO. 2, FEBRUARY 2015
Fig. 1.
Overview of the proposed system for vehicle classiﬁcation. (a) Color
correction. (b) Vehicle classiﬁcation.
more accurately estimated. Xiang et al. [13] proposed a
model-based transformation between two images for reducing
the color distortions between two cameras. Matsushita [14]
constructed an illumination eigenspace for analyzing possible
lighting variations and eliminating unwanted shadow effects.
For object tracking, Madden, Cheng, and Piccardi [7] proposed
a histogram-stretching technique for minimizing the color
differences between two cameras such that the same object can
be well tracked across different cameras. This scheme works
well when the differences between object colors are large.
However, it will fail in vehicle color classiﬁcation because
there are many vehicles with shade colors. The colors of these
vehicles will often be over-stretched by this method.
There are many challenges in the task of vehicle color
classiﬁcation because there are various changes in lighting,
shadow, the time of vehicle capturing, and camera setting
such automatic white balance. Moreover, the vehicle colors are
not uniformly distributed and may not actually represent the
vehicle color. In addition, strong light reﬂections on a vehicle
often result in a fake “white” color. More importantly, there are
many shade (or confused) colors in vehicle color classiﬁcation
such as dark vs. dark navy, white vs. silver, dark vs. dark green,
and so on. In the literature, different methods [23]–[27] have
been proposed to tackle the above challenges. For example,
Brown [23] investigated several color features from different
color spaces to evaluate their effectiveness in vehicle color
classiﬁcation. Furthermore, Fang et al. [24] extracted features
from the HSI color space and then used back propagation
networks to classify vehicles. In [25], Wang et al. detected
the taillights of a vehicle and then extracted its color features
from the CIELab color space to classify vehicles via a KNN
classiﬁer. Yang et al. [26] extracted features from the HSV
and RGB spaces to classify colorful vehicles via a rule-based
classiﬁer. In [27], Baek et al. proposed a brute-force scheme
to divide the hue and saturation values of the HSV color space
into different bins from which a classiﬁer was trained for
vehicle color classiﬁcation. One problem in the above designed
classiﬁers is the lack of ability to deal with shade colors in
vehicle color classiﬁcation. The above methods tend to train
a classiﬁer wrongly by putting vehicles with the same label
together even though their chromatic attributes are different.
Then, mistakes often happen when vehicles are with less
chromatic colors, e.g., “dark navy” but need to be classiﬁed
to a chromatic color category, e.g., “blue”.
This paper presents a novel color-correction technique to
correct vehicles’ colors in real time and then classify each
Fig. 2.
A series of input frames was collected for background modeling and
vehicle extraction.
input vehicle into its corresponding color category. Fig. 1
shows the ﬂowchart of our proposed system. First, a novel
color-correction scheme for minimizing the color distortion
of input frames is proposed. Then, a novel vehicle classi-
ﬁcation scheme for classifying vehicles into different color
categories is proposed. Details of the two methods are shown
in Fig. 1(a) and (b). The color-correction technique (see (a))
builds a mapping function to minimize the color distortions
betweenframes. In real cases, strong light reﬂections on a
vehicle often result in a fake “white” color. Thus, after color
correction, at the stage of vehicle classiﬁcation (see (b)),
a window-removal method is applied to make vehicle pixels
with the same color more concentrated on the foreground
region. To well address the problem of vehicles with shade
colors, this paper proposes a new concept that vehicles with
different chromatic attributes should be separately trained even
though they belong to the same color category. It means
the vehicles with lower chromatic strengths should be ﬁrst
separated from the one with higher chromatic strengths. After
that, each group with different chromatic strengths is then
classiﬁed into detailed labels by its corresponding ﬁner clas-
siﬁer. Thus, a novel tree-based classiﬁer is used to solve
this confusion problem, i.e., vehicles with shade colors. The
proposed scheme can signiﬁcantly reduce the effects of color
distortion. Thus, even under different lighting conditions, each
vehicle can still be correctly classiﬁed into its color category.
The classiﬁcation result can be used for suspicious-vehicle
detection if a vehicle’s color is not the color associated with
its license plate number. In addition, when the camera spatial
relations are known in advance, a suspicious vehicle can
be forward- or backward-tracked using its color for secu-
rity maintenance and vehicle counting. Experimental results
demonstrate the feasibility and superiority of the proposed
approach in vehicle classiﬁcation under different cameras and
lighting conditions.
The remainder of the paper is organized as follows. In the
next section, the details of the color correction are described.
Then, Section III describes the details of the feature extraction
and vehicle classiﬁcation using SVMs. Section IV reports the
experimental results. Finally, some conclusions are presented
in Section V.
II. COLOR CORRECTION
The apparent color of a vehicle changes as a function of
time, space, and lighting conditions. Thus, in the material
that follows, a novel color correction scheme is proposed for
minimizing the effects of lighting changes.


---

# Page 3

HSIEH et al.: VEHICLE COLOR CLASSIFICATION UNDER DIFFERENT LIGHTING CONDITIONS
973
Fig. 3.
Result of foreground extraction. (a) Input frame. (b) Result of
background subtraction.
Fig. 4.
A vehicle is with different colors under various lighting conditions.
A. Foreground Vehicle Extraction
Before color correction, each foreground vehicle is extracted
from its background. In Fig. 2, a series of frames is collected
for constructing the background. Here, this paper uses the
codebook technique [15] to perform the background modeling
and subtraction tasks. The vehicle can be also detected from
single image without background subtraction by using our
previous work [29]. Fig. 3 shows the result of the background
subtraction. (b) is the result of the background subtraction
performed on (a). After several morphological operations and a
connected-component analysis, only the remaining foreground
region with the largest area is used for vehicle analysis.
B. Color Mapping and Correction
For a vehicle, its colors will appear different under different
lighting conditions and viewpoints. Fig. 4 shows an example
that the colors of a vehicle are different under various lighting
conditions. Before vehicle classiﬁcation, a novel color correc-
tion scheme is needed to correct for lighting changes.
Reinhard et al. [16] presented a simple but effective image
inpainting technique that transfers color characteristics from
a source Is to a target image It for color correction. Let μs
and μt be the means of Is and It, respectively. To reduce the
color difference between Is and It, these authors proposed a
mapping function g(p) for transferring the color of a pixel p
at It in the L AB color space to Is:
g(p) = μs + σs
σt
(It(p) −μt),
(1)
where σs and σt are the variances of Is and It, respectively.
Eq. (1) is aglobal color-mapping function because the color
statistics are calculated by using all pixels in the analyzed
image. When images contain different color regions, the
mapping function cannot distinguish different color statistics
among regions and will cause unnatural and saturated results.
To better correct images, Tai, Jia, and Tan [17] deﬁned several
local transfer functions and estimated their parameters via an
EM algorithm. The iterative updating process is quite time-
consuming and not suitable for real-time applications. In [18],
an optimal transfer function is constructed by integrating
different local transfer functions built from many models and
regions. Because many models are involved, this correction
method is also time-consuming. To ﬁt the real-time require-
ment, we reformulate this color correction method to improve
its efﬁciency and effectiveness.
After rewriting Eq.(1), we have
g(p) = σs
σt
It(p) + (μs −σs
σt
μt) = αIt(p) + β,
(2)
where α = σs
σt and β = μs −σs
σt μt. Thus, g(It) becomes a
linear model parameterized by α and β to approximate Is.
Then, we can obtain the parameters α and β by minimizing
the following energy function:
(α, β) = arg min
α,β

p
[Is(p) −αIt(p) −β]2.
(3)
By setting the ﬁrst derivatives of the right term of Eq.(3) (to
α and β) to zero, we obtain
 Is It −α  I 2
t −β  It = 0,
 Is −α  It −Nβ = 0,
(4)
where N is the size of Is. After solving Eq.(4), α and β are
obtained as follows:
α = Nμsμt − It Is
Nμ2t − I 2t
and
β = μt( It Is)−μs
 I 2
t
Nμ2t − I 2t
. (5)
Similar to Eq. (2), Eq. (5) is also a global color mapping
between It and Is and works based on the assumption that a
constant correction function exists between the two images.
However, in complex scenes, this assumption does not always
hold because of different scene content and image-capturing
devices. To solve this problem, we segment the source image
Is to several regions Rs
i using the algorithm proposed by
Felzenszwalb and Huttenlocher [19]. Then for each region Rs
i ,
its corresponding region Rt
i on It is obtained using one-to-one
pixel mapping. A one-to-one mapping means that a pixel in Rs
i
and its correspondence in Rt
i share the same coordinate. Thus,
Rs
i and Rt
i have the same size and their pixel correspondence
is one-to-one. Then, the local color mapping function gi from
Rt
i to Rs
i can be written as
gi(p) = αi It(p) + βi for all p ∈Rt
i .
(6)
Let μt
i and μs
i be the color means of Rt
i and Rs
i , respectively.
Similar to (5), the parameters αi and βi to parameterize gi can
be obtained as
αi =
|Ri|μs
i μt
i −
p∈Rt
i
It(p)Is(p)
|Ri|(μt
i)2 −
p∈Rt
i
I 2
t (p)
and
βi =
μt
i[ 
p∈Rt
i
Is(p)It(p)] −μs
i

p∈Rt
i
I 2
t (p)
|Ri|(μt
i)2 −
p∈Rt
i
I 2
t (p)
,
(7)
where |Ri| denote the size of Ri. By considering the con-
tribution of each color transfer function gi, a weighted color


---

# Page 4

974
IEEE SENSORS JOURNAL, VOL. 15, NO. 2, FEBRUARY 2015
Fig. 5.
Color Correction. (a) Reference image. (b) Image with color
distortions. (c) Pixels with black color showing the background part of (b).
Fig. 6.
Results of color correction. (a) Source image. (b) and (d): Input
frames. (c) and (e): Results of color correction from (b) and (d), respectively.
correction function G(p) can be formed. The importance of
gi for a pixel p is calculated according to the color distance
between p and the mean color μs
i of Rs
i . Let ||x −y|| denote
the Euclidean distance between two colors x and y. Then, the
importance of gi for p is deﬁned by
wi(p) = exp(−||gi(p) −μs
i ||2).
(8)
Assume there are NR segmented regions. Thus, there are NR
local mapping functions. In addition, let ¯wi(p) denote the
normalized version of wi(p),
¯wi(p) =
wi(p)
NR

i=1
wi(p)
.
Then, the weighted correction function G(p) is deﬁned as
G(p) =
Ng

i=1
¯wi(p)gi(p).
(9)
Using Eq. (9), we can map each input frame It to Is for
color correction. However, Eq. (9) works poorly for color
correction if It contains some foreground objects. Thus, before
color correction, all foreground objects must be removed.
In Fig. 5(c), the vehicle region is extracted and removed using
background subtraction. Only the pixels of the background
regions (which are colored black) in It are used for calculating
gi and then building G(p) for color correction.
In real cases, the background (denoted by Ib) must be
adaptively updated for foreground object detection because the
background changes with time. The source image Is is ﬁxed
during the period of color correction. Thus, Ib is not equal
to Is and is just used for background subtraction rather than
Fig. 7.
Vehicle windows with black color.
Fig. 8.
Vehicle window colors became white due to the effect of specular
highlights.
color correction. Fig. 6 shows the results of color correction.
(a) is the source image. (c) and (e) are the results of the color
correction performed on (b) and (d), respectively. After color
correction, the color characteristics of (c) and (e) are similar
to those of (a). For a vehicle moving across different cameras,
the proposed correction method will not correct its colors from
one camera to another camera. Because we just need to ensure
its color label to be correctly classiﬁed under the same camera,
the source image Is is differently chosen from each camera
but ﬁxed under the same camera.
III. VEHICLE CLASSIFICATION
After color correction, different classiﬁers are trained for
classifying vehicles into different categories. In Fig. 7, the
vehicle windows appear black. The black color will cause
the vehicles to be misclassiﬁed as “black”. However, the
effect of specular highlights also often makes a vehicle’s
windows appear a fake white color. In Fig. 8, this effect
makes the vehicle windows appear white and leads to the
misclassiﬁcation of the vehicles as “white”. To reduce this
effect, the vehicle windows must ﬁrst be removed. After their
removal, different vehicle classiﬁers can then be trained to
classify vehicles into different color categories.
A. Vehicle Window Removal
Let R denote the vehicle extracted using a background
subtraction technique. To remove the vehicle’s windows, the
orientation θR of its major axis must ﬁrst be detected. This
paper uses a moment-based approach to detect θR. First, the
central momentof R is deﬁned as
(μp,q)R =

(x,y)∈R
(x −¯x)p (y −¯y)q,
where (¯x, ¯y) = ( 1
|R|

(x,y)∈R x, 1
|R|

(x,y)∈R y) and |R| is the
area of R. Then, as shown in Fig. 9, the orientation θR of R
can be obtained using the equation
θR = arg min
θ

(x,y)∈R
[(x −¯x) sin θ −(y −¯y) cos θ]2. (10)


---

# Page 5

HSIEH et al.: VEHICLE COLOR CLASSIFICATION UNDER DIFFERENT LIGHTING CONDITIONS
975
Fig. 9.
The gravity center ( ¯x, ¯y)R and orientation θR of a vehicle R.
Fig. 10.
(a) Input vehicle. (b) Cutting line used for removing the vehicle
window.
Fig. 11.
Result of vehicle window removal.
Fig. 12.
Result of vehicle window removal from a minivan. (a) Input image.
(b) Result of window removal.
By setting the ﬁrst derivative of Eq.(10) to zero, the direction
θR can be estimated by
θR = 1
2 tan−1

2μ1,1
μ2,0 −μ0,2

.
(11)
If θR ranges from −π/4 to π/4, R is considered “horizontal”;
otherwise, its orientation is “vertical”. Actually, the hood
region of a vehicle will include most of color features. If the
orientation of R is “vertical”, its moving direction should
be also known for determining which part of R is the real
hood region. The moving direction can be easily obtained by
checking the center moving of R across two adjacent frames
via a simple tracking scheme.
Let Lcut denote the cutting line used to remove the windows
of R. If R is “horizontal”, Lcut is the line with the orientation
θR that passes through the center (¯x, ¯y). In Fig. 10, (a) is
the input vehicle and (b) shows the line Lcut that passes
through the center (¯x, ¯y). For each pixel p in R, if p is
below Lcut, p is added to the remaining vehicle ¯R; otherwise,
it is eliminated. Fig. 11 shows the result of vehicle window
removal performed on the image shown in Fig. 10. Fig. 12
shows the result of window removal for a minivan. If R is
“vertical”, Lcut is the line with orientation (θR + π/2) that
passes through the center (¯x, ¯y). Lcut separates R into an
upper part ‘’ and a lower part 0. Because R moves along a
road, its direction of movement can be determined using the
Algorithm 1 Algorithm for Vehicle Window Removal
Input: a vehicle R with a moving direction ⃗d.
Output: the remaining vehicle ¯R after window removal.
Step1: Estimate θR using Eq. (11). If θR ranges from −π/4 to π/4,
go to Step 2; otherwise, go to Step 3.
Step2:
2.1: Find Lcut with θR and the center (¯x, ¯y).
2.2: Add each pixel p in R to the set
¯R if the pixel is
below Lcut.
2.3: Return ¯R.
Step3:
3.1: Find Lcut with the orientation (θ+
R π/2) and the center (¯x, ¯y).
3.2: Separate R into an upper part  and a lower part .
3.3: If the direction ⃗d of movement of R is toward , ¯R = ;
else ¯R =.
3.4: Return ¯R
Fig. 13.
Result of vehicle window removal when the orientation is ‘vertical’.
(a) Input Frame. (b) Result of the proposed algorithm.
Fig. 14.
Seven color appearance categories of vehicle used for color
classiﬁcation.
difference in its position between the current frame and the
previous frame. If the direction of movement of R is toward
,  will be retained for further color classiﬁcation; otherwise,
0 is selected. In Fig. 13, (a) is the input vehicle with a
“vertical” orientation. Because the vehicle moves down, 0 is
retained as the remaining vehicle ¯R. (b) is the result of the
window removal. A tree-based classiﬁer will be trained later
for classifying ¯R into different categories. In Algorithm 1,
details of the window removal algorithm are described.
B. Gray Pixel Identiﬁcation
After window removal, the following stage is to classify
the remaining vehicle
¯R into different categories. In this
paper, seven color categories (“blue”, “green”, “red”, “yellow”,
“white”, “silver”, “black”)are collected for vehicle classiﬁca-
tion (shown in Fig. 14). In this set, there are many shade colors
to be easily misclassiﬁed. For example, a “navy” vehicle in the
“blue” category is often misclassiﬁed into “black”. Traditional
methods [23]–[27] lack the ability to deal with this problem,
i.e., vehicles with shade colors, because a wrong classiﬁer is
designed by putting vehicles with the same label together even
though their chromatic attributes are different. To well address


---

# Page 6

976
IEEE SENSORS JOURNAL, VOL. 15, NO. 2, FEBRUARY 2015
Fig. 15.
A tree structure for vehicle classiﬁcation.
Fig. 16.
Vehicles classiﬁed to “gray” and “color” classes. (a) Gray class.
(b) Color class.
the problem, this paper proposes a new concept that vehi-
cles with different chromatic attributes should be separately
trained. It means the vehicles with lower chromatic strengths,
e.g., “navy”, should be ﬁrst separated from the one with higher
chromatic strengths, e.g. “blue”. After the separation, elements
in a speciﬁc subgroup are then classiﬁed into detailed labels
by using its corresponding ﬁner classiﬁer. A novel tree-based
classiﬁer is then inspired and built to tackle this confusion
problem in color classiﬁcation.
Fig. 15 shows the structure of our proposed tree-based
vehicle classiﬁer. The classiﬁer splits the “blue” and “green”
categories into four categories, “blue”, “dark blue”, “green”,
and “dark green”. Then, at the root node, a G-classiﬁer
(G for “Gray”) is designed to classify vehicles accord-
ing to their non-chromatic strengths into the “gray” and
“color”subgroups. As shown in Fig. 16, the “gray” subgroup
contains the “black”, “silver”, “white”, “dark blue”, and “dark
green” categories, respectively. The “color” subgroup contains
the “red”, “green”, “blue”, and “yellow” categories, respec-
tively. For the child nodes in Fig. 15, the “DG-classiﬁer”
and “DC-classiﬁer” are then trained to classify elements
in the “gray” and “color”subgroups, respectively. Here, the
DG-classiﬁer and DC-classiﬁer denote the “detailed gray
classiﬁer” and “detailed color classiﬁer”, respectively. The
details of the G-classiﬁer will be described in Section III.C.
The frameworks of the DG-classiﬁer and DC-classiﬁer are
discussed in Section III.D.
C. Non-Chromatic Pixel Identiﬁcation
To deﬁne the G-classiﬁer, we ﬁrst normalize a pixel p as
follows:
IR =r/(r + g + b), IG =g/(r +g+b), and IB =b/(r +g+b),
where (r, g, b)t is the color vector of p. If (r, g, b)t is a gray
color, it should be very close to the gray axis, (1/3, 1/3, 1/3)t.
Fig. 17.
(a) Input vehicle. (b) Result of gray pixel detection.
Fig. 18.
Two classiﬁers were trained for classifying vehicles to different
color appearance categories. The DG-classiﬁer is used for detailing the “gray”
subgroup and the DC-classiﬁer is used for detailing the“color”subgroup.
Thus, the distance between p and the gray axis is deﬁned as
dp = (IR −0.333)2 + (IG −0.333)2 + (IB −0.333)2.
In addition, if p belongs to a gray pixel, its color channels
should all have values similar to its mean u p, where u p =
(r +g+b)/3. Then, the distance between p and u p is deﬁned
as follows:
dmean = (r −u p)2 + (g −u p)2 + (b −u p)2.
(12)
Let umean and ud denote the means of dmean and dp, respec-
tively (calculate from the chromatic vehicle class). Then, the
probability of a pixel p belonging to the gray class is deﬁned
as follows:
P(Gray|p) = exp(−(dmean −umean)2
σ 2mean
) exp(−(dp −ud)2
σ 2
d
),
(13)
where σ 2
mean and σ 2
d are the variances of dmean and dp, respec-
tively. The following rule is used for determining whether p
is a gray pixel:
P(Gray|p) > Tgray,
(14)
where Tgray is the threshold determined by averaging all
gray pixels of vehicles during the training stage. In Fig. 17,
(a) shows a vehicle image and (b) is the detection result for
the gray pixels (denoted by in red) performed using Eq. (14).
Given a vehicle ¯R, if the fraction of gray pixels in ¯R is greater
than 80%, ¯R is classiﬁed into the “gray” class; otherwise,
it belongs to the “color” class. Thus, the vehicle shown in
Fig. 17(a) is classiﬁed as “color.”
D. SVM-Based Vehicle Classiﬁers
In the previous section, a G-classiﬁer for classifying vehi-
cles into “gray” and “color” classes was proposed. This
section uses the SVM learning algorithm [21] to train the DG-
classiﬁer and DC-classiﬁer for classifying the above classes.
In Fig. 18, the DC-classiﬁer attempts to classify the “color”
vehicles into four categories, “red”, “green”, “blue”, and
“yellow”. To train this classiﬁer, thirty four features are


---

# Page 7

HSIEH et al.: VEHICLE COLOR CLASSIFICATION UNDER DIFFERENT LIGHTING CONDITIONS
977
Fig. 19.
Feature extraction from A-B color plane for vehicle classiﬁcation.
(a) Input frame. (b) Color mapping onto the A-B plane. (c) 28 dominant colors
extracted for color classiﬁcation.
extracted from both the LAB color space and the RGB color
space. Here, twenty-eight features are extracted from the LAB
domain and the remaining six features are extracted from the
RGB color space. Because the LAB space separates the color
components (A, B) of a pixel from its intensity component
L, we choose LAB space for vehicle analysis. The separation
can make the color components become more stable on an
object even if small lighting changes or shadows exist. Because
L channel is not related to color, only A and B channels
are adopted for color classiﬁcation. In Fig. 19, (a) is the
original frame and (b) is the result of projecting (a) on the
A-B plane. Clearly, different vehicle colors produce different
distributions on the A-B plane. Then, we use polar coordinates
to sample the A-B plane, where 10 units are used to quantize
the radius and the angular direction is quantized into sections
of width 90◦. The sampling rate is non-linear. In Fig. 19 (c),
each quadrant includes seven features. Twenty-eight grids are
extracted from the polar coordinate. Each grid corresponds
to a color bin. Then, we can construct a vector hLab =
(hLab(1), . . . , hLab(k),…, hLab(28)), in which hLab(k) is the
number of pixels in the kth bin, i.e.,
hLab(k) = #

q|q ∈bink
,
(15)
where bink is the kth bin of the polar coordinates.
In real cases, a vehicle color is usually a combination of
‘on’ or ‘off’ selections in the RGB channels. For example,
the ‘yellow’ color is a combination of ‘on’ ﬂags in the
RG channels and an ‘off’ ﬂag in the B channel. The ‘on’
or ‘off’ values for a vehicle color can be useful features for
vehicle color classiﬁcation. Thus, we use the distributions of
pixels whose color channels are larger than other channels
in the RGB space as the other six features. For example,
the 29th feature records the number of pixels for which
the value of the B channel is larger than the G channel.
Table 1 lists all six combinations of color comparisons. Each
combination corresponds to a different feature. Then, a vector
feature h RGB = (h RGB(1), . . . , h RGB(6)) is extracted from
the RGB color space. After integration, a feature vector hDC
with 34 dimensions is formed, h DC = (hLab, h RGB). Based
on this set of features, the DC-classiﬁer is trained using the
SVM training algorithm.
To train the DG-classiﬁer, we quantize each color channel
in the RGB space into eight levels. Because three color
channels are used, a vector hquan with twenty-four features
is extracted from this space. In addition, we record the
TABLE I
SIX COMBINATIONS OF COLOR COMPARISON. EACH COMBINATION
CORRESPONDS TO A NEW FEATURE
distributions of pixels whose color channels are larger than
other channels. Then, as for the DC-classiﬁer, a vector feature
h RGB is extracted. After integration, a feature vector h DG with
30 dimensions is formed, h DG = (hquan, h RGB). With h DG,
the DG-classiﬁer can also be trained using the SVM algorithm.
IV. EXPERIMENTAL RESULTS
To evaluate the performance of our proposed method,
an automatic system for vehicle classiﬁcation was imple-
mented. Seven vehicle appearance categories (blue”, “green”,
“red”, “yellow”, “white”, “silver”, and “black”) were used
for performance evaluation. To train the DG-classiﬁer and the
DC-classiﬁer, a database containing 3373 vehicles, in which
313 images are of white vehicles, 679 images are of black
vehicles, 801 images are of silver vehicles, 404 images are of
red vehicles, 465 images are of green vehicles, 263 images are
of blue vehicles, and 448 images are of yellow vehicles, was
used. Trucks are not included and tested in this paper because
different advertisement text or logos with various colors that
are painted on trucks can confuse the color classiﬁcation. For
training, the SVM library from [21] was used. The radial
basis function (RBF) was selected as the kernel function; the
gamma value used is 0.08125, and the parameter C of nu-SVC
is 12.0. In addition, another test database containing images of
16,648 vehicles, in which 3,243 images are of white vehicles,
2783 images are of black vehicles, 2234 images are of silver
vehicles, 1832 images are of red vehicles, 2303 images are
of green vehicles, 2523 images are of blue vehicles, and
1730 images are of yellow vehicles, was also used. This
vehicle database was collected by the VBIE (Vision-Based
Intelligent Environment) project [28] from different roads,
lighting (recording range from 6AM to 6PM), and weather
conditions (sunny, cloudy, and raining). Now, the dataset is
available from [30].
To theoretically analyze the performance of our proposed
color correction scheme, this paper uses the “Fisher crite-
rion” [22] to evaluate the separation ability of the vehicle
classiﬁcation method before and after color correction. The
criterion uses the ratio of the “between-class” variance to
the “within-class” variance to measure how well a transform
T can separate a space into two classes C1 and C2. The
“between-class” variance is the distance between the classes’
means (denoted by m1 and m2, respectively). The “within-
class” variance is the sum of the classes’ variances, s1 and s2.
Then, the Fisher criterion is deﬁned by
J(T) = between-class distance
within-class distance = |m1 −m2|2
s2
1 + s2
2
.
For a color transform T, a larger value of J corresponds
to a better separation ability. Table 2 lists the separation-


---

# Page 8

978
IEEE SENSORS JOURNAL, VOL. 15, NO. 2, FEBRUARY 2015
TABLE II
SEPARATION ABILITY ANALYSIS AMONG DIFFERENT COLOR
APPEARANCE CATEGORIES OF VEHICLE BEFORE
COLOR CORRECTION
TABLE III
SEPARATION ABILITY ANALYSIS AMONG DIFFERENT COLOR
APPEARANCE CATEGORIES OF VEHICLE
AFTER COLOR CORRECTION
ability analysis for the different vehicle color categories
when the classiﬁcation was performed before color correction.
Table 3 shows the same analysis except that the classiﬁcation
was performed after color correction. Clearly, after color cor-
rection, the value of J is larger; this result implies that vehicles
were classiﬁed more accurately after the color correction
was performed. For comparison, the major color spectrum
histogram representation (MCSHR) [7] was also implemented.
This method is similar to a histogram-stretching technique for
minimizing the color differences between two cameras. Fig. 20
shows a comparison of the results of color correction using our
method and using the MCSHR method. (b) and (c) are the
correction results for (a) using our method and the MCSHR
method, respectively. Clearly, the colors of this vehicle were
over-stretched by the MCSHR method. Fig. 21 shows another
comparison of the results of our method and the MCSHR
method. Table 4 gives the results of a separation-ability
analysis after color correction using the MCSHR scheme.
Comparison with Table 3 clearly demonstrates that our method
performs better than the MCSHR scheme, especially for the
categories “white” and “silver”.
In addition to the MCSHR method, the Reinhard’s method
was also compared in this paper. Here, Eq.(1) and the
aggregation of the estimated regression functions (see Eq.(9))
were integrated together for this comparison. From the com-
parison with Table 5, our method is more superior than
the Reinhard’s method. To examine the effect of image
segmentation, the mean-shift segmentation [20] method was
also adopted in this paper. Table 6 shows the separation
ability analysis using the mean-shift algorithm. Actually, the
segmentation problem is still ill-posed now. Thus, compared
Fig. 20.
Comparison results of color correction using our method and the
MCSHR scheme [7]. (a) Input frame. (b) Result of color correction using our
method. (c) Result of color correction using the MCSHR scheme.
Fig. 21.
Comparison results of color correction using our method and the
MCSHR scheme [7]. (a) Input frame. (b) Result of color correction using our
method. (c) Result of color correction using the MCSHR scheme.
TABLE IV
SEPARATION ABILITY ANALYSIS AMONG DIFFERENT COLOR
APPEARANCE CATEGORIES AFTER COLOR CORRECTION
USING THE MCSHR SCHEME [7]
TABLE V
SEPARATION ABILITY ANALYSIS AMONG DIFFERENT COLOR
APPEARANCE CATEGORIES AFTER COLOR CORRECTION
USING REINHARD’S METHOD (SEE EQ.(1))
Fig. 22.
Results of vehicle window removal. (a) and (c) Input vehicles.
(b) and (d) Results of window removal.
with Table 3, the mean-shift method performs better in some
cases but worse in other cases.
In addition to the separation-ability analysis, we also exam-
ine the effects of vehicle window removal. Fig. 22 shows the
results of vehicle window removal. (a) and (c) are the input


---

# Page 9

HSIEH et al.: VEHICLE COLOR CLASSIFICATION UNDER DIFFERENT LIGHTING CONDITIONS
979
TABLE VI
SEPARATION ABILITY ANALYSIS AMONG DIFFERENT COLOR
APPEARANCE CATEGORIES AFTER COLOR CORRECTION
USING MEAN-SHIFT SEGMENTATION METHOD [20]
TABLE VII
ACCURACY ANALYSIS OF VEHICLE CLASSIFICATION
BEFORE VEHICLE WINDOW REMOVAL
TABLE VIII
ACCURACY ANALYSIS OF VEHICLE CLASSIFICATION USING THE
GRAY-CLASSIFIER BEFORE WINDOW REMOVAL
TABLE IX
ACCURACY ANALYSIS OF VEHICLE CLASSIFICATION USING THE
GRAY-CLASSIFIER AFTER WINDOW REMOVAL
vehicles. (b) and (d) are the results of window removal for
(a) and (c), respectively. Table 7 shows an accuracy analysis
of the vehicle classiﬁcation before vehicle window removal
was performed. After vehicle window removal, the fraction
of vehicle pixels with the same color increases, which yields
signiﬁcant improvements in the vehicle classiﬁcation accuracy.
The following set of experiments was used to evaluate the
performance of the G-classiﬁer to classify vehicles as “gray”
or “color” before and after window removal. Table 8 shows the
accuracy analysis of the G-classiﬁer for classifying vehicles as
“gray” or “color” before window removal. The accuracy for
the “gray” category is 100% because the colors of vehicle
windows naturally belong to the “gray” class and thus do not
lead to errors. However, the third column of the table indicates
that there are many color vehicles misclassiﬁed as “gray” if
their vehicle windows were not removed. Table 9 shows the
Fig. 23.
Results of vehicle classiﬁcation using the DG-classiﬁer. (a) Input
vehicles. (b) Results of vehicle window removal. (c) Results of vehicle
classiﬁcation where the red color shows the detected gray pixels using
Eq. (14).
TABLE X
CONFUSION MATRIX OF VEHICLE CLASSIFICATION USING THE
DG-CLASSIFIER BEFORE VEHICLE WINDOW REMOVAL
TABLE XI
CONFUSION MATRIX OF VEHICLE CLASSIFICATION USING THE
DG-CLASSIFIER AFTER VEHICLE WINDOW REMOVAL
same analysis of the G-classiﬁer but after window removal was
performed. The third column indicates that the accuracy of
color classiﬁcation was signiﬁcantly improved by the window
removal (from 76.81% to 98.61%). However, the accuracy is
still lower for the color class than for the gray class because
some blue or green vehicles are similar to gray vehicles. The
average accuracy of the G-classiﬁer is 99.19%. Clearly, the
accuracy of the G-classiﬁer is sufﬁcient for achieving a highly
accurate vehicle classiﬁcation.
After analyzing the performance of the Gray-classiﬁer,
we evaluate the performance of the DG-classiﬁer and the
DC-classiﬁer. Fig. 23 shows classiﬁcation results of the
DG-classiﬁer. (b) shows the results of vehicle window removal
from (a). (c) shows the results of vehicle classiﬁcation of (b).
The red area denotes the gray pixels detected using Eq. (14).
Table 10 shows the confusion matrix of the DG-classiﬁer
before window removal.
Table 11 shows the same analysis but after window removal.
Some vehicles in the “silver” category are very similar to those
in the “white” category. Thus, they were misclassiﬁed into the
“white” category. In addition, the “navy” and “deep green”
vehicles were often misclassiﬁed into the “black” category.


---

# Page 10

980
IEEE SENSORS JOURNAL, VOL. 15, NO. 2, FEBRUARY 2015
Fig. 24.
Failure case of the DG-classiﬁer of a “silver” vehicle to be “white”.
Fig. 25.
Results of vehicle classiﬁcation using the DC-classiﬁer. (a) Input
vehicles. (b) Results of vehicle window removal. (c) Results of classiﬁcation
where the red color shows the detected gray pixels using Eq.(14).
TABLE XII
CONFUSION MATRIX OF VEHICLE CLASSIFICATION USING THE
DC-CLASSIFIER BEFORE VEHICLE WINDOW REMOVAL
TABLE XIII
CONFUSION MATRIX OF VEHICLE CLASSIFICATION USING THE
DC-CLASSIFIER AFTER VEHICLE WINDOW REMOVAL
Table 9 and Table 11 clearly indicate that window removal
can signiﬁcantly improve the accuracy of classiﬁcation. Fig. 24
shows a case in which our method failed to classify a silver
vehicle. The effect of specular highlights made the colors of
the vehicle windows and body appear white, which caused our
method to fail.
Fig. 25 shows the results of vehicle classiﬁcation using
the DC-classiﬁer. (b) shows the results of vehicle window
removal from (a). In (c), the gray pixels (denoted in red)
were ﬁrst detected using Eq. (14). Then, all the non-gray
pixels were retained for vehicle classiﬁcation using the
DC-classiﬁer. The top captions in (c) show the results of
the vehicle classiﬁcation. Table 12 shows the confusion
matrix of the DC-classiﬁer before window removal. Table 13
shows the same analysis but after window removal. In real
cases, the “red” and “yellow” categories are more eas-
ily classiﬁed because they are more vivid than the blue
Fig. 26.
Results of vehicle classiﬁcation when the road included multiple
vehicles. (a) Two vehicles. (b) Four vehicles.
Fig. 27.
Some false recognition results. (a) False recognition of a blue
vehicle. (b) False recognition of a green vehicle.
Fig. 28. Some false recognition results from front views. (a) False recognition
of a silver vehicle to be “white”. (b) False recognition of a blue vehicle to be
“dark green”.
TABLE XIV
CONFUSION MATRIX OF VEHICLE CLASSIFICATION BEFORE
COLOR CORRECTION (%)
and green colors. When the lighting conditions are poor,
the blue and green colors appear very similar to “black”.
Thus, higher accuracies were obtained for the “red” and
“yellow” categories. Fig. 26 shows the results of vehicle
classiﬁcation performed on an image of a real road that
includes multiple vehicles. Fig. 27 shows two cases in which
the DC-classiﬁer failed. Fig. 28 shows another set of fail-
ure cases caused by shade colors. The effects of specular
highlights caused these vehicles to be misclassiﬁed as a fake
label.
In addition to analyzing the effects of window removal, we
also evaluate the accuracy improvement of vehicle classiﬁca-
tion yielded by performing color correction. Table 14 gives
the confusion matrix of vehicle classiﬁcation before color
correction. The average accuracy of the vehicle classiﬁcation
is approximately 86.58%. Table 15 shows the same accuracy
analysis but after color correction without region segmenta-


---

# Page 11

HSIEH et al.: VEHICLE COLOR CLASSIFICATION UNDER DIFFERENT LIGHTING CONDITIONS
981
TABLE XV
CONFUSION MATRIX OF VEHICLE CLASSIFICATION AFTER COLOR
CORRECTION WITHOUT REGION SEGMENTATION
TABLE XVI
CONFUSION MATRIX OF VEHICLE CLASSIFICATION AFTER COLOR
CORRECTION WITH REGION SEGMENTATION
TABLE XVII
CONFUSION MATRIX OF VEHICLE CLASSIFICATION WHEN VEHICLES
WERE CAPTURED FROM HIGHWAYS
tion was performed. The average accuracy is approximately
92.59%. Table 16 shows the analysis after color correction
with region segmentation was performed (see Eq.(9)). Clearly,
color correction can enhance the color differences between the
“silver” category and other categories.
To further examine the robustness of our system, we also
tested our method for various roads and weather conditions.
Table 17 gives the confusion matrix of vehicle classiﬁcation on
highways. The average accuracy is 92.62%. The most difﬁcult
classiﬁcation case is “silver” because it is very similar to
“white”. Table 18 shows an analysis of vehicle classiﬁcation
for vehicles in different parking spaces. The average accuracy
is 91.56%. The numbers of vehicles tested in the highway
dataset and the parking space dataset are 9,632, and 7,016,
respectively. The two tables indicate that better results were
achieved for the “red” and “yellow” categories because of
their vivid colors. Weather is another important factor that
affects the accuracy of vehicle classiﬁcation. Table 19 shows
the confusion matrix of vehicle classiﬁcation for cloudy days.
The average accuracy is 94.07%. Clearly, on a cloudy day,
better performance is obtained because the sunlight is weaker.
TABLE XVIII
CONFUSION MATRIX OF VEHICLE CLASSIFICATION WHEN VEHICLES
WERE CAPTURED FROM PARKING SPACES
TABLE XIX
CONFUSION MATRIX OF VEHICLE CLASSIFICATION WHEN VEHICLES
WERE CAPTURED UNDER CLOUDY DAYS
TABLE XX
CONFUSION MATRIX OF VEHICLE CLASSIFICATION WHEN A
SECTOR-SAMPLING TECHNIQUE WAS ADOPTED
In Section III.C, the polar coordinate (see Fig. 19(c))
is adopted for sampling some important color bins for
vehicle classiﬁcation. Table 20 shows an accuracy analysis of
vehicle classiﬁcation using a sector-type sampling on the polar
coordinates (see Fig. 19(b)). The average accuracy is 93.18%.
Table 16 shows another confusion matrix of vehicle classi-
ﬁcation when the rectangular sampling shown in Fig. 19(c)
was adopted. The average accuracy is 93.59%. Clearly, the
proposed rectangle-type sampling technique is superior to the
uniform sample scheme. Another advantage of this sampling
technique is an improvement in efﬁciency because sampling
on the A-B color space using rectangular blocks is easier than
sampling using sectors.
For comparison, four methods [24]–[27] for vehicle classi-
ﬁcation were implemented. In [24], the back propagation net-
work was adopted to classify vehicles via container separation
from the HSI color space. Its performances strongly depend
on a proper selection of thresholds used in “container” clas-
siﬁcation. In [25], the success of color classiﬁcation majorly
depends on the detections of vehicle taillights. Their method
is instable to separate the category “dark blue” from “dark


---

# Page 12

982
IEEE SENSORS JOURNAL, VOL. 15, NO. 2, FEBRUARY 2015
TABLE XXI
ACCURACY COMPARISONS AMONG FOUR METHODS [24]–[27]
green”. As to [26], a rule-based classiﬁer was proposed to
classify colorful vehicles into different category based on the
RGB and HSV color space. The used rule-based classier is
easily degraded by the effects of sunlight because the lighting
conditions are out of the deﬁned rules. In [27], a brute-force
scheme was proposed to divide the hue and saturation values
of the HSV color space into 360 elements for training a vehicle
classiﬁer. This method is not stable when the lighting has
changes. Because the vehicle window is remained, its accuracy
is also degraded by the effects of sunlight. Table 21 presents
the accuracy comparisons among our proposed method and
other methods [24]–[27]. The average accuracy of our method
is 93.59%. Clearly, our vehicle classiﬁcation method performs
much better than other methods. Experimental results have
demonstrated the superiority of our method for vehicle classi-
ﬁcation.
V. CONCLUSION
We have proposed a novel method for classifying vehicles
to different color categories. The contributions of this method
are summarized as follows:
1) A novel color correction scheme was proposed for
reducing the effect of lighting change.
2) A novel window-removal scheme was proposed for
removing the effect of sun lighting.
3) A novel tree-based classiﬁer was designed for classify-
ing vehicles into different categories even from different
cameras and under different lighting conditions.
4) A rectangular block sampling technique was proposed
for sampling important features from the A-B color space
for vehicle representation.
The average accuracy of vehicle classiﬁcation with our method
was 9359%. The experimental results demonstrate that the
proposed method is superior to other vehicle classiﬁcation
methods in terms of accuracy, robustness, and stability.
REFERENCES
[1] R. T. Collins et al., “A system for video surveillance and monitor-
ing,” Robotics Institute, Carnegie Mellon Univ., Pittsburgh, PA, USA,
Tech. Rep. CMU-RI-TR-00–12, May 2000.
[2] A. Yilmaz, O. Javed, and M. Shah, “Object tracking: A survey,” ACM
Comput. Surv., vol. 38, no. 4, pp. 1–45, 2006, Art. ID 13.
[3] K.-W. Chen, C.-C. Lai, P.-J. Lee, C.-S. Chen, and Y.-P. Hung, “Adaptive
learning for target tracking and true linking discovering across multiple
non-overlapping cameras,” IEEE Trans. Multimedia, vol. 13, no. 4,
pp. 625–638, Aug. 2011.
[4] C. Picus, R. Pﬂugfelder, and B. Micusik, “Branch and bound global
optima search for tracking a single object in a network of non-
overlapping cameras,” in Proc. IEEE Int. Conf. Comput. Vis. Workshops,
Nov. 2011, pp. 1825–1830.
[5] G. Lian, J. Lai, and W. Zheng, “Spatial-temporal consistent labeling
of tracked pedestrians across non-overlapping camera views,” Pattern
Recognit., vol. 44, no. 5, pp. 1121–1136, May 2011.
[6] G. Lian, J.-H. Lai, C. Y. Suen, and P. Chen, “Matching of tracked
pedestrians across disjoint camera views using CI-DLBP,” IEEE Trans.
Circuits Syst. Video Technol., vol. 22, no. 7, pp. 1087–1099, Jul. 2012.
[7] C. Madden, E. D. Cheng, and M. Piccardi, “Tracking people across
disjoint camera views by an illumination-tolerant appearance represen-
tation,” Mach. Vis. Appl., vol. 18, nos. 3–4, pp. 233–247, May 2007.
[8] D. Makris, T. Ellis, and J. Black, “Bridging the gaps between cameras,”
in Proc. IEEE Comput. Soc. Conf. Comput. Vis. Pattern Recognit., vol. 2,
Jun./Jul. 2004, pp. II-205–II-210.
[9] G. D. Finlayson, M. S. Drew, and B. V. Funt, “Spectral sharpening:
Sensor transformations for improved color constancy,” J. Opt. Soc.
Amer. A, vol. 11, no. 5, pp. 1553–1563, May 1994.
[10] G. Buchsbaum, “A spatial processor model for object colour perception,”
J. Franklin Inst., vol. 310, no. 1, pp. 1–26, 1980.
[11] J. van de Weijer and T. Gevers, “Color constancy based on the grey-edge
hypothesis,” in Proc. IEEE Int. Conf. Image Process., vol. 2, Sep. 2005,
pp. II-722–II-725.
[12] P. V. Gehler, C. Rother, A. Blake, T. Minka, and T. Sharp, “Bayesian
color constancy revisited,” in Proc. IEEE Conf. Comput. Vis. Pattern
Recognit., Jun. 2008, pp. 1–8.
[13] Y. Xiang, B. Zou, and H. Li, “Selective color transfer with multi-source
images,” Pattern Recognit. Lett., vol. 30, no. 7, pp. 682–689, May 2009.
[14] Y. Matsushita, K. Nishino, K. Ikeuchi, and M. Sakaushi, “Illumi-
nation normalization with time-dependent intrinsic images for video
surveillance,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 26, no. 10,
pp. 1336–1347, Oct. 2004.
[15] K. Kim, T. H. Chalidabhongse, D. Harwood, and L. Davis, “Real-
time foreground–background segmentation using codebook model,”
Real-Time Imag., vol. 11, no. 3, pp. 172–185, 2005.
[16] E. Reinhard, M. Ashikhmin, B. Gooch, and P. Shirley, “Color transfer
between images,” IEEE Comput. Graph. Appl., vol. 21, no. 5, pp. 34–41,
Sep./Oct. 2001.
[17] Y.-W. Tai, J. Jia, and C.-K. Tang, “Local color transfer via probabilistic
segmentation by expectation-maximization,” in Proc. IEEE Comput. Soc.
Conf. Comput. Vis. Pattern Recognit., vol. 1, Jun. 2005, pp. 747–754.
[18] M. Oliveira, A. D. Sappa, and V. Santos, “Unsupervised local color
correction for coarsely registered images,” in Proc. IEEE Conf. Comput.
Vis. Pattern Recognit., Jun. 2011, pp. 201–208.
[19] P. F. Felzenszwalb and D. P. Huttenlocher, “Image segmentation using
local variation,” in Proc. IEEE Comput. Soc. Conf. Comput. Vis. Pattern
Recognit., Jun. 1998, pp. 98–104.
[20] D. Comaniciu and P. Meer, “Mean shift: A robust approach toward
feature space analysis,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 24,
no. 5, pp. 603–619, May 2002.
[21] C.-C. Chang and C.-J. Lin. (2001). LIBSVM: A Library for Support
Vector Machines. [Online]. Available: http://www.csie.ntu.edu.tw/∼cjlin/
libsvm
[22] R. O. Duda, P. E. Hart, and D. G. Stork, Pattern Classiﬁcation.
New York, NY, USA: Wiley, 2001.
[23] L. M. Brown, “Example-based color vehicle retrieval for surveillance,”
in Proc. 7th IEEE Int. Conf. Adv. Video Signal Based Surveill.,
Aug./Sep. 2010, pp. 91–96.
[24] J. Fang, H. Yue, X. Li, J. Wu, and Z. Cui, “Color identifying of vehicles
based on color container and BP network,” in Proc. Int. Conf. Bus.
Manage. Electron. Inf., May 2011, pp. 226–229.
[25] Y.-C. Wang, C.-T. Hsieh, C.-C. Han, and K.-C. Fan, “The color
identiﬁcation of automobiles for video surveillance,” in Proc. IEEE Int.
Carnahan Conf. Secur. Technol. (ICCST), Oct. 2011, pp. 1–5.
[26] M. Yang, G. Han, X. Li, X. Zhu, and L. Li, “Vehicle color recognition
using monocular camera,” in Proc. Int. Conf. Wireless Commun. Signal
Process., Nov. 2011, pp. 1–5.
[27] N. Baek, S.-M. Park, K.-J. Kim, and S.-B. Park, “Vehicle color clas-
siﬁcation based on the support vector machine method,” in Advanced
Intelligent Computing Theories and Applications. With Aspects of
Contemporary
Intelligent
Computing
Techniques
(Communications
in Computer and Information Science), vol. 2, Berlin, Germany:
Springer-Verlag, 2007, pp. 1133–1139.
[28] VBIE Web, [Online]. Available: http://vbie.eic.nctu.edu.tw/en/introduction,
accessed Aug. 2008.
[29] J.-W. Hsieh, L.-C. Chen, and D.-Y. Chen, “Symmetrical SURF and
its applications to vehicle detection and vehicle make and model
recognition,”
IEEE Trans. Intell.
Transp.
Syst.,
vol. 15,
no. 1,
pp. 6–20, Feb. 2014.
[30] NTOU
Vehicle
Dataset,
[Online].
Available:
http://
mmplab.cs.ntou.edu.tw/MMR/, accessed Sep. 2013.


---

# Page 13

HSIEH et al.: VEHICLE COLOR CLASSIFICATION UNDER DIFFERENT LIGHTING CONDITIONS
983
Jun-Wei Hsieh (M’06) received the bachelor’s
degree in computer science from Tunghai University,
Taichung, Taiwan, in 1990, and the Ph.D. degree
in computer engineering from National Central Uni-
versity, Zhongli, Taiwan, in 1995. He was a recip-
ient of the Phai-Tao-Phai Award. From 1996 to
2000, he was a Research Fellow with the Industrial
Technology Researcher Institute, Hsinchu, Taiwan,
where he managed a team to develop video-related
technologies. He was an Assistant Professor with
the Department of Electrical Engineering, Yuan Ze
University, Zhongli, Taiwan, from 2001 to 2003, and an Associate Professor
from 2004 to 2009. He was the Chairman and is currently a Professor with the
Department of Computer Science and Engineering, National Taiwan Ocean
University, Keelung, Taiwan. He received the Best Paper Awards from the
Image Processing and Pattern Recognition Society of Taiwan in 2005, 2006,
and 2007, respectively. He was a recipient of the Best Patent Award from
the Industrial Technology Researcher Institute of Taiwan in 2009, and the
best paper awards from IIHMSP 2010, DMS2011, ITOAI 2013, ITOAI 2014,
and CVGIP 2014, respectively. His research interests include content-based
multimedia databases, video surveillance, intelligent transportation system,
computer vision, and pattern recognition.
Li-Chih Chen received the B.S. degree in infor-
mation science from Chinese Culture University,
Taipei, Taiwan, in 1992, and the M.S. degree in
information system from Lawrence Technological
University, Southﬁeld, MI, USA, in 1999. He is
currently pursuing the Ph.D. degree at the Depart-
ment of Electrical Engineering, Yuan Ze University,
Zhongli, Taiwan. He is currently a Lecturer with
the Department of Electrical Engineering, Lee-Ming
Institute of Technology, Taipei.
Sin-Yu Chen was born in Taipei, Taiwan, in 1982.
He received the B.S. and Ph.D. degrees in electri-
cal engineering from Yuan Ze University, Zhongli,
Taiwan, in 2005 and 2011, respectively. His research
interests include image processing, behavior analy-
sis, and video surveillance.
Duan-Yu Chen received the B.S. degree in com-
puter science and information engineering from
National Chaio Tung University, Hsinchu, Taiwan,
in 1996, the M.S. degree in computer science
from National Sun Yat-sen University, Kaohsiung,
Taiwan, in 1998, and the Ph.D. degree in computer
science and information engineering from National
Chiao Tung University in 2004. He was a Post-
Doctoral Research Fellow with Academia Sinica,
Taipei, from 2004 to 2008. He is currently an Asso-
ciate Professor with the Department of Electrical
Engineering, Yuan Ze University, Zhongli, Taiwan. His research interests
include computer vision, video signal processing, content-based video index-
ing and retrieval, and multimedia information system. He was a recipient of
the Young Scholar Research Award from Yuan Ze University in 2012.
Salah Alghyaline received the B.S. degree in com-
puter science from Mutah University, Karak, Jordan,
in 2005, the M.S. degree in computer information
systems from the Arab Academy for Banking and
Financial Sciences University, Amman, Jordan, in
2007. He is currently pursuing the Ph.D. degree at
the Department of Computer Science and Engineer-
ing, National Taiwan Ocean University, Keelung,
Taiwan.
Hui-Fen Chiang received the B.S. degree in com-
puter science and information engineering from
Feng Chia University, Taichung, Taiwan, in 1992,
and the M.S. degree in computer science and infor-
mation engineering from National Central Univer-
sity, Taoyuan, Taiwan, in 1995. She is currently
pursuing the Ph.D. degree at National Taiwan Ocean
University, Keelung, Taiwan. She is currently a
Lecturer with the Department of Digital Multimedia
Design, Taipei Chengshih University of Science and
Technology, Taipei, Taiwan.


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
