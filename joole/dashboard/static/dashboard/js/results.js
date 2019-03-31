var co = costData.find(i => i.year == 2017);
var costs = [{'mois':'2017-01','cost':co['janvier']},
{'mois':'2017-02','cost':co['fevrier']},
{'mois':'2017-03','cost':co['mars']},
{'mois':'2017-04','cost':co['avril']},
{'mois':'2017-05','cost':co['mai']},
{'mois':'2017-06','cost':co['juin']},
{'mois':'2017-07','cost':co['juillet']},

{'mois':'2017-08','cost':co['aout']},

{'mois':'2017-09','cost':co['septembre']},
{'mois':'2017-10','cost':co['octobre']},
{'mois':'2017-11','cost':co['novembre']},

{'mois':'2017-12','cost':co['decembre']},


];   


new Morris.Line({
  // ID of the element in which to draw the chart.
  element: 'costChart',
  // Chart data records -- each entry in this array corresponds to a point on
  // the chart.
  data: 
	 costs,
  // The name of the data record attribute that contains x-values.
  xkey: 'mois',
  // A list of names of data record attributes that contain y-values.
  ykeys: ['cost'],
  // Labels for the ykeys -- will be displayed when you hover over the
  // chart.
  labels: ['Watt']
});
