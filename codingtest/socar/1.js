function solution(map3d) {
    let answer = 0;
    let dx = [1, -1, 0, 0]
    let dy = [0, 0, 1, -1]
    let dz = [-1, 1]
    let zlength = map3d.length
    let xlength = map3d[0].length
    let ylength = map3d[0][0].length

    let visited = Array.from(Array(zlength), () => Array.from(Array(xlength), () => Array(ylength).fill(false)))
    let flag = [0,0]
    let start, end
    // bfs로 깊이 체크해서 풀었습니다.
    for (let z=0; z<zlength; z++){
        for (let x=0; x<xlength; x++){
            for (let y=0; y<ylength; y++){
                if (map3d[z][x][y] === 'S'){
                    start = [z, x, y]
                    flag[0] = 1
                }
                if (map3d[z][x][y] === 'E'){
                    end = [z, x, y]
                    flag[1] = 1
                }
            }
            if (flag[0] && flag[1]) break
        }
    }
    visited[start[0]][start[1]][start[2]] = true
    let returnFlag = false
    bfs(visited, start, end)
    if (returnFlag) return answer
    return -1;

    function bfs(visited, start, end){
        let q = [start]
        while(q.length){
            let qSize = q.length
            for (let i=0; i<qSize; i++){
                let [z, x, y] = q.shift()
                if (z === end[0] && x === end[1] && y === end[2]){
                    returnFlag = true
                    break
                }

                for (let d=0; d<4; d++){
                    let nx = x + dx[d]
                    let ny = y + dy[d]
                    if (nx < 0 || ny < 0 || nx > xlength - 1 || ny > ylength - 1) continue
                    if (!visited[z][nx][ny] && map3d[z][nx][ny] != 'X'){
                        visited[z][nx][ny] = true
                        q.push([z, nx, ny])
                    }
                }
                for (let d=0;d<2;d++){
                    let nz = z + dz[d]
                    if (nz < 0 || nz > zlength - 1) continue
                    if (!visited[nz][x][y] && map3d[nz][x][y] != 'X'){
                        visited[nz][x][y] = true
                        q.push([nz, x, y])
                    }
                }
            }
            if (returnFlag) break;
            answer += 1
        }
    }
}
