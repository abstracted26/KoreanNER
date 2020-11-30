#Importing KoalaNLP's initialize & Finalize
from koalanlp.Util import initialize, finalize
#Importing KoalaNLP APIs
from koalanlp import API
#Importing Entity Recognizer
from koalanlp.proc import EntityRecognizer
def koreannlp(text):
    #Initizaling JDK & APIs
    initialize(java_options="-Xmx4g", ETRI="LATEST")
    #Using Entity Recognizer with the API Key
    recognizer = EntityRecognizer(API.ETRI, etri_key="0d89dc20-55a3-4433-ab01-be3fd7bad359")

    #Parsing the Input String in Korean
    #Sample text for Testing purposes : 
    #"저는 한국 서울에 살고 있습니다 1000 원에 팔겠습니다 저는 판매자이고 LG G8을 
    # 판매하고 있습니다 제 전화 번호는 9370056544이고, 제 전화 번호는 9113480044입니다"
    
    parsed = recognizer(text)

    entities = []
    #Printing Entites
    for entity in parsed[0].getEntities():
        entities.append(entity)

    #Closing Initialized JDK
    finalize()
    #Returning entities
    return entities
