// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

let input = []
let readCnt = 0
let n = 0
rl.on("line", function(line) {
	if (!readCnt) n = parseInt(line.split(' ')[1])
	input.push(line)
	readCnt += 1
	if (readCnt === n + 1) rl.close();
}).on("close", function() {
    solution()
    console.log()
	process.exit();
});

function solution(){
	let xLen = parseInt(input[0][0])
    let yLen = parseInt(input[0][2])
    input.splice(0, 1)
    let visited = Array.from(Array(xLen+1), () => Array(yLen+1).fill(false))
    let birdCnt = 0
    let DronCnt = 0
	for (let i=0; i<xLen; i++){
		for (let j=0; j<yLen; j++){
			if (input[i][j] !== '#' && !visited[i][j]){
                let [bCnt, dCnt] = bfs([i,j])
                // console.log(visited)
				birdCnt += bCnt
				DronCnt += dCnt
			}
		}
    }
    
    console.log(birdCnt, DronCnt)

	function bfs(start) {
		let dx = [-1, 1, 0, 0]
		let dy = [0, 0, -1, 1]
		let q = [start]
		// visited[start[0]][start[1]] = true
        let _dcnt = 0
        let _bcnt = 0
		while(q.length){
            let [x, y] = q.shift()
            if (input[x][y] === 'o') _dcnt += 1
			if (input[x][y] === 'v') _bcnt += 1
            // visited[x][y] = true
            // if (input[x][y] === '#') continue
			for (let d=0; d<4; d++){
				let nx = x + dx[d]
				let ny = y + dy[d]
				if (nx > 0 && ny > 0 && nx < xLen && ny < yLen){
					if (input[nx][ny] != '#' && !visited[nx][ny]){
                        console.log([nx, ny])
                        q.push([nx, ny])
                        visited[nx][ny] = true
					} 
				}
			}
        }
        console.log('--------')
		if (_bcnt >= _dcnt) return [_bcnt, 0]
		return [0, _dcnt]
	}
}