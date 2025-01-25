---
layout: default
title: About Me
---

# About Me
Thank you for reaching out to this site to learn more about me. I am a incident response analyst with a decades worth of experience in the Digital Forensics and Incident Response space (DFIR), currently embarking on a career transition into Data Science and Machine Learning. I have a lifetime of experience in coding, with more than a decade worth of experience in using python specifically. I'm very big in building out automations and forensic tools that help investigators conduct their investigations more efficiently.

This site is a work in progress, and is still being actively built out, but for now you can track my progress in [my journey]({{ site.baseurl }}/journey/) page.

# My Journey
This page will track my progress in becoming a Data Scientist in Machine Learning.

<!-- Application Activity Overview -->
<div style="margin-bottom: 40px;">
    <h2>Application Activity Overview</h2>
    <canvas id="activityChart" width="400" height="200"></canvas>
</div>

<!-- Application Success Pipeline -->
<div style="margin-bottom: 40px;">
    <h2>Application Pipeline</h2>
    <canvas id="pipelineChart" width="400" height="200"></canvas>
</div>

<!-- Weekly Response Rate -->
<div style="margin-bottom: 40px;">
    <h2>Weekly Response Rate</h2>
    <canvas id="responseChart" width="400" height="200"></canvas>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        const data = {{ site.data.email_trends | jsonify }};
        const colors = {
            received: 'rgba(75,192,192,0.6)',    // Teal
            rejected: 'rgba(255,99,132,0.6)',    // Red
            interview: 'rgba(54,162,235,0.6)',   // Blue
            offer: 'rgba(255,206,86,0.6)',       // Yellow
            default: 'rgba(201,203,207,0.4)'     // Gray
        };

        // Utility function to group data by week
        function groupByWeek(data) {
            const weeks = {};
            data.forEach(item => {
                const date = new Date(item.sent_time);
                const week = `${date.getFullYear()}-W${Math.ceil((date.getDate() + date.getDay()) / 7)}`;
                if (!weeks[week]) weeks[week] = {};
                if (!weeks[week][item.relation_id]) weeks[week][item.relation_id] = 0;
                weeks[week][item.relation_id]++;
            });
            return weeks;
        }

        // Activity Chart - Stacked bar showing daily activity
        const activityCtx = document.getElementById('activityChart').getContext('2d');
        const dates = [...new Set(data.map(item => item.sent_time.split('T')[0]))].sort();
        const relations = ['received', 'interview', 'offer', 'rejected'].filter(rel => 
            data.some(item => item.relation_id.toLowerCase().includes(rel))
        );

        new Chart(activityCtx, {
            type: 'bar',
            data: {
                labels: dates,
                datasets: relations.map(relation => ({
                    label: relation.charAt(0).toUpperCase() + relation.slice(1),
                    backgroundColor: colors[relation],
                    data: dates.map(date => 
                        data.filter(item => 
                            item.sent_time.startsWith(date) && 
                            item.relation_id.toLowerCase().includes(relation)
                        ).length
                    )
                }))
            },
            options: {
                responsive: true,
                plugins: {
                    title: { display: true, text: 'Daily Application Activity' },
                    legend: { position: 'top' }
                },
                scales: {
                    x: { stacked: true },
                    y: { stacked: true }
                }
            }
        });

        // Pipeline Chart - Line chart showing cumulative progress
        const pipelineCtx = document.getElementById('pipelineChart').getContext('2d');
        const cumulativeData = {};
        relations.forEach(relation => {
            cumulativeData[relation] = dates.map((date, i) => {
                const prevCount = i > 0 ? cumulativeData[relation][i-1] : 0;
                return prevCount + data.filter(item => 
                    item.sent_time.startsWith(date) && 
                    item.relation_id.toLowerCase().includes(relation)
                ).length;
            });
        });

        new Chart(pipelineCtx, {
            type: 'line',
            data: {
                labels: dates,
                datasets: relations.map(relation => ({
                    label: relation.charAt(0).toUpperCase() + relation.slice(1),
                    borderColor: colors[relation],
                    backgroundColor: colors[relation].replace('0.6', '0.1'),
                    data: cumulativeData[relation],
                    fill: true,
                    tension: 0.4
                }))
            },
            options: {
                responsive: true,
                plugins: {
                    title: { display: true, text: 'Cumulative Application Progress' },
                    legend: { position: 'top' }
                }
            }
        });

        // Response Rate Chart - Weekly success metrics
        const weeklyData = groupByWeek(data);
        const weeks = Object.keys(weeklyData).sort();
        const responseCtx = document.getElementById('responseChart').getContext('2d');
        
        const responseRate = weeks.map(week => {
            const total = Object.values(weeklyData[week]).reduce((a, b) => a + b, 0);
            const responses = Object.entries(weeklyData[week])
                .filter(([key]) => key.toLowerCase().includes('interview') || key.toLowerCase().includes('offer'))
                .reduce((a, [_, val]) => a + val, 0);
            return total > 0 ? (responses / total) * 100 : 0;
        });

        new Chart(responseCtx, {
            type: 'line',
            data: {
                labels: weeks,
                datasets: [{
                    label: 'Positive Response Rate (%)',
                    borderColor: colors.interview,
                    backgroundColor: colors.interview.replace('0.6', '0.1'),
                    data: responseRate,
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    title: { display: true, text: 'Weekly Success Rate' },
                    legend: { position: 'top' }
                },
                scales: {
                    y: {
                        min: 0,
                        max: 100,
                        ticks: { callback: value => value + '%' }
                    }
                }
            }
        });
    });
</script>
