function buildMetaData() {
    console.log("Called buildMetaData")
    d3.json("/data", function(resultData) {
        if (resultData.emotionCategories.length) {
            predictedEmotion  = resultData.predictedEmotion;
            emotionCategories = resultData.emotionCategories;
            probabilities = resultData.probabilities;
            predictedGender = resultData.predictedGender;
            genderCategories = resultData.genderCategories;
            genderProbabilities = resultData.genderProbabilities;
            buildBarChart(predictedEmotion, emotionCategories, probabilities, predictedGender, genderCategories, genderProbabilities);
        }
         else {
            setTimeout(buildMetaData, 300);
        }
    })
};

function buildBarChart(predictedEmotion, emotionCategories, probabilities, predictedGender,  genderCategories, genderProbabilities) {
    trace = {
        y: emotionCategories,
        x: probabilities,
        type: 'bar',
        orientation: "h",
        marker: {
            color: ["#0066aa", "#cfdee3", "#eab9ac", "#aaaacc", "#c5d165", "#99cccc", "#f4b273", '#aa40ff']
        }
    };

    trace2 = {
          x: genderCategories,
          y: genderProbabilities,
          type: 'bar',
          xaxis: 'x2',
          yaxis: 'y2',
          marker: {
               color: ["#0066aa", "#cfdee3"]
          }
    };
    var data = [trace, trace2];

    layout = {

        title: `Predict you are ${predictedGender} and sound ${predictedEmotion}`,
        xaxis: {
            title: "Probability of Each Emotion",
            domain: [0, 0.7]
        },
        yaxis: {
            title: "Emotion type",
        },
        yaxis2: {
            title: "Probability of Each Gender",
            anchor: 'x2'
        },

        xaxis2: {
            title: "Gender type",
            domain: [0.8, 1]
        },
    };

    Plotly.newPlot('result', data, layout);

}
