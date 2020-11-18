var tr_data=[{"t_name":"MAS BBS FEST SPL(02840)","t_dep":"10:40","t_arr":"17:25","2S":"RLWL8\/WL8","SL":"AVAILABLE-0005","3A":"RLWL1\/WL1","2A":"AVAILABLE-0001","1A":""},{"t_name":"TPJ HWH EXP(02664)","t_dep":"12:00","t_arr":"19:07","2S":"RLWL25\/WL7","SL":"RLWL98\/WL39","3A":"RLWL32\/WL14","2A":"RLWL11\/WL7","1A":""}]

var col=[];

for (var i = 0; i < tr_data.length; i++) {
    for (var key in tr_data[i]) {
        if (col.indexOf(key) === -1) {
            col.push(key);
        }
    }
}

header=["train no", "departure", "arrival", "Second Sitting (2S)", "Sleeper(SL)", "AC 3 Tier (3A)", "AC 2 Tier (2A)", "AC First Class (1A)"]

var table = document.createElement("table");
var tr = table.insertRow(-1); 

for (var i=0; i<header.length; i++) {
    var th = document.createElement("th");
    th.innerHTML=header[i];
    tr.appendChild(th);
}


for (var i=0; i<tr_data.length; i++) {
	tr = table.insertRow(-1); 
    for (var j=0; j<header.length; j++){
        var tabCell = tr.insertCell(-1);
        tabCell.innerHTML=tr_data[i][col[j]];
    }
}
  
var divContainer = document.getElementById("showData");
//divContainer.innerHTML = "";
divContainer.appendChild(table);


