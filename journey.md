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
      
        function showLoading() {
            const loadingDiv = document.createElement('div');
            loadingDiv.id = 'loading-indicator';
            loadingDiv.style.cssText = `
                position: fixed;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);
                background: var(--card-background);
                padding: 2rem;
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                z-index: 1000;
                text-align: center;
            `;
            loadingDiv.innerHTML = `
                <div style="margin-bottom: 1rem;">Loading and processing data...</div>
                <div class="progress-info" style="color: var(--secondary-color);"></div>
            `;
            document.body.appendChild(loadingDiv);
            return loadingDiv;
        }

        function updateLoadingProgress(message) {
            const progressInfo = document.querySelector('.progress-info');
            if (progressInfo) {
                progressInfo.textContent = message;
            }
        }

        function hideLoading() {
            const loadingDiv = document.getElementById('loading-indicator');
            if (loadingDiv) {
                loadingDiv.remove();
            }
        }

        document.addEventListener("DOMContentLoaded", async function() {
            const loadingIndicator = showLoading();
            try {
                console.time('Data Loading');
                updateLoadingProgress('Loading data...');
                let rawData = {{ site.data.email_trends | jsonify }};
                console.timeEnd('Data Loading');
                updateLoadingProgress('Data loaded successfully');

                if (!rawData) {
                    throw new Error('Email trends data is not available');
                }
                if (!Array.isArray(rawData)) {
                    throw new Error('Invalid data format');
                }
                console.log('Raw data loaded:', rawData.length, 'entries');

                // Performance optimization: Process data in chunks
                const CHUNK_SIZE = 1000;
                updateLoadingProgress('Processing data in chunks...');
                const processDataInChunks = (inputData, chunkSize, processor) => {
                    console.time('Data Processing');
                    let result = [];
                    for (let i = 0; i < inputData.length; i += chunkSize) {
                        const chunk = inputData.slice(i, i + chunkSize);
                        result = result.concat(processor(chunk));
                        if (i > 0 && i % (chunkSize * 10) === 0) {
                            console.log(`Processed ${i} entries...`);
                        }
                    }
                    console.timeEnd('Data Processing');
                    updateLoadingProgress('Data processing complete');
                    return result;
                };

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
                const processChunk = (chunk) => {
                    return chunk.filter(item => {
                        const category = categorizeRelation(item.relation_id);
                        return category !== null;
                    });
                };

                const processedData = processDataInChunks(rawData, CHUNK_SIZE, processChunk);
                console.log('Processed data:', processedData.length, 'entries');

                // Memory optimization: Clear original data
                rawData = null;

                // Performance optimization: Calculate dates efficiently
                console.time('Date Processing');
                const dateSet = new Set();
                for (const item of processedData) {
                    dateSet.add(item.sent_time.split('T')[0]);
                }
                const dates = Array.from(dateSet).sort();
                console.timeEnd('Date Processing');
                console.log('Date range:', dates[0], 'to', dates[dates.length - 1]);

                const relations = ['received', 'interview', 'offer', 'rejected'];

                // Performance optimization: Pre-calculate date indices
                console.time('Chart Data Preparation');
                const dateIndex = new Map(dates.map((date, index) => [date, index]));
                const relationCounts = relations.map(relation => new Array(dates.length).fill(0));

                // Single pass through data for all charts
                for (const item of processedData) {
                    const date = item.sent_time.split('T')[0];
                    const dateIdx = dateIndex.get(date);
                    const category = categorizeRelation(item.relation_id);
                    if (category !== null) {
                        const relationIdx = relations.indexOf(category);
                        if (relationIdx !== -1) {
                            relationCounts[relationIdx][dateIdx]++;
                        }
                    }
                }
                console.timeEnd('Chart Data Preparation');

                // Initialize chart contexts
                console.time('Chart Rendering');
                const activityCtx = document.getElementById('activityChart')?.getContext('2d');
                const pipelineCtx = document.getElementById('pipelineChart')?.getContext('2d');
                const responseCtx = document.getElementById('responseChart')?.getContext('2d');

                if (!activityCtx || !pipelineCtx || !responseCtx) {
                    throw new Error('Could not initialize chart contexts. Please check if all canvas elements exist.');
                }

                // Activity Chart with pre-calculated data
                new Chart(activityCtx, {
                    type: 'bar',
                    data: {
                        labels: dates,
                        datasets: relations.map((relation, idx) => ({
                            label: relation.charAt(0).toUpperCase() + relation.slice(1),
                            backgroundColor: colors[relation],
                            data: relationCounts[idx]
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

                // Pipeline Chart with optimized cumulative calculation
                const cumulativeData = {};
                relations.forEach((relation, idx) => {
                    let runningTotal = 0;
                    cumulativeData[relation] = relationCounts[idx].map(count => {
                        runningTotal += count;
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

                // Response Rate Chart with optimized weekly calculation
                const weeklyData = new Map();
                for (const item of processedData) {
                    const date = new Date(item.sent_time);
                    const week = `${date.getFullYear()}-W${Math.ceil((date.getDate() + date.getDay()) / 7)}`;
                    const category = categorizeRelation(item.relation_id);
                    
                    if (!weeklyData.has(week)) {
                        weeklyData.set(week, { total: 0, positive: 0 });
                    }
                    const weekStats = weeklyData.get(week);
                    weekStats.total++;
                    if (category === 'interview' || category === 'offer') {
                        weekStats.positive++;
                    }
                }

                const weeks = Array.from(weeklyData.keys()).sort();
                const responseRate = weeks.map(week => {
                    const stats = weeklyData.get(week);
                    const rate = (stats.positive / stats.total) * 100;
                    if (stats.total >= 5) { // Only log weeks with significant data
                        console.log(`Week ${week}: ${rate.toFixed(1)}% (${stats.positive}/${stats.total})`);
                    }
                    return rate;
                });
                console.timeEnd('Chart Rendering');
                hideLoading();

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
                hideLoading();
                showError(`Failed to load or process data: ${error.message}`);
                console.error('Detailed error:', error);
            }
        });
    </script>
    <footer style="text-align: center; padding: 1rem; color: var(--text-color); opacity: 0.8; font-size: 0.9rem; position: fixed; bottom: 0; width: 100%; background: linear-gradient(to bottom, transparent, var(--background-color) 20%); backdrop-filter: blur(5px); border-top: 1px solid rgba(0,0,0,0.1);">
        Page designed and generated by Cline AI Assistant
    </footer>
</body>
</html>
