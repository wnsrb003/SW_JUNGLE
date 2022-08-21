function solution(progresses, speeds) {
    var answer = [];
    while(progresses.length){
        let days = Math.ceil((100 - progresses[0]) / speeds[0])
        let cnt = 1
        for (let i=1; i<progresses.length; i++){
            if (progresses[i] + days * speeds[i] >= 100) cnt++
            else break
        }
        for (let i=0; i<cnt; i++){
            progresses.shift()
            speeds.shift()
        }
        answer.push(cnt)
    }
    return answer;
}