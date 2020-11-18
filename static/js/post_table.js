
//var tr_data=[{"t_name":"MAS BBS FEST SPL(02840)","t_dep":"10:40","t_arr":"17:25","2S":"RLWL8\/WL8","SL":"AVAILABLE-0005","3A":"RLWL1\/WL1","2A":"AVAILABLE-0001","1A":""},{"t_name":"TPJ HWH EXP(02664)","t_dep":"12:00","t_arr":"19:07","2S":"RLWL25\/WL7","SL":"RLWL98\/WL39","3A":"RLWL32\/WL14","2A":"RLWL11\/WL7","1A":""}]
// trying to get the data from requesting the api





function get_data(){

var divContainer = document.getElementById("showData");
while (divContainer.firstChild) {
    divContainer.removeChild(divContainer.firstChild);
}
var spinner = document.createElement("div");
spinner.className="loader";
divContainer.appendChild(spinner);

var formd= new FormData(document.getElementById("form1"));
var fr=formd.get("from");
var to=formd.get("to");
var dt=formd.get("dt");

var URL='http://127.0.0.1:5000/train/'.concat(fr, '/', to, '/', dt);

var request = new XMLHttpRequest();
request.open('GET', URL, true)
request.onload = function() {
var tr_data = JSON.parse(this.response)

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
  

while (divContainer.firstChild) {
    divContainer.removeChild(divContainer.firstChild);
}
divContainer.appendChild(table);

//var tr_data1 = this.response
}

request.send();

}


//var formd= new FormData(document.getElementById("form1"));
//formd.onsubmit = get_data;
//formd.addEventListener('submit', get_data, false)
