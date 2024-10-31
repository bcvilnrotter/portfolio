---
layout: default
title: Home
---

# Purpose
The purpose of this page is to show off my current Github repos as well as other data visualization projects that can show off my ability and expertise in the field. I'm a Senior Incident Response Analyst that has a decades worth of experience in the Digital Forensics / Incident Response (DFIR) field, currently pivoting to a career path that is more focused on programming in the Data Science and AI / Machine Learning space.

Before embarking on this journey I thought it would be novel for me to track job applications through data visualizations. As I was going to online classes and filling in skill gaps, or remapping skills I already gained in my decades long career, I figured it would be beneficial for me to track my progress in my job search through data.

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
        ]
        // Get unique relation names from data
        const uniqueRelations = [...new Set(data.map(item => item.relation_name))];
        // Collect all unique dates in sorted order
        const labels = [...new Set(data.map(item => new Date(item.sent_time).toLocaleDateString()))].sort((a,b) => new Date(a) - new Date(b));
        // Generate datasets for each relation dynamically
        const datasets = uniqueRelations.map((relation,index) => {
            return {
                label: relation,
                backgroundColor: colors[index % colors.length],
                data: labels.map(date => {
                    const entry = data.find(
                        item => item.relation_name === relation && new Date(item.sent_time).toLocaleDateString() === date);
                    return entry ? parseFlost(entry.value) : 0;
                })
            };
        })
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
