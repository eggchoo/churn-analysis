
DROP VIEW IF EXISTS dbo.vw_ChurnData;
GO

USE db_churn;
GO

CREATE VIEW vw_ChurnData AS 
SELECT * 
FROM db_churn.dbo.prod_churn
WHERE Customer_Status IN ('Churned','Stayed'); 
GO

DROP VIEW IF EXISTS dbo.vw_JoinData;
GO
Create View vw_JoinData as
SELECT * 
FROM db_churn.dbo.prod_churn
WHERE Customer_Status = 'Joined';
GO

