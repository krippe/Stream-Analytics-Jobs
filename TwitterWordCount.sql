WITH wordArrayStep AS (
    SELECT 
        CAST (UDF.cleanWordArray(tweet) AS array) AS wordArray
    FROM [TwitterIn] 
    TIMESTAMP BY DATEADD(millisecond, timestamp, '1970-01-01T00:00:00Z')
    )

SELECT 
    COUNT(*) AS counts, 
    arrayElement.ArrayValue AS words,
    System.Timestamp AS Window

INTO [PowerBI]    

FROM
    wordArrayStep AS event
CROSS APPLY GetArrayElements(event.wordArray) AS arrayElement

GROUP BY
    arrayElement.ArrayValue,
    TumblingWindow(hour, 1)
