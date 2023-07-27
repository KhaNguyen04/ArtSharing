#LinkedIn as a social identity provider in an Amazon Cognito user pool in using Flutter
**_[Member: Kha Nguyen]_**

## Introduction:
  Purpose: Set up LinkedIn as a social identity provider in an Amazon Cognito user pool
- Amazon Cognito is a service that provides users pools API
- Autho0 is used as a middle agent between LinkedIn and Amazon Cognito to transfer identity information since LinkedIn doesn't provide all fields to Amazon Cognito

## Steps by steps
Create an Amazon Cognito 
  -First have an AWS account
  -Then create a user pool in Cognito
  Example: (Not required to be exact customizations)
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/d20d5ddf-aa30-46e3-a88e-5852f3c5fe53)
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/4497a018-b551-48ef-8fdb-467876988fde)
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/6d7f19b3-fd56-4690-b090-dfb40c620aaf)
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/d5050791-28bc-4b29-8e57-b4a90e769f5b)
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/c067b824-e718-471a-8c42-d0fd1d05bbfd)
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/e9db170c-f123-4825-b0f3-10b7e585bd25)
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/4b6a411d-2069-4ba2-b560-ed17ae4f612f)
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/4211885c-e055-4ea0-8d77-66659bd27b5d)
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/8c626b43-89e6-4cd7-9c09-93eb1c0a15de)
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/a94526be-e9d5-4fc1-89f2-60af5426c803)


Create an Auth0 application
  -	Sign up for an Auth0 account
  - Create an Auth0 application
    ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/2c9a05ac-54e4-4089-97fb-3f5e660c5b7a)
    Under Choose an application type, choose Single Page Web Applications.
  -  For Allowed Callback URLs, enter https://yourDomainPrefix.auth.region.amazoncognito.com/oauth2/idpresponse.
Note: Replace yourDomainPrefix and region with the values for your user pool. Find them in the Amazon Cognito console on the Domain name tab of the management page for your user pool.
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/d4f5647f-7bef-48ef-bcec-2c97ff701a0c)
  Domain name in Cognito 
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/53085691-77a1-40a9-b3cc-ffb29513ba09)

Create a LinkedIn app
  -Sign up for a LinkedIn account
  -Go to https://developer.linkedin.com/ to create the application
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/ddd5301b-89cf-4999-9008-8694ca398516)
  ![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/1580b3c5-8fbc-4317-baab-51817b92ca4a)












