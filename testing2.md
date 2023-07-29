![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/10e4f214-ffb6-4bae-8c30-745075d8c5f7)
# social identity provider in an Amazon Cognito user pool in using Flutter [Member: Kha Nguyen]

Introduction:
Purpose: Set up Amazon, Facebook, and Google as a social identity provider on in an Amazon Cognito user pool using AWS Amplify

-AWS Amplify is a set of purpose-built tools and features that enables frontend web and mobile developers to quickly and easily build full-stack applications on AWS
-Amazon Cognito is a service that provides users pools API

Documentations & tutorials:
https://www.youtube.com/watch?v=4LVeom2V5S8&t=1160s
https://ui.docs.amplify.aws/flutter/connected-components/authenticator

Not include Apple ID since needed to be paid
Set up

-Create a Flutter app: flutter create my_app  
-Dependencies
  environment:
    sdk: '>=3.0.6 <4.0.0'
  dependencies:
    flutter:
      sdk: flutter
    amplify_flutter: ^1.0.0-next.1
    amplify_auth_cognito: ^1.0.0-next.1
    amplify_authenticator: ^1.0.0-next.1
flutter pub get
-Configure backend:
npm install -g @aws-amplify/cli@latest
Initialize connection to amplify: amplify init
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/71837d46-d1aa-47dc-a9b8-6b53be105580)
New app initilize
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/4078ae40-4a29-4c4b-ac77-e057a7ebb0f1)

Add authentication: amplify add auth

Update and select a social provider:
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/1ddf452a-efa5-48fa-a086-4041711c9c1a)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/cb98e816-5688-45f4-ae43-44947e31704d)

![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/e597e47a-9798-4495-bdf6-a5a11ef1a829)


Amazon
Sign in to Amazon Developer: https://developer.amazon.com/
Create a security profile:
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/c5c16ab7-bf63-4eb1-b235-c36b6f5ace46)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/014021c0-5cf7-4d8d-9c22-f216864932c1)
Client ID & Client Secret:
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/8d2177f3-b1ef-407c-aa0e-53c53e4355ec)
Configuring social sign in in the app: amplify auth update
Enter the Client ID & Client Secret:
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/63a3c35f-dbac-432a-b765-2a7dd880a846)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/64e59e6e-fec9-4f90-8a1c-26f700ddcadc)
then: amplify push
Receive an Endpoint:
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/45330260-0cbc-4963-97eb-e4eef67d16a9)
Paste the "endpoint" to Allowed Origins and "endpoint/oauth2/idpresponse" to Allowed Return URLs:
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/8ad05a8a-86bc-445c-8bb4-223234b96593)
