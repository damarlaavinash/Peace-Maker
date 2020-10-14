import boto3
confi=0
BUCKET = "usharama-face"
KEY = "demo.jpg"
FEATURES_BLACKLIST = ("Landmarks", "Emotions", "Pose", "Quality", "BoundingBox", "Confidence")
ACCESS_ID = " # Place your ACCESS_ID " 
ACCESS_KEY = " # Place your ACCESS_KEY " 
REGION = "# your region "

def detect_faces(bucket, key,REGION,ACCESS_ID,ACCESS_KEY,attributes=['ALL']):
	client = boto3.client('rekognition',region_name=REGION,aws_access_key_id=ACCESS_ID,
         aws_secret_access_key= ACCESS_KEY)
	imageSource=open(key,'rb')
	response = client.detect_faces(
            Image={'Bytes': imageSource.read()},Attributes=['ALL'])
	print('Detected faces for ' + key)
	confi=0
	for faceDetail in response['FaceDetails']:
            for emotion in faceDetail['Emotions']:
                print (emotion)
                dummy=int(emotion['Confidence'])
                print(dummy)
                if(dummy>0):
                    if(confi>=dummy):
                        pass
                    else:
                        confi=dummy
                        status=emotion['Type']
                        print (confi, status)
                        if(status=="HAPPY"):
                                playhappy()
                        elif(status=="SAD")

#detect_faces(BUCKET, KEY,REGION,ACCESS_ID,ACCESS_KEY)
