# Mongo-Python
Learning the intricacies of Mongo db and Python
# Sample Mongo Aggregation
The below aggregation pipeline is a sample use os pyMongo in business intelligence and data analytics.
The role of this pipeline is to:
1. Filter out salaries that are empty strings
2. group salary information by state and find the average salary for professors and associate professors
3. compute salary difference and sort by the new column


```
[
{$match: {AVGSalaryProfessors: {$not: {$type: 2}}, AVGSalaryAssociateProfessors:  {$not: {$type: 2}}}},
{$group: {_id: "$State", StateAVGSalaryProfessors: {$avg: "$AVGSalaryProfessors"}, StateAVGSalaryAssociateProfessors: {$avg: "$AVGSalaryAssociateProfessors"}}},
{$project: {_ID: 1, SalaryDifference: {$subtract: ["$StateAVGSalaryProfessors", "$StateAVGSalaryAssociateProfessors"]}}},
{$sort: { SalaryDifference: 1}}
]
```

