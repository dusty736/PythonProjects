data= {"Gallup": { "WA": 7, "CA": 15, "UT": -30},
    "SurveryUSA": { "CA": 14, "CO": 2, "CT": 13, "FL": 0, "KY": -14},
    "RAND": { "NY": 11.2, "AZ": -9.8, "AR": -18.9 }}
pollster = ["Gallup", "SurveyUSA", "RAND"]    
for poll in data:
    if data.keys() == pollster:
        print poll