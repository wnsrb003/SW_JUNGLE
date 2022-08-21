function solution(queue1, queue2) {
    let answer = 0;
    let q1Front = 0;
    let q2Front = 0;
    let q1End = queue1.length - 1;
    let q2End = queue2.length - 1;
    q1Sum = queue1.reduce((sum, value) => sum + value)
    q2Sum = queue2.reduce((sum, value) => sum + value)
    let mid = (q1Sum+q2Sum) / 2 
    if (mid == q1Sum) return 0
    if (mid % 2 != 0) return -1

    let flagNum = q1End + q2End + 2
    for (let i=0; i<flagNum; i++){
        if (q1Sum > mid){
            let addNum = queue1[q1Front]
            delete queue1[q1Front++]
            queue2[++q2End] = addNum
        }
        else if(q1Sum < mid) {
            let addNum = queue2[q2Front]
            delete queue2[q2Front++]
            queue1[++q1End] = addNum
        }
        answer += 1
        q1Sum = queue1.reduce((sum, value) => sum + value)
        if (q1Sum == mid) break;
    }
    return answer;
}

solution([3, 2, 7, 2], [4, 6, 5, 1])