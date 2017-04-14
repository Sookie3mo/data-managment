/*
@Yiming Liu
inf551 assignment3
*/

use inf551;
#create tables
drop table if exists Candidate;
create table Candidate(year varchar(10), democratName varchar(30),republicanName varchar(30), PRIMARY KEY(year));
drop table if exists Vote;
create table Vote(year varchar(10) ,state varchar(30),elecDemocrat int, elecRepublican int, popDemocrat int, popRepublican int);


#create indexes after inserting all data into tables
ALTER TABLE Candidate ADD INDEX indexYear (year);  #The primary key year works the same with indexYear here.
ALTER TABLE Vote ADD INDEX year_state_elecDe_popDe (year,state,elecDemocrat,popDemocrat); 
ALTER TABLE Vote ADD INDEX year_state_elecRe_popRe (year,state,elecRepublican,popRepublican); 

/*
BY seperating the data into two tables Candidate and Vote, we avoid parts of the redundancy. 
For searching candidate names, we only need to query in table Candidate.
For serching vote information, we use table Candidate and keyword "name" to get the candidate's party, then we use keywords to search into table Vote.


Pros:
1.By adding index indexYear on table Candidate, searching candidates with year in table Candidate will be accelerated in "candidate.py".
2.By adding index year_state_elecDe_popDe on table Vote, searching elecDemocrat,popDemocrat with year and state will be accelerated in "search.py".
3.By adding index year_state_elecRe_popRe on table Vote, searching elecRepublican,popRepublican with year and state will be accelerated in "search.py".

Cons:
The indexes need to be updated if we update,delete or insert to tables,so we can say the indexes speed up the searching, but slow down the updating.
*/

