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

  initChartsPages: function(dados) {
    chartColor = "#FFFFFF";

    meu = dados;
    ctx = document.getElementById('chartHours').getContext("2d");
    console.log("CTX: ", meu)
    backgroundColor: "rgba(23, 100, 13, 0.1)",
    myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: [
          "01 Abril 20",
          "02 Abril",
          "03 Abril",
          "04 Abril",
          "05 Abril",
          "06 Abril",
          "07 Abril",
          "08 Abril",
          "09 Abril",
          "10 Abril",
          "11 Abril",
          "12 Abril",
          "13 Abril",
          "14 Abril",
          "15 Abril",
          "16 Abril",
          "17 Abril",
          "18 Abril",
          "19 Abril",
          "20 Abril",
          "21 Abril",
          "22 Abril",
          "23 Abril",
          "24 Abril",
          "25 Abril",
          "26 Abril",
          "27 Abril",
          "28 Abril",
          "29 Abril",
          "30 Abril",
        ],
        datasets: [{ 
            data: [86,114,106,106,107,111,133,221,783,2478],
            label: "Criação de documento",
            borderColor: "#3e95cd",
            fill: false
          }, { 
            data: [282,350,411,502,635,809,947,1402,3700,5267],
            label: "fluxo de trabalho",
            borderColor: "#8e5ea2",
            fill: false
          }, { 
            data: [168,170,178,190,203,276,408,547,675,734],
            label: "Assinatura",
            borderColor: "#3cba9f",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433, 455, 32, 56, 54],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }, { 
            data: [40,20,10,16,24,38,74,167,508,784],
            label: "Consulta de aviso",
            borderColor: "#e8c3b9",
            fill: false
          }, { 
            data: [6,3,2,2,7,26,82,172,312,433],
            label: "Integração",
            borderColor: "#c45850",
            fill: false
          }
        ]
      },
      options: {
        title: {
          display: false,
          text: 'World population per region (in millions)'
        },
        legend: {
          display: false
        },
      }
    });


    ctx = document.getElementById('chartEmail').getContext("2d");

    myChart = new Chart(ctx, {
      type: 'pie',
      data: {
        labels: ["Documentos", "Fluxo", "Cadastro"],
        datasets: [{
          label: "Erros Problematicos",
          pointRadius: 10,
          pointHoverRadius: 40,
          backgroundColor: [
            '#fcc468',
            '#ef8157',
            '#4acccd',
          ],
          borderWidth: 0,
          data: [342, 530, 120]
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
      data: [0, 19, 15, 20, 30, 40, 40, 50, 25, 30, 50, 70],
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

  initGoogleMaps: function() {
    var myLatlng = new google.maps.LatLng(40.748817, -73.985428);
    var mapOptions = {
      zoom: 13,
      center: myLatlng,
      scrollwheel: false, //we disable de scroll over the map, it is a really annoing when you scroll through page
      styles: [{
        "featureType": "water",
        "stylers": [{
          "saturation": 43
        }, {
          "lightness": -11
        }, {
          "hue": "#0088ff"
        }]
      }, {
        "featureType": "road",
        "elementType": "geometry.fill",
        "stylers": [{
          "hue": "#ff0000"
        }, {
          "saturation": -100
        }, {
          "lightness": 99
        }]
      }, {
        "featureType": "road",
        "elementType": "geometry.stroke",
        "stylers": [{
          "color": "#808080"
        }, {
          "lightness": 54
        }]
      }, {
        "featureType": "landscape.man_made",
        "elementType": "geometry.fill",
        "stylers": [{
          "color": "#ece2d9"
        }]
      }, {
        "featureType": "poi.park",
        "elementType": "geometry.fill",
        "stylers": [{
          "color": "#ccdca1"
        }]
      }, {
        "featureType": "road",
        "elementType": "labels.text.fill",
        "stylers": [{
          "color": "#767676"
        }]
      }, {
        "featureType": "road",
        "elementType": "labels.text.stroke",
        "stylers": [{
          "color": "#ffffff"
        }]
      }, {
        "featureType": "poi",
        "stylers": [{
          "visibility": "off"
        }]
      }, {
        "featureType": "landscape.natural",
        "elementType": "geometry.fill",
        "stylers": [{
          "visibility": "on"
        }, {
          "color": "#b8cb93"
        }]
      }, {
        "featureType": "poi.park",
        "stylers": [{
          "visibility": "on"
        }]
      }, {
        "featureType": "poi.sports_complex",
        "stylers": [{
          "visibility": "on"
        }]
      }, {
        "featureType": "poi.medical",
        "stylers": [{
          "visibility": "on"
        }]
      }, {
        "featureType": "poi.business",
        "stylers": [{
          "visibility": "simplified"
        }]
      }]

    }
    var map = new google.maps.Map(document.getElementById("map"), mapOptions);

    var marker = new google.maps.Marker({
      position: myLatlng,
      title: "Hello World!"
    });

    // To add the marker to the map, call setMap();
    marker.setMap(map);
  },

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






// {
//   type: 'line',

//   data: {
    // labels: [
    //   "01 Abril",
    //   "02 Abril",
    //   "03 Abril",
    //   "04 Abril",
    //   "05 Abril",
    //   "06 Abril",
    //   "07 Abril",
    //   "08 Abril",
    //   "09 Abril",
    //   "10 Abril",
    //   "11 Abril",
    //   "12 Abril",
    //   "13 Abril",
    //   "14 Abril",
    //   "15 Abril",
    //   "16 Abril",
    //   "17 Abril",
    //   "18 Abril",
    //   "19 Abril",
    //   "20 Abril",
    //   "21 Abril",
    //   "22 Abril",
    //   "23 Abril",
    //   "24 Abril",
    //   "25 Abril",
    //   "26 Abril",
    //   "27 Abril",
    //   "28 Abril",
    //   "29 Abril",
    //   "30 Abril",
    // ],
//     datasets: [{
//         label: "Cadastro documento",
//         borderColor: "#6bd098",
//         backgroundColor: "rgba(23, 100, 13, 0.1)",
//         pointRadius: 0,
//         pointHoverRadius: 0,
//         borderWidth: 3,
//         data: [0, 2, 2, 2, 8, 8, 34, 150, 200, 354]
//       },
//       {
//         label: "Intimação",
//         borderColor: "#f17e5d",
//         backgroundColor: "rgba(23, 0, 100, 0.1)",
//         pointRadius: 0,
//         pointHoverRadius: 0,
//         borderWidth: 3,
//         data: [0, 0, 10, 3, 29, 0, 34, 150, 200, 230]
//       },
//       {
//         label: "Liberar documento",
//         borderColor: "#fcc468",
//         backgroundColor: "rgba(90, 100, 100, 0.1)",
//         pointRadius: 0,
//         pointHoverRadius: 0,
//         borderWidth: 3,
//         data: [270, 394, 415, 409, 425, 445, 460, 450, 478, 484]
//       }
//     ]
//   },
//   options: {
//     hover: {
//       mode: 'nearest',
//       intersect: true
//     },
//     legend: {
//       display: false,
//       position: 'top'
//     },
//     tooltips: {
//       enabled: true
//     },

//     scales: {
//       yAxes: [{
//         display: true,
//         scaleLabel: {
//           display: true,
//           labelString: 'Month'
//         },
//         ticks: {
//           fontColor: "#9f9f9f",
//           beginAtZero: false,
//           maxTicksLimit: 5,
//           //padding: 20
//         },
//         gridLines: {
//           drawBorder: false,
//           zeroLineColor: "#ccc",
//           color: 'rgba(255,255,255,0.05)'
//         }

//       }],

//       xAxes: [{
//         display: true,
//         scaleLabel: {
//           display: true,
//           labelString: 'Month'
//         },
//         barPercentage: 1.6,
//         gridLines: {
//           drawBorder: false,
//           color: 'rgba(255,255,255,0.1)',
//           zeroLineColor: "transparent",
//           display: false,
//         },
//         ticks: {
//           padding: 20,
//           fontColor: "#9f9f9f"
//         }
//       }]
//     },
//   }
// }