# Telecom Churn Analysis and Future Churn Prediction 
---
This project was conducted to understand the **reasons for customer churn** in a telecommunications industry and use machine learning to **predict future churners**. The goal of this project is to _**draw a profile of current and future churner**_ and provide insights and recommendations to _**reduce the churn rate**_ for the company. 

---
## Metrics 
- _**Total customers**_
- _**Total churn & Churn rate**_
- _**New joiners**_
  
--- 
## Goals for this project
_**Targeting Churner profile**_ by analyze customer data at below levels:
- _**Demographic**_
  - Gender
  - Age
- _**Geographic**_
  - State
- _**Payments & account info**_
  - Payment method
  - Internet type
  - Contract 
  - Tenure
- _**Service type**_
  - Service type
- _**Churn reason**_
  - churn category
  - churn reason 
  
---
## Data structure 
The dataset contains information about 6,418 customers of a telecommunications company. The dataset comprises 34 variables, each capturing different aspects of customer behavior and demographics.

The dataset had 2 main tables: 
- _**prod_churn**_ is a table of _**all customers**_ including customers who were _**retained, churned, and newly joined**_.
- _**churn_predictions**_ is a table of _**predicted future churners**_ generated using machine learning.
- All the other tables were calculated for the purpose of creating the dashboard. 

![ERD](https://github.com/eggchoo/churn-analysis/blob/main/ERD.png?raw=true)
---
**[View the Power BI Interactive Dashboard here](https://app.powerbi.com/links/dV7FDMM88M?ctid=6f0bb72f-5377-4ddf-936a-b6c72bf21ae2&pbi_source=linkShare&bookmarkGuid=a8e6f4a7-8f13-4535-a8f2-f4912f82b294)**

![Power BI Dashboard](https://github.com/eggchoo/churn-analysis/blob/main/churn%20overview.png?raw=true) 


![Power BI Dashboard](https://github.com/eggchoo/churn-analysis/blob/main/churn%20prediction.png?raw=true)
