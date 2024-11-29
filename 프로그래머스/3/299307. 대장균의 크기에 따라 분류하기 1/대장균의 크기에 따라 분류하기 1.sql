-- 코드를 작성해주세요
SELECT ID , 
    CASE
        WHEN (e.SIZE_OF_COLONY<=100) THEN 'LOW'
        WHEN (e.SIZE_OF_COLONY between 101 and 1000) THEN 'MEDIUM'
        ELSE 'HIGH'
        END AS SIZE
FROM ECOLI_DATA e
ORDER BY ID;