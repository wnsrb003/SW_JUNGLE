function solution(places) {
    var answer = [];
    let visited = Array.from(Array(5), () => Array(5).fill(false))
    let dx = [-1, 1, 0, 0]
    let dy = [0, 0, 1, -1]
    places.forEach((place) => {
        let flag = true
        for(let i=0; i< place.length; i++){
            place[i] = place[i].split('')
        }
        
        for (let i=0; i<5; i++){
            for (let j=0; j<5; j++){
                if (place[i][j] == "P"){
                    if (!bfs(place, [i, j], 0)){
                        flag = false
                    }
                }
            }
        }
        if (flag) answer.push(1)
        else answer.push(0)
    })
    function bfs(graph, start, cnt){
        let [x, y] = start
        graph[x][y] = "X"
        let q = []
        q.push(start)
        while(q.length){
            let [x, y] = q.shift()
            for (let i=0; i<4; i++){
                let nx = x + dx[i]
                let ny = y + dy[i]
                if (nx < 0 || ny < 0 || nx > 4 || ny > 4) continue;
                if (graph[nx][ny] == "P") return 0
                if (graph[nx][ny] == "O"){
                    q.push([nx, ny])
                    graph[nx][ny] = "X"
                }
            }
            cnt += 1
            if (cnt > 3) return 1
        }
        return 1
    }
    return answer;
}

solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])