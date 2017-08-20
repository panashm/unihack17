var data = {
  labels: [
    "Red",
    "Blue",
    "Yellow"
  ],
  datasets: [{
    data: [300, 50, 100],
    backgroundColor: [
      "#FF6384",
      "#36A2EB",
      "#FFCE56"
    ],
    hoverBackgroundColor: [
      "#FF6384",
      "#36A2EB",
      "#FFCE56"
    ]
  }]
};
var ctx = $("#myChart");
var myChart = new Chart(ctx, {
  type: 'pie',
  data: data,
  options: { legend: { display: false }}
});


var data1 = {
  labels: [
    "Red",
    "Blue",
    "Yellow"
  ],
  datasets: [{
    data: [300, 50, 100],
    backgroundColor: [
      "#FF6384",
      "#36A2EB",
      "#FFCE56"
    ],
    hoverBackgroundColor: [
      "#FF6384",
      "#36A2EB",
      "#FFCE56"
    ]
  }]
};
var ctx = $("#myChart1");
var myChart1 = new Chart(ctx, {
  type: 'pie',
  data: data1,
  options: { legend: { display: false }}
});
