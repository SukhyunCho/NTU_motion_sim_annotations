# NTU RGB+D motion similarity annotations
A motion similarity dataset with real-world videos to evaluate motion similarity.

The dataset using for model evaluation in our paper [A Body Part Embedding Model With Datasets for Measuring Human Motion Similarity in 2D](https://github.com/dade-ai/bpe-dev), ECCV 2020.

## Description
It was generated using [the NTU RGB+D 120 dataset](http://rose1.ntu.edu.sg/datasets/actionrecognition.asp).
We use RGB videos and 3D skeletal data of the dataset.
While RGB videos, annotated through AMT by humans, was used to obtain ground truth the motion similarity.

We have refined the dataset and adopted only a portion of the entire dataset.
Especially, we removed the samples without skeletal annotations and then chose 21 actions with large and precise movements.
The video pairs are composed of a sampling of two videos of 39 people per action.
Consequently, the total videos are 1638 videos (21 actions X 39 people X 2 videos). 
Since all pairs can be used for similarity measurements, the candidate pair is 1,340,703 pairs (=1638 combination 2).


## AMT collection
We have obtained motion similarity scores measured by humans with AMT.
One set consists of 1 query video and 10 candidate videos, forming 10 pairs.
One task consists of 21 sets, thus, 210 sample pairs per task.
We have created a total of 100 tasks and performed a survey based on the task to get the human to evaluate motion similarity.
At this moment, we have collected data for 20093 pairs. 
The similarity score for each pair is the average of scores collected from at least ten workers.

### Score
The motion similarity is scored on a 4-point scale for one pair.

|Score  |Description                |
|------:|:-------------------------:|
|1      |utterly different motions  |
|2      |little similar             |
|3      |much similar               |
|4      |same movements             |

### Collection page
<p align="center">
  <img src="./figures/fig_instruction.jpg", width=800>
</p>


## Data

### Histogram
<p align="center", width=10>
  <img src="./figures/fig_histogram.jpg", width=500>
</p>

### Similarity score per actions
<p align="center">
  <img src="./figures/fig_annotation_actions.jpg", width=700>
</p>

## Data cleansing
<p align="center">
  <img src="./figures/fig_cleansing.jpg">
</p>

## Csv file example
|num	|sample1			    |sample2			    |AMT_score  |
|------:|:---------------------:|:---------------------:|:-------------:|
|1	    |S004C002P020R002A007	|S011C003P038R001A022	|1.4            |
|2	    |S007C001P015R002A027	|S024C001P064R001A099	|1.222          |
|3	    |S027C001P080R002A096	|S005C002P016R002A022	|1              |
|…	    |…				        |…				        |…              |
|20091	|S008C003P032R001A026	|S010C002P013R002A009	|1              |
|20092	|S027C001P084R002A100	|S003C001P002R001A027	|1.18           |
|20093	|S001C001P008R001A048	|S011C003P038R001A048	|3.27           |

## Contacts
Sukhyun Cho (chosh90@snu.ac.kr)

## Acknowledgments
- This work was supported by Kakao and Kakao Brain corporations.

- Portions of the research used [the NTU RGB+D 120 Action Recognition Dataset](http://rose1.ntu.edu.sg/datasets/actionrecognition.asp) made available by the ROSE Lab at the Nanyang Technological University, Singapore