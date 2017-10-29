/*
 *
 *  Pie Chart JavaScript
 *
 */

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
	var gain = 99;   // To GET from server
	var left = 1;    //
  var data = google.visualization.arrayToDataTable([
    ['Activity Points', 'Percentage'],
    ['Gained',     gain],
	  ['Left', 	 left],
  ]);
	if(gain==100){
   	var color = 'black';	}
	else{
		var color = 'white';	}
	var options = {
          pieHole: 0.5,
          pieSliceTextStyle: {
            color: color,
          },
          legend: 'none'
        };

        var chart = new google.visualization.PieChart(document.getElementById('donut_single'));
        chart.draw(data, options);
}