# X와 Y를 동시에 담은 장바구니의 수를 조회하는 SQL X와 Y의 이름순으로
# 없을 때는 정보를 포함하지 않는다.

SELECT
  c1.NAME as NAME_X,
  c2.NAME as NAME_Y
  # COUNT(c1.NAME, c2.NAME) as 숫자
FROM
  CART_PRODUCTS c1
JOIN
  CART_PRODUCTS c2
ON
  c1.NAME != c2.NAME
WHERE
  c1.CART_ID = c2.CART_ID
GROUP BY
  c1.NAME, c2.NAME # 여긴 내가 추가