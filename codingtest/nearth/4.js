// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});


let input = []
let chargeTime = 0
let readCnt = 0
let n = 0
rl.on("line", function(line) {
	if (!readCnt) {
		chargeTime = parseInt(line.split(' ')[1])
		n = parseInt(line.split(' ')[0])
	}
	else{
		input.push(line)	
	}
	readCnt += 1
	if (readCnt === n+1) rl.close();
}).on("close", function() {
    solution(input, chargeTime)
    console.log()
	process.exit();
});

function solution(inp, chargeTime){
    let ta = 0
    for (let i=0; i<inp.length; i++){
        if (!i) ta += (parseInt(inp[i][0]) + parseInt(inp[i][2]) + chargeTime)
        else {
            if (ta <= parseInt(inp[i][0])) ta = parseInt(inp[i][0]) + parseInt(inp[i][2]) + chargeTime
            else {
                ta += (parseInt(inp[i][2]) + chargeTime)
            }
        }
    }
    console.log(ta)
}