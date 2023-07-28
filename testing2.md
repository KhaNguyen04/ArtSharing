
# social identity provider in an Amazon Cognito user pool in using Flutter [Member: Kha Nguyen]

Introduction:
Purpose: Set up Amazon, Facebook, and Google as a social identity provider on in an Amazon Cognito user pool using AWS Amplify

-AWS Amplify is a set of purpose-built tools and features that enables frontend web and mobile developers to quickly and easily build full-stack applications on AWS
-Amazon Cognito is a service that provides users pools API

Documentations & tutorials:
https://www.youtube.com/watch?v=4LVeom2V5S8&t=1160s
https://ui.docs.amplify.aws/flutter/connected-components/authenticator

Not include Apple ID since needed to be paid
Steps 

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
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/1ddf452a-efa5-48fa-a086-4041711c9c1a)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/cb98e816-5688-45f4-ae43-44947e31704d)

![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/e597e47a-9798-4495-bdf6-a5a11ef1a829)
