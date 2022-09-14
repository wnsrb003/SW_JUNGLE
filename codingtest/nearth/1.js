// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	let firstCnt = 0
	let secondCnt = 0
	let flag = false
	for (let i=1; i<line.length; i++){
		if (line[i] === line[i-1]) {
			firstCnt += 1
			if (!flag) {
				secondCnt += 1
				flag = 1
			}
			else{
				flag = 0
			}
		}
		else {
			flag = 0
		}
	}
	console.log(firstCnt, secondCnt)
	rl.close();
}).on("close", function() {
	process.exit();
});