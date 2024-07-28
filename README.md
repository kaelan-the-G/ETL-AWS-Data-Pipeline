# BBB [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
Bureau for Business Bean (BBB) group

        # Members:
        Kaelen 
        Michael
        Phoenix 
        Fruzsi

  ## <span id=Description> Description </span>
  A sales forecast program created specifically for the cafe branch data of The Super Cafe Franchise, integrated with Amazon Web Services. The program will automatically processes data upon its upload to an 
  S3 bucket. This process involves removing sensitive information and noramlisizing the data before then automatically loading it into a RedShift database. This data can the be queryed with an SQL query engine.

  ## Elevator Pitch 
  The Bean Business Bureau Data System is an automated analysis and visualization tool for business planning & forecasting that tracks key metrics such as overall sales & product popularity in various time 
  frames. This program was created for The Super Cafe Franchise to resolve their need for a data pipeline automation software for sales analysis and forecasting. Unlike the competition our program offers expanded 
  insights with specifically queryed data, bespoke graphs & visualizations highlighting trends and consumer patterns that would otherwise be missed. It is easy to add data with CSV and our comprehensive error 
  detection and testing will allow for efficient updates and future deployements. Accurate, reliable, durable, secure - cleansing, expandable, intuitive, dynamic, that is the Bean Business Bureau Data system.

  ## Contents
  -[Description](#Description)  
  -[Install](#Install)  
  -[Usage Info](#Usage)  
  -[Contribution](#Contribution)  
  -[Questions](#Questions)  
  -[Tests](#Tests)  
  -[License](#License)  

  ## Product initiation document
  https://docs.google.com/document/d/1FSQwxu9fgONe1-Cq1r67GGJAH0eON9phLxYBTDiPlAs/edit?usp=sharing

  ## Group board
  https://miro.com/app/board/uXjVK5mj_K8=/

  ## <span id=Install> Install </span>
  1. Clone this repo in terminal using ***git clone https://github.com/generation-de-nat2/Bureau-for-Bean-Business.git*** or by simply downloading it as a zip file and extract
  2. Make sure you have a working version of AWS CLI and have setup an SSO profile. For instructions and more info see: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html
  3. Initialize the AWS CLI and run this command to create the deployment bucket: **aws s3 mb s3://bbb-deployment-packages --profile \<your-profile-name\>**

  4. Upload the psycopg2 layer to the deployment bucket using the following command in AWS CLI: **aws s3 cp .github/workflows/Cloudformation/psycopg2.zip s3://bbb-cloudformation-packages/psycopg2.zip --profile= \<your-profile-name\>**
  5. Create your cloudformation ressources by running the following command: **aws cloudformation deploy --template-file bbb-stack-template-S3.yml --stack-name bbb-stack --region eu-west-1 --profile \<your-profile-name\>**
  6. Add a github secret to your repo and add a variable called **AWS_ROLE_ARN**
  7. This can now be connected query engine of your choice

  ## <span id=Usage> Usage </span>
  Upload cafe branch daily data in CSV fromat to the bbb-group-bucket either using **\<path-to-data\> \<s3 uri\> --\<your-profile-name\>** or with the AWS management console.

  ## <span id=Contribution> Contribution </span>
  Created by BBBgroup  
  See github to contribute or report bugs: https://github.com/https://github.com/generation-de-nat2/Bureau-for-Bean-Business

  ## <span id=Questions> Questions </span>
  For issues or feature requests: https://github.com/https://github.com/generation-de-nat2/Bureau-for-Bean-Business  
  For other questions, please email me: 

  ## <span id=Tests> Tests </span>
  Unit tests can be ran through the command **py -m pytest -v -s** from the main repo

  Make sure to replace **py** with the correct command for your operating systems (Windows, Linux, Mac ETC:)

  ## <span id=License> License </span>
  MIT  
  https://opensource.org/licenses/MIT  
  Copyright BBBgroup
      Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  
      
      The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
      
      THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  
