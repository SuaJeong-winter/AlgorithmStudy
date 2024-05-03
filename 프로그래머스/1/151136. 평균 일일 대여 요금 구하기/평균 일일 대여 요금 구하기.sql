SELECT 
ROUND(AVG(DAILY_FEE),0) AS AVERAGE_FEE
# 0을 쓰면 소수점 0자리 즉 정수만 보이게 하는것
# 1을 쓰면 소수점 1자리까지 보여주는 것

FROM CAR_RENTAL_COMPANY_CAR

WHERE CAR_TYPE = "SUV"