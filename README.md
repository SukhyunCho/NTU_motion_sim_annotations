# NTU RGB+D motion similarity annotations
A motion similarity dataset with real-world videos to evaluate motion similarity.

## Data
21394 pairs

## Details
|start  |end    |bins       |
|-------|:-----:|:---------:|
|1.0 	|1.1    |1814 (max) |
|1.1 	|1.2 	|1797       |
|1.2 	|1.3 	|1688       |
|1.3 	|1.4 	|1418       |
|1.4 	|1.5 	|1171       |
|1.5 	|1.6 	|972        |
|1.6 	|1.7 	|801        |
|1.7 	|1.8 	|645        |
|1.8 	|1.9 	|514        |
|1.9 	|2.0 	|342        |
|2.0 	|2.1 	|419        |
|2.1 	|2.2 	|303        |
|2.2 	|2.3 	|269        |
|2.3 	|2.4 	|255        |
|2.4 	|2.5 	|255        |
|2.5 	|2.6 	|237 (min)  |
|2.6 	|2.7 	|247        |
|2.7 	|2.8 	|259        |
|2.8	|2.9 	|246        |
|2.9	|3.0 	|243        |
|3.0	|3.1 	|423        |
|3.1 	|3.2 	|413        |
|3.2 	|3.3 	|483        |
|3.3 	|3.4 	|560        |
|3.4 	|3.5 	|636        |
|3.5	|3.6 	|799        |
|3.6 	|3.7 	|935        |
|3.7 	|3.8 	|956        |
|3.8 	|3.9 	|963        |
|3.9 	|4.0 	|1331       |


## csv file

|num	|query_name			    |cand_name			    |AMT_avg_score  |
|-------|:---------------------:|:---------------------:|:-------------:|
|1	    |S029C001P051R001A102	|S022C001P066R002A095	|1.1            |
|2	    |S004C002P020R002A007	|S011C003P038R001A022	|1.4            |
|3	    |S007C001P015R002A027	|S024C001P064R001A099	|1.2            |
|…	    |…				        |…				        |…              |
|21392	|S008C003P032R001A026	|S010C002P013R002A009	|1              |
|21393	|S027C001P084R002A100	|S003C001P002R001A027	|1.18           |
|21394	|S001C001P008R001A048	|S011C003P038R001A048	|3.27           |

## Discription
It was generated using [the NTU RGB+D 120 dataset](http://rose1.ntu.edu.sg/datasets/actionrecognition.asp).
We use RGB videos and 3D skeletal data of the dataset.
While RGB videos, annotated through AMT by humans, was used to obtain ground truth the motion similarity.

We have refined the dataset and adopted only a portion of the entire dataset.
Especially, we removed the samples without skeletal annotations and then chose 21 actions with large and precise movements.
The video pairs are composed of a sampling of two videos of 39 people per action.
Consequently, the total videos are 1638 videos (21 actions X 39 people X 2 videos). 
Since all pairs can be used for similarity measurements, the candidate pair is 1,340,703 pairs (=1638 combination 2). -> 총 후보 pairs 1,340,703개

We have obtained motion similarity scores measured by humans with AMT.
One set consists of 1 query video and 10 candidate videos, forming 10 pairs.
One task consists of 21 sets, thus, 210 sample pairs per task.
We have created a total of 110 tasks and performed a survey based on the task to get the human to evaluate motion similarity.
The motion similarity is scored on a 4-point scale for one pair, where 1 represents utterly different motions, 2 - little similar, 3 - much similar, and 4 - same movements.
At this moment, we have collected data for 21394 pairs. 
The similarity score for each pair is the average of scores collected from at least ten workers. 
