import speech_recognition as sr
import pyttsx3
import os
print()
print("\t\t\t\t\tWelcome, i am your assistent Jarvis")
print("\t\t\t\t\t------------------------------------")
print()
pyttsx3.speak("Hello I am Jarvis")
pyttsx3.speak("How can i help you")
r =sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("I am Listening to You....")
        audio=r.listen(source)
        print("Done...")
        text=r.recognize_google(audio)
        print(text)
    if ('hello'in text):
        pyttsx3.speak("Hello nitesh How are you")
        
    elif ("I"in text)or("good"in text):
        pyttsx3.speak("Thats great")
        
    elif ("so"in text)or("doing"in text):
        print("\t\t\ttoday we will be working in aws")
        pyttsx3.speak("today we will be working in aws")
        pyttsx3.speak("so what do you want me to do")
        
    elif ("check"in text)or("Key pair"in text):
        pyttsx3.speak("Checking key pair in AWS")
        os.system("aws ec2 describe-key-pairs")
        
    elif ("create"in text)or("key pair"in text):
        pyttsx3.speak("Creating key pair in AWS")
        pyttsx3.speak("key pair created successfully")
        os.system("aws ec2 create-key-pair --key-name Nitesh-key")
                     
    elif ("delete"in text)or("key pair"in text):
        pyttsx3.speak("Deleting key pair in AWS")
        pyttsx3.speak("key pair deleted successfully")
        os.system("aws ec2 delete-key-pair --key-name Nitesh-key")
        
    elif ("check"in text)or("security group"in text):
        pyttsx3.speak("Checking Security group in AWS")
        os.system("aws ec2 describe-security-groups")
        
    elif ("create"in text)or("Security group"in text):
        pyttsx3.speak("Creating security group in AWS")
        pyttsx3.speak("security group created successfully")
        os.system("aws ec2 create-security-group --group-name Nitesh --description nitesh1")
        
    elif ("delete"in text)or("Security group"in text):
        pyttsx3.speak("Deleting Security group in AWS")
        pyttsx3.speak("Security group deleted successfully")
        os.system("aws ec2 delete-security-group --group-name Nitesh")      
    
    elif ("check"in text)or("instances"in text):
        pyttsx3.speak("Checking instances in AWS")
        os.system("aws ec2 describe-instances")
    
    elif ("start"in text)or("instance"in text):
        pyttsx3.speak("starting Client instance")
        os.system("aws ec2 start-instances --instance-ids i-068deae51c9773ff2 ")
        
    elif ("stop"in text)or("instance"in text):
        pyttsx3.speak("stopping client instance")
        os.system("aws ec2 stop-instances --instance-ids i-068deae51c9773ff2 ")
        
    elif ("launch"in text)or("instance"in text):
        pyttsx3.speak("Launching new instance in AWS")
        pyttsx3.speak("new instance launched suucessfully")
        os.system("aws ec2 run-instances --image-id ami-052c08d70def0ac62 --instance-type t2.micro --count 1 --subnet-id subnet-31595659 --security-group-ids sg-026ea953028eef330 --key-name ARTH")
        
    elif ("terminate"in text)or("instance"in text):
        pyttsx3.speak("terminating client instance")
        pyttsx3.speak("client instance terminated successfully")
        os.system("aws ec2 terminate-instances --instance-ids i-068deae51c9773ff2")
        
    elif ("create"in text)or("volume"in text):
        pyttsx3.speak("Creating an ebs volume in AWS")
        os.system("aws ec2 create-volume --availability-zone ap-south-1a --size 1")
        
    elif ("attach"in text)or("volume"in text):
        pyttsx3.speak("attaching an ebs volume to master instance")
        pyttsx3.speak("volume attached successfully")
        os.system("aws ec2 attach-volume --volume-id vol-0b46d2453ff0a064a --instance-id i-061ec2033deb1e8d1 --device /dev/sdf")
        
    elif ("create"in text)or("bucket"in text):
        pyttsx3.speak("bucket created successfull")
        os.system("aws s3 mb s3://nitesh-bucket10105/")
    
    elif ("ok" in text) or ("bye" in text):
        pyttsx3.speak("See you later")
        break
    else:
        pyttsx3.speak("This command is not available ")
        print("Not supported")