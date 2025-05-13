# DriveCap

Interview Code:

  This is Robert Guise's Connections Code. It takes in a file name for an argument and will ouput an alphabetical list of companies with the highest strength partner.
  The file you will run is called Connections.py and will take the file name as an input. I used example test files to test my code.

Design Decisions:

  I approached this problem in pieces and built the person class first. I wanted to make this general purpose to be used for partners and non-partners. 
  This is so I could track strength of each partner and the related companies they have strength with. I then made the connections class to take the file
  process it then when you print the object is prints the list of companies in alphabetical order and highest partner strength is attached. I chose to have the
  class process the file so that it would be easy to store the file name inputed to understand the data it had worked on. This was also useful for having all
  commands being processed as the file is being processed. 

Assumptions: 

  I did not add much error handling into my code since in the description it said that all input files would be correctly formatted. I however would love to add
  error handling to the code and it would not be to hard to do so. I also did not store individual contacts I only kept track of the strength as it did not affect
  the output of the code but could be stored in the person class with slight modification. Also if multiple of the same name of employee is added it will just 
  change the dictionary entry for that person. 
