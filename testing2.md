
# Social identity provider in an Amazon Cognito user pool in using Flutter 

## [Member: Kha Nguyen]


- [Introduction](#introduction)
- [Set up](#set-up)
- [Amazon](#amazon)
- [Facebook](#facebook)
- [Google](#google)

### Introduction:
#### Purpose: Set up Amazon, Facebook, and Google as a social identity provider on in an Amazon Cognito user pool using AWS Amplify

-AWS Amplify is a set of purpose-built tools and features that enables frontend web and mobile developers to quickly and easily build full-stack applications on AWS <br>
-Amazon Cognito is a service that provides users pools API

Documentations & tutorials: <br>
https://www.youtube.com/watch?v=4LVeom2V5S8&t=1160s <br>
https://ui.docs.amplify.aws/flutter/connected-components/authenticator <br>

<em>Not include Apple ID since needed to be paid</em> <br>

### Set up

-Create a Flutter app: 

```
flutter create my_app  
```
-Add Dependencies <br>


```
  environment:
    sdk: '>=3.0.6 <4.0.0'
  dependencies:
    flutter:
      sdk: flutter
    amplify_flutter: ^1.0.0-next.1
    amplify_auth_cognito: ^1.0.0-next.1
    amplify_authenticator: ^1.0.0-next.1
```

<br>
   In terminal: <em> flutter pub get </em> 

-Configure backend: npm install -g @aws-amplify/cli@latest
<br>
<div align="center">
<em> Initialize connection to amplify in IDE: amplify init </em>

![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/71837d46-d1aa-47dc-a9b8-6b53be105580)

<em> New app initilize </em> <br>


![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/4078ae40-4a29-4c4b-ac77-e057a7ebb0f1) <br>
</div>

Add authentication: amplify add auth </em>
<div align="center">

<em> Update and select a social provider: </em> <br>
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/1ddf452a-efa5-48fa-a086-4041711c9c1a) 
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/cb98e816-5688-45f4-ae43-44947e31704d)

![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/e597e47a-9798-4495-bdf6-a5a11ef1a829)
</div>

-main.dart file:
```
import 'package:amplify_auth_cognito/amplify_auth_cognito.dart';
import 'package:amplify_authenticator/amplify_authenticator.dart';
import 'package:amplify_flutter/amplify_flutter.dart';
import 'package:flutter/material.dart';
import 'amplifyconfiguration.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  void initState() {
    super.initState();
    _configureAmplify();
  }

  void _configureAmplify() async {
    try {
      await Amplify.addPlugin(AmplifyAuthCognito());
      await Amplify.configure(amplifyconfig);
      safePrint('Successfully configured');
    } on Exception catch (e) {
      safePrint('Error configuring Amplify: $e');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Authenticator(
      child: MaterialApp(
        builder: Authenticator.builder(),
        home: 
        const Scaffold(
          body:Center(child: Column(
            children: const [ 
              Text('You are logged in!'),
              SignOutButton(),
            ]
          ),) 
        ),
      ),
    );
  }
}
```

### Amazon
Sign in to Amazon Developer: https://developer.amazon.com/<br>

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

Testing in app: <br>
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/25b7414f-bffe-4687-acd4-84bf2ea60b30)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/90483b0f-6668-4707-8c5f-28099f152d39)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/920ee5dd-3d7d-47ad-810d-1e73429b32a7)
<div align="center">
 User succesfully logged in and stored in Cognito </div>


### Facebook
Sign in to Facebook Developer: https://developers.facebook.com/      <br>
Create an app:
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/e51aa3fb-99d7-4ddf-91ac-8ae49a356620)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/a9e93d5e-cbaa-449d-b3a3-f130d38cb7d8)
Configuring social sign in in the app: amplify auth update
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/d82e2b48-6379-4704-b256-93d7ee1db303)
Select Facebook
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/7d582966-06b9-49f4-ab50-c28317d4d7ac)
Get the App ID and App Secret from Facebook Developer
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/6d45a79c-7d38-4b30-a38d-e96bee51a51b)

Paste in to configure Facebook social sign in (Also re-entering other social sign in if there are any):
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/b11c23f5-1085-4972-8111-343502f0b3fb)

Receive an Endpoint:
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/2521c328-e055-4ed1-99f2-0aed00f63f9c)
Paste in App domains the endpoint:
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/85f35958-968c-4d8c-ace5-cb1d2ea17a56)
Paste in Site URL the endpoint+"/oauth2/idpresponse":
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/b0e600fa-d94b-4382-ad01-a35b5543d044)
Paste in ValidOauth Redirect URIs the "endpoint/oauth2/idpresponse":
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/16403a44-f13c-4310-8763-6b85895c1144)

Testing in app: <br>
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/8f06462a-3c69-442c-8713-13b8e9c94388)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/ed38cf6b-d4d9-4017-afdc-491d4e53c69b)


### Google
Sign in to Google Developer: https://console.developers.google.com/project <br>
Create a project: <br>
Get into Credentials in APIs & Services <br>

![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/f52eaaac-875f-45b0-aaba-5456355a981c) <br>
Create Oauth client ID: <br>
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/541685d4-a2cc-4cd3-b29b-303c3b31e43d)
First Configure Consent Screen:(Then enter the required fields with any additional customizations)<br>
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/83bc4330-2459-4598-b259-e341087c61e3) <br>
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/a01bd1f9-d04d-43df-a625-e31bd91c0e4c)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/bd680db2-b34b-4467-adba-b3dde85e1a69) <br>
Configuring social sign in in the app: amplify auth update

Create OAuth client ID <br>
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/87849ace-3dd9-460b-b0cc-9924b018101f)
Save the Client ID & Client Secret <br>
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/07d11a2f-4590-49b5-8851-d08a8e8dcafa)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/09ea70dd-7659-4234-a395-51bdbaff51a0) <br>
Configuring social sign in in the app: <em> amplify auth update </em>
-Update social sign in including Google <br>
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/056de2a7-d159-4082-94d7-af29c2d5c9d2)
-Enter the saved Client ID and Client Secret (Also re-entering other social sign in if there are any) <br>
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/e5c013f6-605c-4855-8581-e0485853780c)
then to Receive an Endpoint : <em> amplify push </em> <br>
Enter the Endpoint in Authorized Javascript origins  & <br>
enter the endpoint+"/oauth2/idpresponse" in Authorized redirect URIs:
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/1319e143-4689-4bc4-9d5d-e2a1823a980a) <br>

Testing Google social sign in: <br>
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/f5189c1b-9c78-43af-a8a5-1ff0c07c809b)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/c24fa7e0-8e3b-4fd4-bc78-d0dff1d959da)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/d336b897-f63a-4f48-b44b-4aadc7caafaf)





