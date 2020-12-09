# kt-proj-presetup

The project is a Heroku Custom Buildpack to do tasks most relevant for Kotlin (Java) projects. 

## Task 1 - Download SSL certificate from S3 Bucket

The Java projects doesn't directly support PEM standard cryptographic keys. Instead it supports a propreitary PKCS format. To learn more about the certificates, you can refer [this](https://security.stackexchange.com/questions/183072/pem-cer-crt-p12-what-is-it-all-about) article. As a first step for a Kotlin (Java) application to support SSL, it needs PKCS12 format file (with an extension `.p12`). You can refer [this](https://www.ssl.com/how-to/create-a-pfx-p12-certificate-file-using-openssl/) article to learn more about how to generate a PKCS12 format certificate. Now, in Envoy, we manage these certificates in AWS S3 buckets. The Task 1 is to download the certificate from S3 and make it available in the Heroku setup so your application can refer the certificate and use it. For this step to work, you need to setup correct values in the below environment variables.

* `AWS_ACCESS_KEY_ID` - Set the AWS Access Key
* `AWS_SECRET_ACCESS_KEY` - Set the AWS Secret Access Key
* `SSL_KEY_STORE_S3_BUCKET` - Set the S3 Bucket name where the certificate managed
* `SSL_KEY_STORE_S3_FILENAME` - Set the S3 Bucket Key (filename along with path if needed) that identifies the certificate
* `SSL_KEY_STORE_OUTPUT_FILENAME` - Set the certificate output filename. You can use more relevant names based on your application.

Once the file downloaded, the certificate will be available in `/app/cert` directory

## Task 2 - Download Datadog Java Agent

It's hard to manage an application in Production without Monitoring in place. The Buildpack designed to download Datadog Java Agent for the monitoring purposes.

Once the file downloaded, the agent will be available in `/app/agent/` directory

> More features to add. Coming soon!
