
def solution(weights):
    answer = 0
    weight_dict = {}
    for weight in weights:
        if weight in weight_dict:
            weight_dict[weight] += 1
        else:
            weight_dict[weight] = 1
    answer = 0
    check=[1,2,1,3]
    
    for weight, count in weight_dict.items():
        if weight in weight_dict or weight * 3 in weight_dict*2 or weight * 2 in weight_dict or weight * 4 in weight_dict*3:
            
            answer += 1
    print(weight_dict.keys()*3)
    print(answer)
solution([100,180,360,100,270])