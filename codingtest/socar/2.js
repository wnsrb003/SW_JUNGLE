function solution(n, k, paths) {
    // 운행하는 공항이 1000개 까지로 꽤 커서 다익스트라 구현
    // 무방향 그래프로 정점간의 간선은 한개만 
    // 1번 정점에서 시작하여 k번 공항 도착
    let timeTable = new Array(n+1).fill(Infinity)
    let mileageTable = new Array(n+1).fill(0)
    let visited = new Array(n+1).fill(false)
    let graph = Array.from({length : n+1}, () => [])
    let priorQ = []

    paths.map((route) => {
        graph[route[0]].push({'dest' :route[1], 'time': route[2], 'mileage' : route[3]})
        graph[route[1]].push({'dest' :route[0], 'time': route[2], 'mileage' : route[3]})
    })

    timeTable[1] = 0
    visited[1] = false
    priorQ.push({
        'dest': 1,
        'time': 0,
        'mileage' : 0
    })
    while(priorQ.length){
        priorQ.sort((a, b) => {
            return a.time - b.time
        })
        const {dest, time, mileage} = priorQ.shift()
        if (visited[dest]) continue
        visited[dest] = true
        graph[dest].forEach((next) => {
            if (timeTable[next.dest] > timeTable[dest] + next.time){
                timeTable[next.dest] = timeTable[dest] + next.time
                mileageTable[next.dest] = mileageTable[dest] + next.mileage
            }
            else if (timeTable[next.dest] === timeTable[dest] + next.time){
                if (mileageTable[next.dest] < mileageTable[dest] + next.mileage){
                    timeTable[next.dest] = timeTable[dest] + next.time
                    mileageTable[next.dest] = mileageTable[dest] + next.mileage
                }
            }
            priorQ.push(next)
        })
    }
    return [timeTable[k], mileageTable[k]];
}
