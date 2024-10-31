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
    const data = {{ site.data.email_trends | jsonify }};
    
    const labels = [...new Set(data.map(item => new Date(item.sent_time).toLocalDateString()))];
    const datasets = [
        { label: 'Relation 1', backgroundColor: 'rgba(75, 192, 192, 0.6)', data: data.filter(item => item.relation_name === "Relation 1").map(item => parseFloat(item.value)) },
        { label: 'Relation 2', backgroundColor: 'rgba(255, 99, 132, 0.6)', data: data.filter(item => item.relation_name === "Relation 2").map(item => parseFloat(item.value)) },
        { label: 'Relation 3', backgroundColor: 'rgba(54, 162, 235, 0.6)', data: data.filter(item => item.relation_name === "Relation 3").map(item => parseFloat(item.value)) },
        { label: 'Relation 4', backgroundColor: 'rgba(255, 206, 86, 0.6)', data: data.filter(item => item.relation_name === "Relation 4").map(item => parseFloat(item.value)) },
        { label: 'Relation 5', backgroundColor: 'rgba(153, 102, 255, 0.6)', data: data.filter(item => item.relation_name === "Relation 5").map(item => parseFloat(item.value)) },
        { label: 'Relation 6', backgroundColor: 'rgba(255, 159, 64, 0.6)', data: data.filter(item => item.relation_name === "Relation 6").map(item => parseFloat(item.value)) }
    ];

    new Chart(document.getElementById("myChart"), {
        type: 'bar',
        data: { labels: labels, datasets: datasets },
        options: { responsive: true, plugins: { legend: { position: 'top' }, tooltip: { mode: 'index', intersect: false } } }
    });
</script>
