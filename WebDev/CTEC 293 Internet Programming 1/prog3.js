
  $(document).ready(function() {
    $("#slide-panel").on("click", function() {
      $(this).slideToggle();
    });

    $("button").on("click", function() {
      var sales = [
        [
          parseInt($("input[name=quarter1-rep1]").val()),
          parseInt($("input[name=quarter1-rep2]").val()),
          parseInt($("input[name=quarter1-rep3]").val())
        ],
        [
          parseInt($("input[name=quarter2-rep1]").val()),
          parseInt($("input[name=quarter2-rep2]").val()),
          parseInt($("input[name=quarter2-rep3]").val())
        ],
        [
          parseInt($("input[name=quarter3-rep1]").val()),
          parseInt($("input[name=quarter3-rep2]").val()),
          parseInt($("input[name=quarter3-rep3]").val())
        ],
        [
          parseInt($("input[name=quarter4-rep1]").val()),
          parseInt($("input[name=quarter4-rep2]").val()),
          parseInt($("input[name=quarter4-rep3]").val())
        ]
      ];

      // Calculate total sales for each quarter
      var quarterTotals = [];
      for (var i = 0; i < sales.length; i++) {
        var total = 0;
        for (var j = 0; j < sales[i].length; j++) {
          total += sales[i][j];
        }
        quarterTotals.push(total);
      }

      // Calculate average sales for each sales representative
      var repAverages = [];
      for (var i = 0; i < sales[0].length; i++) {
        var total = 0;
        for (var j = 0; j < sales.length; j++) {
          total += sales[j][i];
        }
        repAverages.push(total / sales.length);
      }

      // Get top sales representative for each quarter
      var topReps = [];
      for (var i = 0; i < sales.length; i++) {
        var topRepIndex = 0;
        for (var j = 1; j < sales[i].length; j++) {
          if (sales[i][j] > sales[i][topRepIndex]) {
            topRepIndex = j;
          }
        }
        topReps.push(topRepIndex);
      }

      // Update table with results
      for (var i = 0; i < sales.length; i++) {
        $("tbody").append(
          "<tr><td>" + (i+1) + "</td>" +
          "<td>" + quarterTotals[i] + "</td>" +
          "<td>" + repAverages.join(", ") + "</td>" +
          "<td>" + (topReps[i]+1) + "</td></tr>"
        );
      }
    });
  });
