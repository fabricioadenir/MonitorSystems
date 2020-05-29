demo = {
  initPickColor: function() {
    $('.pick-class-label').click(function() {
      var new_class = $(this).attr('new-class');
      var old_class = $('#display-buttons').attr('data-class');
      var display_div = $('#display-buttons');
      if (display_div.length) {
        var display_buttons = display_div.find('.btn');
        display_buttons.removeClass(old_class);
        display_buttons.addClass(new_class);
        display_div.attr('data-class', new_class);
      }
    });
  },

  initDocChart: function() {
    chartColor = "#FFFFFF";

    ctx = document.getElementById('chartHours').getContext("2d");

    myChart = new Chart(ctx, {
      type: 'line',

      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
        datasets: [{
            borderColor: "#6bd098",
            backgroundColor: "#6bd098",
            pointRadius: 0,
            pointHoverRadius: 0,
            borderWidth: 3,
            data: [300, 310, 316, 322, 330, 326, 333, 345, 338, 354]
          },
          {
            borderColor: "#f17e5d",
            backgroundColor: "#f17e5d",
            pointRadius: 0,
            pointHoverRadius: 0,
            borderWidth: 3,
            data: [320, 340, 365, 360, 370, 385, 390, 384, 408, 420]
          },
          {
            borderColor: "#fcc468",
            backgroundColor: "#fcc468",
            pointRadius: 0,
            pointHoverRadius: 0,
            borderWidth: 3,
            data: [370, 394, 415, 409, 425, 445, 460, 450, 478, 484]
          }
        ]
      },
      options: {
        legend: {
          display: false
        },

        tooltips: {
          enabled: false
        },

        scales: {
          yAxes: [{

            ticks: {
              fontColor: "#9f9f9f",
              beginAtZero: false,
              maxTicksLimit: 5,
              //padding: 20
            },
            gridLines: {
              drawBorder: false,
              zeroLineColor: "#ccc",
              color: 'rgba(255,255,255,0.05)'
            }

          }],

          xAxes: [{
            barPercentage: 1.6,
            gridLines: {
              drawBorder: false,
              color: 'rgba(255,255,255,0.1)',
              zeroLineColor: "transparent",
              display: false,
            },
            ticks: {
              padding: 20,
              fontColor: "#9f9f9f"
            }
          }]
        },
      }
    });

  },

  initChartsPages: function(rotinas_com_erro, top_erros) {
    chartColor = "#FFFFFF";
    rotinas = rotinas_com_erro.list_of_routines;
    erros = []
    rotinas.forEach(element => {
      var randomColorGenerator = function () { 
        return '#' + (Math.random().toString(16) + '0000000').slice(2, 8); 
      };
      for (const key in element) {
        element[key].forEach(function(item, i) { if (item == false && item !== 0) element[key][i] = null; })
        rotina = {
          data: element[key],
          label: key,
          borderColor: randomColorGenerator(),
          pointRadius: 2,
          pointBorderWidth: 4,
          fill: true,
          borderWidth: 1,
          order: 0.4

        }
        erros.push(rotina);
      }
    });

    ctx = document.getElementById('chartHours').getContext("2d");

    myChart = new Chart(ctx, {
      backgroundColor: "rgba(23, 100, 13, 0.1)",
      type: 'line',
      hover: false,
      data: {
        labels: rotinas_com_erro.days_of_the_month,
        datasets: erros
      },
      options: {
        title: {
          display: false,
          text: 'World population per region (in millions)'
        },
        legend: {
          display: false,
          position: 'top'
        },
      }
    });
    

    ctx = document.getElementById('chartEmail').getContext("2d");

    myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        datasets: [{
          label: (top_erros.length >= 1 ? Object.keys(top_erros[0]) : "Sem Erros"),
          data: (top_erros.length >= 1 ? Object.values(top_erros[0]) : 0),
          pointRadius: 10,
          pointHoverRadius: 40,
          backgroundColor: '#fcc468',
          borderWidth: 0,
        },
        {
          label: (top_erros.length >= 2 ? Object.keys(top_erros[1]) : "Sem Erros"),
          data: (top_erros.length >= 2 ? Object.values(top_erros[1]) : 0),
          pointRadius: 10,
          pointHoverRadius: 40,
          backgroundColor: '#ef8157',
          borderWidth: 0,
        },
        {
          label: (top_erros.length >= 3 ? Object.keys(top_erros[2]) : "Sem Erros"),
          data: (top_erros.length >= 3 ? Object.values(top_erros[2]) : 0),
          pointRadius: 10,
          pointHoverRadius: 40,
          backgroundColor: '#4acccd',
          borderWidth: 0,
        }]
      },
      options: {
        title: {
          display: false,
          text: 'Predicted world population (millions) in 2050'
        },
        legend: {
          display: false
        },
      }
    });

    var speedCanvas = document.getElementById("speedChart");

    var dataFirst = {
      data: [null, null, null, null, null, 40, 40, 50, 25, 30, 50, 70],
      fill: false,
      borderColor: '#fbc658',
      backgroundColor: 'transparent',
      pointBorderColor: '#fbc658',
      pointRadius: 4,
      pointHoverRadius: 4,
      pointBorderWidth: 8,
    };

    var dataSecond = {
      data: [0, 5, 10, 12, 20, 27, 30, 34, 42, 45, 55, 63],
      fill: false,
      borderColor: '#51CACF',
      backgroundColor: 'transparent',
      pointBorderColor: '#51CACF',
      pointRadius: 4,
      pointHoverRadius: 4,
      pointBorderWidth: 8
    };

    var speedData = {
      labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
      datasets: [dataFirst, dataSecond]
    };

    var chartOptions = {
      legend: {
        display: false,
        position: 'top'
      }
    };

    var lineChart = new Chart(speedCanvas, {
      type: 'line',
      hover: false,
      data: speedData,
      options: chartOptions
    });
  },


  //   }
  //   var map = new google.maps.Map(document.getElementById("map"), mapOptions);

  //   var marker = new google.maps.Marker({
  //     position: myLatlng,
  //     title: "Hello World!"
  //   });

  //   // To add the marker to the map, call setMap();
  //   marker.setMap(map);
  // },

  showNotification: function(from, align) {
    color = 'primary';

    $.notify({
      icon: "nc-icon nc-bell-55",
      message: "Welcome to <b>Paper Dashboard</b> - a beautiful bootstrap dashboard for every web developer."

    }, {
      type: color,
      timer: 8000,
      placement: {
        from: from,
        align: align
      }
    });
  }

};
