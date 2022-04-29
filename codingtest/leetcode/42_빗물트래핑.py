import sys
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [9,8,7,6,7,8,9]
left = 0
right = len(height) - 1
cnt = 0
max_left = height[left]
max_right = height[right]

#스택
# stack = []
# for i in range(len(height)):
#     while stack and height[i] > height[stack[-1]]:
#         top = stack.pop()
#         if not len(stack):
#             break

#         distance = i - stack[-1] - 1
#         waters = min(height[i], height[stack[-1]]) - height[top]
#         cnt += distance * waters
#     stack.append(i)
# print(cnt)
# 양 쪽으로 쪼갠 코드(투포인트)
# max_dam = height.index(max(height))
# for i in range(max_dam+1):
#     max_left = max(max_left, height[i])
#     cnt += max_left - height[i]

# for i in range(len(height)-1, max_dam-1, -1):
#     max_right = max(max_right, height[i])
#     cnt += max_right - height[i]
# print(cnt)

# 정석 풀이(투포인트)
if not height:
    print(0)
while left < right:
    max_left = max(max_left, height[left])
    max_right = max(max_right, height[right])
    
    if max_left <= max_right:
        cnt += max_left - height[left]
        left += 1
    else:
        cnt += max_right  - height[right]
        right -= 1
print(cnt)

