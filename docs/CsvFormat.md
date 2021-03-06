# File Naming:

The Files Should be Named in this Order:

```
Data-(Branch)-(Batch)-(Scheme)-(Semester)[-Reval].csv
```

An Example:

For the Batch That has the SerialNumber 1CR16XX001 (Some Number), Attempting their 6th Semester, The filename Must be:

Ensure that this is followed or the application will fail to parse properly.

```
Data-CS-2016-2015-6.csv
```

If Reval Results for the above then:

```
Data-CS-2016-2015-6-Reval.csv
```

Any File not in this format will be **_ignored_**.



# CSV Format

All of the lines in the CSV file follow the current DataScheme:

```
USN, Name, Attempted Subjects, [SubCode, Subname,Internals,Externals,Total,F/P]*AttemptedSubjects
```

Explaination:

- [...]*AttemptedSubjects -> It means that the stuff in the brackets(not including the brackets themselves) are repeated for every attempted subject

Some Example Lines:

```
1cr16cs004,ABHILASH S,7,15CS71,WEB TECHNOLOGY AND ITS APPLICATIONS,18,28,46,P,15CS741,NATURAL LANGUAGE PROCESSING,16,65,81,P,15CS72,ADVANCED COMPUTER ARCHITECTURES,17,39,56,P,15CS73,MACHINE LEARNING,19,52,71,P,15CS754,STORAGE AREA NETWORKS,16,41,57,P,15CSL76,MACHINE LEARNING  LABORATORY,20,79,99,P,15CSL77,WEB TECHNOLOGY LABORATORY  WITH MINI PROJECT,15,79,94,P,15CSP78,PROJECT PHASE 1 + SEMINAR,97,0,97,P,

```


```csv
1cr16cs001,A S AKASH,7,15CS71,WEB TECHNOLOGY AND ITS APPLICATIONS,17,44,61,P,15CS742,CLOUD COMPUTING AND ITS APPLICATION,17,50,67,P,15CS72,ADVANCED COMPUTER ARCHITECTURES,17,31,48,P,15CS73,MACHINE LEARNING,20,51,71,P,15CS754,STORAGE AREA NETWORKS,19,56,75,P,15CSL76,MACHINE LEARNING  LABORATORY,19,79,98,P,15CSL77,WEB TECHNOLOGY LABORATORY  WITH MINI PROJECT,20,78,98,P,15CSP78,PROJECT PHASE 1 + SEMINAR,97,0,97,P,
```
```csv
1cr16cs002,AARATHI NAIR,7,15CS71,WEB TECHNOLOGY AND ITS APPLICATIONS,13,44,57,P,15CS72,ADVANCED COMPUTER ARCHITECTURES,14,59,73,P,15CS742,CLOUD COMPUTING AND ITS APPLICATION,14,58,72,P,15CS73,MACHINE LEARNING,18,44,62,P,15CS754,STORAGE AREA NETWORKS,16,53,69,P,15CSL76,MACHINE LEARNING  LABORATORY,17,58,75,P,15CSL77,WEB TECHNOLOGY LABORATORY  WITH MINI PROJECT,20,80,100,P,15CSP78,PROJECT PHASE 1 + SEMINAR,93,0,93,P,
```
```csv
1cr16cs005,ABHISHEK DASGUPTA,7,15CS71,WEB TECHNOLOGY AND ITS APPLICATIONS,13,23,36,F,15CS742,CLOUD COMPUTING AND ITS APPLICATION,13,38,51,P,15CS72,ADVANCED COMPUTER ARCHITECTURES,13,21,34,F,15CS73,MACHINE LEARNING,12,18,30,F,15CS754,STORAGE AREA NETWORKS,15,28,43,P,15CSL76,MACHINE LEARNING  LABORATORY,15,45,60,P,15CSL77,WEB TECHNOLOGY LABORATORY  WITH MINI PROJECT,12,40,52,P,15CSP78,PROJECT PHASE 1 + SEMINAR,81,0,81,P,
```
```csv
1cr16cs005,ABHISHEK DASGUPTA,6,15CS651,DATA MINING AND DATA WAREHOUSING,13,16,29,F,
```
```csv
1cr16cs009,ADITYA MAHAVEER YARANAL,7,15CS71,WEB TECHNOLOGY AND ITS APPLICATIONS,14,23,37,F,15CS742,CLOUD COMPUTING AND ITS APPLICATION,13,51,64,P,15CS72,ADVANCED COMPUTER ARCHITECTURES,13,14,27,F,15CS73,MACHINE LEARNING,13,33,46,P,15CS754,STORAGE AREA NETWORKS,13,35,48,P,15CSL76,MACHINE LEARNING  LABORATORY,16,77,93,P,15CSL77,WEB TECHNOLOGY LABORATORY  WITH MINI PROJECT,18,67,85,P,15CSP78,PROJECT PHASE 1 + SEMINAR,81,0,81,P,
```

```csv
1cr16cs010,ADITYA S,7,15CS71,WEB TECHNOLOGY AND ITS APPLICATIONS,13,31,44,P,15CS742,CLOUD COMPUTING AND ITS APPLICATION,12,37,49,P,15CS72,ADVANCED COMPUTER ARCHITECTURES,13,28,41,P,15CS73,MACHINE LEARNING,15,45,60,P,15CS754,STORAGE AREA NETWORKS,14,34,48,P,15CSL76,MACHINE LEARNING  LABORATORY,14,77,91,P,15CSL77,WEB TECHNOLOGY LABORATORY  WITH MINI PROJECT,15,70,85,P,15CSP78,PROJECT PHASE 1 + SEMINAR,70,0,70,P,
1cr16cs006,ABHISHEK KUMAR,7,15CS71,WEB TECHNOLOGY AND ITS APPLICATIONS,13,13,26,F,15CS742,CLOUD COMPUTING AND ITS APPLICATION,12,8,20,F,15CS72,ADVANCED COMPUTER ARCHITECTURES,12,11,23,F,15CS73,MACHINE LEARNING,12,8,20,F,15CS754,STORAGE AREA NETWORKS,12,10,22,F,15CSL76,MACHINE LEARNING  LABORATORY,12,32,44,P,15CSL77,WEB TECHNOLOGY LABORATORY  WITH MINI PROJECT,13,40,53,P,15CSP78,PROJECT PHASE 1 + SEMINAR,82,0,82,P,
1cr16cs006,ABHISHEK KUMAR,6,15CS62,COMPUTER GRAPHICS AND VISUALIZATION,12,1,13,F,15CS664,PYTHON APPLICATION PROGRAMMING,12,2,14,F,
1cr16cs008,ADITYA M KAKDE,7,15CS741,NATURAL LANGUAGE PROCESSING,15,37,52,P,15CS71,WEB TECHNOLOGY AND ITS APPLICATIONS,12,43,55,P,15CS72,ADVANCED COMPUTER ARCHITECTURES,12,42,54,P,15CS73,MACHINE LEARNING,17,57,74,P,15CS754,STORAGE AREA NETWORKS,16,52,68,P,15CSL76,MACHINE LEARNING  LABORATORY,20,79,99,P,15CSL77,WEB TECHNOLOGY LABORATORY  WITH MINI PROJECT,20,80,100,P,15CSP78,PROJECT PHASE 1 + SEMINAR,98,0,98,P,
1cr16cs008,ADITYA M KAKDE,6,15CS63,SYSTEM SOFTWARE AND COMPILER DESIGN,13,32,45,P,
```

