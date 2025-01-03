---
layout: default
title: "My Journey"
permalink: /journey/

# My Journey

This page will track my progress in becoming a Data Scientist in Machine Learning.

<canvas id="myChart" width="400" height="200"></canvas>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    document.addEventListener("DOMContentLoaded",function() {
        const data = {{ site.data.email_trends | jsonify }};
        //Log data to ensure it loads correctly
        console.log("Data:",data);
        // Define colors for each relation
        const colors = [
            'rgba(75,192,192,0.6)',     // Teal
            'rgba(255, 99, 132, 0.6)',  // Red
            'rgba(54, 162, 235, 0.6)',  // Blue
            'rgba(255, 206, 86, 0.6)',  // Yellow
            'rgba(153, 102, 255, 0.6)', // Purple
            'rgba(255, 159, 64, 0.6)'   // Orange            
        ];
        // Get unique relation names from data
        const uniqueRelations = [...new Set(data.map(item => item.relation_id))];
        // Collect all unique dates in sorted order
        const labels = [...new Set(data.map(item => item.sent_time.split('T')[0]))].sort();
        // Generate datasets for each relation dynamically
        const datasets = uniqueRelations.map((relation,index) => {
            return {
                label: relation,
                backgroundColor: colors[index % colors.length],
                data: labels.map(date => {
                    const count = data.filter(item => 
                        item.relation_id === relation && item.sent_time.startsWith(date)).length;
                return count;
                })
            };
        });
        // Log labels and dataset values for debugging
        console.log("Labels:",labels);
        console.log("Datasets:",datasets);
        // Make the chart
        new Chart(document.getElementById("myChart"), {
            type: 'bar',
            data: { labels: labels, datasets: datasets },
            options: { 
                        responsive: true, 
                        plugins: { legend: { position: 'top' }, tooltip: { mode: 'index', intersect: false } },
                        scales: { x: { stacked: true }, y: { stacked: true } }         
            }
        });
    });       
</script>
