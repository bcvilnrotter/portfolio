---
layout: default
title: "My Journey"
permalink: /journey/
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --text-color: #2c3e50;
            --background-color: #f8f9fa;
            --card-background: #ffffff;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--background-color);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .title {
            font-size: 3rem;
            margin-bottom: 2rem;
            color: var(--primary-color);
            animation: fadeInDown 1s ease-out;
            text-align: center;
        }

        .subtitle {
            font-size: 1.5rem;
            color: var(--secondary-color);
            margin-bottom: 2rem;
            animation: fadeInUp 1s ease-out 0.3s backwards;
            text-align: center;
        }

        .card {
            background: var(--card-background);
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
            transform: translateY(0);
            transition: transform 0.3s ease;
            animation: fadeIn 1s ease-out 0.6s backwards;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .error-message {
            color: red;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid red;
            background-color: #ffe6e6;
        }

        canvas {
            max-height: 400px;
        }

        .chart-container {
            margin-bottom: 40px;
            height: 400px;
            position: relative;
            background: var(--card-background);
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease;
        }

        .chart-container:hover {
            transform: translateY(-3px);
        }

        .chart-container h2 {
            color: var(--primary-color);
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }
            
            .title {
                font-size: 2rem;
            }
            
            .subtitle {
                font-size: 1.2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">My Journey</h1>
        <p class="subtitle">Tracking My Progress in Data Science & Machine Learning</p>
        
        <div class="card">
            <p>This page visualizes my journey transitioning into Data Science, tracking application metrics and progress over time. The graphs below show various aspects of my job search process, from daily activities to cumulative progress and success rates.</p>
        </div>

        <!-- Application Activity Overview -->
        <div class="chart-container">
            <h2>Application Activity Overview</h2>
            <canvas id="activityChart"></canvas>
        </div>

        <!-- Application Success Pipeline -->
        <div class="chart-container">
            <h2>Application Pipeline</h2>
            <canvas id="pipelineChart"></canvas>
        </div>

        <!-- Weekly Response Rate -->
        <div class="chart-container">
            <h2>Weekly Response Rate</h2>
            <canvas id="responseChart"></canvas>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.1/dist/chart.min.js"></script>
    <script>
        function showError(message) {
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.textContent = message;
            document.body.appendChild(errorDiv);
            console.error(message);
        }
---
layout: default
title: "My Journey"
permalink: /journey/
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --text-color: #2c3e50;
            --background-color: #f8f9fa;
            --card-background: #ffffff;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--background-color);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .title {
            font-size: 3rem;
            margin-bottom: 2rem;
            color: var(--primary-color);
            animation: fadeInDown 1s ease-out;
            text-align: center;
        }

        .subtitle {
            font-size: 1.5rem;
            color: var(--secondary-color);
            margin-bottom: 2rem;
            animation: fadeInUp 1s ease-out 0.3s backwards;
            text-align: center;
        }

        .card {
            background: var(--card-background);
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
            transform: translateY(0);
            transition: transform 0.3s ease;
            animation: fadeIn 1s ease-out 0.6s backwards;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .error-message {
            color: red;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid red;
            background-color: #ffe6e6;
        }

        canvas {
            max-height: 400px;
        }

        .chart-container {
            margin-bottom: 40px;
            height: 400px;
            position: relative;
            background: var(--card-background);
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease;
        }

        .chart-container:hover {
            transform: translateY(-3px);
        }

        .chart-container h2 {
            color: var(--primary-color);
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }
            
            .title {
                font-size: 2rem;
            }
            
            .subtitle {
                font-size: 1.2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">My Journey</h1>
        <p class="subtitle">Tracking My Progress in Data Science & Machine Learning</p>
        
        <div class="card">
            <p>This page visualizes my journey transitioning into Data Science, tracking application metrics and progress over time. The graphs below show various aspects of my job search process, from daily activities to cumulative progress and success rates.</p>
        </div>

        <!-- Application Activity Overview -->
        <div class="chart-container">
            <h2>Application Activity Overview</h2>
            <canvas id="activityChart"></canvas>
        </div>

        <!-- Application Success Pipeline -->
        <div class="chart-container">
            <h2>Application Pipeline</h2>
            <canvas id="pipelineChart"></canvas>
        </div>

        <!-- Weekly Response Rate -->
        <div class="chart-container">
            <h2>Weekly Response Rate</h2>
            <canvas id="responseChart"></canvas>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.1/dist/chart.min.js"></script>
    <script>
        function showError(message) {
            const errorDiv = document.createElement('div');
            errorDiv.className = 'error-message';
            errorDiv.textContent = message;
            document.body.appendChild(errorDiv);
            console.error(message);
        }

        document.addEventListener("DOMContentLoaded", async function() {
            try {
                let data = {{ site.data.email_trends | jsonify }};
                if (!data) {
                    throw new Error('Email trends data is not available');
                }
                if (!Array.isArray(data)) {
                    throw new Error('Invalid data format');
                }
                console.log('Raw data loaded:', data.length, 'entries');

                const colors = {
                    received: 'rgba(75,192,192,0.6)',    // Teal
                    rejected: 'rgba(255,99,132,0.6)',    // Red
                    interview: 'rgba(54,162,235,0.6)',   // Blue
                    offer: 'rgba(255,206,86,0.6)',       // Yellow
                    default: 'rgba(201,203,207,0.4)'     // Gray
                };

                function categorizeRelation(relation_id) {
                    if (!relation_id) return null;
                    const lower = relation_id.toLowerCase();
                    
                    // Handle exact matches first
                    if (lower === 'received' || lower === 'interview' || 
                        lower === 'offer' || lower === 'rejected') {
                        return lower;
                    }
                    
                    // Skip non-job related emails
                    if (lower === 'no email trend' || lower === 'scam') return null;
                    
                    // Categorize based on keywords
                    if (lower.includes('interview')) return 'interview';
                    if (lower.includes('offer')) return 'offer';
                    if (lower.includes('rejected') || lower.includes('rejection')) return 'rejected';
                    
                    // Default to received for any job-related communication
                    if (lower.includes('job') || lower.includes('career') || 
                        lower.includes('opportunity') || lower.includes('position') ||
                        lower.includes('application') || lower.includes('confirmation') || 
                        lower.includes('notification') || lower.includes('recruitment')) {
                        return 'received';
                    }
                    
                    return null;
                }

                // Pre-process data to remove uncategorized items
                const processedData = data.filter(item => {
                    const category = categorizeRelation(item.relation_id);
                    return category !== null;
                });
                console.log('Processed data:', processedData.length, 'entries');

                // Get unique dates from processed data
                const dates = [...new Set(processedData.map(item => item.sent_time.split('T')[0]))].sort();
                console.log('Date range:', dates[0], 'to', dates[dates.length - 1]);

                const relations = ['received', 'interview', 'offer', 'rejected'];

                // Activity Chart
                const activityCtx = document.getElementById('activityChart').getContext('2d');
                new Chart(activityCtx, {
                    type: 'bar',
                    data: {
                        labels: dates,
                        datasets: relations.map(relation => ({
                            label: relation.charAt(0).toUpperCase() + relation.slice(1),
                            backgroundColor: colors[relation],
                            data: dates.map(date => 
                                processedData.filter(item => 
                                    item.sent_time.startsWith(date) && 
                                    categorizeRelation(item.relation_id) === relation
                                ).length
                            )
                        }))
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
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

                // Pipeline Chart
                const pipelineCtx = document.getElementById('pipelineChart').getContext('2d');
                const cumulativeData = {};
                relations.forEach(relation => {
                    let runningTotal = 0;
                    cumulativeData[relation] = dates.map(date => {
                        const dailyCount = processedData.filter(item => 
                            item.sent_time.startsWith(date) && 
                            categorizeRelation(item.relation_id) === relation
                        ).length;
                        runningTotal += dailyCount;
                        return runningTotal;
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
                        maintainAspectRatio: false,
                        plugins: {
                            title: { display: true, text: 'Cumulative Application Progress' },
                            legend: { position: 'top' }
                        }
                    }
                });

                // Response Rate Chart
                const responseCtx = document.getElementById('responseChart').getContext('2d');
                const weeklyData = {};
                processedData.forEach(item => {
                    const date = new Date(item.sent_time);
                    const week = `${date.getFullYear()}-W${Math.ceil((date.getDate() + date.getDay()) / 7)}`;
                    const category = categorizeRelation(item.relation_id);
                    
                    if (!weeklyData[week]) {
                        weeklyData[week] = { total: 0, positive: 0 };
                    }
                    weeklyData[week].total++;
                    if (category === 'interview' || category === 'offer') {
                        weeklyData[week].positive++;
                    }
                });

                const weeks = Object.keys(weeklyData).sort();
                const responseRate = weeks.map(week => {
                    const rate = (weeklyData[week].positive / weeklyData[week].total) * 100;
                    console.log(`Week ${week}: ${rate.toFixed(1)}% (${weeklyData[week].positive}/${weeklyData[week].total})`);
                    return rate;
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
                        maintainAspectRatio: false,
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
            } catch (error) {
                showError(`Failed to load or process data: ${error.message}`);
            }
        });
    </script>
    <footer style="text-align: center; padding: 1rem; color: var(--text-color); opacity: 0.8; font-size: 0.9rem; position: fixed; bottom: 0; width: 100%; background: linear-gradient(to bottom, transparent, var(--background-color) 20%); backdrop-filter: blur(5px); border-top: 1px solid rgba(0,0,0,0.1);">
        Page designed and generated by Cline AI Assistant
    </footer>
</body>
</html>
