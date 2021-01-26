const svgHeight = 400
const svgWidth = 1000

const margin = {
    top: 50,
    right: 50,
    bottom: 50,
    left: 50
  }

const chartHeight = svgHeight - margin.top - margin.bottom
const chartWidth = svgWidth - margin.left - margin.right

const svg = d3.select("body").append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth)
  
const chartG = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`)

d3.csv("assets/data/MoviesOnStreamingPlatform_updated.csv").then(data => {
    console.log(data)

    const y = d3.scaleLinear()
        .domain([0, d3.max(data.map(d => d.hair_length))])
        .range([chartHeight, 0])

    const x = d3.scaleLinear()
        .domain([0, d3.max(data.map(d => d.num_albums))])
        .range([0, chartWidth])

    const yAxis = d3.axisLeft(y)
    const xAxis = d3.axisBottom(x)

    chartG.append("g")
        .call(yAxis)
    
    chartG.append("g")
        .attr("transform", `translate(0, ${chartHeight})`)
        .call(xAxis)
    
        const labelArea = svg
        .append("g")
        .attr(
          "transform",
          `translate(${svgWidth / 2}, ${svgHeight - margin.bottom + 30})`
        );
    
    labelArea.append("text").attr("stroke", "#000000").text("Num Albums");

    chartG.selectAll("circle")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx", d => x(d.num_albums))
            .attr("cy", d => y(d.hair_length))
            .attr("r", 10)
})

