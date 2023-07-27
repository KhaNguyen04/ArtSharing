#LinkedIn as a social identity provider in an Amazon Cognito user pool in using Flutter <br /> 
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
  -Choose the Auth tab. Confirm that r_emailaddress and r_liteprofile are listed. These permissions are required for Auth0 to access the required LinkedIn user info.
Note: If you don't see the r_emailaddress and r_liteprofile listed, then add the product "Sign In with LinkedIn" to your application. This is found on the Products tab of your LinkedIn Dev page.
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/d0596980-5519-4dcd-8676-fc2eb8a46062)

Under OAuth 2.0 settings, next to Redirect URLs:, choose the pencil icon, and then choose + Add redirect URL.
Under Redirect URLs:, enter https://tenantName.us.auth0.com/login/callback, replacing tenantName with your Auth0 tenant name (or an Auth0 custom domain).

![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/2dccb94f-44db-4590-9ebc-7d2fcaa32dbd)
  Tenant name in Auth0
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/85c812ee-bf9c-4858-ac4e-2455e1fafb6f)

Connect to LinkedIn from Auth0
  On the Auth0 website dashboard, in the left navigation pane, choose Authentication, and then choose Social.
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/1aee62be-0f5d-455c-ba0f-03366d18d84b)
Choose LinkedIn.
On the Settings pane of the LinkedIn dialog box, do the following:
For API Key, enter the Client ID that you copied earlier from your LinkedIn app.
For Secret Key, enter the Client Secret that you copied earlier from your LinkedIn app.
For Attributes, select the Email address check box.

![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/f74e62b8-2be1-48ac-9a99-36acaf04b5a2)
Client ID in Cognito
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/9b07848b-f313-4efa-9cae-351e19ae24ad)

Add OIDC provider to your user pool

In the Amazon Cognito console management page for your user pool, in Sign-in experience, under Federation, choose Identity Providers.

![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/178044e6-06a2-4a43-ba3c-b8cb495148f2)
Choose OpenID Connect.
Enter the details of your Auth0 app for the OIDC provider details, as follows:
For Provider name, enter a name (for example, Auth0-LinkedIn). This name appears in the Amazon Cognito hosted web UI.
Note: You can't change this field after creating the provider.
For Client ID, enter the Client ID that you copied earlier from your Auth0 application.
For Client secret (optional), enter the Client Secret that you copied earlier from your Auth0 application.
For Attributes request method, leave the setting as GET.
For Authorize scope, enter openid profile email.
For Issuer, enter the URL of your Auth0 profile. For example, https://tenantName.auth0.com, replacing tenantName with your Auth0 tenant name.
For Identifiers (optional), you can optionally enter a custom string to use later in the endpoint URL in place of your OIDC provider's name.
Map attributes: Confirm that the OIDC attribute sub is mapped to the user pool attribute Username.
Choose Add OIDC attribute. For the new OIDC attribute, enter email. For User pool attribute, choose Email.
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/44df0ef6-31c8-408d-9407-c58604e113ca)
![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/bc0f6709-684e-48e7-bbcc-6a16c6bcd9c5)

Create app client settings for your user pool

In the Amazon Cognito console management page for your user pool, under App integration, choose App client and analytics.
On the app client page, do the following:
Under Enabled Identity Providers, select the OIDC provider (for example, Auth0-LinkedIn) and Cognito User Pool check boxes.
For Callback URL(s), enter a URL where you want your users to be redirected after logging in. For testing, you can enter any valid URL, such as https://example.com/.
For Sign out URL(s), enter a URL where you want your users to be redirected after logging out. For testing, you can enter any valid URL, such as https://example.com/.
Under Allowed OAuth Flows, select either the Authorization code grant or Implicit grant check box, or both.
Note: The allowed OAuth flows you enable determine which values ("code" or "token") you can use for the response_type parameter in your endpoint URL.
Under Allowed OAuth Scopes, select at least the email and openid check b

![image](https://github.com/KhaNguyen04/ArtSharing/assets/88961521/85d40caa-dbb5-4323-9146-adbfe94cfb00)




