
sql = '''SELECT distinct ProdigyReportName
  FROM [EDW].[dbo].[DimSite]
  where ISNULL(ProdigyReportName,'') <> ''
  ORDER BY ProdigyReportName
'''


## add in sql query info here 
