# TelecomX Churn Analysis and Future Churn Prediction 
---
#### **TeleComX** is a leading telecommunications provider offering broadband, mobile, and digital communication services to customers across multiple regions. This report integrates findings from both the **Churn Analysis** and **Churn Prediction** to provide a comprehensive view of customer attrition within the company. The analysis identifies key factors influencing churn, highlights high-risk customer segments, and presents actionable strategies to improve retention, enhance customer satisfaction, and support long-term business growth.


---
## Metrics 
- _**Total customers**_
- _**Total churn & Churn rate**_
- _**New joiners**_
  
--- 
## Goals for this project
1. _**Identifying churner profile**_ by analyze customer data at below levels:
- _**Demographic**_
  - Gender, Age, State
- _**Payments & account info**_
  - Contract type, Payment method, Internet type
- _**Service type**_
  - Service type
- _**Tenure**_
- _**Churn reason**_
  - churn category, churn reason

2. _**Predicting future churners**_
3. _**Provide business insights and recommendations to stakeholders**_

---
## Data structure 
The dataset contains information about _**6,418 customers of a telecommunications company**_. The dataset comprises 34 variables, each capturing different aspects of customer behavior and demographics.

The dataset had 2 main tables: 
- _**prod_churn**_ is a table of _**all customers**_ including customers who were _**retained, churned, and newly joined**_.
- _**churn_predictions**_ is a table of _**predicted future churners**_ generated using machine learning.
- All the other tables were calculated for the purpose of creating the dashboard. 

![ERD](https://github.com/eggchoo/churn-analysis/blob/main/ERD.png?raw=true)
---

**[View the Power BI Interactive Dashboard here](https://app.powerbi.com/links/dV7FDMM88M?ctid=6f0bb72f-5377-4ddf-936a-b6c72bf21ae2&pbi_source=linkShare&bookmarkGuid=a8e6f4a7-8f13-4535-a8f2-f4912f82b294)**

--- 
## **Executive Summary**
- This report provides an integrated overview of customer churn within the telecom company, combining insights from both _**historical churn analysis**_ and _**predictive modeling**_.  
- Findings reveal that _**short-term contracts**_, _**service quality concerns**_, and _**competitive market pressures**_ are the primary drivers of customer attrition.  
- By implementing targeted retention strategies — including _**contract-based incentives**_, _**enhanced customer support**_, and _**data-driven regional campaigns**_ — the company can significantly _**reduce churn, improve customer satisfaction, and safeguard long-term revenue**_.

---
## **Overall Churn Summary**
- **Total Customers:** 6,418  
- **Total Churn:** 1,732  
- **Churn Rate:** 27.0%  
- **Predicted Churners:** 371 customers identified as high risk  

The results indicate a moderate churn rate, influenced by factors such as contract duration, service type, payment method, and customer experience. Predictive modeling further identifies customers most likely to churn, allowing for proactive intervention and targeted retention campaigns.

---
## **Churn Overview**
![Power BI Dashboard](https://github.com/eggchoo/churn-analysis/blob/main/churn%20overview.png?raw=true) 

## **Key Insights from Churn Analysis**
- **Demographics:** Churn is higher among **female customers (64.15%)** and those aged **over 50 (31.0%)**, reflecting demographic differences in service satisfaction or usage behavior.  
- **Contract Type:** Customers on **month-to-month contracts (46.5%)** have the highest churn, underscoring the impact of contract flexibility on retention.  
- **Internet Type:** **Fiber Optic users (41.1%)** show a higher churn rate than **Cable (25.7%)** or **DSL (19.4%)**, suggesting potential service quality or pricing concerns.  
- **Payment Method:** Customers using **Mailed Check (37.8%)** and **Bank Withdrawal (34.4%)** exhibit higher churn than **Credit Card (14.8%)** users, implying that convenience and automation may improve retention.  
- **Tenure:** Customers in the **6–12 month** range show slightly higher churn (**27.2%**), pointing to a vulnerable period following initial onboarding.  
- **Primary Churn Reasons:** Top reasons include **competitor offers**, **better devices**, and **dissatisfaction with customer support**.

---
## Future Churn Prediction 
![Power BI Dashboard](https://github.com/eggchoo/churn-analysis/blob/main/churn%20prediction.png?raw=true)

## **Key Insights from Churn Prediction**
- **High-Risk Segments:** The model identified **371 customers** with elevated churn probability — **239 females** and **132 males**.  
- **Age and Tenure:** The largest at-risk groups are aged **35–50** and **over 50**, with tenure clustering at both **under 12 months** and **over 24 months**, indicating risk among both new and long-term users.  
- **Contract and Payment:** A substantial majority (**350 customers**) of predicted churners are on **month-to-month plans**, reinforcing the need to incentivize longer-term contracts. Most pay via **Credit Card** or **Bank Withdrawal**, showing that churn risk extends across payment methods.  
- **Geographical Trends:** The highest predicted churn is concentrated in **Uttar Pradesh (43)**, **Maharashtra (39)**, **Tamil Nadu (36)**, and **Karnataka (29)**, suggesting regional retention challenges.
- **Financial Impact:** Predicted churners represent a **monthly charge total of 15,621.25** and **total revenue of 41,132.71**, signaling a meaningful potential revenue risk.

---

## **Integrated Insights**
1. **Contract Duration** is consistently the strongest churn predictor — short-term customers are significantly more likely to leave.  
2. **Value-Added Services** (e.g., device protection, online security) enhance retention, while lack of such services correlates with higher churn.  
3. **Customer Support Quality** plays a central role, with negative experiences driving both historical and predicted churn.  
4. **Tenure-Related Risk** appears in both early-stage (onboarding) and long-term customers (service fatigue or competitor attraction).  
5. **Regional Concentration** of churn in states like **Uttar Pradesh**, **Maharashtra**, and **Tamil Nadu** suggests localized service or competitive challenges.  
6. **External Competition** — including pricing, device offers, and data packages — remains a major factor influencing customer defection.

---

## **Recommendations by Stakeholders**

### **1. Marketing Team**
- Develop **targeted retention campaigns** for **month-to-month customers**, offering loyalty rewards or contract renewal discounts.  
- Implement **regional campaigns** in high-churn states (Uttar Pradesh, Maharashtra, Tamil Nadu, Karnataka) that emphasize reliability, affordability, and service value.  
- Introduce **personalized engagement strategies** for both new and long-term customers, addressing early dissatisfaction and long-term disengagement.  

---

### **2. Customer Service / Support Team**
- Enhance **customer service training** to improve communication quality and issue resolution times.  
- Establish a **customer feedback loop** to capture and act upon complaints before they escalate to cancellations.   

---

### **3. Product & Operations Team**
- Investigate and address **Fiber Optic performance issues** in high-churn regions to improve service stability.  
- Regularly benchmark **device offerings and plan pricing** against competitors to ensure market competitiveness.  
- Expand **value-added services** such as data protection and premium support to strengthen customer loyalty.  

---

### **4. Finance & Billing Team**
- Encourage **digital and automated payment adoption** through small incentives, improving both convenience and customer stickiness.  
- Audit **billing and refund processes** to prevent dissatisfaction stemming from payment errors.  
- Simplify billing statements and enhance **payment transparency** to build customer trust and reduce disputes.



