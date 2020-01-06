WITH tagArray AS (
    SELECT 
        CAST (UDF.makearray(hashtags) AS array) AS tagArray
    FROM [TwitterStream] 
    TIMESTAMP BY DATEADD(millisecond, timestamp, '1970-01-01T00:00:00Z')
    )

SELECT 
    COUNT(*) AS counts, 
    arrayElement.ArrayValue AS hashtags, 
    System.Timestamp AS Window

INTO [TwitterHashtagsByHour]    

FROM
    tagArray AS event
CROSS APPLY GetArrayElements(event.tagArray) AS arrayElement

GROUP BY
    arrayElement.ArrayValue,
    TumblingWindow(hour, 1)
