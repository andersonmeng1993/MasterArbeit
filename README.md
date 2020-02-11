## Masterarbeit/Master Thesis:
In this Git-Repo I will introduce my master thesis, such as the idea and the motivation of my topic. Also
I will upload the code example in the file but without source data. Some pictures would be also added to give 
the reader a better view.

### Thema: Aufbau eines Vorhersagemodells für die Lotpastendruckqualität in der SMT-Fertigungslinie zwischen Pastendrucker und Lotpasteninsepektionssystem unter Einsatz Machine Learning
<h4>Time Period:</h4> 2019 March - 2020. January. 07
<h4>Thesis Language:</h4> germany
<h4>Author:</h4> me
<h4>Major:</h4> M.Sc. Mechanical Engineering
<h4>Necessary knowledges:</h4> Machine learning. Python + Jupyter Notebook, DoE(Design of Experiment), basic knowledge about PCB and solder paste (SMT = Surface Mounted Technology)
<h4>ECTS:</h4> 30 
<h4>Aufgabenstellung:</h4>  
Künstliche Intelligenz als Werkzeug um die Produktivität und Qualität in der Massenfertigung von Produkten zu optimieren, gewinnt durch die Möglichkeit auch multidimensionale Daten zu verarbeiten zunehmend an Bedeutung in Industrie und Forschung. Insbesondere im Bereich der SMT-Elekronikfertigung fallen tagtäglich gigantische Datenmengen an, welche zur Optimierung der Fertigungsprozesse genutzt
werden können.
Ziel dieser Arbeit ist es, den Lotpastendruckprozess am Anfang der SMT-Linie zu
optimieren und Qualitätsvorhersagen zu treffen basierend auf Analysedaten eines
nachgeschalteten Lotpasteninspektionssystems. Zur Auswertung und Analyse der
Daten kommen statistische Modelle und maschinelle Lernverfahren zum Einsatz. 


*Die Arbeit beinhaltet folgende Schwerpunkte:*

- Grundlagen für die Arbeit
  - Recherche und Grundlagen des Pastendrucks in der SMT-Fertigung
  - Grundlagen Datenauswertung mittels ML
- Experimentelle Untersuchung
  - Bedrucken von unterschiedlichen Leiterplatten
  - Aufnahme der bedruckten Leiterplatten im SPI
- Auswertung mittels Maschinellen Lernverfahren
  - Evaluation geeigneter ML Verfahren für das Problem
  - Aufbau der Modelle und Vergleich der geeigneten Verfahren hinsichtlich Eignung
  
*in a word, our topic wants to use ML and the big data from product line to train a ML prediction model, to predict the transfer efficiency of the solder paste*


*Supervior, Department and University:*
- University [FAU](https://www.fau.de/)(Friedrich-Alexander-Universität Erlangen-Nürnberg)
- [Lehrstuhl FAPS](https://www.faps.fau.de/) (Fertigungsautomatisierung und Produktionssystematik)
- Prof. Dr.-Ing Jörg Franke
- M.Sc. Felix Häußler

*Backup for literatur:*
- Google Scholar
- Sci-hub
- Mendeley to implement the all literatures into Word

:clock730:*Time line for the Masterarbeit:* 
1. December 2018, January and February 2019 I began to learn and followed [the tutorial Machine Learning](https://www.coursera.org/learn/machine-learning) on Coursera, and some other tutorial about Python and Data Science, using Pandas to deal with the Dataframe.
2. At end of February I got the topic and got the data begann in March. Between March and April I did some simple machine learning model, such as linear & non-linear regression, and also SVM and NN model using library [Scikit-learn](https://scikit-learn.org/stable/index.html). Did a lot of coding and learned also so many examples, which teaches me how to train a ML model
3. May and Juni the Solder Paste Printer could not work. During these two months just like a stop time, not too much output. But just try to configure the machine and learn to build a NN Model using [tensorflow](https://www.tensorflow.org/)
4. in August and end Juli there were generated nearly 1 million data depending on 2 different PCB, in September was mainly focusing on training NN model using Tensorflow, and end of September depending on a third PCB generated 1 millione data and asigned to be the testset data to test the acurracy of NN model.
5. September to December I worked in Daimler AG as an intern, I work at night for the thesis. But finally we found the Tensorflow NN model can not predict the value, it just outputs the same valus whatever are the inputs. So I just divided the output into different classes so that I built a SVM classification model, which is besser as NN, at least it could output something.
6. At 03.Junary.2020 I printed out the Masterarbeit and copied the data into CD and send them to my supervisor Felix, that time I was in Stuttgart. 
