function formatNum(num){
    if(num < 10){
        return '0' + num
    } else {
        return num.toString()
    }
}

function formatTime(totalseconds){
    const hours = Math.floor(totalseconds/60/60)
    const minutes = Math.floor((totalseconds - hours*60*60) / 60)
    const seconds = totalseconds - hours*60*60 - minutes*60
    return `${formatNum(hours)}:${formatNum(minutes)}:${formatNum(seconds)}`
}

function formatDate(date){
    return `${formatNum(date.getDate())}.${formatNum(date.getMonth()+1)}. ${formatNum(date.getHours())}:${formatNum(date.getMinutes())}:${formatNum(date.getSeconds())}`;
}

let maxNameLen = 0

function formatName(name){
    out = name
    while(out.length < maxNameLen-1){
        out = ' ' + out + ' '
    }
    if(out.length < maxNameLen){
        out = ' ' + out
    }
    return out
}

if(localStorage.json){
    document.getElementById('form').json.value = localStorage.json
}

document.getElementById('form').addEventListener('submit', function (event) {
    event.preventDefault();
    json = event.target.json.value
    localStorage.json = json
    data = JSON.parse(json)
    console.log(data)
    days = [];
    for( let i=0; i < 25; i++){
        const day = {
            label: (i+1).toString(),
            first: [],
            second: []
        }
        for(playerId in data.members){
            maxNameLen = Math.max(maxNameLen, data.members[playerId].name.length);
            if(data.members[playerId].completion_day_level[day.label]){
                const playerDay = data.members[playerId].completion_day_level[day.label];
                if(playerDay && playerDay[1]){
                    day.first.push({
                        playerId: playerId,
                        name: data.members[playerId].name,
                        time: playerDay[1].get_star_ts
                    })
                }
                if(playerDay && playerDay[2]){
                    day.second.push({
                        playerId: playerId,
                        name: data.members[playerId].name,
                        time: playerDay[2].get_star_ts
                    })
                }
            }
        }
        days.push(day)
    }
    days.forEach(day => {
        day.first.sort((a, b) => a.time - b.time)
        day.second.sort((a, b) => a.time - b.time)

        const p1 = document.createElement('p');
        p1.style.whiteSpace = 'pre'
        p1.textContent = `${formatNum(day.label)}-1: `
        for(let i = 0; i < day.first.length; i++){
            if(i>0){
                delta = day.first[i].time - day.first[i-1].time
                p1.textContent += ` > ${formatTime(delta)} > `
            } else {
                date = new Date(day.first[i].time * 1000)
                p1.textContent += `${formatDate(date)} > `
            }
            p1.textContent += formatName(day.first[i].name)
        }
        document.body.appendChild(p1)

        const p2 = document.createElement('p');
        p2.style.whiteSpace = 'pre'
        p2.textContent = `${formatNum(day.label)}-2: `
        for(let i = 0; i < day.second.length; i++){
            if(i>0){
                delta = day.second[i].time - day.second[i-1].time
                p2.textContent += ` > ${formatTime(delta)} > `
            } else {
                date = new Date(day.second[i].time * 1000)
                p2.textContent += `${formatDate(date)} > `
            }
            p2.textContent += formatName(day.second[i].name)
        }
        document.body.appendChild(p2)
        event.target.style.display = 'none'
    });
})