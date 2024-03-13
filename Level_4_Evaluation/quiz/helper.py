import pymongo

client = pymongo.MongoClient("mongodb+srv://[USER]:[PASSWORD]@cluster0.ookfz.mongodb.net/?retryWrites=true&w=majority")
db = client.quiz

# db.questions.insert_one ({'subject':'geo',
#     'q':[
#             {'question':'Capital of US:','options':['Washington D.C.','California','Chicago','Washington'],'correct':'Washington D.C.'},
#             {'question':'What is the name of the tallest mountain in the world?','options':['Mount Kilomanjaro','Mount Everest','Mariana Trench','Appalachians'],'correct':'Mount Everest'},
#             {'question':'Which country has the largest population in the world?','options':['China','India','US','Greenland'],'correct':'China'},
#             {'question':'What is the name of the longest river in Africa?','options':['Amazon River','Nile River','Yangtze River','Mississippi River'],'correct':'Nile River'},
#             {'question':'What American city is the Golden Gate Bridge located in?','options':['Sacramento','San Francisco','Los Angeles','Fremont'],'correct':'San Francisco'},
#         ]
#     }
# )

# db.questions.insert_one ({'subject':'math',
#     'q':[
#             {'question':'7+3','options':['10','11','9','73'],'correct':'10'},
#             {'question':'8*4','options':['12','24','32','48'],'correct':'32'},
#             {'question':'64/8','options':['5','6','7','8'],'correct':'8'},
#             {'question':'100*10','options':['10','100','1000','10000'],'correct':'1000'},
#             {'question':'72-36','options':['18','22','36','42'],'correct':'36'},
#         ]
#     }
# )

# db.questions.insert_one ({'subject':'science',
#     'q':[
#             {'question':'What does DNA stand for?','options':['Deoxyribonucleic Acid','Dino Arms','Doctor\'s National Association','Deoxyribonucleic Antibody'],'correct':'Deoxyribonucleic Acid'},
#             {'question':'How many bones are in the human body?','options':['192','200','206','212'],'correct':'206'},
#             {'question':'The concept of gravity was discovered by which famous physicist?','options':['Jean-Jeacques Rousseau','Sir Isaac Newton','Charles Darwin','Gregory Mendel'],'correct':'Sir Isaac Newton'},
#             {'question':'What is the hardest natural substance on Earth?','options':['Steel','Diamond','Gold','Obsidian'],'correct':'Diamond'},
#             {'question':'Which is the main gas that makes up the Earth\'s atmosphere?','options':['Oxygen','Carbon','Nitrogen','Ozone'],'correct':'Nitrogen'},
#         ]
#     }
# )

db.questions.insert_one ({'subject':'geo1',
    'q':[
            {'question':'What is the capital of Mexico?','options':['Washington D.C.','Buenos Aires','Mexico City','New Mexico'],'correct':'Mexico City'},
            {'question':'What is the name of the largest country in the world?','options':['India','United States','China','Russia'],'correct':'Russia'},
            {'question':'What is the name of the largest ocean in the world?','options':['Pacific Ocean','Atlantic Ocean','Mediterranean Sea','Indian Ocean'],'correct':'Pacific Ocean'},
            {'question':'What U.S. state is home to no documented poisonous snakes?','options':['California','Alaska','Oklahoma','Maine'],'correct':'Alaska'},
            {'question':'Where is the Eiffel Tower located?','options':['Paris','London','San Francisco','Ottawa'],'correct':'Paris'},
        ]
    }
)

db.questions.insert_one ({'subject':'math1',
    'q':[
            {'question':'10*11','options':['99','101','110','111'],'correct':'10'},
            {'question':'17-38','options':['21','19','-19','-21'],'correct':'-21'},
            {'question':'16*4','options':['4','32','48','64'],'correct':'64'},
            {'question':'144/12','options':['8','10','12','14'],'correct':'12'},
            {'question':'63+19','options':['72','74','82','84'],'correct':'82'},
        ]
    }
)

db.questions.insert_one ({'subject':'science1',
    'q':[
            {'question':'Humans and chimpanzees share roughly how much DNA?','options':['50%','90%','98%','100%'],'correct':'98%'},
            {'question':'What is the most abundant gas in the Earth\'s atmosphere?','options':['Oxygen','Carbon','Nitrogen','Ozone'],'correct':'Nitrogen'},
            {'question':'Roughly how long does it take for the sun\'s light to reach Earth?','options':['0.8 seconds','8 seconds','8 minutes','8 hours'],'correct':'8 minutes'},
            {'question':'Which famous British physicist wrote A Brief History of Time?','options':['Isaac Newton','Stephen Hawking','Gregory Mendel','Charles Darwin'],'correct':'Stephen Hawking'},
            {'question':'At what temperature are Celsius and Fahrenheit equal?','options':['-50','-40','40','50'],'correct':'-40'},
        ]
    }
)