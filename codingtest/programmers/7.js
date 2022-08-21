
// DFS
function solution(maps) {
    var answer = 0;
    let dx = [-1, 0, 1, 0]
    let dy = [0, -1, 0, 1]
    let visited = Array.from(Array(maps.length), () => Array(maps.length).fill(false))
    visited[0][0] = true
    dfs(visited, {x:0, y:0}, 0)
    function dfs(visited, start, count){
        let {x, y} = start
        if (x == maps.length - 1 && y == maps.length - 1){
            if (answer > count) answer = count
            return;
        }
        for (let d=0; d<4; d++){
            let newX = x + dx[d]
            let newY = y + dy[d]
            if (newX >= 0 && newY >= 0 && !visited[newX][newY] && maps[newX][newY]){
                visited[newX][newY] = true
                dfs(visited, {x: newX, y: newY}, count+1)
                visited[newX][newY] = false
            }
        }
    }
    return answer;
}

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])