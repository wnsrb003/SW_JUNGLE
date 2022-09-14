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
	else{
		input.push(line)	
	}
	readCnt += 1
	if (readCnt === 3) rl.close();
}).on("close", function() {
    solution(input)
    console.log()
	process.exit();
});

function solution(input){
	let newNum = input[0].split(' ')
	let oldNum = input[1].split(' ')
	let cnt = 0
	for (let i=0; i<newNum.length - 1; i++){
		let pop = parseInt(oldNum.shift()) - 1
		let j = i
		while(pop){
			if (newNum[j] === newNum[j+1]) {
				pop -= 1
				j += 1
			}
			else {
                cnt += 1
                let temp = newNum[j+1]
                newNum[j+1] = newNum[j+2]
                newNum[j+2] = temp
			}
		}
	}
	console.log(cnt)
}