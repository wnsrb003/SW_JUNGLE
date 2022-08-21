function solution(tickets) {
    var answer = ["ICN"];
    let visited = Array(tickets.length).fill(false)
    tickets.sort()
    dfs(visited, "ICN", ["ICN"])
    function dfs(visited, start, trip){
        if (trip.length == tickets.length + 1) {
            answer = trip
            return 1;
        }
        for(let i=0; i<tickets.length; i++){
            if (visited[i]) continue;
            if (tickets[i][0] == start){
                visited[i] = true
                trip.push(tickets[i][1])
                if (dfs(visited, tickets[i][1], trip)) return 1
                visited[i] = false
                trip.pop()
            }
        }
        return 0
    }
    return answer;
}